%def_disable clang

Name: dtkcommon
Version: 5.6.34
Release: alt1

Summary: Deepin desktop schemas

License: BSD-3-Clause and CC0-1.0
Group: System/Configuration/Other
Url: https://github.com/linuxdeepin/dtkcommon

Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%name-%version.tar.gz

%if_enabled clang
BuildRequires(pre): clang-devel
%else
BuildRequires(pre): gcc-c++
%endif
BuildRequires(pre): rpm-build-ninja
BuildRequires: cmake

%description
%summary.

%package -n dtk6-common-configs
Summary: Deepin desktop configs
Group: System/Configuration/Other
BuildArch: noarch
Provides: dtk5-common-schemas = %EVR

%description -n dtk6-common-configs
%summary.

%package -n dtk6-common-devel
Summary: Development files for %name
Group: Development/Other
Provides: dtk5-common = %EVR
Provides: dtk5-common-devel = %EVR
Obsoletes: dtk5-common-devel < %EVR

%description -n dtk6-common-devel
The package provides development files for %name.

%prep
%setup

%build
%if_enabled clang
export CC="clang"
export CXX="clang++"
export AR="llvm-ar"
%endif

%cmake \
  -GNinja \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DDVERSION=%version \
  -DDTK_VERSION=%version \
  -DLIB_INSTALL_DIR=%_libdir \
  -DARCH=%_arch \
#
cmake --build "%_cmake__builddir" -j%__nprocs

%install
%cmake_install

%files -n dtk6-common-configs
%doc LICENSE README.md
%_datadir/dsg/configs/org.deepin.dtk.preference.json

%files -n dtk6-common-devel
%_libdir/cmake/Dtk/DtkConfig.cmake
%_libdir/cmake/Dtk6/Dtk6Config.cmake
%_libdir/cmake/DtkBuildHelper/DtkBuildHelperConfig.cmake
%_libdir/cmake/DtkBuildHelper/DtkBuildHelperConfigVersion.cmake

%changelog
* Wed Sep 11 2024 Leontiy Volodin <lvol@altlinux.org> 5.6.34-alt1
- New version 5.6.34.

* Mon May 06 2024 Leontiy Volodin <lvol@altlinux.org> 5.6.28-alt1
- New version 5.6.28.

* Fri Mar 29 2024 Leontiy Volodin <lvol@altlinux.org> 5.6.26-alt1
- New version 5.6.26.

* Tue Nov 28 2023 Leontiy Volodin <lvol@altlinux.org> 5.6.20-alt1
- New version 5.6.20.
- Switched to dtk6.

* Mon Apr 24 2023 Leontiy Volodin <lvol@altlinux.org> 5.6.9-alt1
- New version 5.6.9.

* Fri Mar 10 2023 Leontiy Volodin <lvol@altlinux.org> 5.6.8-alt1
- New version (5.6.8).

* Wed Jan 18 2023 Leontiy Volodin <lvol@altlinux.org> 5.6.4-alt1
- New version (5.6.4).
- Upstream:
  + Removed dconfig prf and cmake module.

* Wed Jan 11 2023 Leontiy Volodin <lvol@altlinux.org> 5.6.3-alt1
- New version (5.6.3).
- Updated license tag.
- Divided the package into subpackages.

* Thu Jun 02 2022 Leontiy Volodin <lvol@altlinux.org> 5.5.23-alt1
- New version (5.5.23).

* Fri Apr 08 2022 Leontiy Volodin <lvol@altlinux.org> 5.5.21-alt1
- New version (5.5.21).

* Tue Feb 08 2022 Leontiy Volodin <lvol@altlinux.org> 5.5.20-alt1
- New version (5.5.20).

* Tue Jul 06 2021 Leontiy Volodin <lvol@altlinux.org> 5.5.17-alt1
- New version (5.5.17).

* Tue May 18 2021 Leontiy Volodin <lvol@altlinux.org> 5.5.3-alt1
- New version (5.5.3) with rpmgs script.

* Thu Apr 08 2021 Leontiy Volodin <lvol@altlinux.org> 5.5.2-alt1
- Initial build for ALT Sisyphus.
