Name: liri-session
Version: 0.0.20210810
Release: alt1

Summary: The Liri Session
License: GPLv3
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

%_prefix/libexec/liri-daemon

%_libdir/libLiri1*.so.*
%_libdir/qt5/plugins/liri/daemon

%_datadir/desktop-directories/*.directory
%_datadir/glib-2.0/schemas/*.xml
%_datadir/liri-session/systemd-user/autostart/*.desktop
%_datadir/wayland-sessions/liri.desktop

%files devel
%_includedir/Liri*
%_libdir/libLiri1*.so
%_libdir/cmake/Liri1*
%_pkgconfigdir/Liri1*.pc

%changelog
* Tue Aug 10 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.0.20210810-alt1
- updated form git.4690b3d

* Tue Mar 03 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.0.20191109-alt1
- updated form upstream git.6a84698

* Fri Nov 01 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.0.20191017-alt1
- updated form upstream git.2840b1b

* Fri Oct 11 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.0.20191007-alt1
- initial
