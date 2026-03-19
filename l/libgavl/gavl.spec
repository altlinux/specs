%define _unpackaged_files_terminate_build 1

Name: libgavl
Version: 2.0.1
Release: alt2

Summary: Common A/V support library for gmerlin projects
License: GPLv2+
Group: System/Libraries
Url: https://github.com/bplaum/gavl
Vcs: https://github.com/bplaum/gavl.git

Source: %name-%version.tar

Patch: %name-%version-%release.patch

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

%package devel
Summary: Development files for libgavl
Group: Development/C

Requires: libgavl = %version-%release

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

%files
%doc AUTHORS COPYING README
%_libdir/*.so.*

%files devel
%_includedir/gavl
%_libdir/*.so
%_pkgconfigdir/*.pc

%files doc
%_docdir/gavl
%_docdir/libgavl-%version

%changelog
* Thu Mar 19 2026 Grant Makyan <karonus@altlinux.org> 2.0.1-alt2
- Fix i586 build.

* Thu Mar 05 2026 Grant Makyan <karonus@altlinux.org> 2.0.1-alt1
- First build for ALT.
