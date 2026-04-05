%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%define appname io.elementary.onboarding

Name: elementary-onboarding
Version: 8.1.0
Release: alt1

Summary: Onboarding app for new users
License: GPL-3.0-or-later
Group: Other
Url: https://github.com/elementary/onboarding

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-build-vala

BuildRequires: meson
BuildRequires: cmake
BuildRequires: vala-tools
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: pkgconfig(granite-7)
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(pantheon-wayland-1)

%description
Onboarding assists users during their first log in to elementary
OS.

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

%files -f %appname.lang
%doc COPYING README.md
%_sysconfdir/xdg/autostart/%{appname}.desktop
%_sysconfdir/guest-session/prefs.sh
%_bindir/%appname
%_desktopdir/%{appname}.desktop
%_iconsdir/hicolor/*/apps/%{appname}.svg
%_datadir/glib-2.0/schemas/%{appname}.gschema.xml
%_datadir/metainfo/%{appname}.metainfo.xml

%changelog
* Sun Apr 05 2026 Nikolay Strelkov <snk@altlinux.org> 8.1.0-alt1
- New version 8.1.0.

* Fri Nov 28 2025 Nikolay Strelkov <snk@altlinux.org> 8.0.4-alt1
- New version 8.0.4.

* Sat Sep 20 2025 Nikolay Strelkov <snk@altlinux.org> 8.0.3-alt1
- Initial build for Sisyphus
