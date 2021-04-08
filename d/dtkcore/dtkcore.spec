%def_disable clang

Name: dtkcore
Version: 5.4.13
Release: alt1
Summary: Deepin tool kit core modules
License: LGPL-2.1 and LGPL-3.0+ and GPL-3.0
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dtkcore
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%name-%version.tar.gz

%if_enabled clang
BuildRequires(pre): clang11.0-devel
%else
BuildRequires(pre): gcc-c++
%endif
BuildRequires: git-core
BuildRequires: glibc-core
BuildRequires: fdupes
BuildRequires: qt5-base-devel
BuildRequires: gsettings-qt-devel
BuildRequires: libgtest-devel
BuildRequires: dtk5-common

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
%qmake_qt5 \
%if_enabled clang
    QMAKE_STRIP= -spec linux-clang \
%endif
    CONFIG+=nostrip \
    PREFIX=%prefix \
    DTK_VERSION=%version \
    VERSION=%version \
    LIB_INSTALL_DIR=%_libdir \
    unix:LIBS+="-ldl" \
    DEEPIN_OS_TYPE=Desktop \
    DEEPIN_OS_VERSION=20.2 \
#
%make_build

%install
%makeinstall INSTALL_ROOT=%buildroot
chmod +x %buildroot%_libdir/libdtk-%version/DCore/bin/dtk-license.py
chmod +x %buildroot%_libdir/libdtk-%version/DCore/bin/dtk-translate.py

%files -n libdtk5-core
%doc README.md LICENSE
%_libdir/lib%name.so.5*
%dir %_libdir/libdtk-5*/
%_libdir/libdtk-5*/DCore/

%files -n dtk5-core-devel
%doc doc/Specification.md
%_libdir/lib%name.so
%_includedir/libdtk-*/
%_qt5_archdatadir/mkspecs/modules/*.pri
%_libdir/cmake/DtkCore/
%_libdir/cmake/DtkCMake/
%_libdir/cmake/DtkTools/
%_pkgconfigdir/dtkcore.pc

%changelog
* Thu Apr 08 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.13-alt1
- New version (5.4.13) with rpmgs script.

* Tue Mar 09 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.10-alt1
- New version (5.4.10) with rpmgs script.

* Thu Dec 03 2020 Leontiy Volodin <lvol@altlinux.org> 5.4.0-alt1
- New version (5.4.0) with rpmgs script.

* Mon Nov 30 2020 Leontiy Volodin <lvol@altlinux.org> 5.2.2.16-alt1
- New version (5.2.2.16) with rpmgs script.

* Mon Oct 05 2020 Leontiy Volodin <lvol@altlinux.org> 5.2.2.15-alt1
- New version (5.2.2.15) with rpmgs script.

* Mon Aug 17 2020 Leontiy Volodin <lvol@altlinux.org> 5.2.2.3-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).
