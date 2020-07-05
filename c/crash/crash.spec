# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1

Name:    crash
Version: 7.2.8.0.21.gc4862e1
Release: alt1
Summary: Linux kernel crash utility
Group:   Development/Debuggers
License: GPL-3.0-only
Url:     https://crash-utility.github.io/
Vcs:     https://github.com/crash-utility/crash.git
# Docs:  https://crash-utility.github.io/crash_whitepaper.html

Source0: %name-%version.tar
Source1: gdb-7.6.tar.gz

BuildRequires: ncurses-devel
BuildRequires: zlib-devel
BuildRequires: makeinfo
BuildRequires: flex

%description
The core analysis suite is a self-contained tool that can be used to
investigate either live systems, kernel core dumps created from dump creation
facilities.

%prep
%setup
install -m644 %SOURCE1 .
rm -f extensions/eppic.c

%build
%make_build --output-sync=none RPMPKG=%version-%release CFLAGS="%optflags"
%make_build extensions

%install
%makeinstall_std
mkdir -p %buildroot%_man8dir
install -m 0644 crash.8 %buildroot%_man8dir
mkdir -p %buildroot%_includedir/crash
install -m 0644 defs.h %buildroot%_includedir/crash
mkdir -p %buildroot%_libdir/crash/extensions
install -m 0644 extensions/*.so %buildroot%_libdir/crash/extensions

%files
%doc README COPYING3
%_bindir/crash
%_includedir/crash/defs.h
%_man8dir/crash.8*
%_libdir/crash/extensions

%changelog
* Thu Jun 25 2020 Vitaly Chikunov <vt@altlinux.org> 7.2.8.0.21.gc4862e1-alt1
- First import of 7.2.8-21-gc4862e1.
