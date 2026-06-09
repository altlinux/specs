%def_disable clang

Name: dtkcommon
Version: 6.7.43
Release: alt1

Summary: Deepin desktop schemas

License: BSD-3-Clause and CC0-1.0
Group: System/Configuration/Other
Url: https://github.com/linuxdeepin/dtkcommon
Vcs: https://github.com/linuxdeepin/dtkcommon

Packager: Leontiy Volodin <lvol@altlinux.org>

# Source-url: %url/archive/%version/%name-%version.tar.gz
Source: %name-%version.tar
Patch: %name-%version-%release.patch

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
%patch -p1

%build
%if_enabled clang
export CC="clang"
export CXX="clang++"
export AR="llvm-ar"
%endif

%cmake \
  -GNinja \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DDTK_VERSION=%version \
  -DLIB_INSTALL_DIR=%_libdir \
#
cmake --build "%_cmake__builddir" -j%__nprocs

%install
%cmake_install

%files -n dtk6-common-configs
%doc LICENSE README.md CHANGELOG.md
%_datadir/dsg/configs/org.deepin.dtk.preference.json

%files -n dtk6-common-devel
%_libdir/cmake/Dtk/DtkConfig.cmake
%_libdir/cmake/Dtk6/Dtk6Config.cmake
%_libdir/cmake/DtkBuildHelper/DtkBuildHelperConfig.cmake
%_libdir/cmake/DtkBuildHelper/DtkBuildHelperConfigVersion.cmake

%changelog
* Tue Jun 09 2026 Leontiy Volodin <lvol@altlinux.org> 6.7.43-alt1
- New version 6.7.43.

* Thu May 14 2026 Leontiy Volodin <lvol@altlinux.org> 6.7.41-alt1
- New version 6.7.41.

* Thu Apr 23 2026 Leontiy Volodin <lvol@altlinux.org> 6.7.39-alt1
- New version 6.7.39.

* Thu Jan 22 2026 Leontiy Volodin <lvol@altlinux.org> 6.7.31-alt1
- New version 6.7.31.

* Wed Dec 10 2025 Leontiy Volodin <lvol@altlinux.org> 5.7.28-alt1
- New version 5.7.28.

* Fri Nov 07 2025 Leontiy Volodin <lvol@altlinux.org> 5.7.26-alt1
- New version 5.7.26.

* Fri Oct 24 2025 Leontiy Volodin <lvol@altlinux.org> 5.7.24-alt1
- New version 5.7.24.

* Wed Oct 15 2025 Leontiy Volodin <lvol@altlinux.org> 5.7.23-alt1
- New version 5.7.23.

* Tue Aug 19 2025 Leontiy Volodin <lvol@altlinux.org> 5.7.21-alt1
- New version 5.7.21.

* Tue Jul 22 2025 Leontiy Volodin <lvol@altlinux.org> 5.7.19-alt1
- New version 5.7.19.

* Thu Feb 13 2025 Leontiy Volodin <lvol@altlinux.org> 5.7.9-alt1
- New version 5.7.9.

* Thu Jan 16 2025 Leontiy Volodin <lvol@altlinux.org> 5.7.8-alt1
- New version 5.7.8.
- Added vcs tag.

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
