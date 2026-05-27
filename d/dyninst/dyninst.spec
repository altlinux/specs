%define _unpackaged_files_terminate_build 1
%define major_ver 13
%define libname lib%name

Name: dyninst
Version: %major_ver.0.0
Release: alt5

Summary: Tools for binary instrumentation, analysis, and modification
License: LGPL-2.1-or-later
Group: Development/Tools
Url: https://www.paradyn.org
VCS: https://github.com/dyninst/dyninst

ExcludeArch: %ix86

Requires: %libname%major_ver = %EVR

# Source-url: https://github.com/dyninst/%name/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar
Patch1: %name-%version-alt.patch

BuildRequires: binutils-devel
BuildRequires: boost-filesystem-devel
BuildRequires: boost-flyweight-devel
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libdw-devel
BuildRequires: libgomp-devel
BuildRequires: tbb-devel

%description
%summary

%package -n %libname%major_ver
Summary: %name libraries
Group: Development/C

%description -n %libname%major_ver
%summary

%package devel
Summary: Header files for compiling programs with Dyninst
Group: Development/C
Requires: %libname%major_ver = %EVR

%description devel
%summary

%package devel-static
Summary: Static libraries for compiling programs with Dyninst
Group: Development/C
Requires: %name-devel = %EVR

%description devel-static
%summary

%package doc
Summary: Documentation for using the Dyninst API
Group: Development/Documentation
BuildArch: noarch

%description doc
%summary

%prep
%setup
%patch1 -p1
sed -i 's;\(set(DYNINST_INSTALL_LIBDIR \)".*"\()\);\1${CMAKE_INSTALL_LIBDIR}\2;' \
    cmake/DyninstLibrarySettings.cmake

%build
%__cmake \
    -DCMAKE_INSTALL_PREFIX=%prefix \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DCMAKE_INSTALL_LIBDIR=%_libdir \
    -DDYNINST_INSTALL_LIBDIR=%_libdir \
    -DDYNINST_ENABLE_FILEFORMAT_PE=ON \
    -DDYNINST_ENABLE_CAPSTONE=ON \
    -S . -B "%_cmake__builddir" \
    #
%cmake_build

%install
%cmake_install

mkdir -p %buildroot%_defaultdocdir/%name
while IFS= read -r d; do
    pdir="`echo $d | cut -d/ -f-2`"
    [[ -n $pdir ]] || continue

    bname=`basename $pdir`
    docfile="$pdir/doc/$bname.pdf"
    [[ -f $docfile ]] && install -pm 644 $docfile %buildroot%_defaultdocdir/%name ||:
done <<<$(find . -type d -name 'doc')

%files
%doc README.md COPYRIGHT
%_bindir/parseThat

%files -n %libname%major_ver
%_libdir/*.so.%{major_ver}*

%files devel
%_libdir/*.so
%_includedir/*.h
%_includedir/mnemonics
%_includedir/registers
%_cmakedir/Dyninst

%files devel-static
%_libdir/libdyninstAPI_RT.a

%files doc
%_defaultdocdir/%name

%changelog
* Wed May 27 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 13.0.0-alt5
- fix ftbfs

* Fri Apr 24 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 13.0.0-alt4
- fix ftbfs

* Wed Feb 25 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 13.0.0-alt3
- fix failure when forking mutatee process (closes: 58006)

* Wed Feb 18 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 13.0.0-alt2
- fix crash on startup of `parseThat` (closes: 57894)

* Wed Feb 04 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 13.0.0-alt1
- initial build for ALT Linux
