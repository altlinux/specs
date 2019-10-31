Name: liri-session
Version: 0.0.20191007
Release: alt1

Summary: The Liri Session
License: GPL
Group: Graphical desktop/Other
Url: https://github.com/lirios/session

Source: %name-%version-%release.tar

BuildRequires: cmake cmake-modules-liri qt5-tools-devel
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5GSettings)
BuildRequires: pkgconfig(Liri1Xdg)

%package devel
Summary: The Liri Session
Group: Development/C++

%description
%summary is responsible for bootstrapping the initial environment and
launching critical desktop services, including the shell, as well as
XDG autostart applications.

%description devel
%summary
this package contains development part of %name

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files
%_sysconfdir/xdg/menus/*.menu

%_bindir/liri-session
%_bindir/liri-session-ctl

%_prefix/lib/systemd/user/liri-*
%_prefix/lib/systemd/user-generators/liri-*

%_prefix/libexec/liri-daemon
%_prefix/libexec/liri-launcher

%_libdir/libLiri1*.so.*
%_libdir/qt5/plugins/liri/daemon

%_datadir/dbus-1/services/io.liri.Launcher.service
%_datadir/desktop-directories/*.directory
%_datadir/glib-2.0/schemas/*.xml
%_datadir/wayland-sessions/liri.desktop

%files devel
%_includedir/Liri*
%_libdir/libLiri1*.so
%_libdir/cmake/Liri1*
%_pkgconfigdir/Liri1*.pc

%changelog
* Fri Oct 11 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.0.20191007-alt1
- initial
