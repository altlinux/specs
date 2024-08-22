Name: volumes-profile-cliff-workstation
Version: 0.4
Release: alt1

Summary: Volumes description for SP Workstation
License: GPL-2.0-or-later
Group: System/Configuration/Other

Url: http://www.altlinux.org/Installer/beans
Source: %name-%version.tar

BuildArch: noarch

%define hookdir %_datadir/install2/initinstall.d

%description
%summary.

%prep
%setup

%install
mkdir -p %buildroot%hookdir
install -pm755 *.sh %buildroot%hookdir/

%files
%hookdir/*

%changelog
* Wed Aug 21 2024 Anton Midyukov <antohami@altlinux.org> 0.4-alt1
- Always create a partition larger than 10GB

* Mon Aug 19 2024 Anton Midyukov <antohami@altlinux.org> 0.3-alt1
- Set '/' = 50 GiB

* Wed Aug 24 2022 Anton Midyukov <antohami@altlinux.org> 0.2-alt1
- 10-vm-profile.sh: add nvme, mmcblk support
- No swap partition by default (security reasons)

* Wed Aug 24 2022 Anton Midyukov <antohami@altlinux.org> 0.1-alt1
- initial fork from volumes-profile-alt-workstation 0.2-alt1
