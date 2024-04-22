%def_without clang

%define repo dde-application-manager
%define _libexecdir %_prefix/libexec

Name: deepin-application-manager
Version: 1.2.4.0.1.g6096
Release: alt1

Summary: App manager for Deepin

License: LGPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dde-application-manager

Source: %url/archive/%version/%repo-%version.tar.gz
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-ninja
BuildRequires: cmake libgtest-devel libsystemd-devel python3-module-setuptools qt6-base-devel dtk6-common-devel libdtk6core-devel
%if_with clang
BuildRequires: clang-devel
%else
BuildRequires: gcc-c++
%endif

%description
%summary.

%prep
%setup -n %repo-%version
%patch -p1

%build
%if_with clang
export CC="clang"
export CXX="clang++"
export AR="llvm-ar"
export NM="llvm-nm"
export READELF="llvm-readelf"
%endif
export PATH=%_qt6_bindir:$PATH
%cmake \
    -GNinja \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DCMAKE_INSTALL_SYSCONFDIR=%_sysconfdir \
#
cmake --build "%_cmake__builddir" -j%__nprocs

%install
%cmake_install

# don't use dpkg
rm -rf %buildroot%_sysconfdir/dpkg/dpkg.cfg.d/am-update-hook

%files
%_bindir/%repo
%_bindir/dde-am
%_bindir/app-identifier
%dir %_libexecdir/deepin/
%dir %_libexecdir/deepin/application-manager/
%_libexecdir/deepin/application-manager/app-launch-helper
%_libexecdir/deepin/application-manager/app-update-notifier
%_libexecdir/deepin/application-manager/dockEnv.sh
%_unitdir/org.desktopspec.ApplicationUpdateNotifier1.service
%_userunitdir/org.desktopspec.ApplicationManager1.service
%dir %_userunitdir/dde-session-initialized.target.wants/
%_userunitdir/dde-session-initialized.target.wants/org.desktopspec.ApplicationManager1.service
%_datadir/dbus-1/system-services/org.desktopspec.ApplicationUpdateNotifier1.service
%_datadir/dbus-1/system.d/org.desktopspec.ApplicationUpdateNotifier1.conf
%_datadir/dbus-1/services/org.desktopspec.ApplicationManager1.service
%dir %_datadir/%repo/
%_datadir/%repo/org.desktopspec.*.xml
%dir %_datadir/deepin/
%dir %_datadir/deepin/%repo/
%dir %_datadir/deepin/%repo/hooks.d/
%_datadir/deepin/%repo/hooks.d/1-dockEnv.json
%dir %_datadir/dsg/
%dir %_datadir/dsg/configs/
%dir %_datadir/dsg/configs/%repo/
%_datadir/dsg/configs/%repo/com.deepin*.json
%dir %_datadir/dsg/configs/org.deepin.dde.application-manager/
%_datadir/dsg/configs/org.deepin.dde.application-manager/org.deepin.dde.am.json

%changelog
* Mon Apr 22 2024 Leontiy Volodin <lvol@altlinux.org> 1.2.4.0.1.g6096-alt1
- New version 1.2.4-1-g6096.

* Fri Apr 05 2024 Leontiy Volodin <lvol@altlinux.org> 1.2.2.0.2.d541-alt1
- New version 1.2.2-2-gd541c43.
- Switched to dtk6 by upstream.

* Fri Mar 29 2024 Leontiy Volodin <lvol@altlinux.org> 1.2.1-alt1
- New version 1.2.1.

* Mon Mar 25 2024 Leontiy Volodin <lvol@altlinux.org> 1.2.0.0.5.b504-alt1
- New version 1.2.0-5-gb504363.

* Thu Mar 07 2024 Leontiy Volodin <lvol@altlinux.org> 1.1.9-alt1
- New version 1.1.9.

* Tue Jan 30 2024 Leontiy Volodin <lvol@altlinux.org> 1.1.8-alt1
- New version 1.1.8.

* Tue Jan 16 2024 Leontiy Volodin <lvol@altlinux.org> 1.1.7-alt1
- New version 1.1.7.
- Updated license tag.

* Fri Dec 15 2023 Leontiy Volodin <lvol@altlinux.org> 1.1.4.0.1.b75b-alt1
- Initial build for ALT Sisyphus.
