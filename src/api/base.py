"""
基础接口定义
所有能力模块都应该遵循这些接口规范
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, Optional


class BaseCapability(ABC):
    """所有能力模块的基类"""

    @property
    def name(self) -> str:
        """能力名称"""
        return self.__class__.__name__

    @property
    def description(self) -> str:
        """能力描述"""
        return self.__doc__ or ""

    @abstractmethod
    async def execute(self, **kwargs) -> Dict[str, Any]:
        """
        执行能力

        Args:
            **kwargs: 执行参数

        Returns:
            执行结果字典
        """
        pass

    def validate_params(self, **kwargs) -> bool:
        """
        验证参数是否合法

        Args:
            **kwargs: 输入参数

        Returns:
            True 合法，False 不合法
        """
        return True


class BaseBrowserCapability(BaseCapability):
    """浏览器自动化能力基类"""

    @abstractmethod
    async def navigate(self, url: str) -> Dict[str, Any]:
        """导航到URL"""
        pass

    @abstractmethod
    async def click(self, selector: str) -> Dict[str, Any]:
        """点击元素"""
        pass

    @abstractmethod
    async def fill(self, selector: str, value: str) -> Dict[str, Any]:
        """填充输入框"""
        pass

    @abstractmethod
    async def screenshot(self, path: str) -> Dict[str, Any]:
        """截图"""
        pass


class BaseTranslationCapability(BaseCapability):
    """翻译能力基类"""

    @abstractmethod
    async def translate(self, text: str, source: str, target: str) -> str:
        """翻译文本"""
        pass


class BaseSpeechCapability(BaseCapability):
    """语音识别基类"""

    @abstractmethod
    async def recognize(self, audio_path: str) -> str:
        """语音识别"""
        pass


class BaseTTSCapability(BaseCapability):
    """文字转语音基类"""

    @abstractmethod
    async def synthesize(self, text: str, output_path: str) -> str:
        """文字转语音"""
        pass
