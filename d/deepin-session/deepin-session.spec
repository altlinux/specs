%def_without clang

%define repo dde-session
%define _libexecdir %_prefix/libexec

Name: deepin-session
Version: 1.2.6
Release: alt1

Summary: Launching DDE components systemd service

License: GPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dde-session

Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%repo-%version.tar.gz
Patch: %name-%version-%release.patch

# Requires: startdde deepin-dock deepin-session-ui deepin-polkit-agent deepin-kwin2

BuildRequires(pre): rpm-build-ninja rpm-build-systemd rpm-build-kf5
# Automatically added by buildreq on Fri Oct 27 2023
# optimized out: cmake-modules gcc-c++ glib2-devel glibc-kernheaders-generic glibc-kernheaders-x86 libX11-devel libdouble-conversion3 libgio-devel libgpg-error libgsettings-qt libp11-kit libqt5-concurrent libqt5-core libqt5-dbus libqt5-network libqt5-xml libsasl2-3 libssl-devel libstdc++-devel pkg-config python3 python3-base python3-dev python3-module-setuptools qt5-base-common sh5 xorg-proto-devel
BuildRequires: cmake dtkcore gsettings-qt-devel libXcursor-devel libXfixes-devel libdtkcore-devel libsecret-devel libsystemd-devel qt5-base-devel
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
export PATH=%_qt5_bindir:$PATH
%cmake \
    -GNinja \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
#
cmake --build "%_cmake__builddir" -j%__nprocs

%install
%cmake_install

%files
%_sysconfdir/X11/Xsession.d/00deepin-dde-env
%_sysconfdir/X11/Xsession.d/01deepin-profile
%_sysconfdir/X11/Xsession.d/94qt_env
%exclude %_sysconfdir/profile.d/deepin-xdg-dir.sh
%_bindir/dde-session
%_bindir/dde-login-reminder
%_bindir/dde-keyring-checker
%_bindir/dde-version-checker
%_bindir/dde-xsettings-checker
%_libexecdir/dde-session-ctl
%_datadir/dbus-1/services/org.deepin.dde.Session1.service
%_datadir/xsessions/dde-x11.desktop
# %%_datadir/wayland-sessions/dde-wayland.desktop
%_userunitdir/dde-session*
%_userunitdir/dde-desktop.service
%_userunitdir/dde-display.service
%_userunitdir/dde-dock.service
%_userunitdir/dde-lock.service
%_userunitdir/dde-osd*
%_userunitdir/dde-polkit-agent.service
%_userunitdir/dde-login-reminder.service
%dir %_userunitdir/dde-osd.target.wants/
%_userunitdir/dde-osd.target.wants/dde-login-reminder.service
%_userunitdir/dde-keyring-checker.service
%_userunitdir/dde-version-checker.service
%_userunitdir/dde-xsettings-checker.service

%changelog
* Mon Apr 08 2024 Leontiy Volodin <lvol@altlinux.org> 1.2.6-alt1
- New version 1.2.6.

* Thu Feb 08 2024 Leontiy Volodin <lvol@altlinux.org> 1.2.5-alt1
- New version 1.2.5.

* Thu Dec 21 2023 Leontiy Volodin <lvol@altlinux.org> 1.2.1-alt1
- Initial build for ALT Sisyphus.
