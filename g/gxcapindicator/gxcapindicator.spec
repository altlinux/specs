%define _unpackaged_files_terminate_build 1

Name: gxcapindicator
Version: 1.2
Release: alt3

Summary: Simple and universal Cap/Num lock key indicator in the tray
License: GPL-3.0
Group: Graphical desktop/Other
Url: https://codeberg.org/ItsZariep/GXCapIndicator
VCS: https://github.com/ItsZariep/GXCapIndicator

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires: pkgconfig(libinput)
BuildRequires: pkgconfig(libevdev)
BuildRequires: pkgconfig(ayatana-appindicator3-0.1)

%description
GXCapIndicator is a simple tool for indicating the status of Caps Lock
and Num Lock keys in the system tray.

Features
* Monitor Caps Lock and Num Lock keys;
* Toggle Caps Lock and Num Lock with an on-screen button;
* Hideable indicators;
* Adjustable update rate;
* Wayland support (with Evdev);

%prep
%setup
%patch -p1

%build
%make_build PREFIX=%buildroot/%_prefix WITHX11=1

%install
%makeinstall_std PREFIX=%buildroot/%_prefix WITHX11=1

%files
%doc README.md
%_bindir/*
%_desktopdir/%{name}.desktop
%_iconsdir/hicolor/*/devices/*

%changelog
* Thu Apr 23 2026 Nikolay Strelkov <snk@altlinux.org> 1.2-alt3
- Fixed FTBFS caused by gcc15.

* Sun Mar 16 2025 Nikolay Strelkov <snk@altlinux.org> 1.2-alt2
- Added upstream mirror URL, corrected license.

* Sat Mar 15 2025 Nikolay Strelkov <snk@altlinux.org> 1.2-alt1
- Initial build for Sisyphus
