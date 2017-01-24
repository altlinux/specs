Name:     gvfs-shares
Version:  1.1
Release:  alt1

Summary:  Script for automount specified GIO locations
License:  GPLv3+
Group:    System/Configuration/Networking
URL: 	  http://altlinux.org/gvfs-shares
Packager: Andrey Cherepanov <cas@altlinux.org> 
BuildArch: noarch

Source1:   %name
Source2:   gvfs-automount.desktop

Requires:  fuse-gvfs gvfs-backend-smb gvfs-utils

%description
Script for automount specified GIO locations.

%install
install -Dm755 %SOURCE1 %buildroot%_bindir/%name
install -Dm644 %SOURCE2 %buildroot%_sysconfdir/xdg/autostart/gvfs-automount.desktop

%files
%_bindir/%name
%_sysconfdir/xdg/autostart/gvfs-automount.desktop

%changelog
* Tue Jan 24 2017 Andrey Cherepanov <cas@altlinux.org> 1.1-alt1
- Support --help and --version, correct process unknown command

* Wed Dec 28 2016 Andrey Cherepanov <cas@altlinux.org> 1.0-alt1
- Initial build in Sisyphus

