Name: installer-feature-sambaDC-stage3
Version: 0.1
Release: alt1

Summary: Tweak up the system for samba-DC
License: GPL
Group: System/Configuration/Other

Url: http://www.altlinux.org/Installer/beans
BuildArch: noarch
Requires: task-samba-dc

%description
%summary

%prep

%post
for s in smbd nmbd winbind; do chkconfig $s off; done 2>/dev/null ||:
mv -v /etc/samba/smb.conf{,.sample} 2>/dev/null ||:

%files

%changelog
* Wed Apr 27 2016 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- initial release

