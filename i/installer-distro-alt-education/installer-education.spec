Name:    installer-distro-alt-education
Version: 11.1
Release: alt6

Summary: Installer common files for ALT Education
License: GPL-2.0
Group: System/Configuration/Other

Url: http://altlinux.org/installer/beans
Source: %name-%version.tar

BuildArch: noarch

BuildRequires: alterator rpm-devel

Provides: installer-distro-education = %EVR
Obsoletes: installer-distro-education < %EVR

%define feature installer-feature-simply-linux

%description
Installer common files for ALT Education.

%package stage2
Summary: Installer stage2
Group: System/Configuration/Other
Provides: installer-distro-education-stage2 = %EVR
Obsoletes: installer-distro-education-stage2 < %EVR
Requires: %name = %version-%release
Requires: installer-common-stage2
# volumes profile
Requires: volumes-profile-education
#modules
Requires: alterator-sysconfig
Requires: alterator-license
#Requires: alterator-auth
Requires: alterator-datetime
Requires: alterator-net-eth
Requires: alterator-net-wifi
Requires: alterator-net-vlan
Requires: installer-feature-network-settings-copy
Requires: alterator-vm
Requires: alterator-pkg
Requires: alterator-luks
Requires: x-cursor-theme-jimmac
Requires: bc
#features
Requires: installer-feature-samba-usershares-stage2
Requires: installer-feature-desktop-suspend-stage2
Requires: installer-feature-runlevel5-stage2
Requires: installer-feature-xdg-user-dirs
Requires: installer-feature-auto-domain
Requires: installer-feature-quota-stage2

%description stage2
Installer stage2

%package stage3
Summary: Installer stage3
Group: System/Configuration/Other
Provides: installer-distro-education-stage3 = %EVR
Obsoletes: installer-distro-education-stage3 < %EVR
Requires: %name = %version-%release
Requires: installer-stage3
#modules
%ifnarch armh
Requires: alterator-grub
%endif
Requires: alterator-users
Requires: alterator-root
Requires: alterator-luks
#Requires: alterator-x11
Requires: installer-feature-nfs-client-stage3
Requires: installer-feature-online-repo
Requires: installer-feature-lightdm-stage3
Requires: installer-feature-bell-off-stage3

%description stage3
Installer stage3

%package -n volumes-profile-alt-education
Summary: Volumes profile for ALT Education
Group: System/Configuration/Other
Provides: volumes-profile-education = %EVR
Obsoletes: volumes-profile-education < %EVR

%description -n volumes-profile-alt-education
Volumes profile for ALT Education.

%prep
%setup

%install
%makeinstall
rm -rf %buildroot%_datadir/alterator/help/ru_RU \
       %buildroot%_datadir/alterator/help/ru_UA \
       %buildroot%_datadir/alterator/steps

# Don't expand groups lists
mkdir -p %buildroot%_sysconfdir/alterator
echo "expand-description=no" >%buildroot%_sysconfdir/alterator/pkg-groups.conf

%find_lang alterator-simply-linux

