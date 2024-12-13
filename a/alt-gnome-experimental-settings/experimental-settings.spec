%define _unpackaged_files_terminate_build 1
%def_enable check
%define app_id org.altlinux.gnome.ExperimentalSettings
%define bin_name experimental-settings

Name: alt-gnome-experimental-settings
Version: 0.1.3
Release: alt1

Summary: Experimental Alt settings for GNOME desktop environment
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME

Url: https://gitlab.gnome.org/Armatik/alt-experimental-settings
Vcs: https://gitlab.gnome.org/Armatik/alt-experimental-settings
Source: %name-%version.tar

Requires: alt-panelmoded

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: vala
BuildRequires: blueprint-compiler
BuildRequires: pkgconfig(libadwaita-1)
%if_enabled check
BuildRequires: desktop-file-utils
BuildRequires: appstream
BuildRequires: libgio
%endif

%description
Try out the new features of the system now!

Experimental settings have been created to enable all users
of Alt operating systems with a graphical GNOME environment
to try the latest features developed specifically for Alt

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome %bin_name

%check
export AS_VALIDATE_NONET="true"
%meson_test

%files -f %bin_name.lang
%_bindir/%bin_name
%_desktopdir/%app_id.desktop
%_iconsdir/hicolor/*/apps/%{app_id}*.svg
%_datadir/glib-2.0/schemas/%app_id.gschema.xml
%_datadir/metainfo/%app_id.metainfo.xml

%changelog
* Fri Dec 13 2024 Semen Fomchenkov <armatik@altlinux.org> 0.1.3-alt1
- Initial build for Sisyphus.
