%define _unpackaged_files_terminate_build 1

Name: elementary-sound-theme
Version: 1.1.0
Release: alt1

Summary: A bespoke sound for your theme
License: Unlicense
Group: Graphical desktop/Other
Url: https://github.com/elementary/sound-theme

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-build-vala

BuildRequires: meson
BuildRequires: cmake
BuildRequires: vala-tools

BuildArch: noarch

%description
%summary

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%files
%doc LICENSE README.md
%dir %_datadir/sounds/elementary/
%_datadir/sounds/elementary/index.theme
%dir %_datadir/sounds/elementary/stereo
%_datadir/sounds/elementary/stereo/audio-volume-change.wav
%_datadir/sounds/elementary/stereo/bell.wav
%_datadir/sounds/elementary/stereo/dialog-error.ogg
%_datadir/sounds/elementary/stereo/dialog-information.oga
%_datadir/sounds/elementary/stereo/dialog-warning.ogg

%changelog
* Sun Sep 21 2025 Nikolay Strelkov <snk@altlinux.org> 1.1.0-alt1
- Initial build for Sisyphus
