Name: fnott
Version: 1.6.0
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
BuildRequires: pkgconfig(systemd)
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
%_sysconfdir/xdg/fnott
%_bindir/fnott
%_bindir/fnottctl
%_libexecdir/systemd/user/*.service
%_datadir/dbus-1/services/*.service
%_datadir/zsh/site-functions/_fnott*
%_desktopdir/fnott.desktop
%_man1dir/fnott.1*
%_man1dir/fnottctl.1*
%_man5dir/fnott.ini.5*

%changelog
* Thu May 02 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 1.6.0-alt1
- 1.6.0 released

* Thu Apr 18 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 1.5.0-alt1
- 1.5.0 released

* Fri Jul 14 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.1-alt1
- 1.4.1 released

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
