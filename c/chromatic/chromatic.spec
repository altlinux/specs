%def_enable snapshot
%define optflags_lto %nil

# for version see meson.build
%define ver_major 0.1
%define rdn_name io.github.nate_xyz.Chromatic

%def_disable check
%def_disable bootstrap

Name: chromatic
Version: %ver_major.2
Release: alt1

Summary: Fine-tune your instruments with Chromatic
License: GPL-3.0-or-later
Group: Sound
Url: https://github.com/nate-xyz/chromatic

%if_disabled snapshot
Source: %url/archive/%version/%name-%version.tar.gz
%else
Vcs: https://github.com/nate-xyz/chromatic.git
Source: %name-%version.tar
%endif
Source1: %name-%version-cargo.tar

%define adwaita_ver 1.2

Requires: dconf

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson rust-cargo
BuildRequires: pkgconfig(libadwaita-1) >= %adwaita_ver

BuildRequires: pkgconfig(portaudio-2.0)
%{?_enable_check:BuildRequires: /usr/bin/appstream-util desktop-file-utils}

%description
Chromatic detects the frequency of audio input, converts it to a musical
note with the correct semitone and octave, and displays the cents error.
Cents are displayed on an analog gauge to make tuning more visually
intuitive. Requires PulseAudio or PipeWire.

%prep
%setup -n %name-%version %{?_disable_bootstrap:-a1}
%{?_enable_bootstrap:
mkdir .cargo
cargo vendor | sed 's/^directory = ".*"/directory = "vendor"/g' > .cargo/config
tar -cf %_sourcedir/%name-%version-cargo.tar .cargo/ vendor/}

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
%_desktopdir/%rdn_name.desktop
%_datadir/%name/
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_iconsdir/hicolor/*/apps/%{rdn_name}*.svg
%_datadir/appdata/%rdn_name.appdata.xml
%doc README*


%changelog
* Wed Jan 03 2024 Yuri N. Sedunov <aris@altlinux.org> 0.1.2-alt1
- first build for Sisyphus (ffaeb50)


