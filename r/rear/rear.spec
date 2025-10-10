Name: rear
Version: 2.9
Release: alt1

Summary: Relax-and-Recover is a Linux disaster recovery and system migration tool
License: GPL-3.0
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
#Requires: nfsclient portmap rpcbind

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

%build
TZ=UTC %make_build doc

%install
%make_install install DESTDIR="%buildroot" sbindir="%_sbindir" OFFICIAL=1
chmod a+x %buildroot%_datadir/%name/lib/*.sh
rm -r %buildroot%_datadir/%name/skel/SESAM
rm -r %buildroot%_datadir/%name/restore/VEEAM
rm -r %buildroot%_datadir/%name/skel/default/usr/lib/systemd

%check
%make validate OFFICIAL=1

%files
%doc MAINTAINERS COPYING README.md doc/*.txt
%config(noreplace) %_sysconfdir/%name/
%config(noreplace) %_sysconfdir/%name/cert/
%_datadir/%name/
%_localstatedir/%name/
%_sbindir/%name
%_man8dir/%name.8*

%changelog
* Thu Oct 09 2025 Andrew A. Vasilyev <andy@altlinux.org> 2.9-alt1
- Initial build for ALT.

