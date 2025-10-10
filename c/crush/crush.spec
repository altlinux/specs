# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict,lint=relaxed

Name: crush
Version: 0.10.4
Release: alt1
Summary: The glamourous AI coding agent for your favourite terminal
License: FSL-1.1-MIT
Group: Development/Other
Url: https://github.com/charmbracelet/crush

Source: %name-%version.tar
BuildRequires: golang

%description
Your new coding bestie, now available in your favourite terminal.
Your tools, your code, and your workflows, wired into your LLM of choice.

Features:
- Multi-Model: choose from a wide range of LLMs or add your own via OpenAI- or
    Anthropic-compatible APIs
- Flexible: switch LLMs mid-session while preserving context
- Session-Based: maintain multiple work sessions and contexts per project
- LSP-Enhanced: Crush uses LSPs for additional context, just like you do
- Extensible: add capabilities via MCPs (http, stdio, and sse)

Note: Automatic provider updates are disabled and could be enabled in config or
  CRUSH_DISABLE_PROVIDER_AUTO_UPDATE=0 env or updated manually with
  'crush update-providers' invocation.

%prep
%setup

%build
go build -v -buildmode=pie -ldflags="-X github.com/charmbracelet/crush/internal/version.Version=%version"
set -C
./crush completion bash > _bash
./crush completion zsh  > _zsh
./crush completion fish > _fish
./crush man > crush.1

%install
install -Dp crush -t %buildroot%_bindir
install -Dpm644 _bash %buildroot%_datadir/bash-completion/completions/%name
install -Dpm644 _fish %buildroot%_datadir/fish/vendor_completions.d/%name.fish
install -Dpm644 _zsh  %buildroot%_datadir/zsh/site-functions/_%name
install -Dpm644 crush.1 -t %buildroot%_man1dir

%check
%buildroot%_bindir/crush --version | grep -Fx '%name version %version'
# Test and ensure provides fetching is disabled.
# 1. If providers auto-update is not disabled test will fail with:
# panic: Failed to initialize config: failed to load providers: failed to load providers
go test ./...
# 2. Also, crush logs will fail.
./crush logs >log 2>&1
grep -q 'Providers auto-update is disabled' log
{ ! grep -E 'unable to fetch|http' log; }

%files
%define _customdocdir %_docdir/%name
%doc LICENSE.md README.md
%doc .gear/example-ollama-crush.json
%_bindir/crush
%_datadir/bash-completion/completions/%name
%_datadir/fish/vendor_completions.d/%name.fish
%_datadir/zsh/site-functions/_%name
%_man1dir/%name.1*

%changelog
* Thu Oct 09 2025 Vitaly Chikunov <vt@altlinux.org> 0.10.4-alt1
- Experimental import v0.10.4 (2025-09-30).
