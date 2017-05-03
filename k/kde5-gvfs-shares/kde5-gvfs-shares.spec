Name: kde5-gvfs-shares
Version: 0.1.1
Release: alt3
%K5init

Summary: Samba shares plugin for Dolphin

License: GPL
Group: Graphical desktop/KDE
BuildArch: noarch

Requires: kf5-filesystem gvfs-shares

Source: %name-%version.tar

BuildRequires(pre): rpm-build-kf5
BuildRequires: kde5-kdialog

%description
This plugin allows mounting samba shares from Dolphin

%prep
%setup

%install
install -D -m 0644 gvfs-shares-add.desktop %buildroot%_K5srv/ServiceMenus/gvfs-shares-add.desktop
install -D -m 0755 kde5-gvfs-shares %buildroot%_bindir/kde5-gvfs-shares

%files
%_K5srv/ServiceMenus/gvfs-shares-add.desktop
%_bindir/kde5-gvfs-shares

%changelog
* Wed May 03 2017 Oleg Solovyov <mcpain@altlinux.org> 0.1.1-alt3
- Fixed behavior on mounting shares with whitespaces

* Wed May 03 2017 Oleg Solovyov <mcpain@altlinux.org> 0.1.1-alt2
- Minor fixes

* Tue May 02 2017 Oleg Solovyov <mcpain@altlinux.org> 0.1.1-alt1
- Added bash-script for mounting shares

* Mon May 01 2017 Oleg Solovyov <mcpain@altlinux.org> 0.1.0-alt1
- Initial build
