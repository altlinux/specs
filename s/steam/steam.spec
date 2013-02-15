Name: steam
Version: 1.0.0.27
Release: alt1

Summary: Installer for the Steam software distribution service
License: Proprietary
Group: Games/Other

URL: http://www.steampowered.com/
Packager: Nazarov Denis <nenderus@altlinux.org>
Vendor: Valve Corporation

ExclusiveArch: %ix86

Source0: http://repo.steampowered.com/%name/pool/%name/s/%name/%{name}_%version.tar.gz
Patch0: %name-%version-alt.patch

Requires: libGL
Requires: glibc >= 2.15

BuildRequires: python-module-distribute
BuildRequires: xterm
BuildRequires: zenity

%description
Steam is a software distribution service with an online store, automated
installation, automatic updates, achievements, SteamCloud synchronized
savegame and screenshot functionality, and many social features.

%prep
%setup -n %name-%version
%patch0 -p1

%install
%make DESTDIR=%buildroot install

%files
%_bindir/*
%dir %_libdir/%name
%_libdir/%name/*
%_desktopdir/*
%_docdir/*
%_miconsdir/*
%_iconsdir/hicolor/24x24/apps/*
%_niconsdir/*
%_liconsdir/*
%_iconsdir/hicolor/256x256/apps/*
%_man6dir/*
%_pixmapsdir/*

%changelog 
* Fri Feb 15 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0.27-alt1
- Version 1.0.0.27

* Mon Feb 11 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0.25-alt2
- Fix end of line in desktop file

* Sun Feb 10 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0.25-alt1
- Initial build for ALT Linux

