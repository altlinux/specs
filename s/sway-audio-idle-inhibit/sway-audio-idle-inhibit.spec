%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: sway-audio-idle-inhibit
Version: 0.2.0
Release: alt1

Summary: Prevents swayidle from sleeping while any application is outputting or receiving audio
License: GPL-3.0-only
Group: Graphical desktop/Other
Url: https://github.com/ErikReider/SwayAudioIdleInhibit

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-cmake

BuildRequires: meson
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(libsystemd)
BuildRequires: pkgconfig(libpulse)

%description
Prevents swayidle/hypridle from sleeping while any application is
outputting or receiving audio. Requires systemd/elogind inhibit support.

This only works for Pulseaudio / Pipewire Pulse.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%files
%doc LICENSE README.md
%_bindir/sway-audio-idle-inhibit

%changelog
* Sun Dec 21 2025 Nikolay Strelkov <snk@altlinux.org> 0.2.0-alt1
- Initial build for Sisyphus
