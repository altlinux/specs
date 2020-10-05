Name: dtkcore
Version: 5.2.2.15
Release: alt1
Summary: Deepin tool kit core modules
License: LGPL-2.1 and LGPL-3.0+ and GPL-3.0
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dtkcore
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%name-%version.tar.gz

BuildRequires: gcc-c++ git-core fdupes qt5-linguist qt5-declarative-devel qt5-multimedia-devel qt5-x11extras-devel gsettings-qt-devel

%description
Deepin tool kit core modules.

%package -n libdtk5-core
Summary: Libraries for %name
Group: System/Libraries

%description -n libdtk5-core
Deepin tool kit core modules.
Libraries for %name.

%package -n dtk5-core-devel
Summary: Development package for %name
Group: Development/KDE and QT
Requires: qt5-base-devel

%description -n dtk5-core-devel
Header files and libraries for %name.

%prep
%setup

%build
%__subst 's/system(lrelease/system(lrelease-qt5/g' src/dtk_translation.prf
%qmake_qt5 \
    CONFIG+=nostrip \
    PREFIX=%prefix \
    DTK_VERSION=%version \
    LIB_INSTALL_DIR=%_libdir \
    DEEPIN_OS_TYPE=ALT \
    DEEPIN_OS_VERSION=9
%make_build

%install
%makeinstall INSTALL_ROOT=%buildroot

%files -n libdtk5-core
%doc README.md LICENSE
%_libdir/lib%name.so.5*
%dir %_libdir/libdtk-5*/
%_libdir/libdtk-5*/DCore/
%_datadir/glib-2.0/schemas/com.deepin.dtk.gschema.xml

%files -n dtk5-core-devel
%doc doc/Specification.md
%_libdir/lib%name.so
%_includedir/libdtk-*/
%_qt5_archdatadir/mkspecs/features/*.prf
%_qt5_archdatadir/mkspecs/modules/*.pri
%_libdir/cmake/Dtk/
%_libdir/cmake/DtkCore/
%_libdir/cmake/DtkCMake/
%_libdir/cmake/DtkTools/
%_pkgconfigdir/dtkcore.pc

%changelog
* Mon Oct 05 2020 Leontiy Volodin <lvol@altlinux.org> 5.2.2.15-alt1
- New version (5.2.2.15) with rpmgs script.

* Mon Aug 17 2020 Leontiy Volodin <lvol@altlinux.org> 5.2.2.3-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).
