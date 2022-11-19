# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict,unresolved=normal

Name:    crash
Version: 8.0.2
Release: alt1
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
Source1: gdb-10.2.tar.gz

ExcludeArch: e2k
BuildRequires: flex
BuildRequires: gcc-c++
BuildRequires: makeinfo
BuildRequires: ncurses-devel
BuildRequires: zlib-devel

%description
The core analysis suite is a self-contained tool that can be used to
investigate either live systems, kernel core dumps created from dump
creation facilities.

Whitepaper: https://crash-utility.github.io/crash_whitepaper.html

Note: You will need -debuginfo package for the current kernel installed
      for this tool to work!

%prep
%setup
install -m644 %SOURCE1 .
mv crash-extensions/*.c extensions/
tar xvf crash-extensions/crash-gcore-command-* -C extensions --strip-components=1
tar xvf crash-extensions/ptdump-*              -C extensions --strip-components=1

%build
%add_optflags $(getconf LFS_CFLAGS)
%make_build --output-sync=none RPMPKG=%version-%release CFLAGS="%optflags" CXXFLAGS="%optflags"
# Build what builds. Does not support -j.
%make -ki extensions

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
* Sat Nov 19 2022 Vitaly Chikunov <vt@altlinux.org> 8.0.2-alt1
- Update to 8.0.2 (2022-11-16).

* Mon May 02 2022 Vitaly Chikunov <vt@altlinux.org> 8.0.1-alt1
- Update to 8.0.1 (2022-04-26).

* Mon Dec 20 2021 Vitaly Chikunov <vt@altlinux.org> 8.0.0-alt1
- Updated to 8.0.0-4-g6968345893 (2021-12-08) which is based on gdb-10.2
  with DWARF 5 support.
- Fixed lfs=strict build on 32-bit systems.

* Wed May 12 2021 Vitaly Chikunov <vt@altlinux.org> 7.3.0-alt1
- Update to 7.3.0 (2021-04-27).

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
