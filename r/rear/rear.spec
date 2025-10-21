%ifdef _priority_distbranch
%define altbranch %_priority_distbranch
%else
%define altbranch %(rpm --eval %%_priority_distbranch)
%endif
%if "%altbranch" == "%nil"
%define altbranch sisyphus
%endif

Name: rear
Version: 2.9
Release: alt2

Summary: Relax-and-Recover is a Linux disaster recovery and system migration tool
License: GPL-2.0-or-later AND GPL-3.0-only
Group: System/Base
URL: http://relax-and-recover.org/

Vcs: https://github.com/rear/rear.git
Source: %name-%version.tar

BuildArch: noarch

BuildRequires: ronn

%filter_from_requires /^\/.OPAL_PBA_SETTINGS\.sh/d
%filter_from_requires /^\/bin\/sshd/d
%filter_from_requires /^\/etc\/scripts\/dhcp-setup-functions\.sh/d
%filter_from_requires /^\/etc\/scripts\/system-setup-functions\.sh/d

%ifarch %ix86 x86_64
Requires: syslinux
Requires: syslinux-extlinux
%endif
Requires: binutils
Requires: ethtool
Requires: gzip
Requires: iputils
Requires: parted
Requires: tar
Requires: openssl
Requires: gawk
Requires: attr
Requires: bc

### If you require NFS, you may need the below packages
#Requires: nfs-client rpcbind

### Required for Bacula support
#Requires: bacula

### Required for OBDR
#Requires: lsscsi sg3_utils

Requires: iproute2
Requires: mkisofs

Requires: util-linux

%description
Relax-and-Recover is the leading Open Source disaster recovery and system
migration solution. It comprises of a modular
frame-work and ready-to-go workflows for many common situations to produce
a bootable image and restore from backup using this image. As a benefit,
it allows to restore to different hardware and can therefore be used as
a migration tool as well.

Currently Relax-and-Recover supports various boot media (incl. ISO, PXE,
OBDR tape, USB or eSATA storage), a variety of network protocols (incl.
sftp, ftp, http, nfs, cifs) as well as a multitude of backup strategies
(incl.  IBM TSM, MircroFocus Data Protector, Symantec NetBackup, EMC NetWorker,
Bacula, Bareos, BORG, Duplicity, rsync).

Relax-and-Recover was designed to be easy to set up, requires no maintenance
and is there to assist when disaster strikes. Its setup-and-forget nature
removes any excuse for not having a disaster recovery solution implemented.

%prep
%setup
sed -i -e 's!/usr/share/rear/!/usr/share/doc/rear/!g' `grep -rl /usr/share/rear/ [A-Za-z]*`
echo -e "OS_VENDOR=ALT\nOS_VERSION=%altbranch" >etc/rear/os.conf

%build
TZ=UTC %make_build doc

%install
%make_install install DESTDIR="%buildroot" sbindir="%_sbindir" datadir="%_datadir/doc" OFFICIAL=1
chmod a+x %buildroot%_datadir/doc/%name/lib/*.sh
rm -r %buildroot%_datadir/doc/%name/skel/SESAM
rm -r %buildroot%_datadir/doc/%name/restore/VEEAM
mv %buildroot%_datadir/doc/man %buildroot%_datadir

%check
%make validate OFFICIAL=1

%files
%doc MAINTAINERS COPYING README.md doc/*.txt
%config(noreplace) %_sysconfdir/%name/
%_datadir/doc/%name/
%_localstatedir/%name/
%_sbindir/%name
%_man8dir/%name.8*

%changelog
* Sat Oct 18 2025 Andrew A. Vasilyev <andy@altlinux.org> 2.9-alt2
- change datadir to /usr/share/doc/rear to fit systemd units path test (Closes: #56457)
- add R: syslinux-extlinux (Closes: #56456)

* Thu Oct 09 2025 Andrew A. Vasilyev <andy@altlinux.org> 2.9-alt1
- Initial build for ALT.

