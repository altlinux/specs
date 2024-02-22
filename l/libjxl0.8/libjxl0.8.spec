%def_enable snapshot

%define _name jxl
%define sover 0.8
%define libname lib%_name%sover

%def_disable tools
%def_disable man
%def_disable plugins
%def_disable tests
%def_disable check

Name: %libname
Version: %sover.2
Release: alt2

Summary: JPEG XL image format reference implementation
License: BSD-3-Clause
Group: System/Libraries
Url: https://github.com/libjxl/libjxl

ExcludeArch: armh

%if_disabled snapshot
Source: https://github.com/libjxl/libjxl/archive/v%version/lib%_name-%version.tar.gz
%else
Vcs: https://github.com/libjxl/libjxl.git
Source: lib%_name-%version.tar
%endif

%define gif_ver 5.1
%define hwy_ver 1.0.3

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++ ninja-build
#BuildRequires: libgif-devel >= %gif_ver
BuildRequires: highway-devel >= %hwy_ver
BuildRequires: libjpeg-devel openexr-devel libpng-devel libwebp-devel
BuildRequires: libavif-devel libbrotli-devel liblcms2-devel zlib-devel
%{?_enable_plugins:BuildRequires: libgdk-pixbuf-devel}
%{?_enable_man:BuildRequires: asciidoc-a2x}
%{?_enable_tests:BuildRequires: libgtest-devel}
%{?_enable_check:BuildRequires: ctest}

%description
JPEG XL image format reference implementation Library.

%prep
%setup -n lib%_name-%version

%build
%add_optflags %(getconf LFS_CFLAGS)
%cmake -GNinja \
    -DJPEGXL_FORCE_SYSTEM_HWY=ON \
    -DJPEGXL_FORCE_SYSTEM_BROTLI=ON \
    -DJPEGXL_FORCE_SYSTEM_GTEST=ON \
    -DJPEGXL_FORCE_SYSTEM_LCMS2=ON \
    %{?_enable_tools:-DJPEGXL_ENABLE_TOOLS=ON} \
    -DJPEGXL_ENABLE_MANPAGES=ON \
    %{?_enable_plugins:-DJPEGXL_ENABLE_PLUGINS=ON} \
    %{?_disable_tests:-DBUILD_TESTING=OFF} \
%nil
%cmake_build

%install
%cmake_install
rm -f %buildroot%_libdir/*.a

%check
%cmake_build -t test

%files
%_libdir/lib%{_name}*.so.%{sover}*

%changelog
* Thu Feb 22 2024 Yuri N. Sedunov <aris@altlinux.org> 0.8.2-alt2
- compat library

* Wed Jun 14 2023 Yuri N. Sedunov <aris@altlinux.org> 0.8.2-alt1
- 0.8.2

* Sat Feb 04 2023 Yuri N. Sedunov <aris@altlinux.org> 0.8.1-alt1
- 0.8.1

* Sun Jan 29 2023 Yuri N. Sedunov <aris@altlinux.org> 0.8.0-alt1
- 0.8.0

* Tue Dec 27 2022 Yuri N. Sedunov <aris@altlinux.org> 0.7.0-alt0.5
- first preview for Sisyphus
- built with bundled 'sjpeg' and 'skcms' libraries
- temporarily disabled armh build


