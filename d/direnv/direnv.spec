# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict,lint=relaxed

Name: direnv
Version: 2.34.0
Release: alt1
Summary: unclutter your .profile
License: MIT
Group: Shells
Url: http://direnv.net
Vcs: https://github.com/direnv/direnv

Source: %name-%version.tar
BuildRequires: golang

%description
direnv is an extension for your shell. It augments existing shells with
a new feature that can load and unload environment variables depending
on the current directory.

%prep
%setup

%build
%{?_is_lp64:export CGO_ENABLED=0}
go build -v -buildmode=pie -ldflags "-X main.version=%version" main.go

%install
install -Dp main -T %buildroot%_bindir/direnv
install -Dpm644 man/direnv*.1 -t %buildroot%_man1dir

%check
%buildroot%_bindir/direnv --version | grep -Fx '%version'
go test ./...

%files
%doc CHANGELOG.md LICENSE README.md docs/*.md
%_bindir/direnv
%_man1dir/direnv*.1*
# fish: /usr/share/fish/completions/direnv.fish
# zsh-completions: /usr/share/zsh/site-functions/_direnv

%changelog
* Fri Mar 08 2024 Vitaly Chikunov <vt@altlinux.org> 2.34.0-alt1
- First import v2.34.0-2-g07254a6 (2024-03-03).
