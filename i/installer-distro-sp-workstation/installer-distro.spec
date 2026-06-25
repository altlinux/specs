%define distro sp-workstation
Name: installer-distro-%distro
Version: 11.0
Release: alt5

License: GPL-2.0-or-later
Group: System/Configuration/Other
#BuildRequires: alterator-officer
Summary: Installer files for the %distro distro

Source: %name-%version.tar

%description
Installer files for %distro distro.

%package common
Summary: %distro installer common files
License: GPL-2.0-or-later
Group: System/Configuration/Other

%description common
%distro Installer common files.
Needed also for alterator-setup.

%package stage2
Summary: %distro installer stage2 files
License: GPL-2.0-or-later
Group: System/Configuration/Other
# live packages
Requires: livecd-net-eth
Requires: livecd-auto-hostname
# installer
Requires: installer-common-stage2
#modules
Requires: alterator-sysconfig
Requires: alterator-datetime
Requires: alterator-pkg
Requires: alterator-vm
Requires: alterator-notes
Requires: alterator-net-eth
Requires: alterator-net-bridge
Requires: alterator-net-vlan
Requires: alterator-net-wifi
Requires: installer-feature-network-settings-copy
Requires: %name-common = %EVR
Requires: x-cursor-theme-jimmac
Requires: installer-feature-integalert-stage2

%description stage2
%distro installer stage2 files.

%package stage3
Summary: %distro installer stage3 files
License: GPL-2.0-or-later
Group: System/Configuration/Other
Provides: installer-%distro-stage3 = %name-%version
#modules
Requires: alterator-users
#Requires: alterator-officer
Requires: alterator-root
Requires: installer-feature-nfs-server-stage3
Requires: installer-feature-powerbutton-stage3
Requires: installer-feature-integalert-stage3
Requires: alterator-luks

%description stage3
%distro installer stage3 files.

%prep
%setup

%install
%define install2dir %_datadir/install2
mkdir -p %buildroot%install2dir
mkdir -p %buildroot%install2dir/steps
cp -a * %buildroot%install2dir/
cp -a steps.d/* %buildroot%install2dir/steps 

%files common
#%%install2dir/steps/users-officer.desktop
%install2dir/*.d/*

%files stage2
%install2dir/alterator-menu
%install2dir/installer-steps
%ghost %install2dir/services-*
%ghost %install2dir/systemd-*

%files stage3

%changelog
* Thu Jun 25 2026 Anton Midyukov <antohami@altlinux.org> 11.0-alt5
- 52-installer-added-smem-1.sh: fix sed.

* Thu Feb 19 2026 Anton Midyukov <antohami@altlinux.org> 11.0-alt4
- stage2: remove dependency on installer-feature-gnome-keymap-stage2.

* Fri Jan 02 2026 Anton Midyukov <antohami@altlinux.org> 11.0-alt3
- stage2: add dependency on installer-feature-gnome-keymap-stage2.

* Wed Jun 11 2025 Anton Midyukov <antohami@altlinux.org> 11.0-alt2
- installer-steps: change order of steps, luks after preinstall

* Mon Jun 02 2025 Anton Midyukov <antohami@altlinux.org> 11.0-alt1
- Initial build from instllaer-distro-cliff
- replace installer step to stage2
