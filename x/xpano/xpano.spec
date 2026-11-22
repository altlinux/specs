%define _unpackaged_files_terminate_build 1

%ifarch loongarch64
%def_without check
%else
%def_with check
%endif

Name: xpano
Version: 0.19.3
Release: alt1

Summary: Automated panorama stiching tool
License: GPL-3.0-or-later
Group: Graphics
Url: https://github.com/krupkat/xpano

Source: %name-%version.tar
Source1: submodules-%name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-cmake

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(sdl2)
BuildRequires: pkgconfig(opencv5)
BuildRequires: pkgconfig(spdlog)
BuildRequires: pkgconfig(exiv2)
BuildRequires: pkgconfig(gtk+-3.0)

%if_with check
BuildRequires: ctest
BuildRequires: catch-devel
%endif

%description
Xpano is a tool for panorama stitching with focus on simplicity and ease
of use, major features include:

- Auto detection of groups of images that can be stitched into panoramas;
- Preview + zoom + pan of the computed panoramas;
- Crop mode, boundary auto fill, selectable projection types;
- Projection adjustments: pitch, yaw and roll;
- Export of full resolution panoramas including exif metadata.

%prep
%setup -a1
%patch -p1

mkdir opencv-compat
cat > opencv-compat/OpenCVConfig.cmake <<-'EOF'
    list(TRANSFORM OpenCV_FIND_COMPONENTS REPLACE "^(opencv_)?calib3d$" "calib")
    list(TRANSFORM OpenCV_FIND_COMPONENTS REPLACE "^(opencv_)?features2d$" "features")

    include("%_libdir/cmake/opencv5/OpenCVConfig.cmake")

    foreach(_pair "calib3d;calib" "features2d;features")
        list(GET _pair 0 _old)
        list(GET _pair 1 _new)
        if(TARGET opencv_${_new} AND NOT TARGET opencv_${_old})
        add_library(opencv_${_old} INTERFACE IMPORTED GLOBAL)
        set_target_properties(opencv_${_old} PROPERTIES
            INTERFACE_LINK_LIBRARIES opencv_${_new})
        endif()
    endforeach()
EOF

sed -i "s|Categories=.*|Categories=Graphics;2DGraphics;RasterGraphics;GTK;|" misc/build/linux/xpano.desktop

%build
%cmake \
       -DOpenCV_DIR="opencv-compat" \
%ifarch loongarch64
       -DXPANO_WITH_MULTIBLEND=OFF \
%endif
%if_with check
       -DBUILD_TESTING=ON
%else
       -DBUILD_TESTING=OFF
%endif

%cmake_build

%install
%cmake_install

%check
%ifarch riscv64
%ctest -E "Stitcher pipeline polling"
%else
%ctest
%endif

%files
%doc CONTRIBUTING.md LICENSE README.md
%_bindir/Xpano
%_desktopdir/xpano.desktop
%_iconsdir/hicolor/scalable/apps/xpano.svg
%_datadir/metainfo/cz.krupkat.Xpano.metainfo.xml
%_pixmapsdir/xpano.png
%dir %_datadir/xpano
%dir %_datadir/xpano/assets
%_datadir/xpano/assets/NotoSans-Regular.ttf
%_datadir/xpano/assets/NotoSansSymbols2-Regular.ttf
%_datadir/xpano/assets/OFL.txt
%_datadir/xpano/assets/icon.png
%dir %_datadir/xpano/licenses
%_datadir/xpano/licenses/CHANGELOG.md
%_datadir/xpano/licenses/alpaca-license.txt
%_datadir/xpano/licenses/exiv2-notice.txt
%_datadir/xpano/licenses/google-noto-license.txt
%_datadir/xpano/licenses/imgui-license.txt

%ifnarch loongarch64
%_datadir/xpano/licenses/multiblend-license.txt
%_datadir/xpano/licenses/multiblend-notice.txt
%endif

%_datadir/xpano/licenses/nativefiledialog-extended-license.txt
%_datadir/xpano/licenses/opencv-notice.txt
%_datadir/xpano/licenses/simde-license.txt
%_datadir/xpano/licenses/thread-pool-license.txt
%_datadir/xpano/licenses/xpano-license.txt

%changelog
* Sun Nov 22 2026 Nikolay Strelkov <snk@altlinux.org> 0.19.3-alt1
- Initial build for Sisyphus
