%define _libexecdir %_prefix/libexec
%define sover 0

%def_disable clang

Name: treeland
Version: 0.8.8
Release: alt1

Summary: Wayland compositor for DDE

License: GPL-2.0-or-later and CC-BY-3.0
Group: System/Configuration/Other
Url: https://github.com/linuxdeepin/treeland
Vcs: https://github.com/linuxdeepin/treeland

# Source-url: %url/archive/%version/%name-%version.tar.xz
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-dqt6 rpm-build-ninja patchelf
# Automatically added by buildreq on Fri Feb 21 2025
# optimized out: cmake-modules dqt6-base-common dqt6-base-devel dqt6-declarative-devel dqt6-tools gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 libX11-devel libcap-ng libcrypt-devel libddm-auth-devel libddm-auth0 libddm-common-devel libddm-common0 libdisplay-info libdouble-conversion3 libdqt6-concurrent libdqt6-core libdqt6-dbus libdqt6-gui libdqt6-network libdqt6-opengl libdqt6-qml libdqt6-qmlcompiler libdqt6-qmlmodels libdqt6-qmlworkerscript libdqt6-quick libdqt6-quickcontrols2 libdqt6-quickcontrols2basic libdqt6-quickcontrols2fusion libdqt6-quickcontrols2imagine libdqt6-quickcontrols2material libdqt6-quickcontrols2universal libdqt6-quickeffects libdqt6-quicklayouts libdqt6-quickshapes libdqt6-quicktemplates2 libdqt6-quicktest libdqt6-shadertools libdqt6-test libdqt6-waylandclient libdqt6-widgets libdqt6-xml libdtk6core-devel libdtk6gui-devel libdtk6log-devel libglvnd-devel libgpg-error libp11-kit libpixman-devel libsasl2-3 libssl-devel libstdc++-devel libudev-devel libwayland-client libwayland-client-devel libwayland-cursor libwayland-cursor-devel libwayland-server libwayland-server-devel libxcb-devel libxcb-render-util libxcbutil-errors libxcbutil-icccm libxkbcommon-devel ninja-build openssl-config pkg-config python3 python3-base sh5 vulkan-headers wayland-devel xorg-proto-devel xz
BuildRequires: cmake ddm-devel dqt6-shadertools-devel dqt6-tools-devel dqt6-declarative-devel dqt6-wayland-devel dtk6-common-devel libdtk6declarative-devel libdtk6systemsettings-devel libpam-devel libsystemd-devel libwayland-egl-devel libwlroots-devel libxcbutil-icccm-devel treeland-protocols wayland-protocols libdrm-devel wlr-protocols libinput-devel libXau-devel libmpv-devel dqt6-remoteobjects-devel
BuildRequires: libdqt6-qmlcompiler libdqt6-quicktemplates2 libdqt6-quickcontrols2 libdqt6-quicktest libdqt6-concurrent vulkan-headers
%if_enabled clang
BuildRequires: clang-devel lld-devel
%else
BuildRequires: gcc-c++ 
%endif

Requires: libdqt6-qml = %_dqt6_version

%add_findprov_lib_path %_dqt6_libdir

%description
Treeland is a wayland compositor based on wlroots and QtQuick, designed
to provide efficient and flexible graphical interface support.

%package data
Summary: Data files for %name
Group: System/Configuration/Other
BuildArch: noarch

%description data
This package provides data files for %name.

%package wayland-session
Summary: Wayland files for %name
Group: System/Configuration/Other
BuildArch: noarch

%description wayland-session
This package provides wayland files for %name.

%package wallpaper-factory
Summary: Wallpaper factory tool for %name
Group: System/Configuration/Other
Requires: libdqt6-gui = %_dqt6_version
Requires: libdqt6-quick = %_dqt6_version
Requires: libdqt6-waylandclient = %_dqt6_version

%description wallpaper-factory
This package provides wallpaper factory tool for %name.

%package -n libtreeland%sover
Summary: Library for %name
Group: System/Libraries
Requires: libdqt6-core = %_dqt6_version
Requires: libdqt6-gui = %_dqt6_version
Requires: libdqt6-qml = %_dqt6_version
Requires: libdqt6-quick = %_dqt6_version

%description -n libtreeland%sover
This package provides main library for %name.

%package -n libtreeland-protocol-capture-v1_%sover
Summary: treeland-protocol-capture-v1 library for %name
Group: System/Libraries
Requires: libdqt6-quick = %_dqt6_version

