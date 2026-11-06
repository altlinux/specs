# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%define app_id com.mattjakeman.ExtensionManager

Name: gnome-extension-manager
Version: 0.7.0
Release: alt1

Summary: A utility for browsing and installing GNOME Shell Extensions
License: GPL-3.0
Group: Graphical desktop/GNOME
Url: https://github.com/mjakeman/extension-manager
Vcs: https://github.com/mjakeman/extension-manager.git

Source: %name-%version.tar

Obsoletes: extension-manager < %EVR
Provides: extension-manager = %EVR

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: gcc-c++
BuildRequires: libbacktrace-devel
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: typelib(Adw) 
BuildRequires: pkgconfig(libsoup-3.0)
BuildRequires: pkgconfig(blueprint-compiler)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(glycin-2)
BuildRequires: pkgconfig(glycin-gtk4-2)

%description
A native tool for browsing, installing, and managing GNOME Shell Extensions.

With Extension Manager you can:
* Browsing and searching extensions from extensions.gnome.org
* Installation and Removal
* Enabling and Disabling
* Updating in-app 
* Screenshots & Images
* Ratings & Comments

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang extension-manager

%files -f extension-manager.lang
%doc README.md
%_bindir/extension-manager
%_datadir/applications/%app_id.desktop
%_datadir/dbus-1/services/%app_id.service
%_datadir/glib-2.0/schemas/%app_id.gschema.xml
%_datadir/icons/hicolor/scalable/apps/%app_id.svg
%_datadir/icons/hicolor/symbolic/apps/%app_id-symbolic.svg
%_datadir/metainfo/%app_id.metainfo.xml
%_datadir/gnome-shell/search-providers/%app_id.search-provider.ini

%changelog
* Fri Nov 06 2026 Anton Midyukov <antohami@altlinux.org> 0.7.0-alt1
- New version 0.7.0.

* Thu Oct 02 2025 Anton Midyukov <antohami@altlinux.org> 0.6.5-alt1
- New version 0.6.5.

* Wed Sep 17 2025 Anton Midyukov <antohami@altlinux.org> 0.6.4-alt1
- New version 0.6.4.

* Wed Apr 02 2025 Anton Midyukov <antohami@altlinux.org> 0.6.3-alt1
- New version 0.6.3.

* Wed Mar 19 2025 Anton Midyukov <antohami@altlinux.org> 0.6.2-alt1
- New version 0.6.2.

* Sat Feb 15 2025 Anton Midyukov <antohami@altlinux.org> 0.6.1-alt2
- Fix BR

* Fri Jan 10 2025 Anton Midyukov <antohami@altlinux.org> 0.6.1-alt1
- New version 0.6.1.

* Thu Dec 19 2024 Anton Midyukov <antohami@altlinux.org> 0.6.0-alt1
- new version 0.6.0

* Sat May 25 2024 Roman Alifanov <ximper@altlinux.org> 0.5.1-alt1
- new version 0.5.1 (with rpmrb script)

* Sun Mar 31 2024 Roman Alifanov <ximper@altlinux.org> 0.5.0-alt1
- new version 0.5.0 (with rpmrb script)

* Sun Mar 31 2024 Roman Alifanov <ximper@altlinux.org> 0.4.3-alt2
- fix rebuild: unnecessary BR removed

* Mon Nov 27 2023 Roman Alifanov <ximper@altlinux.org> 0.4.3-alt1
- new version 0.4.3 (with rpmrb script)

* Thu Jul 20 2023 Roman Alifanov <ximper@altlinux.org> 0.4.2-alt3
- renaming package because old name was not specified

* Mon Jul 10 2023 Roman Alifanov <ximper@altlinux.org> 0.4.2-alt2
- build without removing backtrace-supported.h

* Mon Jun 26 2023 Roman Alifanov <ximper@altlinux.org> 0.4.2-alt1
- Initial build for Sisyphus.
