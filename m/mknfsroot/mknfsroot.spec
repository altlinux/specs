%define mknfsrootuser _mknfsroot

Name: mknfsroot
Version: 0.4
Release: alt4

AutoReq: yes, noshell

Summary: tool to build autoinstall images
Group: Development/Other
License: GPL

Source: %name-%version.tar

BuildArch: noarch

Prereq: hasher-priv
Requires: mkimage libshell

Packager: Stanislav Ievlev <inger@altlinux.org>

%description
tool to build autoinstall images

%prep
%setup

%install
%__install -d %buildroot/%_localstatedir/%name
for i in scripts/* ;do
%__install -Dpm 755 $i %buildroot/%_sbindir/`basename $i`
done

%__install -d %buildroot/%_sysconfdir/%name
cp -a etc/* %buildroot/%_sysconfdir/%name

%pre
%_sbindir/groupadd -r -f %mknfsrootuser
%_sbindir/useradd -r -g %mknfsrootuser -d %_localstatedir/%name -s /dev/null -n %mknfsrootuser > /dev/null 2>&1
if ! getent group hashman |cut -d: -f4 |tr , '\n' |fgrep -qsx %mknfsrootuser; then
	hasher-useradd %mknfsrootuser &&
	printf '%%s\n%%s\n' 'allow_ttydev=YES' 'allowed_mountpoints=/dev/pts' \
		>> /etc/hasher-priv/user.d/%mknfsrootuser
fi

%files
%_sbindir/*
%config(noreplace) %_sysconfdir/%name
%attr(0755,%mknfsrootuser,%mknfsrootuser) %_localstatedir/%name

%changelog
* Sat Nov 01 2008 Stanislav Ievlev <inger@altlinux.org> 0.4-alt4
- remove design features from sample profile

* Tue Oct 14 2008 Stanislav Ievlev <inger@altlinux.org> 0.4-alt3
- more sample improvements

* Mon Oct 13 2008 Stanislav Ievlev <inger@altlinux.org> 0.4-alt2
- fix sample profile

* Wed Sep 10 2008 Stanislav Ievlev <inger@altlinux.org> 0.4-alt1
- update for latest alterator
- minor bugfixes

* Tue Apr 08 2008 Stanislav Ievlev <inger@altlinux.org> 0.3-alt1
- replace spt with mkimage

* Wed Feb 27 2008 Stanislav Ievlev <inger@altlinux.org> 0.2-alt2
- update sample profile for latest alterator-hpc

* Thu Feb 21 2008 Stanislav Ievlev <inger@altlinux.org> 0.2-alt1
- remove zero timeout
- add per-node limits tuning

* Mon Feb 04 2008 Stanislav Ievlev <inger@altlinux.org> 0.1-alt8
- fix hostname setup

* Mon Feb 04 2008 Stanislav Ievlev <inger@altlinux.org> 0.1-alt7
- update to new installer:
    /root instead of /users/root
    /hpc-mpi
- add mvapich, mvapich2 packages

* Fri Jan 18 2008 Stanislav Ievlev <inger@altlinux.org> 0.1-alt6
- add udev-rules-hpc

* Fri Jan 18 2008 Stanislav Ievlev <inger@altlinux.org> 0.1-alt5
- update profile for new hpc kernel and altlinux-release-hpc

* Thu Sep 27 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt4
- replace sysklogd with syslog-ng

* Mon Sep 24 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt3
- improve nfs support
- fix nfsroot shutdown
- add support for directory splitting between nodes

* Thu Sep 20 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt2
- use installer backends instead of installer package
- use tar image type
- rename unsetupnfsroot to removenfsroot

* Tue Sep 18 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt1
- Initial build
