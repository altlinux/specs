%define _unpackaged_files_terminate_build 1

Name:    juhradial-mx
Version: 0.4.4
Release: alt1

Summary: Radial menu overlay for Logitech MX Master mice
License: GPL-3.0-or-later
Group:   System/Configuration/Hardware
URL:     https://www.juhlabs.com/
VCS:     https://github.com/JuhLabs/juhradial-mx

Source:  %name-%version.tar
Source1: %name-development-%version.tar
Patch:   juhradial-mx-systemd-path.patch

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust rpm-build-python3

Requires: python3
Requires: python3-module-PyQt6
Requires: python3-module-pygobject3
Requires: python3-module-cryptography
Requires: glib2
Requires: libgtk4-gir
Requires: libadwaita-gir
Requires: libpango-gir
Requires: libgdk-pixbuf-gir
Requires: libgraphene-gir

# Internal Python modules shipped by this package.
%add_python3_req_skip overlay overlay.flow overlay.flow.marconi
%add_python3_req_skip overlay.flow.client overlay.flow.clipboard
%add_python3_req_skip overlay.flow.constants overlay.flow.crypto
%add_python3_req_skip overlay.flow.juhflow_bridge overlay.flow.keys
%add_python3_req_skip overlay.flow.logi_discovery
%add_python3_req_skip overlay.flow.logi_presence
%add_python3_req_skip overlay.flow.logi_server overlay.flow.managers
%add_python3_req_skip overlay.flow.server
%add_python3_req_skip overlay_actions overlay_constants overlay_cursor
%add_python3_req_skip overlay_media overlay_painting
%add_python3_req_skip settings_config settings_constants settings_css
%add_python3_req_skip settings_dialog_apps settings_dialog_button
%add_python3_req_skip settings_dialog_macro settings_dialog_radial
%add_python3_req_skip settings_dialogs settings_flow_discovery
%add_python3_req_skip settings_macro_actions settings_macro_recorder
%add_python3_req_skip settings_macro_storage settings_macro_timeline
%add_python3_req_skip settings_page_buttons settings_page_devices
%add_python3_req_skip settings_page_easyswitch settings_page_gaming
%add_python3_req_skip settings_page_haptics settings_page_macros
%add_python3_req_skip settings_page_scroll settings_page_settings
%add_python3_req_skip settings_sidebar settings_theme settings_widgets
%add_python3_req_skip themes i18n

%description
JuhRadial MX is a Logi Options+ style radial menu for Logitech MX Master
mice on Linux. Hold the gesture button to open an animated radial overlay
with quick actions (screenshots, DPI, Logi Flow, media, haptics, custom
macros and more). The Rust daemon (juhradiald) reads evdev and hidraw
events, exposes a session D-Bus API and executes actions; the Python
overlay (PyQt6 radial menu, GTK4/libadwaita settings UI) renders the
interface.

%prep
%setup -a1
%patch -p1
%rust_prep

%build
cd daemon
%rust_build

%install
cd daemon
%rust_install juhradiald
cd ..

install -Dm755 scripts/juhradial-mx.sh %buildroot%_bindir/juhradial-mx
install -Dm755 scripts/juhradial-settings.sh %buildroot%_bindir/juhradial-settings

mkdir -p %buildroot%_datadir/juhradial
for f in overlay/*.py; do
	sed '1{/^#!\/.*python/d}' "$f" > "%buildroot%_datadir/juhradial/$(basename "$f")"
done
cp -a overlay/flow %buildroot%_datadir/juhradial/
cp -a overlay/locales %buildroot%_datadir/juhradial/
cp -a assets %buildroot%_datadir/juhradial/

install -Dm644 packaging/juhradial-mx.desktop \
	%buildroot%_desktopdir/juhradial-mx.desktop

install -Dm644 packaging/org.kde.juhradialmx.settings.desktop \
	%buildroot%_desktopdir/org.kde.juhradialmx.settings.desktop

install -Dm644 assets/juhradial-mx.svg \
	%buildroot%_iconsdir/hicolor/scalable/apps/juhradial-mx.svg

install -Dm644 packaging/systemd/juhradialmx-daemon.service \
	%buildroot%_userunitdir/juhradialmx-daemon.service

install -Dm644 packaging/udev/99-juhradialmx.rules \
	%buildroot%_udevrulesdir/99-juhradialmx.rules

install -Dm644 packaging/udev/60-ydotool-uinput.rules \
	%buildroot%_udevrulesdir/60-ydotool-uinput.rules

%post
udevadm trigger --subsystem-match=hidraw --subsystem-match=input || :
echo "NOTE: enable the daemon user service with:"
echo "            systemctl --user enable --now juhradialmx-daemon.service"

%postun

%files
%doc LICENSE README.md CONTRIBUTING.md
%_bindir/juhradiald
%_bindir/juhradial-mx
%_bindir/juhradial-settings
%_datadir/juhradial
%_desktopdir/juhradial-mx.desktop
%_desktopdir/org.kde.juhradialmx.settings.desktop
%_iconsdir/hicolor/scalable/apps/juhradial-mx.svg
%_userunitdir/juhradialmx-daemon.service
%_udevrulesdir/99-juhradialmx.rules
%_udevrulesdir/60-ydotool-uinput.rules

%changelog
* Tue Sep 08 2026 Sergey Palcheh <minergenon@altlinux.org> 0.4.4-alt1
- Initial build for Sisyphus
