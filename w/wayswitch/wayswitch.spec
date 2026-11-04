Name: wayswitch
Version: 1.0.0
Release: alt1

Summary: Automatic Russian and English keyboard layout correction for Wayland

License: MIT AND CC-BY-SA-4.0
Group: System/Configuration/Other
URL: https://github.com/Wetoshkin/WaySwitch
# Source-url: https://github.com/Wetoshkin/WaySwitch/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar
Source1: README.ALT
Patch0: %name-input-privacy.patch
Patch1: %name-alt-package-actions.patch

BuildArch: noarch
AutoProv: nopython3
# XKB loads its layout data at runtime; import scanning cannot discover it.
Requires: xkeyboard-config
BuildRequires: rpm-build-python3 rpm-build-gir
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: python3-module-pytest libxkbcommon xkeyboard-config
BuildRequires: python3-module-evdev python3-module-pygobject3

# evdev and GI are intentionally imported inside functions by upstream.
%set_python3_req_method strict

%description
WaySwitch corrects words typed with the wrong Russian or English keyboard
layout on Wayland and provides a GTK settings interface. It includes a
GNOME Shell extension and a KDE Plasma widget.

The daemon requires access to input event devices and /dev/uinput.
See README.ALT for device permissions, privacy and desktop integration.

%prep
%setup
%patch0 -p1
%patch1 -p1
cp %SOURCE1 .

%build
%pyproject_build

%install
# Use the same desktop/device integration as the upstream Arch/RPM recipes.
bash tools/stage.sh %buildroot %python3_sitelibdir
%pyproject_install
rm -r %buildroot%_datadir/licenses %buildroot%_docdir/%name

%check
python3 -c 'import evdev, gi'
PYTHONPATH=. python3 -m pytest -q

%files
%doc README.md README.en.md README.ALT LICENSE
%_bindir/wayswitch
%_bindir/wayswitch-gui
%python3_sitelibdir/wayswitch/
%python3_sitelibdir/%{pyproject_distinfo wayswitch}/
%_udevrulesdir/60-wayswitch.rules
%_modulesloaddir/wayswitch.conf
%_userunitdir/wayswitch.service
%dir %_datadir/gnome-shell
%dir %_datadir/gnome-shell/extensions
%_datadir/gnome-shell/extensions/wayswitch@siberia.ru/
%dir %_datadir/plasma
%dir %_datadir/plasma/plasmoids
%_datadir/plasma/plasmoids/ru.siberia.wayswitch/
%config(noreplace) %_sysconfdir/xdg/autostart/wayswitch-session.desktop
%_desktopdir/ru.siberia.WaySwitch.Settings.desktop
%_iconsdir/hicolor/scalable/apps/ru.siberia.WaySwitch.svg
%_iconsdir/hicolor/symbolic/apps/ru.siberia.WaySwitch*symbolic.svg

%changelog
* Tue Nov 03 2026 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt1
- initial build for ALT Linux.

