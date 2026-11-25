%define _unpackaged_files_terminate_build 1
%define app_id org.altlinux.StudioFX.Ui

%def_enable check

Name: studiofx-ui
Version: 0.1.0
Release: alt1
Summary: GTK client for StudioFX audio/video processing daemon
Group: Graphical desktop/GNOME
License: GPL-3.0-or-later
Url: https://altlinux.space/alt-gnome/StudioFX-UI
Vcs: https://altlinux.space/alt-gnome/StudioFX-UI

Source0: %name-%version.tar

Requires: typelib(Adw)
Requires: studiofx

BuildRequires: meson
BuildRequires: vala
BuildRequires: blueprint-compiler
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(gstreamer-app-1.0)
%if_enabled check
BuildRequires: desktop-file-utils
BuildRequires: appstream
%endif

%description
StudioFX UI is a graphical client for the StudioFX daemon. The application
adjusts microphone and headphone processing (RNNoise, AGC, compressor),
device selection, background segmentation, blurring, zooming, and
automatic camera cropping.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome %name

%check
%meson_test

%files -f %name.lang
%_bindir/%name
%_desktopdir/%app_id.desktop
%_iconsdir/hicolor/scalable/apps/%app_id.svg
%_datadir/metainfo/%app_id.metainfo.xml
%_datadir/glib-2.0/schemas/%app_id.gschema.xml

%changelog
* Fri Nov 20 2026 Vladislav Petrukhin <vladp@altlinux.org> 0.1.0-alt1
- Initial build.

