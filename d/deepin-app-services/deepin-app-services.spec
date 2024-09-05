%def_without clang
%def_with docs

%define repo dde-app-services

Name: deepin-app-services
Version: 1.0.25
Release: alt3

Summary: Service collection of DDE applications

License: LGPL-3.0-or-later
Group: System/Configuration/Other
Url: https://github.com/linuxdeepin/dde-app-services

Source: %url/archive/%version/%repo-%version.tar.gz
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-ninja rpm-macros-dqt5
%if_with clang
BuildRequires: clang-devel
%else
BuildRequires: gcc-c++
%endif
# Automatically added by buildreq on Fri Oct 20 2023
# optimized out: cmake-modules gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 libdouble-conversion3 libdtkcore-devel libdtkgui-devel libglvnd-devel libgpg-error libgsettings-qt libp11-kit libdqt5-core libdqt5-dbus libdqt5-gui libdqt5-help libdqt5-network libdqt5-printsupport libdqt5-sql libdqt5-svg libdqt5-test libdqt5-widgets libdqt5-x11extras libdqt5-xml libsasl2-3 libssl-devel libstartup-notification libstdc++-devel python3 python3-base dqt5-base-common dqt5-base-devel dqt5-tools sh5
BuildRequires: cmake libdtkwidget-devel libgtest-devel
%if_with docs
BuildRequires: doxygen dqt5-base-doc dqt5-tools-devel
%endif

%description
%summary.

%if_with docs
%package doc
Summary: %name documantation
Group: Documentation
BuildArch: noarch

%description doc
This package provides %name documantation.
%endif

%prep
%setup -n %repo-%version
%patch -p1

%build
export PATH=%_dqt5_bindir:$PATH
export CMAKE_PREFIX_PATH=%_dqt5_libdir/cmake:$CMAKE_PREFIX_PATH
%if_enabled clang
export CC="clang"
export CXX="clang++"
export AR="llvm-ar"
%endif
%cmake \
  -GNinja \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DCMAKE_SKIP_INSTALL_RPATH:BOOL=NO \
  -DCMAKE_INSTALL_RPATH=%_dqt5_libdir \
  -DDVERSION=%version \
%if_with docs
  -DBUILD_DOCS=ON \
  -DQCH_INSTALL_DESTINATION=%_dqt5_docdir \
%else
  -DBUILD_DOCS=OFF \
%endif
#
cmake --build "%_cmake__builddir" -j%__nprocs

%install
%cmake_install
chmod +x %buildroot%_datadir/bash-completion/completions/dde-dconfig
%find_lang --output=%name.lang dde-dconfig dde-dconfig-editor

%files -f %name.lang
%doc LICENSE README.md
%_bindir/dde-dconfig*
%_datadir/dbus-1/interfaces/org.desktopspec.ConfigManager*.xml
%_datadir/dbus-1/system.d/org.desktopspec.ConfigManager.conf
%_datadir/dbus-1/system-services/org.desktopspec.ConfigManager.service
%_datadir/bash-completion/completions/dde-dconfig
# package translations outside %%find_lang
%dir %_datadir/dde-dconfig/
%dir %_datadir/dde-dconfig/translations/
%_datadir/dde-dconfig/translations/dde-dconfig_zh_CN.qm
%dir %_datadir/dde-dconfig-editor/
%dir %_datadir/dde-dconfig-editor/translations/
%_datadir/dde-dconfig-editor/translations/dde-dconfig-editor_zh_CN.qm
# ---
%_unitdir/dde-dconfig-daemon.service
%_prefix/lib/sysusers.d/dde-dconfig-daemon.conf
%_prefix/lib/tmpfiles.d/dde-dconfig-daemon-tmpfiles.conf
%dir %_datadir/dsg/
%dir %_datadir/dsg/configs/
%dir %_datadir/dsg/configs/dconfig-example/
%dir %_datadir/dsg/configs/dconfig-example/a/
%dir %_datadir/dsg/configs/overrides/
%dir %_datadir/dsg/configs/overrides/dconfig-example/
%dir %_datadir/dsg/configs/overrides/dconfig-example/example/
%dir %_datadir/dsg/configs/overrides/dconfig-example/example/a/
%_datadir/dsg/configs/dconfig-example/example.json
%_datadir/dsg/configs/dconfig-example/a/example.json
%_datadir/dsg/configs/example.json
%_datadir/dsg/configs/overrides/dconfig-example/example/dconf-example.override.json
%_datadir/dsg/configs/overrides/dconfig-example/example/dconf-example.override.a.json
%_datadir/dsg/configs/overrides/dconfig-example/example/a/dconf-example.override.a.json

%if_with docs
%files doc
%_dqt5_docdir/dde-dconfig-doc.qch
%endif

%changelog
* Mon Sep 02 2024 Leontiy Volodin <lvol@altlinux.org> 1.0.25-alt3
- Built via separate qt5 instead system (ALT #48138).

* Mon Sep 02 2024 Leontiy Volodin <lvol@altlinux.org> 1.0.25-alt2
- Applied usrmerge.

* Tue Jan 30 2024 Leontiy Volodin <lvol@altlinux.org> 1.0.25-alt1
- New version 1.0.25.

* Fri Jan 19 2024 Leontiy Volodin <lvol@altlinux.org> 1.0.24.0.2.3acd-alt2
- Requires: libqt5-core = %%_qt5_version.

* Tue Jan 16 2024 Leontiy Volodin <lvol@altlinux.org> 1.0.24.0.2.3acd-alt1
- New version 1.0.24-2-g3acd198.

* Fri Oct 20 2023 Leontiy Volodin <lvol@altlinux.org> 1.0.23-alt1
- New version 1.0.23.

* Mon Mar 13 2023 Leontiy Volodin <lvol@altlinux.org> 0.0.22-alt1
- New version.

* Wed Feb 22 2023 Leontiy Volodin <lvol@altlinux.org> 0.0.21-alt1
- New version.

* Thu Jan 19 2023 Leontiy Volodin <lvol@altlinux.org> 0.0.20-alt2
- Fixed build with dtkgui 5.6.4.

* Tue Dec 13 2022 Leontiy Volodin <lvol@altlinux.org> 0.0.20-alt1
- Initial build for ALT Sisyphus.
