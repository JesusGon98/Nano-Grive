"""Tests for lazy provider exports from nano_grive.providers."""

from __future__ import annotations

import importlib
import sys


def test_importing_providers_package_is_lazy(monkeypatch) -> None:
    monkeypatch.delitem(sys.modules, "nano_grive.providers", raising=False)
    monkeypatch.delitem(sys.modules, "nano_grive.providers.anthropic_provider", raising=False)
    monkeypatch.delitem(sys.modules, "nano_grive.providers.openai_compat_provider", raising=False)
    monkeypatch.delitem(sys.modules, "nano_grive.providers.openai_codex_provider", raising=False)
    monkeypatch.delitem(sys.modules, "nano_grive.providers.github_copilot_provider", raising=False)
    monkeypatch.delitem(sys.modules, "nano_grive.providers.azure_openai_provider", raising=False)

    providers = importlib.import_module("nano_grive.providers")

    assert "nano_grive.providers.anthropic_provider" not in sys.modules
    assert "nano_grive.providers.openai_compat_provider" not in sys.modules
    assert "nano_grive.providers.openai_codex_provider" not in sys.modules
    assert "nano_grive.providers.github_copilot_provider" not in sys.modules
    assert "nano_grive.providers.azure_openai_provider" not in sys.modules
    assert providers.__all__ == [
        "LLMProvider",
        "LLMResponse",
        "AnthropicProvider",
        "OpenAICompatProvider",
        "OpenAICodexProvider",
        "GitHubCopilotProvider",
        "AzureOpenAIProvider",
    ]


def test_explicit_provider_import_still_works(monkeypatch) -> None:
    monkeypatch.delitem(sys.modules, "nano_grive.providers", raising=False)
    monkeypatch.delitem(sys.modules, "nano_grive.providers.anthropic_provider", raising=False)

    namespace: dict[str, object] = {}
    exec("from nano_grive.providers import AnthropicProvider", namespace)

    assert namespace["AnthropicProvider"].__name__ == "AnthropicProvider"
    assert "nano_grive.providers.anthropic_provider" in sys.modules
