# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict,lint=relaxed

Name: gum
Version: 0.8.0
Release: alt1
Summary: A tool for glamorous shell scripts
License: MIT
Group: Terminals
Url: https://github.com/charmbracelet/gum

Source: %name-%version.tar

BuildRequires: golang

%description
%summary.

%prep
%setup

%build
go build -v -buildmode=pie -ldflags="-X main.Version=%version"
./gum man > gum.1
./gum completion bash > gum.bash
./gum completion fish > gum.fish
./gum completion zsh  > gum.zsh

%install
install -Dp gum %buildroot%_bindir/gum
install -Dpm644 gum.1 %buildroot%_man1dir/gum.1
install -Dpm644 gum.bash %buildroot%_datadir/bash-completion/completions/gum
install -Dpm644 gum.fish %buildroot%_datadir/fish/vendor_completions.d/gum.fish
install -Dpm644 gum.zsh  %buildroot%_datadir/zsh/site-functions/_gum

%check
./gum style --border double --padding "2 4" --width 50 --align center "$(./gum -v)"

%files
%doc LICENSE README.md examples
%_bindir/gum
%_man1dir/gum.1*
%_datadir/bash-completion/completions/gum
%_datadir/fish/vendor_completions.d/gum.fish
%_datadir/zsh/site-functions/_gum

%changelog
* Wed Dec 14 2022 Vitaly Chikunov <vt@altlinux.org> 0.8.0-alt1
- First import v0.8.0 (2022-10-11).
