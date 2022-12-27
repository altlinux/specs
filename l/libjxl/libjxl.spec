%def_enable snapshot
%define _unpackaged_files_terminate_build 1

%define _name jxl

%def_enable tools
%def_enable man
%def_disable tests
%def_disable check

Name: lib%_name
Version: 0.7.0
Release: alt0.5

Summary: JPEG XL image format reference implementation
License: BSD-3-Clause
Group: System/Libraries
Url: https://github.com/libjxl/libjxl

ExcludeArch: armh

%if_disabled snapshot
Source: https://github.com/libjxl/libjxl/archive/v%version/%name-%version.tar.gz
%else
Vcs: https://github.com/libjxl/libjxl.git
Source: %name-%version.tar
%endif

%define gif_ver 5.1

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++ ninja-build
#BuildRequires: libgif-devel >= %gif_ver
BuildRequires: highway-devel
BuildRequires: libjpeg-devel openexr-devel libpng-devel libwebp-devel
BuildRequires: libavif-devel libbrotli-devel liblcms2-devel zlib-devel
%{?_enable_man:BuildRequires: asciidoc-a2x}
%{?_enable_tests:BuildRequires: libgtest-devel}

%description
JPEG XL image format reference implementation Library.

%package devel
Summary: Development files for JPEG XL library
Group: Development/C++
Requires: %name = %EVR

%description devel
This package provides JPEG XL development files.

%package tools
Summary: The JPEG XL library command line tools
Group: Graphics
Requires: %name = %EVR

%description tools
This package provides JPEG XL tools.


%prep
%setup

%build
%add_optflags %(getconf LFS_CFLAGS)
%cmake -GNinja \
    -DJPEGXL_FORCE_SYSTEM_HWY=ON \
    -DJPEGXL_FORCE_SYSTEM_BROTLI=ON \
    -DJPEGXL_FORCE_SYSTEM_GTEST=ON \
    -DJPEGXL_FORCE_SYSTEM_LCMS2=ON \
    %{?_enable_tools:-DJPEGXL_ENABLE_TOOLS=ON} \
    -DJPEGXL_ENABLE_MANPAGES=ON \
    %{?_disable_tests:-DBUILD_TESTING=OFF} \
%nil
%cmake_build

%install
%cmake_install
rm -f %buildroot%_libdir/*.a
rm -rf %buildroot%_includedir/hwy/
rm -f %buildroot%_pkgconfigdir/libhwy*.pc

%check
%cmake_build -d test

%files
%_libdir/%{name}*.so.*
%doc AUTHORS README* PATENTS

%files devel
%_libdir/%{name}*.so
%_includedir/%_name/
%_pkgconfigdir/%{name}*.pc

%if_enabled tools
%files tools
%_bindir/c%_name
%_bindir/d%_name
%_bindir/benchmark_xl
%_bindir/cjpeg_hdr
%_bindir/%{_name}info
%_man1dir/c%_name.1*
%_man1dir/d%_name.1*
%endif

%changelog
* Tue Dec 27 2022 Yuri N. Sedunov <aris@altlinux.org> 0.7.0-alt0.5
- first preview for Sisyphus
- built with bundled 'sjpeg' and 'skcms' libraries
- temporarily disabled armh build


