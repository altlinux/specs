Name: fnott
Version: 1.4.0
Release: alt1

Summary: Notification daemon for wlroots-based Wayland compositor
License: MIT
Group: Graphical desktop/Other
Url: https://codeberg.org/dnkl/fnott

Source: %name-%version-%release.tar

BuildRequires: meson scdoc
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(fcft) >= 3.0.0
BuildRequires: pkgconfig(fontconfig)
BuildRequires: pkgconfig(libpng)
BuildRequires: pkgconfig(pixman-1)
BuildRequires: pkgconfig(tllist)
BuildRequires: pkgconfig(wayland-protocols)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-cursor)

%description
keyboard driven and lightweight notification daemon for
wlroots-based Wayland compositors.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%files
%doc %_defaultdocdir/fnott
%_bindir/fnott
%_bindir/fnottctl
%_datadir/fnott
%_datadir/zsh/site-functions/_fnott*
%_desktopdir/fnott.desktop
%_man1dir/fnott.1*
%_man1dir/fnottctl.1*
%_man5dir/fnott.ini.5*

%changelog
* Fri Mar 31 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.0-alt1
- 1.4.0 released

* Mon Aug 08 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3.0-alt1
- 1.3.0 released

* Sat Feb 12 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2.1-alt1
- 1.2.1 released

* Sat Feb 05 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2.0-alt1
- 1.2.0 released

* Sun Oct 10 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.1.2-alt1
- 1.1.2 released

* Mon Aug 02 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.1.1-alt1
- 1.1.1 released
