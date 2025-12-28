%define _unpackaged_files_terminate_build 1

%define appname io.elementary.capnet-assist

Name: capnet-assist
Version: 8.0.2
Release: alt1

Summary: Captive Portal Assistant
License: GPL-3.0-or-later
Group: System/Configuration/Networking
Url: https://github.com/elementary/capnet-assist

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-build-vala

BuildRequires: meson
BuildRequires: cmake
BuildRequires: vala-tools
BuildRequires: pkgconfig(gcr-4)
BuildRequires: pkgconfig(granite-7)
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(webkitgtk-6.0)
BuildRequires: vapi(gcr-4)

%description
Assists users in connective to Captive Portals such as those found on
public access points in train stations, coffee shops, universities, etc.
Upon detection, the assistant appears showing the captive portal. Once a
connection is known to have been established, it dismisses itself.
Written in Vala and using WebkitGtk+.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%find_lang %appname

%check
%meson_test

%files -f %{appname}.lang
%doc COPYING README.md
%_bindir/%appname
%_desktopdir/%{appname}.desktop
%_datadir/glib-2.0/schemas/%{appname}.gschema.xml
%_iconsdir/hicolor/*/apps/%{appname}.svg
%_datadir/metainfo/%{appname}.metainfo.xml

%changelog
* Sun Dec 28 2025 Nikolay Strelkov <snk@altlinux.org> 8.0.2-alt1
- Initial build for Sisyphus
