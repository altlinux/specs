%define distro backup-server
Name: installer-distro-%distro
Version: 6.0
Release: alt1
Packager: Radik Usupov <radik@altlinux.org>

Summary: Installer files for backup server
License: GPL
Group: System/Configuration/Other
BuildArch: noarch

Source: %name-%version.tar

%description
Installer files for backup server.

%package stage2
Summary: Installer stage2
License: GPL
Group: System/Configuration/Other
Provides: installer-%distro-stage2 = %name-%version
Requires: installer-stage2
#modules
Requires: alterator-sysconfig
Requires: alterator-datetime
Requires: alterator-pkg
Requires: alterator-vm
Requires: alterator-notes
Requires: x-cursor-theme-jimmac
Requires: installer-feature-services

%description stage2
Installer backup server stage2.

%package stage3
Summary: Installer stage3
License: GPL
Group: System/Configuration/Other
Provides: installer-%distro-stage3 = %name-%version
Requires: installer-stage3
#modules
Requires: alterator-grub
Requires: alterator-distro-backup-server >= 0.4-alt2
Requires: installer-feature-powerbutton-stage3
Requires: installer-feature-eth-by-mac-stage3

%description stage3
Installer backup server stage3.

%prep
%setup

%install
%define install2dir %_datadir/install2
mkdir -p %buildroot%install2dir
cp -a * %buildroot%install2dir/

%files stage2
%install2dir/alterator-menu
%install2dir/steps/*
%install2dir/installer-steps
%install2dir/*.d/*

%files stage3

%changelog
* Tue Nov 23 2010 Radik Usupov <radik@altlinux.org> 6.0-alt1
- Build from sisyphus
- Fix spec-file from sisyphus
- Change packager

* Fri Dec 04 2009 Stanislav Ievlev <inger@altlinux.org> 5.0-alt8
- turn on alteratord service by default

* Wed Nov 18 2009 Stanislav Ievlev <inger@altlinux.org> 5.0-alt7
- update for newest alterator-distro-backup-server

* Wed Oct 21 2009 Stanislav Ievlev <inger@altlinux.org> 5.0-alt6
- menu order: update to new menu style

* Wed Aug 26 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 5.0-alt5
- smart swap size calculation (ALT #21245)

* Thu Aug 20 2009 Stanislav Ievlev <inger@altlinux.org> 5.0-alt4
- change config from standard ahttpd
  instead of using separate ahttpd-backup-server daemon

* Thu Aug 13 2009 Stanislav Ievlev <inger@altlinux.org> 5.0-alt3
- drop first two steps

* Thu Jun 18 2009 Stanislav Ievlev <inger@altlinux.org> 5.0-alt2
- use own vm setup instead of vm setup from office server

* Tue Jun 09 2009 Stanislav Ievlev <inger@altlinux.org> 5.0-alt1
- Initial build
