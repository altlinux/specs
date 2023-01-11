%def_disable clang

Name: dtkcommon
Version: 5.6.3
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
BuildRequires: glibc-core
BuildRequires: qt5-base-devel
BuildRequires: qt5-tools

%description
%summary.

%package -n dtk5-common-schemas
Summary: Deepin desktop schemas
Group: System/Configuration/Other
BuildArch: noarch

%description -n dtk5-common-schemas
%summary.

%package -n dtk5-common-devel
Summary: Development files for %name
Group: Development/Other
Provides: dtk5-common

%description -n dtk5-common-devel
The package provides development files for %name.

%prep
%setup

%build
export QTDIR=%_qt5_prefix
export PATH=%_qt5_bindir:$PATH
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
  -DMKSPECS_INSTALL_DIR=%_qt5_archdatadir/mkspecs \
  -DARCH=%_arch \
#
cmake --build "%_cmake__builddir" -j%__nprocs

%install
%cmake_install

%files -n dtk5-common-schemas
%doc LICENSE README.md
%_datadir/glib-2.0/schemas/com.deepin.dtk.gschema.xml

%files -n dtk5-common-devel
%_libdir/cmake/Dtk/DtkConfig.cmake
%_libdir/cmake/Dtk/DtkInstallDConfigConfig.cmake
%_qt5_archdatadir/mkspecs/features/*.prf
%_qt5_archdatadir/mkspecs/modules/qt_lib_dtkcommon.pri

%changelog
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
