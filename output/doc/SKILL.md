---
name: doc
description: Use when working with doc
doc_version: 
---

# Doc Skill

Use when working with doc, generated from official documentation.

## When to Use This Skill

This skill should be triggered when:
- Working with doc
- Asking about doc features or APIs
- Implementing doc solutions
- Debugging doc code
- Learning doc best practices

## Quick Reference

### Common Patterns

*Quick reference patterns will be added as you use the skill.*

### Example Code Patterns

**Example 1** (json):
```json
{
    list:[], //实例化的表格对象列表
    defaults:{}, //默认表格参数
    columnDefaults:{}, //默认列参数
    config:{}, //相关按钮的DOM选择类
    button:{}, //默认编辑、删除、排序按钮配置
    api:{} //封装的API方法
}
```

## Reference Files

This skill includes comprehensive documentation in `references/`:

- **doc.md** - Doc documentation

Use `view` to read specific reference files when detailed information is needed.

## Working with This Skill

### For Beginners
Start with the getting_started or tutorials reference files for foundational concepts.

### For Specific Features
Use the appropriate category reference file (api, guides, etc.) for detailed information.

### For Code Examples
The quick reference section above contains common patterns extracted from the official docs.

## Resources

### references/
Organized documentation extracted from official sources. These files contain:
- Detailed explanations
- Code examples with language annotations
- Links to original documentation
- Table of contents for quick navigation

### scripts/
Add helper scripts here for common automation tasks.

### assets/
Add templates, boilerplate, or example projects here.

## Notes

- This skill was automatically generated from official documentation
- Reference files preserve the structure and examples from source docs
- Code examples include language detection for better syntax highlighting
- Quick reference patterns are extracted from common usage examples in the docs

## Updating

To refresh this skill with updated documentation:
1. Re-run the scraper with the same configuration
2. The skill will be rebuilt with the latest information
