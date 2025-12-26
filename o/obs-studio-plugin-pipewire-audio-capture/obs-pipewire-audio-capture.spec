%define oname linux-pipewire-audio

Name: obs-studio-plugin-pipewire-audio-capture
Version: 1.2.1
Release: alt1

Summary: Audio device and application capture for OBS Studio using PipeWire

License: GPL-2.0-only
Group: Video

Url: https://github.com/dimtpap/obs-pipewire-audio-capture
Vcs: https://github.com/dimtpap/obs-pipewire-audio-capture

Source: %name-%version.tar

BuildRequires(Pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++ libobs-devel
BuildRequires: pipewire-libs-devel

%description
%summary.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%_libdir/obs-plugins/%oname.so
%_datadir/obs/obs-plugins/%oname
%doc *.md LICENSE

%changelog
* Fri Dec 26 2025 Aleksandr Shamaraev <shad@altlinux.org> 1.2.1-alt1
- Initial build for ALT Linux.

