%def_enable snapshot
%define _unpackaged_files_terminate_build 1

%define _name jxl
%define sover 0.10
%define libname lib%_name%sover

%def_enable tools
%def_enable man
%def_enable plugins
%def_enable gimp_plugin
%def_disable tests
%def_disable check

Name: lib%_name
Version: %sover.3
Release: alt1

Summary: JPEG XL image format reference implementation
License: BSD-3-Clause
Group: System/Libraries
Url: https://github.com/libjxl/libjxl

%if_disabled snapshot
Source: https://github.com/libjxl/libjxl/archive/v%version/%name-%version.tar.gz
%else
Vcs: https://github.com/libjxl/libjxl.git
Source: %name-%version.tar
%endif

%define gif_ver 5.1
%define hwy_ver 1.1.0

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++ ninja-build
#BuildRequires: libgif-devel >= %gif_ver
BuildRequires: highway-devel >= %hwy_ver
BuildRequires: libjpeg-devel openexr-devel libpng-devel libwebp-devel
BuildRequires: libavif-devel libbrotli-devel liblcms2-devel zlib-devel
%{?_enable_plugins:BuildRequires: libgdk-pixbuf-devel}
%{?_enable_gimp_plugin:BuildRequires: libgimp-devel}
%{?_enable_man:BuildRequires: asciidoc-a2x}
%{?_enable_tests:BuildRequires: libgtest-devel}
%{?_enable_check:BuildRequires: ctest}

%description
JPEG XL image format reference implementation Library.

%package -n %libname
Summary: JPEG XL image format reference implementation Library.
Group: System/Libraries
Requires: %name-pixbuf-loader = %EVR
Obsoletes: %name < 0.9

%description -n %libname
This package provides shared JPEG XL libraries.

%package pixbuf-loader
Summary: JPEG XL image loader for GTK+ applications
Group: System/Libraries
Conflicts: %name < 0.9

%description pixbuf-loader
This package provides JPEG XL image loader for gdk-pixbuf.

%package devel
Summary: Development files for JPEG XL library
Group: Development/C++
Requires: %libname = %EVR

%description devel
This package provides JPEG XL development files.

%package tools
Summary: The JPEG XL library command line tools
Group: Graphics
Requires: %libname = %EVR

%description tools
This package provides JPEG XL tools.

%package -n gimp-plugin-%name
Summary: JPEG XL plugin for GIMP
Group: Graphics
Requires: %libname = %EVR
Requires: gimp

%description -n gimp-plugin-%name
This package provides JPEG XL support for GIMP.

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
    %{?_enable_plugins:-DJPEGXL_ENABLE_PLUGINS=ON} \
    %{?_disable_tests:-DBUILD_TESTING=OFF} \
%nil
%cmake_build

%install
%cmake_install
rm -f %buildroot%_libdir/*.a

%check
%cmake_build -t test

%files -n %libname
%_libdir/%{name}*.so.%{sover}*
%doc AUTHORS README* PATENTS

%{?_enable_plugins:
%files pixbuf-loader
%_libdir/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-jxl.so
%_datadir/thumbnailers/jxl.thumbnailer
%_datadir/mime/packages/image-jxl.xml
%{?_enable_gimp_plugin:
%files -n gimp-plugin-%name
%_libdir/gimp/2.0/plug-ins/file-jxl/file-jxl}
}

%files devel
%_libdir/%{name}*.so
%_includedir/%_name/
%_pkgconfigdir/%{name}*.pc

%if_enabled tools
%files tools
%_bindir/c%_name
%_bindir/d%_name
%_bindir/benchmark_xl
%_bindir/cjpegli
%_bindir/djpegli
%_bindir/%{_name}info
%{?_enable_man:%_man1dir/c%_name.1*
%_man1dir/d%_name.1*}
%endif

%changelog
* Thu Jun 27 2024 Yuri N. Sedunov <aris@altlinux.org> 0.10.3-alt1
- 0.10.3

* Fri Mar 08 2024 Yuri N. Sedunov <aris@altlinux.org> 0.10.2-alt1
- 0.10.2

* Wed Feb 28 2024 Yuri N. Sedunov <aris@altlinux.org> 0.10.1-alt1
- 0.10.1

* Sat Feb 24 2024 Yuri N. Sedunov <aris@altlinux.org> 0.10.0-alt1.2
- moved gdk-pixbuf loader to separate package
- new gimp-plugin-libjxl package

* Thu Feb 22 2024 Yuri N. Sedunov <aris@altlinux.org> 0.10.0-alt1.1
- enabled plugins again

* Thu Feb 22 2024 Yuri N. Sedunov <aris@altlinux.org> 0.10.0-alt1
- 0.10.0

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


