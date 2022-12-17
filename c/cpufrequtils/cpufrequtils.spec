%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%define libname libcpufreq

Name: cpufrequtils
Version: 008
Release: alt4
Summary: Tools to determine and set CPUfreq settings
License: GPLv2
Group: System/Legacy libraries
Url: https://git.kernel.org/pub/scm/linux/kernel/git/brodo/cpufrequtils.git/about/
Vcs: git://git.kernel.org/pub/scm/utils/kernel/cpufreq/cpufrequtils.git
Requires: %libname = %EVR

Source: %name-%version.tar

%description
Command line tools to determine current CPUfreq settings and to modify
them (cpufreq-info and cpufreq-set), and debug tools.

These tools are obsoleted use cpupower instead.

%package -n %libname
Summary: Library for %name
Group: System/Legacy libraries

%description -n %libname
Library which offers a unified access method for userspace tools and
programs to the cpufreq core and drivers in the Linux kernel

Please consider switch to libcpupower.

%package -n %libname-devel
Summary: Headers for developing files for %libname
Group: Development/C
Requires: %libname = %EVR
Obsoletes: %name-devel
Conflicts: libcpupower-devel

%description -n %libname-devel
%summary.

This library is obsoleted, please use libcpupower-devel.

%prep
%setup

%build
%add_optflags %(getconf LFS_CFLAGS)
%make_build CFLAGS="%optflags" V=1 STRIP=:

%install
%makeinstall_std mandir=%_mandir libdir=%_libdir V=true
%find_lang cpufrequtils

%files -f cpufrequtils.lang
%doc AUTHORS COPYING README
%_bindir/*
%_man1dir/*

%files -n %libname
%_libdir/libcpufreq.so.*

%files -n %libname-devel
%_includedir/*
%_libdir/libcpufreq.so

%changelog
* Sat Dec 17 2022 Vitaly Chikunov <vt@altlinux.org> 008-alt4
- Update to the latest upstream version from git commit a2f0c39 (2011-08-13).
- Fixed lfs=strict build on 32-bit systems.
- Fixed build of debuginfo package.
- Added conflict with libcpupower-devel (ALT#41107), users should switch to
  it instead.

* Sun Apr 19 2020 Michael Shigorin <mike@altlinux.org> 008-alt3
- further fixed build on non-x86 architectures, notably E2K
- minor spec cleanup

* Thu Feb 14 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 008-alt2
- Fixed build on non-x86 architectures (patch by Zhang Le).

* Tue Jul 24 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 008-alt1.1
- Rebuilt for set-versions

* Thu Aug 05 2010 Victor Forsiuk <force@altlinux.org> 008-alt1
- Version 008.

* Mon Jun 15 2009 Victor Forsyuk <force@altlinux.org> 005-alt3
- Fix FTBFS (specify a tag for libtool).

* Fri Dec 12 2008 Victor Forsyuk <force@altlinux.org> 005-alt2
- Remove obsolete ldconfig calls.

* Mon Aug 11 2008 Victor Forsyuk <force@altlinux.org> 005-alt1
- Version 005.

* Wed Jul 30 2008 Victor Forsyuk <force@altlinux.org> 004-alt1
- Version 004 (new: removed dependency on libsysfs, added support
  for cpufreq statistics).

* Mon May 26 2008 Victor Forsyuk <force@altlinux.org> 003-alt1
- Version 003.

* Thu Apr 19 2007 Victor Forsyuk <force@altlinux.org> 002-alt2
- Fix 64 bit build.

* Wed Apr 18 2007 Victor Forsyuk <force@altlinux.org> 002-alt1
- Version 002.
- Eliminate duplication of library in utils package.

* Tue Mar 28 2006 Anton Farygin <rider@altlinux.ru> 001-alt1
- new version

* Mon Mar 20 2006 Anton Farygin <rider@altlinux.ru> 0.4-alt3
- fixed build

* Tue Feb 21 2006 Anton Farygin <rider@altlinux.ru> 0.4-alt2
- split package to library and utils part

* Wed Feb 01 2006 Anton Farygin <rider@altlinux.ru> 0.4-alt1
- new version

* Wed Jun 29 2005 Anton Farygin <rider@altlinux.ru> 0.3-alt1
- first build for ALT Linux
