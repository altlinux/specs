Name: eepm-play-gui
Version: 0.3.0
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
* Tue Oct 15 2024 Roman Alifanov <ximper@altlinux.org> 0.3.0-alt1
- fix error: tput: unknown terminfo capability '2'
- added flags dialog and button
- added the ability to answer a question from the terminal (such as [Y/n])
- added the --auto flag and other minor improvements
- added reset button

* Wed Oct 09 2024 Roman Alifanov <ximper@altlinux.org> 0.2.1-alt1
- some improvements (thx rirusha@)

* Tue Oct 08 2024 Roman Alifanov <ximper@altlinux.org> 0.2.0-alt1
- redesign + changing the color of the row when the state is changed
- added filter: changed
- resetting the button status and lists immediately after command running

* Thu Oct 03 2024 Roman Alifanov <ximper@altlinux.org> 0.1.0-alt1
- initial build
