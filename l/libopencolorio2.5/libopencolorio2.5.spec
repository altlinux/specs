# Legacy library: keeps soname 2.5 alive for packages which are not yet
# rebuilt against opencolorio 2.6 (libopenimageio3.1, LuxMark).
# Build only the core shared library: no apps, no python, no devel.

%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
%set_verify_elf_method strict

%define soname 2.5

Name: libopencolorio%soname
Version: 2.5.2
Release: alt2
Summary: Enables color transforms and image display across graphics apps
License: BSD-3-Clause
Group: System/Libraries
URL: https://opencolorio.org
VCS: https://github.com/AcademySoftwareFoundation/OpenColorIO

Source: %name-%version.tar

Patch1: opencolorio-alt-install.patch
Patch2: opencolorio-alt-armh-multiple-definition.patch

BuildRequires: cmake gcc-c++
BuildRequires: openexr-devel
BuildRequires: libexpat-devel
BuildRequires: liblcms2-devel
BuildRequires: libminizip-ng-compat-devel
BuildRequires: libyaml-cpp-devel
BuildRequires: pystring-devel
BuildRequires: zlib-devel

%description
OpenColorIO (OCIO) enables color transforms and image display to be handled in
a consistent manner across multiple graphics applications.

This is a compatibility package which provides the legacy
libOpenColorIO.so.%soname for applications which have not yet been rebuilt
against opencolorio 2.6.

%prep
%setup
%patch1 -p1
%patch2 -p1

%build
%add_optflags -D_FILE_OFFSET_BITS=64

# disable debugging wrappers
%add_optflags -DNDEBUG

%cmake \
	-DBUILD_SHARED_LIBS:BOOL=ON \
	-DOCIO_BUILD_STATIC=OFF \
	-DOCIO_BUILD_APPS=OFF \
	-DOCIO_BUILD_PYTHON=OFF \
	-DOCIO_BUILD_DOCS=OFF \
	-DOCIO_BUILD_TESTS=OFF \
	-DOCIO_BUILD_GPU_TESTS=OFF \
	-DOCIO_WARNING_AS_ERROR:BOOL=OFF \
%ifnarch x86_64 %e2k
	-DOCIO_USE_SSE=OFF \
	-DOCIO_USE_SSE2=OFF \
%endif
	-DCMAKE_CXX_STANDARD=14 \
	-Dminizip-ng_INCLUDE_DIR=%_includedir/minizip \
	%nil

%cmake_build

%install
%cmake_install

# Keep the core library only
%__rm -rf %buildroot%_bindir \
	%buildroot%_includedir \
	%buildroot%_mandir \
	%buildroot%_datadir/ocio \
	%buildroot%_libdir/cmake \
	%buildroot%_pkgconfigdir
%__rm -f %buildroot%_libdir/libOpenColorIO.so

%files
%doc LICENSE THIRD-PARTY.md
%_libdir/libOpenColorIO.so.%{soname}
%_libdir/libOpenColorIO.so.%{soname}.*

%changelog
* Fri Oct 02 2026 Nazarov Denis <nenderus@altlinux.org> 2.5.2-alt2
- Bump release: avoid N-V-R clash with the libopencolorio2.5 subpackage
  of opencolorio-2.5.2-alt1

* Fri Oct 02 2026 Nazarov Denis <nenderus@altlinux.org> 2.5.2-alt1
- Legacy library for packages which are not yet rebuilt against
  opencolorio 2.6 (libopenimageio3.1, LuxMark)
