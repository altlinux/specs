%define _unpackaged_files_terminate_build 1
%define _name session-keeper
%define uuid %_name@altlinux.org

Name: gnome-shell-extension-%_name
Version: 1.0.6
Release: alt1

Summary: Saving a GNOME user session
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME

URL: https://altlinux.space/alt-gnome/session-keeper
VCS: https://altlinux.space/alt-gnome/session-keeper

Source0: %name-%version.tar
Source1: node-modules.tar
Source2: npm-cache.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: zip
BuildRequires: npm
BuildRequires: libgio

Requires: gnome-shell >= 45

ExcludeArch: i586

%description
Session keeper is a GNOME extension for saving and restoring application
sessions.

%prep
%setup -a 1 -a 2
%patch -p 1

%build
%meson

%install
%meson_install
%find_lang --with-gnome %_name

%files -f %_name.lang
%_datadir/gnome-shell/extensions/%uuid/
%_datadir/metainfo/%_name.metainfo.xml

%changelog
* Mon Mar 30 2026 David Sultaniiazov <x1z53@altlinux.org> 1.0.6-alt1
- Update to 1.0.6.
- Fix URL and VCS spell.

* Sun Dec 07 2025 David Sultaniiazov <x1z53@altlinux.org> 1.0.5-alt1
- Update to 1.0.5.

* Mon Aug 18 2025 David Sultaniiazov <x1z53@altlinux.org> 1.0.3-alt1
- Update to 1.0.3.

* Thu Aug 14 2025 David Sultaniiazov <x1z53@altlinux.org> 1.0.2-alt1
- Initial build. (thx armatik@)
