%def_disable clang

Name: dtkwidget
Version: 5.5.44
Release: alt1
Summary: Deepin tool kit widget modules
License: LGPL-3.0+ and GPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dtkwidget
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%name-%version.tar.gz

%if_enabled clang
BuildRequires(pre): clang12.0-devel
%endif
BuildRequires: qt5-linguist
BuildRequires: qt5-base-devel-static
BuildRequires: qt5-svg-devel
BuildRequires: qt5-x11extras-devel
BuildRequires: dtk5-core-devel
BuildRequires: dtk5-gui-devel
BuildRequires: dtk5-common
BuildRequires: gsettings-qt-devel
BuildRequires: deepin-qt-dbus-factory-devel
BuildRequires: libudev-devel
BuildRequires: librsvg-devel
BuildRequires: libstartup-notification-devel
BuildRequires: libXi-devel
BuildRequires: libX11-devel
BuildRequires: libXext-devel
BuildRequires: libxcbutil-devel
BuildRequires: libxkbcommon-devel
BuildRequires: libXrender-devel
BuildRequires: libcups-devel
BuildRequires: libgtest-devel
# libQt5Gui.so.5(Qt_5_PRIVATE_API)(64bit) needed by dtkwidget
BuildRequires: libqt5-gui

%description
DtkWidget is Deepin graphical user interface for deepin desktop development.

%package -n libdtk5-widget
Summary: Libraries for %name
Group: System/Libraries

%description -n libdtk5-widget
DtkWidget is Deepin graphical user interface for deepin desktop development.
Libraries for %name.

%package -n dtk5-widget-devel
Summary: Development package for %name
Group: Development/KDE and QT

%description -n dtk5-widget-devel
Header files and libraries for %name.

%package -n dtk5-widget-examples
Summary: Examples for %name
Group: Development/KDE and QT

%description -n dtk5-widget-examples
DtkWidget is Deepin graphical user interface for deepin desktop development.
Examples for %name.

%prep
%setup
sed -i "s|'/lib'|'/%_lib'|" conanfile.py
sed -i 's|dtkBuildMultiVersion(5.5)|dtkBuildMultiVersion|' \
    src/src.pro
sed -i 's|$$QT.dtkcore.libs/examples|$$QT.dtkcore.libs/dtkwidget5-examples|' \
    examples/dwidget-examples/collections/collections.pro

%build
export PATH=%{_qt5_bindir}:$PATH
%qmake_qt5 \
%if_enabled clang
    QMAKE_STRIP= -spec linux-clang \
%endif
    CONFIG+=nostrip \
    PREFIX=%_prefix \
    LIB_INSTALL_DIR=%_libdir \
    VERSION=%version \
#

%make_build

%install
%makeinstall INSTALL_ROOT=%buildroot

%files -n libdtk5-widget
%doc README.md LICENSE
%_libdir/lib%name.so.5*
%dir %_libdir/libdtk-5*/
%dir %_libdir/libdtk-5*/DWidget/
%_libdir/libdtk-5*/DWidget/bin/
%_datadir/libdtk-5*/

%files -n dtk5-widget-devel
%_includedir/libdtk-5*/
%_qt5_archdatadir/mkspecs/modules/*.pri
%_libdir/cmake/DtkWidget/
%_pkgconfigdir/%name.pc
%_libdir/lib%name.so

%files -n dtk5-widget-examples
%_libdir/dtkwidget5-examples/

%changelog
* Wed May 04 2022 Leontiy Volodin <lvol@altlinux.org> 5.5.44-alt1
- New version (5.5.44).

* Tue Mar 22 2022 Leontiy Volodin <lvol@altlinux.org> 5.5.42-alt1
- New version (5.5.42).

* Tue Feb 08 2022 Leontiy Volodin <lvol@altlinux.org> 5.5.37-alt1
- New version (5.5.37).

* Tue Jul 06 2021 Leontiy Volodin <lvol@altlinux.org> 5.5.17.1-alt1
- New version (5.5.17.1).

* Mon Jun 28 2021 Leontiy Volodin <lvol@altlinux.org> 5.5.7-alt1
- New version (5.5.7) with rpmgs script.

* Mon May 17 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.20-alt1
- New version (5.4.20) with rpmgs script.

* Thu Apr 08 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.16-alt1
- New version (5.4.16) with rpmgs script.

* Tue Mar 09 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.10-alt1
- New version (5.4.10) with rpmgs script.

* Mon Nov 30 2020 Leontiy Volodin <lvol@altlinux.org> 5.4.1-alt1
- New version (5.4.1) with rpmgs script.

* Wed Oct 28 2020 Leontiy Volodin <lvol@altlinux.org> 5.3.0-alt1
- New version (5.3.0) with rpmgs script.

* Mon Oct 05 2020 Leontiy Volodin <lvol@altlinux.org> 5.2.2.15-alt1
- New version (5.2.2.15) with rpmgs script.

* Mon Aug 17 2020 Leontiy Volodin <lvol@altlinux.org> 5.2.2.3-alt1
- Initial build for ALT Sisyphus (thanks fedora and archlinux for this spec).
