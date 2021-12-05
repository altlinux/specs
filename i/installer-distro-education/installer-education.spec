Name:    installer-distro-education
Version: 10.0
Release: alt2

Summary: Installer common files for ALT Education
License: GPL-2.0
Group: System/Configuration/Other

Url: http://altlinux.org/installer/beans
Source: %name-%version.tar

ExcludeArch: armh

BuildRequires: alterator rpm-devel

%define feature installer-feature-simply-linux

%description
Installer common files for ALT Education.

%package stage2
Summary: Installer stage2
Group: System/Configuration/Other
Requires: %name = %version-%release
Requires: installer-common-stage2
# volumes profile
Requires: volumes-profile-education
#modules
Requires: alterator-sysconfig
Requires: alterator-license
#Requires: alterator-auth
Requires: alterator-datetime
Requires: alterator-vm
Requires: alterator-pkg
Requires: alterator-luks
Requires: x-cursor-theme-jimmac
Requires: bc
#features
Requires: installer-feature-autohostname-stage2
Requires: installer-feature-samba-usershares-stage2
Requires: installer-feature-desktop-other-fs-stage2
Requires: installer-feature-desktop-suspend-stage2
Requires: installer-feature-hwtweaks-stage2
Requires: installer-feature-set-tz
Requires: installer-feature-runlevel5-stage2
Requires: installer-feature-xdg-user-dirs
Requires: installer-feature-auto-domain
Requires: installer-feature-services
Requires: installer-feature-quota-stage2

%description stage2
Installer stage2

%package stage3
Summary: Installer stage3
Group: System/Configuration/Other
Requires: %name = %version-%release
Requires: installer-stage3
#modules
%ifnarch armh
Requires: alterator-grub
%endif
Requires: alterator-users
Requires: alterator-root
Requires: alterator-net-eth dhcpcd
Requires: alterator-luks
#Requires: alterator-x11
Requires: installer-feature-nfs-client-stage3
Requires: installer-feature-setup-network-stage3
Requires: installer-feature-online-repo
%ifnarch %e2k
Requires: installer-feature-repo-add
%endif
Requires: installer-feature-resolver-bind-stage3
Requires: installer-feature-lightdm-stage3
Requires: installer-feature-bell-off-stage3
Requires: installer-feature-efi-stage3

%description stage3
Installer stage3

%package -n volumes-profile-education
Summary: Volumes profile for ALT Education
Group: System/Configuration/Other

%description -n volumes-profile-education
Volumes profile for ALT Education.

%prep
%setup

%install
%makeinstall
rm -rf %buildroot%_datadir/alterator/help/ru_RU \
       %buildroot%_datadir/alterator/help/ru_UA \
       %buildroot%_datadir/alterator/steps
%find_lang alterator-simply-linux

%files -f alterator-simply-linux.lang
%_datadir/install2/help/*

%files stage2
%_datadir/install2/installer-steps
%_datadir/install2/*.d/*
%exclude %_datadir/install2/initinstall.d/10-vm-profile.sh
%_datadir/install2/steps/*
%_datadir/install2/alterator-menu
%_datadir/install2/systemd-enabled
%_datadir/install2/systemd-disabled

%files stage3
%_datadir/alterator/ui/simply-linux

%files -n volumes-profile-education
%_datadir/install2/initinstall.d/10-vm-profile.sh

%changelog
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