%description -n libtreeland-protocol-capture-v1_%sover
This package provides treeland-protocol-capture-v1 library for %name.

%package -n lib%name-devel
Summary: Development files for %name
Group: Development/C++

%description -n lib%name-devel
This package provides development files for %name.

%package -n libdwaylibserver%sover
Summary: waylibserver library for %name
Group: System/Libraries
Requires: libdqt6-core = %_dqt6_version
Requires: libdqt6-gui = %_dqt6_version
Requires: libdqt6-qml = %_dqt6_version
Requires: libdqt6-quick = %_dqt6_version

%description -n libdwaylibserver%sover
This package provides waylibserver library for %name.

%package -n libdwaylibserver-devel
Summary: Development files for waylibserver
Group: Development/C++

%description -n libdwaylibserver-devel
This package provides development files for waylibserver.

%package -n libdqwlroots%sover
Summary: qwlroots library for %name
Group: System/Libraries
Requires: libdqt6-core = %_dqt6_version

%description -n libdqwlroots%sover
This package provides qwlroots library for %name.

%package -n libdqwlroots-devel
Summary: Development files for qwlroots
Group: Development/C++

%description -n libdqwlroots-devel
This package provides development files for qwlroots.

%package -n libdwaylib-devel
Summary: Development files for waylib
Group: Development/C++

%description -n libdwaylib-devel
This package provides development files for waylib.

%prep
%setup
%autopatch -p1
sed -i 's|${TREELAND_DATA_DIR}/qml/Treeland|%_dqt6_qmldir|' \
  src/CMakeLists.txt
sed -i 's|${TREELAND_DATA_DIR}/qml|%_dqt6_qmldir|' \
  src/modules/capture/CMakeLists.txt
sed -i '/add_library(\${TARGET}/a SHARED' \
  qwlroots/src/CMakeLists.txt
sed -e 's|CMAKE_INSTALL_LIBDIR|DCMAKE_INSTALL_LIBDIR|g;' \
    -e 's|CMAKE_INSTALL_INCLUDEDIR|DCMAKE_INSTALL_INCLUDEDIR|g;' \
    -i $(find ./waylib -name 'CMakeLists.txt' -o -name '*.cmake') \
       $(find ./qwlroots -name 'CMakeLists.txt' -o -name '*.cmake')

%build
%if_enabled clang
%define optflags_lto -flto=thin
export CC=clang
export CXX=clang++
export LDFLAGS="-fuse-ld=lld $LDFLAGS"
%endif
%DQ6build \
  -DWITH_SUBMODULE_WAYLIB=ON \
  -DBUILD_TESTS=OFF \
  -DBUILD_EXAMPLES=OFF \
  -DDCMAKE_INSTALL_LIBDIR=%_dqt6_libdir \
  -DDCMAKE_INSTALL_INCLUDEDIR=%_dqt6_headerdir

%install
%DQ6install
# cleanup illegal rpaths
patchelf %buildroot%_libdir/libtreeland-protocol-capture-v1.so.%sover --add-needed libtreeland.so.%sover

# package translations
%find_lang --with-qt treeland

%files -f treeland.lang
%doc LICENSES/ README*.md debian/changelog
%_bindir/treeland
%_bindir/treeland.sh
%_libexecdir/treeland-sd
%_libexecdir/treeland-screensaver
%_libexecdir/treeland-session-helper
%_libexecdir/treeland-xwayland
%_unitdir/treeland.service
%_datadir/dbus-1/system.d/org.deepin.compositor1.conf
%dir %_userunitdir/dde-session-pre.target.wants/
%_userunitdir/dde-session-pre.target.wants/treeland*
%dir %_userunitdir/dde-session-shutdown.target.wants/
%_userunitdir/dde-session-shutdown.target.wants/treeland*
%_userunitdir/treeland*
%dir %_libdir/treeland/
%_libdir/treeland/plugins/
%dir %_datadir/treeland/
%dir %_datadir/treeland/translations

%files data
%dir %_datadir/dsg/
%dir %_datadir/dsg/configs/
%_datadir/dsg/configs/org.deepin.dde.treeland/
%dir %_datadir/treeland/
%_datadir/wayland-sessions/treeland.desktop
%_datadir/dbus-1/interfaces/org.freedesktop.ScreenSaver.xml

%files wayland-session
%_bindir/treeland-user-wrapper
%_datadir/wayland-sessions/treeland-user.desktop

%files wallpaper-factory
%_bindir/treeland-wallpaper-factory

