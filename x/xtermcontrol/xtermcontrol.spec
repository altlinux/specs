# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: xtermcontrol
Version: 3.8
Release: alt1
Summary: Dynamic control of XFree86 xterm properties
License: GPL-2.0-or-later
Group: System/XFree86
Url: https://thrysoee.dk/xtermcontrol/
Vcs: https://github.com/JessThrysoee/xtermcontrol

Source: %name-%version.tar
%{?!_without_check:%{?!_disable_check:
BuildRequires: /dev/pts
BuildRequires: xterm
BuildRequires: xvfb-run
}}

%description
makes it easy to change colors, title, font and geometry of a running
XFree86 xterm(1), as well as to report the current settings of the
aforementioned properties.

%prep
%setup

%build
%add_optflags %(getconf LFS_CFLAGS)
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%check
xvfb-run xterm -e 'make test >&3 2>&1; echo $? > exitcode' 3>&1 | cat -v
exit $(cat exitcode)

%files
%doc ChangeLog
%_bindir/xtermcontrol
%_man1dir/xtermcontrol.1*

%changelog
* Mon Dec 25 2023 Vitaly Chikunov <vt@altlinux.org> 3.8-alt1
- First import 3.8 (2021-05-04).
