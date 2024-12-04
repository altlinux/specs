# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict,lint=relaxed

Name: gitleaks
Version: 8.21.2
Release: alt1
Summary: Protect and discover secrets using Gitleaks
License: MIT
Group: Development/Tools
Url: https://gitleaks.io
Vcs: https://github.com/gitleaks/gitleaks

Source: %name-%version.tar
BuildRequires: golang
%{?!_without_check:%{?!_disable_check:
BuildRequires: git-core
}}

%description
Gitleaks is a tool for detecting secrets like passwords, API keys, and
tokens in git repos, files, and whatever else you wanna throw at it via
stdin.

%prep
%setup

%build
go build -v -buildmode=pie -ldflags "-X=github.com/zricethezav/gitleaks/v8/cmd.Version=%version"
./gitleaks completion bash > %name.bash
./gitleaks completion fish > %name.fish
./gitleaks completion zsh  > %name.zsh

%install
install -Dp gitleaks -t %buildroot%_bindir
install -Dpm644 %name.bash %buildroot%_datadir/bash-completion/completions/%name
install -Dpm644 %name.fish %buildroot%_datadir/fish/vendor_completions.d/%name.fish
install -Dpm644 %name.zsh  %buildroot%_datadir/zsh/site-functions/_%name
%define _customdocdir %_docdir/%name

%check
%buildroot%_bindir/gitleaks version | grep -Fx '%version'
go test -v \
%ifarch x86_64 aarch64
	-race \
%endif
	./...

%files
%doc CONTRIBUTING.md LICENSE README.md USERS.md scripts/pre-commit.py
%_bindir/gitleaks
%_datadir/bash-completion/completions/%name
%_datadir/fish/vendor_completions.d/%name.fish
%_datadir/zsh/site-functions/_%name

%changelog
* Wed Dec 04 2024 Vitaly Chikunov <vt@altlinux.org> 8.21.2-alt1
- First import v8.21.2-17-g6018012 (2024-12-01).
