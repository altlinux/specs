%define _name whisper
%define ver_major 1.3
%define rdn_name it.mijorus.%_name

%def_disable check

Name: %_name
Version: %ver_major.1
Release: alt1

Summary: Listen to your microphone
License: GPL-3.0-or-later
Group: Sound
Url: https://github.com/mijorus/whisper

Vcs: https://github.com/mijorus/whisper.git

Source: %name-%version.tar

BuildArch: noarch

%add_python3_path %_datadir/%_name

Requires: python3-module-pygobject3
Requires: typelib(Adw) = 1
Requires: dconf
# requirements.txt
Requires: python3-module-pulsectl >= 24.11.0
Requires: python3-module-dbus >= 1.2.18

BuildRequires(pre): rpm-macros-meson rpm-build-python3 rpm-build-gir
BuildRequires: meson /usr/bin/glib-compile-resources
BuildRequires: gtk4-update-icon-cache
%{?_enable_check:BuildRequires: /usr/bin/desktop-file-validate /usr/bin/appstream-util
BuildRequires: /usr/bin/glib-compile-schemas}

%description
Whisper allows you to listen to your microphone through your speakers.
It's useful for testing your microphone or for listening to your voice.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name

%check
%__meson_test

%files -f %name.lang
%_bindir/%name
%_datadir/%name/
%_desktopdir/%rdn_name.desktop
%_datadir/icons/hicolor/*/*/*.svg
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_datadir/appdata/%rdn_name.appdata.xml
%doc README.*

%changelog
* Sun Mar 22 2026 Yuri N. Sedunov <aris@altlinux.org> 1.3.1-alt1
- 1.3.1

* Tue Feb 18 2025 Yuri N. Sedunov <aris@altlinux.org> 1.3.0-alt1
- first build for Sisyphus
