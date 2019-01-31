Name:     shared-desktop-icons
Version:  1.1
Release:  alt1

Summary:  Put all files from /usr/share/Desktop to all user desktops
License:  GPLv3+
Group:    Other
Url:      https://altlinux.org/shared-desktop-icons

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name.desktop
Source1: shared-desktop-icons-sync

BuildRequires(pre): rpm-build-xdg
Requires: bash
Requires: rsync
Requires: xdg-user-dirs

BuildArch: noarch

%description
Put all files from /usr/share/Desktop to all user desktops by autostart
mechanism. It is usable to make default applications icons to desktop.

%prep

%install
install -d %buildroot%_datadir/Desktop
install -Dm0644 %SOURCE0 %buildroot%_xdgconfigdir/autostart/%name.desktop
install -Dm0755 %SOURCE1 %buildroot%_bindir/shared-desktop-icons-sync

%files
%dir %_datadir/Desktop
%_bindir/shared-desktop-icons-sync
%_xdgconfigdir/autostart/%name.desktop

%changelog
* Thu Jan 31 2019 Andrey Cherepanov <cas@altlinux.org> 1.1-alt1
- Sync only files which are not deleted early from desktop by user.

* Sun May 06 2018 Andrey Cherepanov <cas@altlinux.org> 1.0-alt1
- Initial build in Sisyphus
