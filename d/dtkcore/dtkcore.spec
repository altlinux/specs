%define _libexecdir %_prefix/libexec

%def_disable clang
%def_without docs

Name: dtkcore
Version: 5.6.34
Release: alt1

Summary: Deepin tool kit core modules

License: LGPL-2.1+ and LGPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dtkcore

Source: %url/archive/%version/%name-%version.tar.gz
Patch: %name-%version-%release.patch

Provides: libdtk5-core = %EVR
Obsoletes: libdtk5-core < %EVR
Provides: dtk5-core = %EVR
Obsoletes: dtk5-core < %EVR

BuildRequires(pre): rpm-build-ninja deepin-desktop-base rpm-macros-dqt5
BuildRequires: cmake rpm-build-python3 dtk6-common-devel libdtklog-devel gsettings-qt-devel libsystemd-devel dqt5-base-devel libuchardet-devel libspdlog-devel libicu-devel
%if_enabled clang
BuildRequires: clang-devel lld-devel
%else
BuildRequires: gcc-c++
%endif
%if_with docs
BuildRequires: dqt5-base-doc
%endif

Requires: libdqt5-dbus = %_dqt5_version

%description
Deepin tool kit core modules.

%package -n lib%{name}5
Summary: Libraries for %name
Group: System/Libraries
Requires: libdqt5-core = %_dqt5_version

%description -n lib%{name}5
Deepin tool kit core modules.
Libraries for %name.

%package -n lib%name-devel
Summary: Development package for %name
Group: Development/KDE and QT
Provides: dtk5-core-devel = %EVR
Obsoletes: dtk5-core-devel < %EVR
Requires: dtkcore = %EVR

%description -n lib%name-devel
Header files and libraries for %name.

%if_with docs
%package doc
Summary: %name documantation
Group: Documentation
BuildArch: noarch
Provides: dtk5-core-doc = %EVR
Obsoletes: dtk5-core-doc < %EVR

%description doc
This package provides %name documantation.
%endif

%prep
%setup
%patch -p1

%build
%if_enabled clang
export CC=clang CXX=clang++ LDFLAGS="-fuse-ld=lld $LDFLAGS"
%endif
export PATH=%_dqt5_bindir:$PATH
%cmake \
  -GNinja \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DCMAKE_PREFIX_PATH=%_dqt5_libdir/cmake \
  -DCMAKE_SKIP_INSTALL_RPATH:BOOL=no \
  -DCMAKE_INSTALL_RPATH=%_dqt5_libdir \
  -DCMAKE_INSTALL_LIBDIR=%_lib \
  -DDTK_VERSION=%version \
  -DLIBRARY_INSTALL_DIR=%_lib \
  -DD_DSG_APP_DATA_FALLBACK=/var/dsg/appdata \
  -DBUILD_WITH_SYSTEMD=ON \
%if_without docs
  -DBUILD_DOCS=OFF \
%endif
  -DMKSPECS_INSTALL_DIR=%_dqt5_archdatadir/mkspecs/modules/ \
  -DFEATURES_INSTALL_DIR=%_dqt5_archdatadir/mkspecs/features/ \
  #
cmake --build %_cmake__builddir -j%__nprocs

%install
%cmake_install

%files
%doc README.md LICENSE
%dir %_libexecdir/dtk5
%dir %_libexecdir/dtk5/DCore/
%_libexecdir/dtk5/DCore/bin/

%files -n lib%{name}5
%_libdir/lib%name.so.5*

%files -n lib%name-devel
%doc docs/Specification.md
%_libdir/lib%name.so
%dir %_includedir/dtk5/
%_includedir/dtk5/DCore/
%_dqt5_archdatadir/mkspecs/modules/qt_lib_dtkcore.pri
%_dqt5_archdatadir/mkspecs/features/dtk_install_dconfig.prf
%_libdir/cmake/DtkCore/
%_libdir/cmake/DtkCMake/
%_libdir/cmake/DtkTools/
%_libdir/cmake/DtkDConfig/
%_pkgconfigdir/dtkcore.pc

%if_with docs
%files doc
%_dqt5_datadir/doc/dtkcore.qch
%endif

%changelog
* Wed Sep 11 2024 Leontiy Volodin <lvol@altlinux.org> 5.6.34-alt1
- New version 5.6.34.

* Mon May 06 2024 Leontiy Volodin <lvol@altlinux.org> 5.6.28-alt1
- New version 5.6.28.
- Built via separate qt5 instead system (ALT #48138).

* Fri Mar 29 2024 Leontiy Volodin <lvol@altlinux.org> 5.6.26-alt1
- New version 5.6.26.

* Wed Mar 20 2024 Leontiy Volodin <lvol@altlinux.org> 5.6.25-alt1
- New version 5.6.25.

* Tue Mar 05 2024 Leontiy Volodin <lvol@altlinux.org> 5.6.22-alt2
- Requires: libqt5-core = %%_qt5_version.

* Tue Jan 16 2024 Leontiy Volodin <lvol@altlinux.org> 5.6.22-alt1
- New version 5.6.22.

* Thu Nov 30 2023 Leontiy Volodin <lvol@altlinux.org> 5.6.20-alt1
- New version 5.6.20.
- Renamed subpackages:
  + libdtk5-core -> libdtkcore5.
  + dtk5-core-devel -> libdtkcore-devel.
  + dtk5-core -> dtkcore.
  + dtk5-core-doc -> dtkcore-doc.

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