%files -n libtreeland%sover
%_libdir/libtreeland.so.%{sover}*

%files -n libtreeland-protocol-capture-v1_%sover
%_libdir/libtreeland-protocol-capture-v1.so.%{sover}*

%files -n lib%name-devel
%_libdir/libtreeland.so
%_libdir/libtreeland-protocol-capture-v1.so
%dir %_includedir/treeland/
%dir %_includedir/treeland/modules/
%_includedir/treeland/modules/personalization/
%_libdir/cmake/treeland/

%files -n libdwaylibserver%sover
%_dqt6_libdir/libwaylibserver.so.%{sover}*

%files -n libdwaylibserver-devel
%_dqt6_libdir/libwaylibserver.so
%_dqt6_headerdir/waylibserver/
%_dqt6_libdir/cmake/WaylibServer/
%_dqt6_libdir/pkgconfig/waylibserver.pc

%files -n libdqwlroots%sover
%_dqt6_libdir/libqwlroots.so.%{sover}*

%files -n libdqwlroots-devel
%_dqt6_libdir/libqwlroots.so
%_dqt6_headerdir/qwlroots/
%_dqt6_libdir/cmake/QWlroots/
%_dqt6_libdir/pkgconfig/qwlroots.pc

%files -n libdwaylib-devel
%_dqt6_libdir/cmake/Waylib/

%changelog
* Thu Jun 11 2026 Leontiy Volodin <lvol@altlinux.org> 0.8.8-alt1
- New version 0.8.8.

* Tue May 12 2026 Leontiy Volodin <lvol@altlinux.org> 0.8.6-alt1
- New version 0.8.6.

* Fri Mar 27 2026 Leontiy Volodin <lvol@altlinux.org> 0.8.5-alt1
- New version 0.8.5.

* Wed Mar 04 2026 Leontiy Volodin <lvol@altlinux.org> 0.8.4-alt1
- New version 0.8.4.

* Fri Feb 27 2026 Leontiy Volodin <lvol@altlinux.org> 0.8.3-alt1
- New version 0.8.3.

* Tue Nov 18 2025 Leontiy Volodin <lvol@altlinux.org> 0.7.8-alt1
- New version 0.7.8.

* Tue Nov 11 2025 Leontiy Volodin <lvol@altlinux.org> 0.7.7-alt2
- Enabled wayland session only.

* Mon Nov 10 2025 Leontiy Volodin <lvol@altlinux.org> 0.7.7-alt1
- New version 0.7.7.

* Fri Oct 31 2025 Leontiy Volodin <lvol@altlinux.org> 0.7.6-alt1
- New version 0.7.6.

* Mon Oct 20 2025 Leontiy Volodin <lvol@altlinux.org> 0.7.4-alt1
- New version 0.7.4.

* Wed Sep 24 2025 Leontiy Volodin <lvol@altlinux.org> 0.7.3-alt1
- New version 0.7.3.
- Packaged data and wayland files separately.

* Fri Sep 19 2025 Leontiy Volodin <lvol@altlinux.org> 0.7.2-alt1
- New version 0.7.2.

* Tue Sep 02 2025 Leontiy Volodin <lvol@altlinux.org> 0.7.0-alt1
- New version 0.7.0.

* Tue Aug 05 2025 Leontiy Volodin <lvol@altlinux.org> 0.6.2-alt1
- New version 0.6.2.

* Tue Jul 29 2025 Leontiy Volodin <lvol@altlinux.org> 0.5.21.0.13.a613-alt1
- New version 0.5.21-13-ga6134c2.

* Mon Jun 23 2025 Leontiy Volodin <lvol@altlinux.org> 0.5.21.0.7.7acf-alt1
- New version 0.5.21-7-g7acf621 (Qt6.9).

* Mon Apr 21 2025 Leontiy Volodin <lvol@altlinux.org> 0.5.21-alt1
- New version 0.5.21.

* Fri Mar 14 2025 Leontiy Volodin <lvol@altlinux.org> 0.5.20-alt1
- New version 0.5.20.

* Fri Mar 07 2025 Leontiy Volodin <lvol@altlinux.org> 0.5.19-alt1.1
- Fixed BuildRequires.

* Wed Mar 05 2025 Leontiy Volodin <lvol@altlinux.org> 0.5.19-alt1
- New version 0.5.19.

* Tue Mar 04 2025 Leontiy Volodin <lvol@altlinux.org> 0.5.17-alt1
- Initial build for ALT Sisyphus.
