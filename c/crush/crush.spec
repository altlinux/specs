# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict,lint=relaxed

%define import_path github.com/charmbracelet/crush
%define go_builddir .build

Name: crush
Version: 0.81.0
Release: alt1
Summary: The glamourous AI coding agent for your favourite terminal
License: FSL-1.1-MIT
Group: Development/Other
Url: https://charm.land
Vcs: https://github.com/charmbracelet/crush

ExcludeArch: %ix86

Source: %name-%version.tar
BuildRequires(pre): rpm-build-golang
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

%prep
%setup
%__sed -i '/TestCoderAgent/a t.Skip("noNetwork")' internal/agent/agent_test.go

%build
export BUILDDIR="$PWD/%go_builddir"
export IMPORT_PATH="%import_path"
export LDFLAGS="-X github.com/charmbracelet/crush/internal/version.Version=%version"
export GOFLAGS="-buildmode=pie"
%golang_prepare
%golang_build %go_builddir/src/%import_path
set -C
./%go_builddir/bin/%name completion bash > _bash
./%go_builddir/bin/%name completion zsh  > _zsh
./%go_builddir/bin/%name completion fish > _fish
./%go_builddir/bin/%name man > crush.1

%install
export BUILDDIR="$PWD/%go_builddir"
export IGNORE_SOURCES=1

%golang_install
%__install -Dpm644 _bash %buildroot%_datadir/bash-completion/completions/%name
%__install -Dpm644 _fish %buildroot%_datadir/fish/vendor_completions.d/%name.fish
%__install -Dpm644 _zsh  %buildroot%_datadir/zsh/site-functions/_%name
%__install -Dpm644 %name.1 -t %buildroot%_man1dir

%check
%buildroot%_bindir/%name --version | grep -Fx '%name version %version'
cd %go_builddir/src/%import_path/
%gotest ./...

%files
%define _customdocdir %_docdir/%name
%doc LICENSE.md README.md
%doc .gear/example-*-%name.json
%_bindir/%name
%_datadir/bash-completion/completions/%name
%_datadir/fish/vendor_completions.d/%name.fish
%_datadir/zsh/site-functions/_%name
%_man1dir/%name.1*

%changelog
* Tue Jun 30 2026 Andrey Limachko <liannnix@altlinux.org> 0.81.0-alt1
- updated from 0.74.1 to 0.81.0

* Sat May 30 2026 Andrey Limachko <liannnix@altlinux.org> 0.74.1-alt1
- updated from 0.73.0 to 0.74.1

* Wed May 27 2026 Andrey Limachko <liannnix@altlinux.org> 0.73.0-alt1
- updated from 0.70.0 to 0.73.0

* Thu May 21 2026 Andrey Limachko <liannnix@altlinux.org> 0.70.0-alt1
- updated from 0.67.0 to 0.70.0

* Thu May 14 2026 Andrey Limachko <liannnix@altlinux.org> 0.67.0-alt1
- updated from 0.65.3 to 0.67.0

* Tue May 05 2026 Andrey Limachko <liannnix@altlinux.org> 0.65.3-alt1
- updated from 0.64.0 to 0.65.3

* Thu Apr 30 2026 Andrey Limachko <liannnix@altlinux.org> 0.64.0-alt1
- Update to v0.64.0.

* Fri Apr 10 2026 Andrey Limachko <liannnix@altlinux.org> 0.56.0-alt1
- Update to v0.56.0.

* Sun Feb 08 2026 Andrey Limachko <liannnix@altlinux.org> 0.39.3-alt1
- Update to v0.39.3.

* Thu Feb 05 2026 Andrey Limachko <liannnix@altlinux.org> 0.39.1-alt1
- Update to v0.39.1.

* Mon Feb 02 2026 Andrey Limachko <liannnix@altlinux.org> 0.38.0-alt1
- Update to v0.38.0.

* Thu Jan 29 2026 Andrey Limachko <liannnix@altlinux.org> 0.36.0-alt2
- Update spec and build schema.
- Patch: Add allowed_commands configuration with CLI support.

* Wed Jan 28 2026 Andrey Limachko <liannnix@altlinux.org> 0.36.0-alt1
- Update to v0.36.0.

* Sun Jan 25 2026 Andrey Limachko <liannnix@altlinux.org> 0.35.0-alt1
- Update to v0.35.0.

* Mon Jan 19 2026 Andrey Limachko <liannnix@altlinux.org> 0.33.3-alt1
- Update to v0.33.3.

* Wed Jan 14 2026 Andrey Limachko <liannnix@altlinux.org> 0.32.1-alt1
- Update to v0.32.1.

* Tue Jan 13 2026 Andrey Limachko <liannnix@altlinux.org> 0.32.0-alt1
- Update to v0.32.0.

* Tue Dec 23 2025 Andrey Limachko <liannnix@altlinux.org> 0.29.1-alt1
- Update to v0.29.1.

* Fri Dec 19 2025 Andrey Limachko <liannnix@altlinux.org> 0.28.0-alt1
- Update to v0.28.0.

* Tue Dec 09 2025 Andrey Limachko <liannnix@altlinux.org> 0.22.1-alt1
- Experimental update to v0.22.1 (2025-12-08).

* Mon Nov 03 2025 Vitaly Chikunov <vt@altlinux.org> 0.13.7-alt1
- Experimental update to v0.13.7 (2025-10-31).

* Thu Oct 09 2025 Vitaly Chikunov <vt@altlinux.org> 0.10.4-alt1
- Experimental import v0.10.4 (2025-09-30).
