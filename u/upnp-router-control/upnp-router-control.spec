%define _unpackaged_files_terminate_build 1

%define appname org.upnproutercontrol.UPnPRouterControl

Name: upnp-router-control
Version: 0.3.6
Release: alt1

Summary: Access some parameters of the router and manage port forwarding
License: GPL-3.0-or-later
Group: Other
Url: https://gitlab.gnome.org/DnaX/upnp-router-control

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson

BuildRequires: meson
BuildRequires: cmake
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(gssdp-1.6)
BuildRequires: pkgconfig(gupnp-1.6)

%description
A GTK application to access the parameters of the router exposed via
UPnP-IGD. Access to network speed, external IP and model name.
It can manage port forwarding through a simple GUI interface.

%prep
%setup
sed -i "s|Categories=.*|Categories=GTK;Network;RemoteAccess;|" data/org.upnproutercontrol.UPnPRouterControl.desktop.in

%build
%meson
%meson_build

%install
%meson_install

%find_lang %name

%check
%meson_test

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING NEWS README README.md
%_bindir/upnp-router-control
%_desktopdir/%{appname}.desktop
%_datadir/glib-2.0/schemas/%{appname}.gschema.xml
%_iconsdir/hicolor/*/apps/%{appname}.png
%_iconsdir/hicolor/scalable/apps/%{appname}.svg
%_man1dir/upnp-router-control.1.*
%_datadir/metainfo/%{appname}.appdata.xml

%changelog
* Wed Apr 22 2026 Nikolay Strelkov <snk@altlinux.org> 0.3.6-alt1
- New version 0.3.6.

* Sun Dec 28 2025 Nikolay Strelkov <snk@altlinux.org> 0.3.5-alt1
- Initial build for Sisyphus
