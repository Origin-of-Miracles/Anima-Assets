"""
Anima-Assets 资源验证工具

用于验证 persona 配置文件和模型文件的格式正确性。

Usage:
    python validate.py personas/aris.json
    python validate.py --all
"""

import json
import sys
from pathlib import Path
from typing import Dict, List, Optional

# 必填字段定义
REQUIRED_PERSONA_FIELDS = [
    "id",
    "name",
    "name_en",
    "system_prompt"
]

OPTIONAL_PERSONA_FIELDS = [
    "school",
    "club",
    "role",
    "personality_traits",
    "speech_patterns",
    "example_dialogues",
    "model_override",
    "temperature_override"
]


class ValidationError(Exception):
    """验证错误"""
    pass


def validate_persona_json(file_path: Path) -> Dict:
    """
    验证 persona JSON 文件格式
    
    Args:
        file_path: JSON 文件路径
        
    Returns:
        解析后的 JSON 对象
        
    Raises:
        ValidationError: 验证失败时抛出
    """
    # 检查文件存在
    if not file_path.exists():
        raise ValidationError(f"文件不存在: {file_path}")
    
    # 解析 JSON
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        raise ValidationError(f"JSON 格式错误: {e}")
    
    # 检查必填字段
    for field in REQUIRED_PERSONA_FIELDS:
        if field not in data:
            raise ValidationError(f"缺少必填字段: {field}")
        
        if not data[field]:
            raise ValidationError(f"字段不能为空: {field}")
    
    # 检查 ID 格式（只能包含小写字母、数字、下划线）
    persona_id = data["id"]
    if not persona_id.replace("_", "").isalnum() or not persona_id.islower():
        raise ValidationError(
            f"ID 格式错误: {persona_id}（只能包含小写字母、数字、下划线）"
        )
    
    # 检查文件名是否与 ID 匹配
    expected_filename = f"{persona_id}.json"
    if file_path.name != expected_filename:
        raise ValidationError(
            f"文件名不匹配: 期望 {expected_filename}，实际 {file_path.name}"
        )
    
    # 检查 example_dialogues 格式
    if "example_dialogues" in data and data["example_dialogues"]:
        for i, dialogue in enumerate(data["example_dialogues"]):
            if not isinstance(dialogue, dict):
                raise ValidationError(f"example_dialogues[{i}] 必须是对象")
            
            if "user" not in dialogue or "assistant" not in dialogue:
                raise ValidationError(
                    f"example_dialogues[{i}] 必须包含 user 和 assistant 字段"
                )
    
    return data


def validate_model_files(persona_id: str) -> Dict[str, bool]:
    """
    检查模型文件是否存在
    
    Args:
        persona_id: 学生 ID
        
    Returns:
        文件存在状态字典
    """
    base_path = Path(__file__).parent.parent
    
    results = {
        "geo": (base_path / f"models/geo/students/{persona_id}.geo.json").exists(),
        "animation": (base_path / f"models/animations/students/{persona_id}.animation.json").exists(),
        "texture": (base_path / f"models/textures/students/{persona_id}.png").exists()
    }
    
    return results


def print_validation_result(file_path: Path, success: bool, message: str = ""):
    """打印验证结果"""
    status = "✅ PASS" if success else "❌ FAIL"
    print(f"{status} | {file_path.name}")
    if message:
        print(f"       └─ {message}")


def validate_all_personas():
    """验证所有 persona 配置文件"""
    personas_dir = Path(__file__).parent.parent / "personas"
    
    if not personas_dir.exists():
        print("❌ personas/ 目录不存在")
        return False
    
    json_files = list(personas_dir.glob("*.json"))
    
    if not json_files:
        print("⚠️  未找到任何 JSON 文件")
        return True
    
    print(f"\n🔍 开始验证 {len(json_files)} 个 persona 配置...\n")
    
    all_success = True
    
    for json_file in json_files:
        try:
            data = validate_persona_json(json_file)
            print_validation_result(json_file, True)
            
            # 检查模型文件
            model_status = validate_model_files(data["id"])
            if not all(model_status.values()):
                missing = [k for k, v in model_status.items() if not v]
                print(f"       ⚠️  缺少模型文件: {', '.join(missing)}")
            
        except ValidationError as e:
            print_validation_result(json_file, False, str(e))
            all_success = False
    
    print(f"\n{'='*50}")
    if all_success:
        print("✅ 所有验证通过！")
    else:
        print("❌ 存在验证错误，请修复后重试")
    
    return all_success


def main():
    """主函数"""
    if len(sys.argv) < 2:
        print("Usage: python validate.py <file.json> | --all")
        sys.exit(1)
    
    arg = sys.argv[1]
    
    if arg == "--all":
        success = validate_all_personas()
        sys.exit(0 if success else 1)
    else:
        file_path = Path(arg)
        
        try:
            data = validate_persona_json(file_path)
            print_validation_result(file_path, True)
            
            # 检查模型文件
            model_status = validate_model_files(data["id"])
            print("\n模型文件状态:")
            for file_type, exists in model_status.items():
                status = "✅" if exists else "❌"
                print(f"  {status} {file_type}")
            
            sys.exit(0)
            
        except ValidationError as e:
            print_validation_result(file_path, False, str(e))
            sys.exit(1)


if __name__ == "__main__":
    main()
