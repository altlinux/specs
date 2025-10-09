# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name:    jaqalmixer
Version: 02102025
Release: alt1

Summary: Advanced control panel for low-level soundcard configuration
License: GPL-3.0-only
Group:   Sound
Url:     https://codeberg.org/zynskeyfolf/JaqalMixer
VCS:     https://codeberg.org/zynskeyfolf/JaqalMixer

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: qt6-base-devel
BuildRequires: libalsa-devel
Requires: alsa-utils

%description
JaqalMixer is an advanced control panel application that gives you
direct access to the low-level controls of your soundcard, such
as analog volume controls, signal routing, jack sensor indicators,
S/PDIF status codes and several other settings (varies by hardware).

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%_bindir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/64x64/apps/%name.png
%doc *.md

%changelog
* Tue Oct 07 2025 Polina Poidenko <polipoki@altlinux.org> 02102025-alt1
- Initial build for Sisyphus.
