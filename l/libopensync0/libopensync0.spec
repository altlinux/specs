Name: libopensync0
Version: 0.22
Release: alt4.1

Summary: A Platform and Distribution Independent Synchronization Framework
License: %lgpl2plus
Group: System/Libraries
URL: http://www.opensync.org/
Packager: Mobile Development Team <mobile@packages.altlinux.org>

Source: libopensync-%version.tar.bz2
Patch71: opensync_user.c.diff
Patch72: libopensync-fix-vcal-reminder.diff
Patch73: libopensync-vformat-infinite-loop.diff
Patch74: alt-libopensync-linkage_fix.diff
Patch75: alt-libopensync-python-lib-check-lib64.patch
Patch76: libopensync-wrapper-err.patch

# Automatically added by buildreq on Thu Oct 16 2008
BuildRequires: gcc-c++ glib2-devel libsqlite3-devel libxml2-devel python-devel swig
BuildRequires: rpm-build-licenses

%description
OpenSync is a synchronization framework that is platform and
distribution independent. It consists of several plug-ins that can be
used to connect to devices, a powerful sync engine, and the framework
itself. The synchronization framework is kept very flexible and is
capable of synchronizing any type of data, including contacts,
calendar, tasks, notes, and files.

%package devel
Summary: Header files, libraries and development documentation for %name
Group: Development/C
Conflicts: libopensync-devel
Requires: %name = %version

%description devel
This package contains the header files, static libraries and development
documentation for %name. If you like to develop programs using %name,
you will need to install %name-devel.

%package tools
Summary: Tools for %name
Group: Development/Other
Requires: %name
Conflicts: libopensync-tools

%description tools
Tools to test and debug %name.

%package -n python-module-opensync0
Summary: Python module for %name.
Group: Development/Python
Requires: %name
Conflicts: python-module-opensync

%description -n python-module-opensync0
Python module for %name.

%prep
%setup -q -n libopensync-%version
%patch71 -p1
%patch72 -p0
%patch73 -p0
%patch74 -p1
%patch75 -p1
%patch76 -p0

%build
# echo > acinclude.m4
%autoreconf
CFLAGS="-fno-strict-aliasing -I%_includedir/python%_python_version" %configure --disable-profiling --enable-tools --disable-unit-tests --enable-python
%make_build

%install
%make_install install DESTDIR=%buildroot
rm -f %buildroot%_libdir/*.la
rm -f %buildroot%_libdir/opensync/formats/*.la
rm -f %buildroot%python_sitelibdir/*.la
mkdir -p %buildroot%_datadir/opensync/defaults

%files
%_libdir/*.so.*
%_libdir/opensync
%_libexecdir/osplugin
%_datadir/opensync/defaults

%files devel
%_includedir/opensync-1.0
%_pkgconfigdir/*.pc
%_libdir/*.so

%files tools
%_bindir/*

%files -n python-module-opensync0
%dir %python_sitelibdir/*

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.22-alt4.1
- Rebuild with Python-2.7

* Mon Nov 01 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.22-alt4
- Fixed build

* Wed Nov 25 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.22-alt3.1
- Rebuilt with python 2.6

* Mon Sep 07 2009 Alexey Shabalin <shaba@altlinux.ru> 0.22-alt3
- add patch for werr build failure

* Thu Oct 16 2008 Andriy Stepanov <stanv@altlinux.ru> 0.22-alt2
- Stable version.

* Mon Apr 02 2007 Alexey Shabalin <shaba@altlinux.ru> 0.22-alt1
- 0.22

* Mon Feb 12 2007 Alexey Shabalin <shaba@altlinux.ru> 0.21-alt1
- 0.21
- cleanup spec (drop cvs)

* Wed Nov 08 2006 Alexey Shabalin <shaba@altlinux.ru> 0.20-alt1
- release 0.20

* Tue Oct 03 2006 Alexey Shabalin <shaba@altlinux.ru> 0.19-alt2
- release 0.19
- build puthon module
- fix spec (add in files %%_libexecdir/osplugin)
- fix BuildRequires

* Thu Sep 21 2006 Alexey Shabalin <shaba@altlinux.ru> 0.19-alt1cvs20060921
- svn version 20060921 

* Tue Jul 18 2006 Alexey Shabalin <shaba@altlinux.ru> 0.18-alt2cvs20060718
- svn version 20060718

* Mon May 29 2006 Alexey Shabalin <shaba@altlinux.ru> 0.18-alt2cvs20060529
- svn version 20060529
- set_verify_elf_method relaxed
- add directory %%_datadir/opensync/defaults

* Tue Nov 22 2005 Alexey Shabalin <shaba@altlinux.ru> 0.18-alt1
- 0.18 release
- build for Sisyphus

* Fri Sep 30 2005 Alexey Shabalin <shaba@altlinux.ru> 0.18-alt0.1.cvs20050930
- Initial package
