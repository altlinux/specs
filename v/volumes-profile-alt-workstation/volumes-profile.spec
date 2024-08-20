Name: volumes-profile-alt-workstation
Version: 1.0
Release: alt1

Summary: Volumes description for ALT Workstation
License: GPLv2+
Group: System/Configuration/Other

Url: http://www.altlinux.org/Installer/beans
Source: %name-%version.tar

BuildArch: noarch
Conflicts: alterator-vm < 0.4.32-alt2

%define hookdir %_datadir/install2/initinstall.d

%description
%summary

%prep
%setup

%install
mkdir -p %buildroot%hookdir
install -pm755 *.sh %buildroot%hookdir/

%files
%hookdir/*

%changelog
* Thu Aug 15 2024 Mikhail Efremov <sem@altlinux.org> 1.0-alt1
- Don't create separate /home partition if disk size <= 900Gb.
- Fix typo in comments.
- Set swap to memory size in case of >4Gb.
- Reduce maximum swap size.
- Improve comments.

* Thu Jan 11 2024 Mikhail Efremov <sem@altlinux.org> 0.4-alt1
- Add btrfs profile.
- Use Ext4 instead of Ext2/3.

* Thu Aug 25 2022 Mikhail Efremov <sem@altlinux.org> 0.3-alt1
- Add nvme, mmcblk support (by Anton Midyukov).

* Wed Aug 24 2022 Mikhail Efremov <sem@altlinux.org> 0.2-alt1
- Use a common title for profiles.

* Fri Aug 20 2021 Michael Shigorin <mike@altlinux.org> 0.1.1-alt1
- E2K: increase /boot size from 512 Mb to 1 Gb for serviceability

* Thu Jul 22 2021 Mikhail Efremov <sem@altlinux.org> 0.1-alt1
- Initial build (based on Simply Linux profile).
