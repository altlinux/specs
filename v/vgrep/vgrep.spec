# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict,lint=relaxed

Name: vgrep
Version: 2.6.1
Release: alt2
Summary: a user-friendly pager for grep
License: GPL-3.0
Group: Text tools
Url: https://github.com/vrothberg/vgrep

Source: %name-%version.tar
BuildRequires: golang
BuildRequires: go-md2man

%description
vgrep is a pager for grep, git-grep, ripgrep and similar grep implementations,
and allows for opening the indexed file locations in a user-specified editor
such as vim or emacs. vgrep is inspired by the ancient cgvg scripts but
extended to perform further operations such as listing statistics of files and
directory trees or showing the context lines before and after the matches.

%prep
%setup

%build
go build -v \
	%ifnarch loongarch64
	-buildmode=pie \
	%endif
	-ldflags="-X main.version=%version"
go-md2man -in docs/vgrep.1.md -out docs/vgrep.1

%install
install -Dp vgrep -t %buildroot%_bindir
install -D -p -m 0644 docs/vgrep.1 %buildroot%_man1dir/vgrep.1

%define _customdocdir %_docdir/%name

%files
%doc README.md LICENSE
%_bindir/vgrep
%_man1dir/vgrep.1*

%changelog
* Mon Nov 27 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 2.6.1-alt2
- NMU: fixed FTBFS on LoongArch.

* Sat Jun 10 2023 Vitaly Chikunov <vt@altlinux.org> 2.6.1-alt1
- First import v2.6.1-10-g5bda867 (2023-06-05).
