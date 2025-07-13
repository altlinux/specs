# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict,lint=relaxed

Name: ets
Version: 0.3.1
Release: alt1
Summary: Command output timestamper
License: MIT
Group: Other
Url: https://github.com/gdubicki/ets/

Source: %name-%version.tar
BuildRequires: golang

%description
ets is a command output timestamper - it prefixes each line of a
command's output with a timestamp.

The purpose of ets is similar to that of moreutils ts(1), but ets
differentiates itself from similar offerings by running commands
directly within ptys, hence solving thorny issues like pipe buffering
and commands disabling color and interactive features when detecting
a pipe as output.

%prep
%setup

%build
go build -v -buildmode=pie -ldflags="-X main.version=%version"

%install
install -Dp ets -t %buildroot%_bindir
install -Dpm644 ets.1 -t %buildroot%_man1dir

%check
%buildroot%_bindir/ets --version | grep -Fx '%version'

%files
%define _customdocdir %_docdir/%name
%doc CHANGELOG.md COPYING README.md
%_bindir/ets
%_man1dir/ets.1*

%changelog
* Sun Jul 13 2025 Vitaly Chikunov <vt@altlinux.org> 0.3.1-alt1
- First import v0.3.1 (2025-03-02).
