%def_disable clang
%def_disable docs

%define llvm_ver 15

Name: dtkcore
Version: 5.6.8
Release: alt1
Summary: Deepin tool kit core modules
License: LGPL-2.1 and LGPL-3.0+ and GPL-3.0
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dtkcore
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%name-%version.tar.gz
Patch: dtkcore-5.6.5-alt-fix-underlinked-libraries.patch

%if_enabled clang
#BuildRequires(pre): rpm-macros-llvm-common
BuildRequires: clang%llvm_ver.0-devel
BuildRequires: lld%llvm_ver.0-devel
BuildRequires: llvm%llvm_ver.0-devel
%else
BuildRequires(pre): gcc-c++
%endif
BuildRequires(pre): rpm-build-ninja
BuildRequires: cmake
BuildRequires: rpm-build-python3
BuildRequires: glibc-core
BuildRequires: qt5-base-devel
BuildRequires: gsettings-qt-devel
BuildRequires: libgtest-devel
BuildRequires: dtk5-common-devel
BuildRequires: libsystemd-devel
BuildRequires: doxygen qt5-tools
%if_enabled docs
BuildRequires: qt5-base-doc
%endif
BuildRequires: libuchardet-devel

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
%patch -p1
# Fix broken configs.
sed -i '/libdir=/s/${prefix}//' \
  misc/dtkcore.pc.in
sed -i -e '/.tools/s/@CMAKE_INSTALL_PREFIX@//; /.libs/s/@CMAKE_INSTALL_PREFIX@//;' \
  misc/qt_lib_dtkcore.pri.in

%build
%if_enabled clang
export CC=clang-%llvm_ver CXX=clang++-%llvm_ver LDFLAGS="-fuse-ld=lld-%llvm_ver $LDFLAGS"
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
  -DD_DSG_APP_DATA_FALLBACK=/var/dsg/appdata \
  -DBUILD_WITH_SYSTEMD=ON \
%if_disabled docs
  -DBUILD_DOCS=OFF \
%endif
  #
cmake --build %_cmake__builddir -j%__nprocs

%install
%cmake_install

%files -n dtk5-core
%doc README.md LICENSE
%_bindir/qdbusxml2cpp-fix

%files -n libdtk5-core
%_libdir/lib%name.so.5*
%dir %_libdir/dtk5/
%_libdir/dtk5/DCore/

%files -n dtk5-core-devel
%doc docs/Specification.md
%_libdir/lib%name.so
%dir %_includedir/dtk5/
%_includedir/dtk5/DCore/
%_qt5_archdatadir/mkspecs/modules/*.pri
%_qt5_archdatadir/mkspecs/features/dtk_install_dconfig.prf
%_libdir/cmake/DtkCore/
%_libdir/cmake/DtkCMake/
%_libdir/cmake/DtkTools/
%_libdir/cmake/DtkDConfig/DtkDConfigConfig.cmake
%_pkgconfigdir/dtkcore.pc

%if_enabled docs
%files -n dtk5-core-doc
%_qt5_datadir/doc/dtkcore.qch
%endif

%changelog
* Fri Mar 10 2023 Leontiy Volodin <lvol@altlinux.org> 5.6.8-alt1
- New version.

* Tue Feb 21 2023 Leontiy Volodin <lvol@altlinux.org> 5.6.6-alt1
- New version.

* Mon Feb 13 2023 Leontiy Volodin <lvol@altlinux.org> 5.6.5-alt1
- New version.
- Fixed underlinked libraries.

* Thu Jan 19 2023 Leontiy Volodin <lvol@altlinux.org> 5.6.4-alt2
- Fixed broken configs.

* Wed Jan 18 2023 Leontiy Volodin <lvol@altlinux.org> 5.6.4-alt1
- New version.

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
