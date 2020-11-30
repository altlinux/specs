# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name:    crash
Version: 7.2.9
Release: alt2
Summary: Linux kernel crash utility
Group:   Development/Debuggers
License: GPL-3.0-only
Url:     https://crash-utility.github.io/
Vcs:     https://github.com/crash-utility/crash.git
# Docs:  https://crash-utility.github.io/crash_whitepaper.html
# Mailing list: https://www.redhat.com/archives/crash-utility/
# Extensions Url: https://crash-utility.github.io/extensions.html
# Extensions Vcs: https://github.com/crash-utility/crash-extensions.git

Source0: %name-%version.tar
Source1: gdb-7.6.tar.gz

ExcludeArch: e2k
BuildRequires: ncurses-devel
BuildRequires: zlib-devel
BuildRequires: makeinfo
BuildRequires: flex

%description
The core analysis suite is a self-contained tool that can be used to
investigate either live systems, kernel core dumps created from dump
creation facilities.

Whitepaper: https://crash-utility.github.io/crash_whitepaper.html

Note: You will need -debuginfo package for the kernel installed for this
 tool to work! Because, it requires vmlinux binary present in -debuginfo.

%prep
%setup
install -m644 %SOURCE1 .
mv crash-extensions/*.c extensions/
tar xvf crash-extensions/crash-gcore-command-* -C extensions --strip-components=1
tar xvf crash-extensions/ptdump-*              -C extensions --strip-components=1

%build
%make_build --output-sync=none RPMPKG=%version-%release CFLAGS="%optflags"
# Build what builds.
%make_build --keep-going --ignore-errors extensions

%install
%makeinstall_std
install -Dp -m0644 crash.8 %buildroot%_man8dir/crash.8
install -Dp -m0644 defs.h  %buildroot%_includedir/crash/defs.h
mkdir -p %buildroot%_libdir/crash/extensions
install -p -m0644 extensions/*.so %buildroot%_libdir/crash/extensions

%files
%doc README COPYING3
%_bindir/crash
%_includedir/crash
%_man8dir/crash.8*
%_libdir/crash

%changelog
* Mon Nov 30 2020 Vitaly Chikunov <vt@altlinux.org> 7.2.9-alt2
- Add usage note to %%description.

* Wed Nov 25 2020 Vitaly Chikunov <vt@altlinux.org> 7.2.9-alt1
- Update to 7.2.9 (2020-11-20).

* Sun Jul 12 2020 Vitaly Chikunov <vt@altlinux.org> 7.2.8.0.21.gc4862e1-alt3
- spec: ExcludeArch: e2k

* Wed Jul 08 2020 Vitaly Chikunov <vt@altlinux.org> 7.2.8.0.21.gc4862e1-alt2
- Add crash-extensions 80b218f.

* Thu Jun 25 2020 Vitaly Chikunov <vt@altlinux.org> 7.2.8.0.21.gc4862e1-alt1
- First import of 7.2.8-21-gc4862e1.
