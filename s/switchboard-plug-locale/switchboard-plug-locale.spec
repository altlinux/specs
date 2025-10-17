%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%define appname io.elementary.settings.locale

Name: switchboard-plug-locale
Version: 8.0.2
Release: alt1

Summary: Switchboard Locale Plug
License: GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/elementary/settings-locale

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-build-vala

BuildRequires: meson
BuildRequires: cmake
BuildRequires: vala-tools
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(switchboard-3)
BuildRequires: pkgconfig(polkit-gobject-1)
BuildRequires: pkgconfig(accountsservice)
BuildRequires: pkgconfig(gnome-desktop-4)
BuildRequires: pkgconfig(ibus-1.0)

%description
Region & Language plug for Switchboard.
Change your region and language settings.

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
%_libdir/switchboard-3/personal/libio.elementary.settings.locale.so
%_libdir/switchboard-3/personal/pantheon-locale/languagelist
%_libdir/switchboard-3/personal/pantheon-locale/packages_blocklist
%_datadir/glib-2.0/schemas/io.elementary.settings.locale.gschema.xml
%_datadir/metainfo/io.elementary.settings.locale.appdata.xml
%_datadir/polkit-1/actions/io.elementary.settings.locale.policy

%changelog
* Sun Sep 21 2025 Nikolay Strelkov <snk@altlinux.org> 8.0.2-alt1
- Initial build for Sisyphus
