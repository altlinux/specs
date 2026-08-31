%define _unpackaged_files_terminate_build 1
%define app_id org.altlinux.Tailor

%def_with check

Name: tailor-adw
Version: 0.1.1
Release: alt1

Summary: Create bootable drives
License: GPL-3.0-or-later
Group: System/Configuration/Other
Url: https://altlinux.space/qualimock/Tailor
VCS: https://altlinux.space/qualimock/Tailor

Source0: %name-%version.tar
Source1: 50-tailor-primary-distro-alt.gschema.override
Patch0: tailor-0.1.1-alt-add-primary-distro-translation.patch

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: vala
BuildRequires: blueprint-compiler
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(libosinfo-1.0)
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: pkgconfig(udisks2)

%description
Tailor is an application for writing OS images to USB drives.

Pick an OS and edition from the built-in catalog (or supply your own ISO),
pick a target drive, and Tailor downloads, verifies, and flashes it.

%description -l ru
Портной это приложение для записи образов ОС на USB носители.

Выберите ОС и редакцию из каталога (или используйте свой ISO образ),
выберите целевое устройство, и Портной загрузит, подтвердит и запишет образ.

%prep
%setup
%autopatch -p1

%build
%meson
%meson_build

%install
%meson_install
install -pD -m0644 %SOURCE1 %buildroot%_datadir/glib-2.0/schemas/
%find_lang --with-gnome tailor

%check
%__meson_test

%files -f tailor.lang
%doc README.md
%_bindir/tailor
%_desktopdir/%app_id.desktop
%_datadir/glib-2.0/schemas/%app_id.gschema.xml
%_datadir/glib-2.0/schemas/50-tailor-primary-distro-alt.gschema.override
%_datadir/metainfo/%app_id.metainfo.xml
%_iconsdir/hicolor/*/apps/*.svg

%changelog
* Mon Aug 31 2026 Alexey Volkov <qualimock@altlinux.org> 0.1.1-alt1
- initial build for ALT
