Name: dtkwm
Version: 2.0.12
Release: alt1
Summary: Deepin graphical user interface library
License: GPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dtkwm
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%name-%version.tar.gz

BuildRequires: gcc-c++ dtk5-core-devel libudev-devel qt5-base-devel-static qt5-x11extras-devel libX11-devel libxcb-devel libxcbutil-devel libXext-devel libXrender-devel

%description
DtkWm is used to handle double screen for deepin desktop development.
This package contains the shared libraries.

%package -n libdtk5-wm
Summary: Library for %name
Group: Graphical desktop/Other

%description -n libdtk5-wm
DtkWm is used to handle double screen for deepin desktop development.
This package contains the shared libraries.

%package -n dtk5-wm-devel
Summary: Development package for %name
Group: Graphical desktop/Other

%description -n dtk5-wm-devel
Header files and libraries for %name.

%prep
%setup

%build
%qmake_qt5 \
    CONFIG+=nostrip \
    PREFIX=%prefix \
    LIB_INSTALL_DIR=%_libdir \
    DTK_MODULE_NAME=%name
%make_build

%install
%makeinstall INSTALL_ROOT=%buildroot

%files -n libdtk5-wm
%doc README.md
%doc LICENSE
%_libdir/libdtkwm.so.*

%files -n dtk5-wm-devel
%_includedir/libdtk-*/
%_qt5_archdatadir/mkspecs/modules/qt_lib_dtkwm.pri
%dir %_libdir/cmake/DtkWm/
%_libdir/cmake/DtkWm/DtkWmConfig.cmake
%_pkgconfigdir/dtkwm.pc
%_libdir/libdtkwm.so

%changelog
* Thu Mar 05 2020 Leontiy Volodin <lvol@altlinux.org> 2.0.12-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).