%files -f alterator-simply-linux.lang
%_datadir/install2/help/*

%files stage2
%_sysconfdir/alterator/pkg-groups.conf
%_datadir/install2/installer-steps
%_datadir/install2/*.d/*
%exclude %_datadir/install2/initinstall.d/10-vm-profile.sh
%_datadir/install2/steps/*
%_datadir/install2/alterator-menu
%_datadir/install2/systemd-enabled
%_datadir/install2/systemd-disabled

%files stage3
%_datadir/alterator/ui/simply-linux

%files -n volumes-profile-alt-education
%_datadir/install2/initinstall.d/10-vm-profile.sh

%changelog
* Sun Jun 28 2026 Ajrat Makhmutov <rauty@altlinux.org> 11.1-alt6
- 10-vm-profile.sh: Fix swap cap and pad it for hibernation.

* Tue Dec 23 2025 Ajrat Makhmutov <rauty@altlinux.org> 11.1-alt5
- Remove sysconfig-proxy step from installer steps.

* Sat Dec 20 2025 Ajrat Makhmutov <rauty@altlinux.org> 11.1-alt4
- Remove outdated "Requires" tags (Closes: 57148).

* Wed Nov 12 2025 Fedor Moseichuck <phobos@altlinux.org> 11.1-alt3
- installer-steps: Replace pkg-groups with pkg-radiogroups

* Sun Oct 05 2025 Ajrat Makhmutov <rauty@altlinux.org> 11.1-alt2
- installer-steps: Replace vm-blonde with vm-ortodox.
- installer-steps: Move sysconfig-proxy step after installer-network step.

* Sat Oct 04 2025 Ajrat Makhmutov <rauty@altlinux.org> 11.1-alt1
- installer-steps:
  + Add sysconfig-proxy step.
  + Select additional applications before
    partitioning the disk and check for free space.

* Sat Jun 21 2025 Andrey Cherepanov <cas@altlinux.org> 11.0-alt7
- Move network setup step to stage2.
- stage2: add alterator-net-wifi and alterator-net-vlan.

* Sat Jun 21 2025 Andrey Cherepanov <cas@altlinux.org> 11.0-alt6
- stage2: Add pkg-groups.conf with hidden details for group during installation.

* Wed Jun 18 2025 Andrey Cherepanov <cas@altlinux.org> 11.0-alt5
- Removed installer-feature-hwtweaks-stage2 (ALT #54829).
- Removed installer-feature-set-tz (A:T #54828).

* Thu Jan 09 2025 Andrey Cherepanov <cas@altlinux.org> 11.0-alt4
- 10-vm-profile.sh; extent single / partition to all available disk size.

* Tue Dec 24 2024 Andrey Cherepanov <cas@altlinux.org> 11.0-alt3
- Removed requiirement of installer-feature-repo-add.

* Thu Dec 12 2024 Andrey Cherepanov <cas@altlinux.org> 11.0-alt2
- Renamed to installer-distro-alt-education.
- volumes-profile-alt-education: disabled home partition in auto mode (ALT #52373).

* Tue Oct 15 2024 Andrey Cherepanov <cas@altlinux.org> 11.0-alt1
- Bump version for p11 and Sisyphus where armh is deprecated.

* Tue Oct 15 2024 Andrey Cherepanov <cas@altlinux.org> 10.0-alt6
- Removed installer-feature-desktop-other-fs-stage2.

* Fri Jul 14 2023 Andrey Cherepanov <cas@altlinux.org> 10.0-alt5
- Do not enable bind service.

* Thu Jul 06 2023 Andrey Cherepanov <cas@altlinux.org> 10.0-alt4
- Remove installer-feature-resolver-bind-stage3 due to dmsmasq and bind problems.

* Mon Aug 15 2022 Andrey Cherepanov <cas@altlinux.org> 10.0-alt3
- Removed requirement of obsoleted installer-feature-efi-stage3.

* Sun Dec 05 2021 Andrey Cherepanov <cas@altlinux.org> 10.0-alt2
- Do not enable dnsmasq service by default because it crashes after suspend.

* Thu Dec 02 2021 Andrey Cherepanov <cas@altlinux.org> 10.0-alt1
- Remove installer-feature-local-clock from requirements.

* Fri Aug 20 2021 Michael Shigorin <mike@altlinux.org> 9.2-alt5
- E2K: increase /boot size from 512 Mb to 1 Gb for serviceability.

* Wed Jul 28 2021 Michael Shigorin <mike@altlinux.org> 9.2-alt4
- E2K: added /boot support to volumes-profile-education.

* Wed Jul 28 2021 Michael Shigorin <mike@altlinux.org> 9.2-alt3
- Fix stage2/stage3 dependency issue.

* Tue Apr 20 2021 Andrey Cherepanov <cas@altlinux.org> 9.2-alt2
- Set default size for root filesystem to 50 GiB.

* Tue Apr 06 2021 Andrey Cherepanov <cas@altlinux.org> 9.2-alt1
- Remove orphained hook for lightdm theme set.
- Add all needed installer-features from mkimage-profiles.
- Update enabled and disabled services from mkimage-profiles.

* Sat Jul 04 2020 Andrey Cherepanov <cas@altlinux.org> 9.1-alt3
- Exclude armh from build architectures.
- Remove autreq of installer-stage2.
- Fix License according to SPDX.
- Remove unpackaged files.
- Package volumes-profile-education as separate package.

* Fri Jul 03 2020 Andrey Cherepanov <cas@altlinux.org> 9.1-alt2
- Do not use deprecated installer-feature-symlinks-from-sbin.

* Thu Jun 04 2020 Andrey Cherepanov <cas@altlinux.org> 9.1-alt1
- Enable cups-browsed service.

* Fri Jun 07 2019 Andrey Cherepanov <cas@altlinux.org> 9.0-alt1
- Create new installer based on installer-distro-junior.
- Make autopatrition script from volumes-profile-lite.
- Increase size of / to 28G.
