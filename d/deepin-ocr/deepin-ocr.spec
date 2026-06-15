%def_disable clang
%def_disable check

Name: deepin-ocr
Version: 6.5.16
Release: alt2

Summary: Base character recognition ability on DDE

License: GPL-3.0+
Group: Graphics
Url: https://github.com/linuxdeepin/deepin-ocr
Vcs: https://github.com/linuxdeepin/deepin-ocr

# Source-url: https://github.com/linuxdeepin/deepin-ocr/archive/%version/%name-%version.tar.gz
Source: %name-%version.tar
Patch: %name-%version-%release.patch

# Automatically added by buildreq on Wed Apr 23 2025
# optimized out: cmake cmake-modules dqt6-base-common dqt6-base-devel dqt6-tools gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 libclang-cpp19 libdouble-conversion3 libdqt6-core libdqt6-dbus libdqt6-gui libdqt6-network libdqt6-printsupport libdqt6-qml libdqt6-waylandclient libdqt6-widgets libdqt6-xml libdtk6core-devel libdtk6gui-devel libdtk6log-devel libglvnd-devel libgpg-error libjson-c5 libp11-kit libsasl2-3 libssl-devel libstartup-notification libstdc++-devel libwayland-client libwayland-cursor libxkbcommon-devel llvm19.1-libs ninja-build pkg-config python3 python3-base sh5 vulkan-headers
BuildRequires: dqt6-tools-devel dtk6-common-devel libGLU-devel libdtk6ocr-devel libdtk6widget-devel python3-devel libncnn-devel deepin-libopencv_world-devel libwayland-client-devel
BuildRequires: libcups-devel libdqt6-qml
%if_enabled clang
BuildRequires: rpm-macros-llvm-common
BuildRequires: clang-devel lld-devel libomp%_llvm_version-devel
%else
BuildRequires: gcc-c++ libgomp-devel
%endif
%if_enabled check
BuildRequires: ctest libgtest-devel
%if_enabled clang
BuildRequires: clang%_llvm_version-support
%else
BuildRequires: libasan-devel-static
%endif
%endif

%description
Deepin OCR provides the base character recognition ability on DDE.

%prep
%setup
%patch -p1
# deepin's opencv_mobile does not have .pc file
sed -i 's| opencv_mobile||' src/CMakeLists.txt

%build
%if_enabled clang
%define optflags_lto -flto=thin
export CC=clang
export CXX=clang++
export LDFLAGS="-fuse-ld=lld $LDFLAGS"
%endif
export CPLUS_INCLUDE_PATH=%_includedir/deepin/opencv4:%_includedir/opencv4:$CPLUS_INCLUDE_PATH
export LIBS=" -L%_libdir/deepin -lopencv_world":$LIBS
%if_enabled check
export CPLUS_INCLUDE_PATH=%_dqt6_headerdir/QtTest:$CPLUS_INCLUDE_PATH
%endif
%DQ6build

%install
%DQ6install
%find_lang --with-qt %name

%if_enabled check
%check
%ctest --test-dir BUILD
%endif

%files -f %name.lang
%doc debian/changelog
%doc LICENSE README*.md
%_bindir/%name
%_desktopdir/%name.desktop
%_datadir/dbus-1/services/com.deepin.Ocr.service
%_iconsdir/hicolor/scalable/apps/%name.svg
%dir %_datadir/dsg/
%dir %_datadir/dsg/configs/
%dir %_datadir/dsg/configs/%name/
%_datadir/dsg/configs/%name/%name.common.json
%dir %_datadir/%name/
%dir %_datadir/%name/translations/
%_datadir/%name/translations/deepin-ocr_es_419.qm
%_datadir/%name/translations/deepin-ocr_ky@Arab.qm

%changelog
* Mon Jun 15 2026 Leontiy Volodin <lvol@altlinux.org> 6.5.16-alt2
- Fixed build on dqt6-declarative 6.10.3.

* Mon Jan 26 2026 Leontiy Volodin <lvol@altlinux.org> 6.5.16-alt1
- New version 6.5.16.
- Fixed build on dtk 6.7.31.

* Mon Dec 15 2025 Leontiy Volodin <lvol@altlinux.org> 6.5.15-alt1
- New version 6.5.15.

* Thu Nov 20 2025 Leontiy Volodin <lvol@altlinux.org> 6.5.12-alt1
- New version 6.5.12.

* Mon Oct 27 2025 Leontiy Volodin <lvol@altlinux.org> 6.5.11-alt1
- New version 6.5.11.

* Fri Sep 12 2025 Leontiy Volodin <lvol@altlinux.org> 6.5.9-alt1
- New version 6.5.9.

* Fri Jun 27 2025 Leontiy Volodin <lvol@altlinux.org> 6.5.6-alt1
- New version 6.5.6.

* Tue May 06 2025 Leontiy Volodin <lvol@altlinux.org> 6.5.1-alt1
- New version 6.5.1.

* Wed Apr 23 2025 Leontiy Volodin <lvol@altlinux.org> 6.5.0-alt1
- New version 6.5.0.
- Added vcs tag.
- Switched to dqt6.

* Tue Sep 10 2024 Leontiy Volodin <lvol@altlinux.org> 1.0.7-alt2
- Built via separate qt5 instead system (ALT #48138).

* Fri Feb 03 2023 Leontiy Volodin <lvol@altlinux.org> 1.0.7-alt1
- Initial build for ALT Sisyphus.
