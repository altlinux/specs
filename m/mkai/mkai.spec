%define mkaiuser _mkai

Name: mkai
Version: 0.3
Release: alt2

AutoReq: yes, noshell

Summary: tool to build autoinstall images
Group: Development/Other
License: GPL

Source: %name-%version.tar

BuildArch: noarch

Prereq: hasher-priv
Requires: spt libshell

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
%_sbindir/groupadd -r -f %mkaiuser
%_sbindir/useradd -r -g %mkaiuser -d %_localstatedir/%name -s /dev/null -n %mkaiuser > /dev/null 2>&1
if ! getent group hashman |cut -d: -f4 |tr , '\n' |fgrep -qsx %mkaiuser; then
	hasher-useradd %mkaiuser &&
	printf '%%s\n%%s\n' 'allow_ttydev=YES' 'allowed_mountpoints=/dev/pts' \
		>> /etc/hasher-priv/user.d/%mkaiuser
fi

%files
%_sbindir/*
%config(noreplace) %_sysconfdir/%name
%attr(0755,%mkaiuser,%mkaiuser) %_localstatedir/%name

%changelog
* Wed Feb 27 2008 Stanislav Ievlev <inger@altlinux.org> 0.3-alt2
- update sample profile to latest alterator-hpc

* Thu Feb 21 2008 Stanislav Ievlev <inger@altlinux.org> 0.3-alt1
- add hpc-settings package to default profile

* Mon Feb 04 2008 Stanislav Ievlev <inger@altlinux.org> 0.2-alt8
- update to new installer: 
    /root instead of /users/root
    /hpc-mpi
- add mvapich and mvapich2 packages

* Mon Jan 21 2008 Stanislav Ievlev <inger@altlinux.org> 0.2-alt7
- use kernel-image-hpc in installer

* Fri Jan 18 2008 Stanislav Ievlev <inger@altlinux.org> 0.2-alt6
- add udev-rules-hpc

* Fri Jan 18 2008 Stanislav Ievlev <inger@altlinux.org> 0.2-alt5
- update profile for new hpc kernel and altlinux-release-hpc

* Thu Sep 27 2007 Stanislav Ievlev <inger@altlinux.org> 0.2-alt4
- replace sysklogd with syslog-ng

* Mon Sep 24 2007 Stanislav Ievlev <inger@altlinux.org> 0.2-alt3
- improve nfs support
- update for the new sysconfig backend
- use more common hooks from spt

* Thu Sep 20 2007 Stanislav Ievlev <inger@altlinux.org> 0.2-alt2
- rename unsetupai to removeai

* Mon Sep 17 2007 Stanislav Ievlev <inger@altlinux.org> 0.2-alt1
- add setupai/unsetupai scripts

* Mon Sep 10 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt3
- create iso with PXE data

* Tue Sep 04 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt2
- change etc structure
- add support for home storage

* Wed Aug 15 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt1
- Initial release
