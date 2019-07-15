Name: dtkgui
Version: 5.2.2.1
Release: alt1
Summary: Deepin Toolkit, gui module for DDE look and feel
License: LGPL-3.0 and GPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dtkgui
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%name-%version.tar.gz

BuildRequires: gcc-c++ dtk5-core-devel qt5-x11extras-devel librsvg-devel

%description
Deepin Toolkit, gui module for DDE look and feel.

%package -n libdtk5-gui
Summary: Library for %name
Group: Graphical desktop/Other

%description -n libdtk5-gui
DtkGui is used for DDE look and feel.
This package contains the shared libraries.

%package -n dtk5-gui-devel
Summary: Development package for %name
Group: Graphical desktop/Other

%description -n dtk5-gui-devel
Header files and libraries for %name.

%prep
%setup

%build
%qmake_qt5 \
    "CONFIG += nostrip" \
    PREFIX=%_prefix \
    LIB_INSTALL_DIR=%_libdir \
    DTK_VERSION=%version
%make_build

%install
%makeinstall INSTALL_ROOT=%buildroot

%files -n libdtk5-gui
%doc README.md
%doc LICENSE
%_libdir/libdtkgui.so.5*
%dir %_libdir/libdtk-5*/
%_libdir/libdtk-5*/DGui/
%_sysconfdir/dbus-1/system.d/com.deepin.dtk.FileDrag.conf

%files -n dtk5-gui-devel
%_includedir/libdtk-5*/
%_qt5_archdatadir/mkspecs/modules/qt_lib_dtkgui.pri
%dir %_libdir/cmake/DtkGui/
%_libdir/cmake/DtkGui/DtkGuiConfig.cmake
%_pkgconfigdir/dtkgui.pc
%_libdir/libdtkgui.so

%changelog
* Wed Jul 29 2020 Leontiy Volodin <lvol@altlinux.org> 5.2.2.1-alt1
- Initial build for ALT Sisyphus.
