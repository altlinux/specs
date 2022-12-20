%def_disable clang
%def_disable docs

Name: dtkcore
Version: 5.6.3
Release: alt1
Summary: Deepin tool kit core modules
License: LGPL-2.1 and LGPL-3.0+ and GPL-3.0
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dtkcore
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%name-%version.tar.gz

%if_enabled clang
BuildRequires(pre): clang-devel
%else
BuildRequires(pre): gcc-c++
%endif
BuildRequires(pre): rpm-build-ninja
BuildRequires: cmake
BuildRequires: rpm-build-python3
BuildRequires: git-core
BuildRequires: glibc-core
BuildRequires: fdupes
BuildRequires: qt5-base-devel
BuildRequires: gsettings-qt-devel
BuildRequires: libgtest-devel
BuildRequires: dtk5-common
BuildRequires: doxygen qt5-tools

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

%if_enabled docs
%package -n dtk5-core-doc
Summary: %name documantation
Group: Documentation
BuildArch: noarch

%description -n dtk5-core-doc
This package provides %name documantation.
%endif

%prep
%setup
%if_disabled docs
sed -i '/\/docs\/html\/dtkcore.qch/d' \
  docs/CMakeLists.txt
%endif

%build
%if_enabled clang
export CC="clang"
export CXX="clang++"
export AR="llvm-ar"
export NM="llvm-nm"
export READELF="llvm-readelf"
%endif
export PATH=%_qt5_bindir:$PATH
%cmake \
  -GNinja \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DMKSPECS_INSTALL_DIR=%_qt5_archdatadir/mkspecs/modules/ \
  -DCMAKE_INSTALL_LIBDIR=%_libdir \
  -DDTK_VERSION=%version \
  -DVERSION=%version \
  -DLIB_INSTALL_DIR=%_libdir \
#
cmake --build %_cmake__builddir -j%__nprocs

%install
%cmake_install

%files -n dtk5-core
%doc README.md LICENSE
%_bindir/qdbusxml2cpp-fix

%files -n libdtk5-core
%_libdir/lib%name.so.5*
%dir %_libdir/libdtk-5*/
%_libdir/libdtk-5*/DCore/

%files -n dtk5-core-devel
%doc docs/Specification.md
%_libdir/lib%name.so
%_includedir/libdtk-*/
%_qt5_archdatadir/mkspecs/modules/*.pri
%_libdir/cmake/DtkCore/
%_libdir/cmake/DtkCMake/
%_libdir/cmake/DtkTools/
%_pkgconfigdir/dtkcore.pc

%if_enabled docs
%files -n dtk5-core-doc
%_qt5_datadir/doc/dtkcore.qch
%endif

%changelog
* Mon Dec 19 2022 Leontiy Volodin <lvol@altlinux.org> 5.6.3-alt1
- New version.
- Disabled doc subpackage.

* Fri Dec 02 2022 Leontiy Volodin <lvol@altlinux.org> 5.6.2.2-alt1
- New version.

* Fri Nov 11 2022 Leontiy Volodin <lvol@altlinux.org> 5.6.2.1-alt1
- New version.

* Fri Oct 14 2022 Leontiy Volodin <lvol@altlinux.org> 5.6.2-alt1
- New version.
- Upstream:
  + use cmake instead qmake.

* Wed Jun 08 2022 Leontiy Volodin <lvol@altlinux.org> 5.5.32-alt1
- New version.
- Upstream:
  + chore: dtkcore_config.h miss include some Class.

* Mon May 23 2022 Leontiy Volodin <lvol@altlinux.org> 5.5.31-alt1
- New version.
- Upstream:
  + fix: application crash when dconfig is invalid.
  + fix: DConfig can't find resource.

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
