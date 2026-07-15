%define _unpackaged_files_terminate_build 1

Name: appmanager
Version: 3.7.2
Release: alt1

Summary: MacOS style AppImage installer and management application
License: GPL-3.0-or-later
Group: System/Configuration/Packaging
Url: https://github.com/kem-a/AppManager

Source: %name-%version.tar

BuildRequires(pre): meson
BuildRequires(pre): rpm-build-vala

BuildRequires: vala-tools
BuildRequires: cmake
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: pkgconfig(libsecret-1)
BuildRequires: pkgconfig(gnutls)

Requires: /usr/bin/dwarfsextract
Requires: /usr/bin/unsquashfs
Requires: /usr/bin/zsync
Requires: libfuse
Requires: /usr/bin/fusermount2
Requires: appimage-thumbnailer

ExclusiveArch: x86_64 aarch64

%description
AppManager lets you install or uninstall AppImages with a familiar
drag-and-drop workflow inspired by macOS. It handles desktop
integration, icon extraction, executable bits, and app updates.

%prep
%setup
sed 's/"fusermount"/"fusermount2"/' src/windows/main_window.vala
sed -i "s|Categories=.*|Categories=GNOME;GTK;Settings;PackageManager;|" data/app-manager.desktop.in

%build
%meson \
       -Dbundle_dwarfs=false \
       -Dbundle_zsync=false \
       -Dbundle_unsquashfs=false
%meson_build

%install
%meson_install

%find_lang app-manager

%files -f app-manager.lang
%doc LICENSE README.md
%_bindir/app-manager
%_desktopdir/*.desktop
%_iconsdir/hicolor/scalable/apps/*.svg
%_datadir/glib-2.0/schemas/com.github.AppManager.gschema.xml
%_datadir/glib-2.0/schemas/gschemas.compiled
%_datadir/metainfo/com.github.AppManager.metainfo.xml

%changelog
* Wed Jul 15 2026 Nikolay Strelkov <snk@altlinux.org> 3.7.2-alt1
- Initial build for Sisyphus
