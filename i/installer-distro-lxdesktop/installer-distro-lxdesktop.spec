%define distro lxdesktop
Name: installer-distro-%distro
Version: 6.0
Release: alt5

Summary: Installer files for LXDEsktop distro 
License: GPL
Group: System/Configuration/Other
BuildArch: noarch
Packager: Radik Usupov <radik@altlinux.org>
Source: %name-%version.tar
BuildRequires: alterator rpm-devel

%description
Installer files for LXDEsktop distro.

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
Requires: x-cursor-theme-Vanilla-DMZ-AA
Requires: installer-feature-services

%description stage2
LXDEsktop Installer stage2.

%package stage3
Summary: Installer stage3
License: GPL
Group: System/Configuration/Other
Provides: installer-%distro-stage3 = %name-%version
Requires: installer-stage3
#modules
Requires: alterator-grub
Requires: alterator-users
Requires: alterator-root
Requires: alterator-net-eth dhcpcd
Requires: alterator-net-general
Requires: installer-feature-nfs-server-stage3
Requires: installer-feature-powerbutton-stage3

%description stage3
LXDEsktop Installer stage3.

%prep
%setup

%install
%makeinstall

%find_lang alterator-lxdesktop

%files -f alterator-lxdesktop.lang
%_datadir/install2/help/*

%files stage2
%_datadir/install2/installer-steps
%_datadir/install2/*.d/*
%_datadir/install2/steps/*
%_datadir/install2/alterator-menu

%files stage3
%_datadir/alterator/ui/lxdesktop

%changelog
* Mon Mar 19 2012 Radik Usupov <radik@altlinux.org> 6.0-alt5
- Added grub reconfigure script
- Updated remove-installer-lxdesktop-pkgs

* Thu Mar 08 2012 Radik Usupov <radik@altlinux.org> 6.0-alt4
- Fixed 55_drop_apps_from_menu

* Thu Feb 23 2012 Radik Usupov <radik@altlinux.org> 6.0-alt3
- Added 55_drop_apps_from_menu script

* Thu Nov 17 2011 Radik Usupov <radik@altlinux.org> 6.0-alt2
- Added more group for user
- Added postinstall script
- Fixed vm-profile

* Tue Feb 22 2011 Radik Usupov <radik@altlinux.org> 6.0-alt1
- Initial build

