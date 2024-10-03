Name: eepm-play-gui
Version: 0.1.0
Release: alt1
License: AGPL2

Summary: GUI for epm play

Group: System/Configuration/Packaging

Url: https://gitlab.eterfund.ru/ximper/eepm-play-gui

BuildArch: noarch

Source: %name-%version.tar

AutoProv: no

Requires: eepm-repack

BuildRequires(pre): rpm-macros-meson rpm-macros-systemd
BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-build-gir

BuildRequires: libadwaita-gir-devel
BuildRequires: meson

%add_python3_path %_datadir/%name

%description
GUI frontend for install third-party applications using epm play.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name

%files -f %name.lang
%_bindir/%name

%_datadir/%name
%_datadir/glib-2.0/schemas/*.gschema.xml
%_datadir/metainfo/*.metainfo.xml

%_desktopdir/ru.eepm.PlayGUI.desktop

%_iconsdir/hicolor/*/apps/*.svg

%changelog
* Thu Oct 03 2024 Roman Alifanov <ximper@altlinux.org> 0.1.0-alt1
- initial build
