%def_disable clang

Name: dtkcore
Version: 5.5.30
Release: alt1
Summary: Deepin tool kit core modules
License: LGPL-2.1 and LGPL-3.0+ and GPL-3.0
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dtkcore
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%name-%version.tar.gz

%if_enabled clang
BuildRequires(pre): clang12.0-devel
%else
BuildRequires(pre): gcc-c++
%endif
BuildRequires: rpm-build-python3
BuildRequires: git-core
BuildRequires: glibc-core
BuildRequires: fdupes
BuildRequires: qt5-base-devel
BuildRequires: gsettings-qt-devel
BuildRequires: libgtest-devel
BuildRequires: dtk5-common

%description
Deepin tool kit core modules.

%package -n dtk5-core
Summary: %summary
Group: Graphical desktop/Other

%description -n dtk5-core
Deepin tool kit core modules.
Binaries for %name.

%package -n libdtk5-core
Summary: Libraries for %name
Group: System/Libraries
Requires: dtk5-core

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
chmod +x tools/script/dtk-{license,translate}.py
sed -i 's|dtkBuildMultiVersion(5.5)|dtkBuildMultiVersion|'  \
    src/src.pro

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
    DEEPIN_OS_VERSION=20.4 \
#
%make_build

%install
%makeinstall INSTALL_ROOT=%buildroot

%files -n dtk5-core
%doc README.md LICENSE
%_bindir/qdbusxml2cpp-fix

%files -n libdtk5-core
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
* Fri Apr 08 2022 Leontiy Volodin <lvol@altlinux.org> 5.5.30-alt1
- New version (5.5.30).

* Tue Feb 08 2022 Leontiy Volodin <lvol@altlinux.org> 5.5.23-alt1
- New version (5.5.23).

* Tue Jul 06 2021 Leontiy Volodin <lvol@altlinux.org> 5.5.17.1-alt1
- New version (5.5.17.1).

* Wed Jun 30 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.17-alt1
- New version (5.4.17).

* Mon May 17 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.15-alt1
- New version (5.4.15) with rpmgs script.

* Thu May 06 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.13-alt2
- Added rpm-build-python3 into BR.

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
