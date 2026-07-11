%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: irontick
Version: 1.0
Release: alt1

Summary: Lightweight, precise, and cross-platform metronome
License: GPL-3.0-or-later
Group: Sound
Url: https://github.com/olegkapitonov/IronTick

Source: %name-%version.tar

BuildRequires(pre): cmake

BuildRequires: gcc-c++
BuildRequires: pkgconfig(Qt6)
BuildRequires: pkgconfig(Qt6Multimedia)

%description
A lightweight, precise, and cross-platform metronome application built with
the Qt 6 framework.
This metronome generates a continuous audio stream with clicks instead of
using a timer-based approach like many others, which results in much more
stable and precise audio timing.

Features:

* High Precision: stable audio playback with minimal latency.
* Time Signatures: support for common musical meters (2/4, 3/4, 4/4, 6/8).
* Visual Feedback: flashing visual indicators for strong and weak beats.
* Tempo Control: adjust tempo from the keyboard.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc README.md images
%_bindir/IronTick
%_desktopdir/IronTick.desktop
%_pixmapsdir/IronTick.png

%changelog
* Sat Jul 11 2026 Nikolay Strelkov <snk@altlinux.org> 1.0-alt1
- Initial build for Sisyphus
