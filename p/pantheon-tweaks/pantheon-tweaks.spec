%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%define appname io.github.pantheon_tweaks.pantheon-tweaks

Name: pantheon-tweaks
Version: 2.5.2
Release: alt1

Summary: A system customization app for the Pantheon desktop environment.
License: GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/pantheon-tweaks/pantheon-tweaks

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-build-vala

BuildRequires: meson
BuildRequires: cmake
BuildRequires: vala-tools
BuildRequires: sassc
BuildRequires: pkgconfig(granite-7)
BuildRequires: pkgconfig(switchboard-3)

%description
A system customization app for the Pantheon Desktop that lets you
easily and safely customise your desktop's appearance.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%find_lang %name --all-name

%check
%meson_test

%files -f %{name}.lang
%doc AUTHORS CONTRIBUTORS COPYING README.md
%_bindir/%name
%_desktopdir/%{appname}.desktop
%_iconsdir/hicolor/*/apps/%{appname}.png
%_datadir/glib-2.0/schemas/%{name}.gschema.xml
%_datadir/metainfo/%{appname}.metainfo.xml

%changelog
* Tue May 05 2026 Nikolay Strelkov <snk@altlinux.org> 2.5.2-alt1
- New version 2.5.2.

* Fri Jan 30 2026 Nikolay Strelkov <snk@altlinux.org> 2.5.1-alt1
- New version 2.5.1.

* Sun Oct 26 2025 Nikolay Strelkov <snk@altlinux.org> 2.5.0-alt1
- Initial build for Sisyphus
