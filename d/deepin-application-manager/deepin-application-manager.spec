%def_without clang

%define repo dde-application-manager
%define _libexecdir %_prefix/libexec

Name: deepin-application-manager
Version: 1.1.8
Release: alt1

Summary: App manager for Deepin

License: LGPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dde-application-manager

Source: %url/archive/%version/%repo-%version.tar.gz
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-ninja
BuildRequires: cmake libgtest-devel libsystemd-devel python3-module-setuptools qt6-base-devel
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
%dir %_libexecdir/deepin/
%dir %_libexecdir/deepin/application-manager/
%_libexecdir/deepin/application-manager/app-launch-helper
%_libexecdir/deepin/application-manager/app-update-notifier
%_unitdir/org.desktopspec.ApplicationUpdateNotifier1.service
%_userunitdir/org.desktopspec.ApplicationManager1.service
%dir %_userunitdir/dde-session-initialized.target.wants/
%_userunitdir/dde-session-initialized.target.wants/org.desktopspec.ApplicationManager1.service
%_datadir/dbus-1/system-services/org.desktopspec.ApplicationUpdateNotifier1.service
%_datadir/dbus-1/system.d/org.desktopspec.ApplicationUpdateNotifier1.conf
%_datadir/dbus-1/services/org.desktopspec.ApplicationManager1.service
%dir %_datadir/%repo/
%_datadir/%repo/org.desktopspec.*.xml
%dir %_datadir/dsg/
%dir %_datadir/dsg/configs/
%dir %_datadir/dsg/configs/%repo/
%_datadir/dsg/configs/%repo/com.deepin*.json

%changelog
* Tue Jan 30 2024 Leontiy Volodin <lvol@altlinux.org> 1.1.8-alt1
- New version 1.1.8.

* Tue Jan 16 2024 Leontiy Volodin <lvol@altlinux.org> 1.1.7-alt1
- New version 1.1.7.
- Updated license tag.

* Fri Dec 15 2023 Leontiy Volodin <lvol@altlinux.org> 1.1.4.0.1.b75b-alt1
- Initial build for ALT Sisyphus.
