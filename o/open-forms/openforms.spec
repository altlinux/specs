%define _unpackaged_files_terminate_build 1
%define _name open_forms
%define appId in.aryank.openforms

Name:    open-forms
Version: 0.2_211225
Release: alt2

Summary: A simple, local-first form collection app for GNOME.
License: GPL-3.0-or-later
Group:   Other
URL:     https://github.com/Aryan20/open_forms
VCS:     https://github.com/Aryan20/open_forms

Source: %name-%version.tar

%add_python3_path %_datadir/%_name

BuildArch: noarch

BuildRequires(pre): rpm-macros-meson rpm-build-python3
BuildRequires: meson
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(glib-2.0)

Requires: typelib(Adw) = 1

%description
OpenForms is a simple, local-first form collection app for GNOME.
It is designed for situations where setting up online forms is impractical.
OpenForms works fully offline, stores responses locally, and avoids complexity.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%files
%_datadir/applications/%appId.desktop
%_datadir/metainfo/%appId.metainfo.xml
%_datadir/glib-2.0/schemas/%appId.gschema.xml
%_datadir/dbus-1/services/%appId.service
%_datadir/icons/hicolor/scalable/apps/%appId.svg
%_datadir/icons/hicolor/symbolic/apps/%appId-symbolic.svg
%_bindir/%_name
%_datadir/%_name

%changelog
* Tue Dec 23 2025 Pavel Mitrofanov <cobalt@altlinux.org> 0.2_211225-alt2
- Chore: cleaned up file checks and added python3 patch.

* Tue Dec 23 2025 Pavel Mitrofanov <cobalt@altlinux.org> 0.2_211225-alt1
- Initial build for Sisyphus.
