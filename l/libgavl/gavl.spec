%define _unpackaged_files_terminate_build 1
%define soname 3

Name: libgavl
Version: 2.0.1
Release: alt4

Summary: Common A/V support library for gmerlin projects
License: GPLv2+
Group: System/Libraries
Url: https://github.com/bplaum/gavl
Vcs: https://github.com/bplaum/gavl.git

Source: %name-%version.tar
Patch: %name-%version-%release.patch

# The gavl library is not available for i586:
# https://github.com/bplaum/gavl/issues/16
ExcludeArch: %ix86

BuildRequires: automake
BuildRequires: libtool
BuildRequires: libnettle-devel
BuildRequires: libgnutls-devel
BuildRequires: libpng-devel
BuildRequires: zlib-devel
BuildRequires: libGL-devel
BuildRequires: libdrm-devel
BuildRequires: doxygen

%description
gavl is a support library used by other packages in the gmerlin project. It
contains data structures and routines for handling uncompressed (and some
compressed) audio and video data, connectors, metadata/value containers, and
various utility code shared by gmerlin components.

%package -n libgavl%soname
Summary: Common A/V support library for gmerlin projects
License: GPLv2+
Group: System/Libraries
Obsoletes: libgavl < %EVR
Provides: libgavl = %EVR

%description -n libgavl%soname
gavl is a support library used by other packages in the gmerlin project. It
contains data structures and routines for handling uncompressed (and some
compressed) audio and video data, connectors, metadata/value containers, and
various utility code shared by gmerlin components.

%package devel
Summary: Development files for libgavl
Group: Development/C

%description devel
Header files and pkg-config metadata for developing applications using libgavl.

%package doc
Summary: API documentation for libgavl
Group: Documentation
BuildArch: noarch

%description doc
Generated API reference for libgavl.

%prep
%setup
%autopatch -p1

%build
%autoreconf
%configure --with-cpuflags=none

%make_build

%install
%makeinstall_std

%files -n libgavl%soname
%doc AUTHORS COPYING README
%_libdir/*.so.%{soname}*

%files devel
%_includedir/gavl
%_libdir/*.so
%_pkgconfigdir/*.pc

%files doc
%_docdir/gavl
%_docdir/libgavl%soname-%version

%changelog
* Tue Mar 24 2026 Grant Makyan <karonus@altlinux.org> 2.0.1-alt4
- Back to sisyphus repository.

* Tue Oct 12 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.4.0-alt5
- Fixed build with LTO

* Fri Nov 30 2018 Leontiy Volodin <lvol@altlinux.org> 1.4.0-alt4
- Added patch for Makefile (thanks debian for this patch)

* Thu Apr 12 2018 Michael Shigorin <mike@altlinux.org> 1.4.0-alt3
- updated for all of %%e2k

* Wed Apr 11 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.0-alt2
- ditto for arm

* Thu Aug 03 2017 Michael Shigorin <mike@altlinux.org> 1.4.0-alt1.1
- E2K: explicit -lm

* Tue Jul 21 2015 Hihin Ruslan <ruslandh@altlinux.ru> 1.4.0-alt1
- New version

* Thu Sep 22 2011 Hihin Ruslan <ruslandh@altlinux.ru> 1.2.0-alt1.0
- New version

* Mon Mar 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.2-alt1.2
- Rebuilt for debuginfo

* Wed Nov 03 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.2-alt1.1
- Rebuilt for soname set-versions

* Sat Apr 24 2010 Hihin Ruslan <ruslandh@altlinux.ru> 1.1.2-alt1
- 1.1.2

* Sun Dec 28 2008 Led <led@altlinux.ru> 1.1.0-alt1
- 1.1.0

* Sat Aug 02 2008 Led <led@altlinux.ru> 1.0.1-alt1
- 1.0.1

* Wed May 28 2008 Led <led@altlinux.ru> 1.0.0-alt1
- 1.0.0

* Sat Mar 15 2008 Led <led@altlinux.ru> 0.2.7-alt1
- initial build
