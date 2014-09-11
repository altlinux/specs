Name: forensic-scripts
Version: 0.2
Release: alt1

Summary: Handle MDRAID, LVM2 and filesystems read-only via loop devices
License: GPLv2+
Group: File tools

Url: http://en.altlinux.org/rescue
Source: %name-%version.tar
Packager: Michael Shigorin <mike@altlinux.org>

BuildArch: noarch
Conflicts: startup-rescue <= 0.22

%description
These scripts arrange Linux software RAID and volume manager
block devices to be handled via read-only loop devices so as
to deny any write access to those in filesystem-independent
way when activating block devices and mounting filesystems.

See also http://www.forensicswiki.org/wiki/Forensic_Live_CD_issues

Author: Maxim Suhanov

%prep
%setup

%build

%install
mkdir -p %buildroot/sbin
install -pm755 *-forensic %buildroot/sbin

%files
/sbin/*

%changelog
* Thu Sep 11 2014 Michael Shigorin <mike@altlinux.org> 0.2-alt1
- ext3: mount as -t ext4 -o noload
- btrfs: ignore explicitly

* Mon May 12 2014 Michael Shigorin <mike@altlinux.org> 0.1-alt2
- made noarch

* Mon May 12 2014 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- initial release based on startup-rescue 0.22-alt1

