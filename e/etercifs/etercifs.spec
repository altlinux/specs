# Etersoft (c) 2007-2017
# Multiplatform spec for Korinf autobuild system (ALT Linux package spec policy)

%define modname etercifs

Name: etercifs
Version: 5.6.0
Release: alt1

Summary: Advanced Common Internet File System for Linux with Etersoft extension

Packager: Vitaly Lipatov <lav@altlinux.org>

License: GPLv2
Group: System/Kernel and hardware
Url: http://wiki.etersoft.ru/etercifs

BuildArch: noarch

Source: ftp://updates.etersoft.ru/pub/Etersoft/CIFS@Etersoft/%version/sources/tarball/%name-%version.tar
Source1: ftp://updates.etersoft.ru/pub/Etersoft/CIFS@Etersoft/%version/sources/tarball/etercifs-sources-%version.tar.xz

Conflicts: linux-cifs

BuildRequires: rpm-build-intro

Requires: gcc make

# We definitely needs mount.cifs command
Requires: cifs-utils

# We definitely have to use distr_vendor
Requires: eepm

%description
This package contains Etersoft modified CIFS kernel module
with WINE@Etersoft sharing access support.

The CIFS VFS is a virtual file system for Linux to allow access to
servers and storage appliances compliant with the SNIA CIFS
Specification version 1.0 or later.
Popular servers such as Samba, Windows 2000, Windows XP and many others
support CIFS by default.
The CIFS VFS provides some support for older servers based on the more
primitive SMB (Server Message Block) protocol (you also can use the
Linux file system smbfs as an alternative for accessing these).
CIFS VFS is designed to take advantage of advanced network file system
features such as locking, Unicode (advanced internationalization),
hardlinks, dfs (hierarchical, replicated name space), distributed
caching and uses native TCP names (rather than RFC1001, Netbios names).

Unlike some other network file systems all key network function
including authentication is provided in kernel (and changes to mount
and/or a mount helper file are not required in order to enable the CIFS
VFS). With the addition of upcoming improvements to the mount helper
(mount.cifs) the CIFS VFS will be able to take advantage of the new CIFS
URL specification though.

%if %_vendor != "alt"
%package -n dkms-etercifs
Summary: DKMS-ready CIFS Linux kernel module with Etersoft extensions
Group: System/Kernel and hardware
Requires(preun): dkms
Requires(post): dkms

Requires: etercifs = %version-%release

Buildarch: noarch

%description -n dkms-etercifs
The CIFS VFS is a virtual file system for Linux to allow access to
servers and storage appliances compliant with the SNIA CIFS
Specification version 1.0 or later.

This package contains DKMS-ready CIFS Linux kernel module with Etersoft
extensions.
%endif

%prep
%setup

%install
mkdir -p %buildroot%_sysconfdir/sysconfig/
cat <<EOF >%buildroot%_sysconfdir/sysconfig/%name.conf
# etercifs configuration file

# this options useful only for wine share using and security=share setting in smb.conf
#MOUNT_OPTIONS=user=guest,pass=,rw,iocharset=utf8,noperm,forcemand,direct,nounix
# wine options since etercifs 4.4.5 enable full wine support
MOUNT_OPTIONS=user=guest,pass=,rw,iocharset=utf8,noperm,wine

# default path for share mounting
DEFAULT_MOUNTPOINT=/net/sharebase

# disable package version checking
# CHECK_VERSION=0
EOF

%__subst "s|@DATADIR@|%_datadir/%name|g" functions.sh etercifs etermount etercifs-build
%__subst "s|@SYSCONFIGDIR@|%_sysconfdir/sysconfig|g" functions.sh etercifs etermount
%__subst "s|@INITDIR@|%_initdir|g" etercifs.service

install -D -m644 buildmodule.sh %buildroot%_datadir/%name/buildmodule.sh
install -D -m644 checkmodule.sh %buildroot%_datadir/%name/checkmodule.sh
install -D -m755 source.sh %buildroot%_datadir/%name/source.sh
install -D -m644 source.table %buildroot%_datadir/%name/source.table
install -D -m644 functions.sh %buildroot%_datadir/%name/functions.sh
install -D -m755 %name-build %buildroot%_sbindir/%name-build

cat <<EOF >%buildroot%_datadir/%name/package.conf
DATADIR=%_datadir/%name
SRC_DIR=%_usrsrc/%name-%version
MODULENAME=%name
MODULEFILENAME=%name.ko
MODULEVERSION=%version
PACKAGEVEREL=%version-%release
CHECK_VERSION=1
EOF

mkdir -p %buildroot%_sysconfdir/modprobe.d
cat <<EOF >%buildroot%_sysconfdir/modprobe.d/etersoft.conf
# wine@etersoft
install cifs /sbin/modprobe etercifs
blacklist cifs
EOF

install -D -m755 %name %buildroot%_initdir/%name
install -D -m644 %name.service %buildroot%_unitdir/%name.service
install -D -m755 %name.outformat %buildroot%_datadir/%name

cp %SOURCE1 %buildroot%_datadir/%name/

mkdir -p %buildroot%_bindir
install -m755 etermount %buildroot%_bindir/

%if %_vendor != "alt"
# dkms part
mkdir -p %buildroot%_usrsrc/%modname-%version/
cat > %buildroot%_usrsrc/%modname-%version/dkms.conf <<EOF
# DKMS file for Linux CIFS with Etersoft's extensions

PACKAGE_NAME="%modname"
PACKAGE_VERSION="%version"

BUILT_MODULE_NAME[0]="etercifs"
DEST_MODULE_LOCATION[0]="/kernel/fs/cifs/"
REMAKE_INITRD="no"
AUTOINSTALL="YES"
EOF

%post -n dkms-etercifs
if [ "$1" = 1 ]
then
  dkms add -m %modname -v %version --rpm_safe_upgrade
fi
%_initdir/%modname build

%preun -n dkms-etercifs
if [ "$1" = 0 ]
then
  dkms remove -m %modname -v %version --rpm_safe_upgrade --all
fi
%endif

%post
%post_service %name

%preun
%preun_service %name

%files
%doc README.ETER AUTHORS README TODO
%_bindir/etermount
%_sbindir/%name-build
%_initrddir/%name
%_unitdir/%name.service
%config %_sysconfdir/sysconfig/%name.conf
%config %_sysconfdir/modprobe.d/etersoft.conf
%_datadir/%name/

%if %_vendor != "alt"
%files -n dkms-etercifs
%_usrsrc/%modname-%version/dkms.conf
%endif

%changelog
* Wed Nov 22 2017 Vitaly Lipatov <lav@altlinux.ru> 5.6.0-alt1
- add 4.11 (v4.11)
- add 4.12 (v4.12)
- add 4.13 (v4.13)
- add 4.14 (v4.14)

* Wed Nov 22 2017 Vitaly Lipatov <lav@altlinux.ru> 5.5.5-alt1
- rename centos70 to centos7 (eterbug #11965)

* Thu Sep 21 2017 Vitaly Lipatov <lav@altlinux.ru> 5.5.4-alt1
- etercifs server: drop --wait from rmmod
- do not use sec= by default

* Tue Apr 18 2017 Vitaly Lipatov <lav@altlinux.ru> 5.5.3-alt1
- update 4.9 to correct sources (eterbug #11619)

* Tue Apr 04 2017 Vitaly Lipatov <lav@altlinux.ru> 5.5.2-alt1
- fix build on Fedora 25 and later
- use eepm instead lsb_release

* Tue Apr 04 2017 Vitaly Lipatov <lav@altlinux.ru> 5.5.1-alt1
- add sources for 4.7
- add sources for 4.8
- add sources for 4.9
- add sources for 4.10

* Sun Mar 05 2017 Vitaly Lipatov <lav@altlinux.ru> 5.5.0-alt3
- implement regexp support in source.table and use it
- some fixes, prepare to epm using

* Sun Mar 05 2017 Vitaly Lipatov <lav@altlinux.ru> 5.5.0-alt2
- switch kernel detection on data driven code with source.table

* Sat Mar 04 2017 Vitaly Lipatov <lav@altlinux.ru> 5.5.0-alt1
- aggregate all sources tarball to one tarball
- major rewrite all scripts

* Fri Mar 03 2017 Konstantin Artyushkin <akv@altlinux.org> 5.4.18-alt1
- fix build for CentOS 7 with 3.10.0-514.* kernel

* Thu Jan 26 2017 Konstantin Artyushkin <akv@altlinux.org> 5.4.17-alt1
- Added SUSE 13.2 specific kernel 3.16.7.* support

* Wed Sep 14 2016 Konstantin Artyushkin <akv@altlinux.org> 5.4.16-alt2
- add ROSA/2014 support

* Fri Aug 19 2016 Konstantin Artyushkin <akv@altlinux.org> 5.4.16-alt1
- Added GosLinux 6.4 support 

* Sun Jul 03 2016 Pavel Shilovsky <piastry@altlinux.org> 5.4.15-alt1
- Add sources for 4.6 (v4.6.3)
- Add sources for 4.5 (v4.5.7)
- Update 4.2 sources from stable (v4.2.8-ckt12)
- Update 3.19 sources from stable (v3.19.8-ckt22)
- Update 3.13 sources from stable (v3.13.11-ckt39)
- Update 4.4 sources from stable (v4.4.14)
- Update 4.1 sources from stable (v4.1.27)
- Update 3.18 sources from stable (v3.18.36)
- Update 3.16 sources from stable (v3.16.36)
- Update 3.14 sources from stable (v3.14.73)
- Update 3.12 sources from stable (v3.12.61)
- Update 3.10 sources from stable (v3.10.102)
- Update 3.4 sources from stable (v3.4.112)
- Update 3.2 sources from stable (v3.2.81)
- Add support for 3.10.0-327.10.1.el7 CentOS 7

* Fri Feb 05 2016 Vitaly Lipatov <lav@altlinux.ru> 5.4.14-alt2
- functions.sh: small workround and update comments
- rewrite for separate OpenVZ-kernels checking

* Sun Dec 06 2015 Pavel Shilovsky <piastry@altlinux.org> 5.4.14-alt1
- Add sources for 4.4 (v4.4-rc3)
- Add sources for 4.3 (v4.3)
- Add sources for 4.2 (v4.2.6)
- Update 4.1 sources from stable (v4.1.13)
- Update 3.19 sources from stable (v3.19.8-ckt10)
- Update 3.18 sources from stable (v3.18.24)
- Update 3.16 sources from stable (v3.16.7-ckt20)
- Update 3.14 sources from stable (v3.14.57)
- Update 3.13 sources from stable (v3.13.11-ckt30)
- Update 3.12 sources from stable (v3.12.51)
- Update 3.10 sources from stable (v3.10.93)
- Update 3.2 sources from stable (v3.2.74)

* Sun Jun 21 2015 Pavel Shilovsky <piastry@altlinux.org> 5.4.13-alt1
- Update CentOS 7.0 sources (3.10.0-229.1.2)
- Update .gear/rules
- Add sources for 4.1 (v4.1-rc8)
- Update 3.16 sources from stable (v3.16.7-ckt13)
- Update 3.13 sources from stable (v3.13.11-ckt21)
- Update 4.0 sources from stable (v4.0.5)
- Update 3.19 sources from stable (v3.19.8)
- Update 3.18 sources from stable (v3.18.16)
- Update 3.14 sources from stable (v3.14.44)
- Update 3.12 sources from stable (v3.12.44)
- Update 3.10 sources from stable (v3.10.80)
- Update 3.4 sources from stable (v3.4.108)
- Update 3.2 sources from stable (v3.2.69)

* Tue Mar 03 2015 Pavel Shilovsky <piastry@altlinux.org> 5.4.12-alt1
- Add sources for 4.0 (v4.0-rc1)
- Update 3.13 sources from stable (v3.13.11-ckt16)
- Update 3.16 sources from stable (v3.16.7-ckt7)
- Update 3.19 sources from stable (v3.19)
- Update 3.18 sources from stable (v3.18.8)
- Update 3.14 sources from stable (v3.14.34)
- Update 3.12 sources from stable (v3.12.38)
- Update 3.2 sources from stable (v3.2.67)

* Wed Dec 24 2014 Pavel Shilovsky <piastry@altlinux.org> 5.4.11-alt1
- Add sec=ntlmv2 to MOUNT_OPTIONS
- Add sources for 3.19 (v3.19-rc1)
- Add sources for 3.18 (v3.18.1)
- Add sources for 3.17 (v3.17.7)
- Update 3.16 sources from stable (v3.16.7)
- Update 3.14 sources from stable (v3.14.27)
- Update 3.12 sources from stable (v3.12.35)
- Update 3.10 sources from stable (v3.10.63)
- Update 3.4 sources from stable (v3.4.105)
- Update 3.2 sources from stable (v3.2.65)

* Fri Aug 08 2014 Pavel Shilovsky <piastry@altlinux.org> 5.4.10-alt1
- Detect CentOS 7.0 during build
- Add sources for CentOS 7.0
- Add sources for 3.16 (v3.16)
- Update 3.15 sources from stable (v3.15.9)
- Update 3.14 sources from stable (v3.14.16)
- Fix missed share_access setting for 3.13
- Update 3.12 sources from stable (v3.12.26)
- Update 3.10 sources from stable (v3.10.52)
- Update 3.4 sources from stable (v3.4.102)
- Fix build for ROSA

* Wed May 28 2014 Pavel Shilovsky <piastry@altlinux.org> 5.4.9-alt1
- Add sources for 3.15 (v3.15-rc7)
- Add sources for 3.14 (v3.14.4)
- Add sources for 3.13 (v3.13.11)
- Fix memory leaks in SMB2_open for 3.12
- Update 3.12 sources from stable (v3.12.20)
- Update 3.11 sources from stable (v3.11.10)
- Update 3.10 sources from stable (v3.10.40)
- Update 3.4 sources from stable (v3.4.91)
- Update 3.2 sources from stable (v3.2.59)
- Update 2.6.34 sources from stable (v2.6.34.15)
- Fix an exec path in etercifs.service
- Fix build error message
- Fix build warnings for CentOS 6.0

* Sun Nov 10 2013 Pavel Shilovsky <piastry@altlinux.org> 5.4.8-alt1
- Add sources for 3.12 (v3.12)
- Add sources for 3.11 (v3.11.7)
- Fix STATUS_SHARING_VIOLATION error mapping for 3.9 and 3.10
- Fix a selection of the latest supported kernel version
- Fix a memory leak when a lease break comes for 3.8
- Update 3.10 sources from stable (v3.10.18)
- Update 3.9 sources from stable (v3.9.11)
- Update 3.4 sources from stable (v3.4.68)
- Update 3.2 sources from stable (v3.2.52)
- Update 3.0 sources from stable (v3.0.101)

* Thu Jun 27 2013 Pavel Shilovsky <piastry@altlinux.org> 5.4.7-alt1
- Add sources for 3.10 (v3.10-rc5)
- Add sources for 3.9 (v3.9.7)
- Update 3.8 sources from stable (v3.8.10)
- Update 3.4 sources from stable (v3.4.50)
- Update 3.2 sources from stable (v3.2.47)
- Update 3.0 sources from stable (v3.0.83)
- Update 2.6.32 sources from stable (v2.6.32.61)
- Do not use --wait for rmmod
- Add etercifs-build script
- Add systemd support

* Fri Mar 01 2013 Pavel Shilovsky <piastry@altlinux.org> 5.4.6-alt1
- Add sources for 3.8 (v3.8.1)
- Update 3.7 sources from stable (v3.7.10)
- Update 3.4 sources from stable (v3.4.34)
- Update 3.2 sources from stable (v3.2.39)
- Update 3.0 sources from stable (v3.0.67)
- Update 2.6.34 sources from stable (v2.6.34.14)

* Thu Dec 13 2012 Pavel Shilovsky <piastry@altlinux.org> 5.4.5-alt2
- Add condstop support to etercifs init script

* Wed Dec 12 2012 Pavel Shilovsky <piastry@altlinux.org> 5.4.5-alt1
- Update 3.7 sources from stable (v3.7)
- Update 3.6 sources from stable (v3.6.10)
- Update 3.4 sources from stable (v3.4.23)
- Update 3.2 sources from stable (v3.2.35)
- Fix build on Open SUSE 12.1

* Wed Oct 31 2012 Pavel Shilovsky <piastry@altlinux.org> 5.4.4-alt1
- Add sources for 3.7 (v3.7-rc2)
- Add sources for 3.6 (v3.6.4)
- Update 3.5 sources from stable (v3.5.7)
- Update 3.4 sources from stable (v3.4.16)
- Update 3.2 sources from stable (v3.2.32)
- Update 2.6.34 sources from stable (v2.6.34.13)

* Thu Aug 16 2012 Vitaly Lipatov <lav@altlinux.ru> 5.4.3-alt2
- cleanup spec, fix requires to /sbin/mount.cifs

* Mon Aug 13 2012 Pavel Shilovsky <piastry@altlinux.org> 5.4.3-alt1
- Add sources for 3.5 (v3.5.1)
- Add sources for 3.4 (v3.4.8)
- Update 3.3 sources from stable (v3.3.8)
- Update 3.2 sources from stable (v3.2.27)
- Update 3.0 sources from stable (v3.0.40)

* Fri Apr 13 2012 Pavel Shilovsky <piastry@altlinux.org> 5.4.2-alt1
- Add Fedora 15 2.6.{41,42} kernels support
- Update .gear/rules
- Add sources for 3.3 (v3.3.1)
- Add RERemix to RHEL-like distros
- Update 3.2 sources from stable (v3.2.14)
- Update 3.0 sources from stable (v3.0.27)
- Update 2.6.34 sources from stable (v2.6.34.11)
- Update 2.6.32 sources from stable (v2.6.32.59)

* Wed Feb 15 2012 Pavel Shilovsky <piastry@altlinux.org> 5.4.1-alt1
- Fix build on CentOS 6.0
- Update from stable trees (v2.6.27.61, v3.0.21, v3.2.6)
- Lower default wsize when posix extension are not used for 3.0 and 3.1
- Fix oops in session setup code for null user mounts for 3.1

* Fri Jan 20 2012 Pavel Shilovsky <piastry@altlinux.org> 5.4.0-alt1
- Fix build on CentOS
- Update from stable trees (v2.6.32.48, v2.6.33.20, v3.0.9)
- Add sources for 3.2 (v3.2.1)

* Thu Dec 01 2011 Pavel Shilovsky <piastry@altlinux.org> 5.3.0-alt1
- Remove rwpidforward from wine mount option for 3.0 and 3.1

* Mon Nov 21 2011 Pavel Shilovsky <piastry@altlinux.org> 5.2.0-alt1
- Fix LinuxWizard detection
- Update from stable trees (v2.6.32.48, v2.6.33.20, v3.0.9)
- Implement byte range lock cache for 3.0
- Add sources for 3.1 (v3.1.1)
- Fix module source selecting

* Tue Nov 01 2011 Pavel Shilovsky <piastry@altlinux.org> 5.0.2-alt1
- Update 3.0 sources from stable (v3.0.8)
- Fix DFS handling in cifs_get_file_info (v2.6.34..v3.0)
- Add sources for OVZ CentOS 5.7
- Add sources for CentOS 6.0

* Sun Oct 09 2011 Pavel Shilovsky <piastry@altlinux.org> 5.0.1-alt1
- Add Fedora 15 2.6.40 kernel support
- Add modprobe.d/etersoft.conf
- Fix module sources selecting
- Update 3.0 sources from stable (v3.0.6)
- Fix incorrect max RFC1002 write size value for 2.6.39 and 3.0

* Mon Sep 05 2011 Pavel Shilovsky <piastry@altlinux.org> 5.0.0-alt1
- Change share flags shift to 28
- Add sources for 3.0
- Update from stable/longterm trees

* Tue May 31 2011 Pavel Shilovsky <piastry@altlinux.org> 4.8.2-alt1
- Add sources for 2.6.39
- Update from stable/longterm trees

* Thu May 12 2011 Pavel Shilovsky <piastry@altlinux.org> 4.8.1-alt1
- Add sources for CentOS 5.6
- Fix memory over bound bug in cifs_parse_mount_options
- Update from stable/longterm trees

* Tue Apr 05 2011 Pavel Shilovsky <piastry@altlinux.org> 4.8.0-alt1
- Add strict cache mode for 2.6.32, 2.6.35 and 2.6.37
- Add sources for 2.6.38 with strict cache mode

* Wed Mar 02 2011 Pavel Shilovsky <piastry@altlinux.org> 4.6.2-alt2
- Fix build on RHEL-like distros

* Sat Feb 19 2011 Pavel Shilovsky <piastry@altlinux.org> 4.6.2-alt1
- Fix oplock handling problem for other kernels
- Update from stable/longterm trees

* Wed Feb 09 2011 Pavel Shilovsky <piastry@altlinux.org> 4.6.1-alt1
- Fix oplock handling problem for 2.6.37

* Wed Jan 12 2011 Pavel Shilovsky <piastry@altlinux.org> 4.6.0-alt1
- Fix share flags' shift during creating
- Add sources for 2.6.37

* Thu Dec 30 2010 Pavel Shilovsky <piastry@altlinux.org> 4.5.9-alt1
- Fix pid-forward in cifs_writepages

* Wed Dec 29 2010 Pavel Shilovsky <piastry@altlinux.org> 4.5.8-alt1
- Add sources for CentOS 5.5
- Bugs' fixing

* Sat Nov 27 2010 Pavel Shilovsky <piastry@altlinux.org> 4.5.7-alt1
- Add sources for 2.6.35 and 2.6.36

* Thu Nov 25 2010 Pavel Shilovsky <piastry@altlinux.org> 4.5.6-alt1
- Add sources for 2.6.34

* Mon Nov 09 2010 Pavel Shilovsky <piastry@altlinux.org> 4.5.5-alt3
- Delete redundant code
- Fix changelog bugs

* Mon Nov 08 2010 Pavel Shilovsky <piastry@altlinux.org> 4.5.5-alt2
- Fix port bug for CentOS 5.4

* Mon Nov 08 2010 Pavel Shilovsky <piastry@altlinux.org> 4.5.5-alt1
- Fix tunnel port problem

* Thu Oct 14 2010 Pavel Shilovsky <piastry@altlinux.org> 4.5.4-alt1
- Fix missing share flags during creating for 2.6.31, 2.6.32, 2.6.33

* Mon Jun 28 2010 Pavel Shilovsky <piastry@altlinux.org> 4.5.3-alt1
- Add testing support for new kernels
- Add sources for 2.6.33

* Tue Jun 08 2010 Vitaly Lipatov <lav@altlinux.ru> 4.5.2-alt2
- fix etermount with 2 params
- cleanup install section in spec
- fix depmod after build for using KERNELVERSION

* Sat Apr 10 2010 Pavel Shilovsky <piastry@altlinux.org> 4.5.2-alt1
- Fix build for legacy, CentOS 5.2, 2.6.23, 2.6.24

* Sat Apr 10 2010 Vitaly Lipatov <lav@altlinux.ru> 4.5.0-alt5
- add gprintf function instead /etc/init.d/functions include (see eterbug #5283)
- fix init scripts according to LSB
- cleanup install section in spec
- fix depmod after build for using KERNELVERSION

* Mon Mar 22 2010 Vitaly Lipatov <lav@altlinux.ru> 4.5.0-alt4
- add requires for samba-client and direct using /sbin/mount.cifs

* Thu Mar 18 2010 Pavel Shilovsky <piastry@altlinux.org> 4.5.0-alt3
- Fix gprintf problem on Mandriva

* Mon Mar 15 2010 Pavel Shilovsky <piastry@altlinux.org> 4.5.0-alt2
- Fix rmmod after umount problem

* Fri Mar 12 2010 Pavel Shilovsky <piastry@altlinux.org> 4.5.0-alt1
- Fix share flags shift for 2.6.32
- Change default permissions (except 2.6.31, 2.6.32)

* Sat Mar 06 2010 Vitaly Lipatov <lav@altlinux.ru> 4.4.5-alt2
- move etermount to /usr/bin
- move etercifs.conf to /etc/sysconfig
- add print mounted resources in etermount
- update readme, messages and comments

* Tue Mar 02 2010 Pavel Shilovsky <piastry@altlinux.org> 4.4.5-alt1
- Implement WINE logic
- Fix losing locks during fork()

* Sun Feb 21 2010 Pavel Shilovsky <piastry@altlinux.org> 4.4.4-alt1
- Add sources for 2.6.32
- Update README.ETER, CHANGES and .gear/rules

* Fri Feb 19 2010 Vitaly Lipatov <lav@altlinux.ru> 4.4.3-alt2
- cleanup spec, rewrite changelog, add comments to etercifs.conf
- update README, CHANGES

* Wed Feb 17 2010 Pavel Shilovsky <piastry@altlinux.org> 4.4.3-alt1
- fix using port mount option for kernel 2.6.29, 2.6.30 (eterbug #4875)
- add mmap for nobrl direct shares for legacy kernel

* Wed Jan 27 2010 Evgeny Sinelnikov <sin@altlinux.ru> 4.4.2-alt4
- Update for Sisyphus

* Wed Jan 20 2010 Pavel Shilovsky <piastry@altlinux.org> 4.4.2-alt3
- Fix build for CentOS 5.4

* Sat Jan 16 2010 Pavel Shilovsky <piastry@altlinux.org> 4.4.2-alt2
- Missing .gear/rules for CentOS 5.4

* Thu Jan 14 2010 Pavel Shilovsky <piastry@altlinux.org> 4.4.2-alt1
- Add sources for CentOS 5.4
- Bugfixes

* Tue Dec 29 2009 Pavel Shilovsky <piastry@altlinux.org> 4.4.1-alt1
- Fixed direct problem

* Mon Dec 14 2009 Evgeny Sinelnikov <sin@altlinux.ru> 4.4.0-alt2
- Fixed forcemand open problems for 2.6.30 and 2.6.31
- Fixed test version of 2.6.31 for build and update

* Tue Oct 27 2009 Evgeny Sinelnikov <sin@altlinux.ru> 4.4.0-alt1
- Fixed mandatory reading problems

* Tue Oct 27 2009 Evgeny Sinelnikov <sin@altlinux.ru> 4.3.9-alt2
- Update fixes for 2.6.31

* Wed Oct 14 2009 Evgeny Sinelnikov <sin@altlinux.ru> 4.3.9-alt1
- Fixed fd duplicate problem with locks
- Add sources for 2.6.31

* Mon Aug 03 2009 Evgeny Sinelnikov <sin@altlinux.ru> 4.3.8-alt5
- Fix build with {clear,drop,inc}_nlink() functions.
- Add bugfixes from upstream for 2.6.30

* Tue Jul 28 2009 Vitaly Lipatov <lav@altlinux.ru> 4.3.8-alt4
- update README and ChangeLog, fix messages

* Mon Jul 27 2009 Evgeny Sinelnikov <sin@altlinux.ru> 4.3.8-alt3
- Fix building for legacy code with FALSE using
- Fix missing definition for 2.6.29

* Mon Jul 27 2009 Vitaly Lipatov <lav@altlinux.ru> 4.3.8-alt2
- fix messages, fix url and source path

* Mon Jul 27 2009 Evgeny Sinelnikov <sin@altlinux.ru> 4.3.8-alt1
- Revert fix for POSIX locks behavior during close() using storage_lock
- Add requries for gcc and make

* Mon Jul 27 2009 Evgeny Sinelnikov <sin@altlinux.ru> 4.3.7-alt4
- Fix build for 2.6.30

* Sat Jul 25 2009 Evgeny Sinelnikov <sin@altlinux.ru> 4.3.7-alt3
- Update and fix broken module for 2.6.30

* Tue Jul 07 2009 Evgeny Sinelnikov <sin@altlinux.ru> 4.3.7-alt2
- Try to fix #10754 like Eter#4059 for SLES

* Fri Jul 03 2009 Evgeny Sinelnikov <sin@altlinux.ru> 4.3.7-alt1
- Add sources for 2.6.30
- Add bugfixes from upstream for 2.6.27-2.6.29

* Thu Jul 02 2009 Evgeny Sinelnikov <sin@altlinux.ru> 4.3.6-alt4
- Fixed legacy-1.50c building for 2.6.18 (Eter#4059)

* Tue May 05 2009 Evgeny Sinelnikov <sin@altlinux.ru> 4.3.6-alt3
- Add kernel-source-etercifs packages providing and support

* Mon May 04 2009 Evgeny Sinelnikov <sin@altlinux.ru> 4.3.6-alt2
- Rebuild with git.eter builder

* Wed Apr 15 2009 Konstantin Baev <kipruss@altlinux.org> 4.3.6-alt1
- Revert "use cifs_file_aio_read instead of generic_file_aio_read" in all sources
- Add etermount --help and remove not necessary messages
- Re-add mount option 'direct' in /etc/etercifs.conf

* Mon Apr 13 2009 Konstantin Baev <kipruss@altlinux.org> 4.3.5-alt1
- Fix build in CentOS 5.2 default kernel 2.6.18-92.el5 (add sources/centos52)

* Fri Apr 10 2009 Konstantin Baev <kipruss@altlinux.org> 4.3.4-alt2
- Bugfix in spec
- Add RHEL support with CentOS
- Add parameter CHECK_VERSION in /etc/etercifs.conf for disabeling
  checking package version while loading the module

* Fri Apr 10 2009 Konstantin Baev <kipruss@altlinux.org> 4.3.4-alt1
- Add etercifs sources for CentOS kernel 2.6.18-128 (fix bug Eter#3770)
- Add CentOS specific part in building scripts

* Wed Apr 08 2009 Konstantin Baev <kipruss@altlinux.org> 4.3.3-alt1
- Fix compile problem in kernel 2.6.29 (RT#9966)
- update sources/2.6.29 (up to 2.6.29.1)
- Now old module don't loading if installed newer version of etercifs
- fixed error in cifs_lock_storage: don't remove lock from pid list if unlocking failed by server

* Wed Apr 01 2009 Konstantin Baev <kipruss@altlinux.org> 4.3.2-alt2
- Add etermount script

* Wed Apr 01 2009 Konstantin Baev <kipruss@altlinux.org> 4.3.2-alt1
- Fixed bug connected with not moving pointer after cifs_user_read() in cifs_file_aio_read()

* Tue Mar 31 2009 Konstantin Baev <kipruss@altlinux.org> 4.3.1-alt1
- Remove oplock part of Etersoft patches (sources < 2.6.27)
- use cifs_file_aio_read instead of generic_file_aio_read in all sources

* Mon Mar 30 2009 Konstantin Baev <kipruss@altlinux.org> 4.3.0-alt1
- add sources/2.6.29
- Fix bugs Eter#1185 and Eter#3660 (F_GETLK problem connected with wrong returning file_lock structure)
- Fix bugs Eter#3237 (problem remove lock at Windows share)
- Refactoring code, which solved kmem_cache_destroy problem
- Correct message about loaded version of etercifs module (in status command)
- Some bugfixes

* Thu Mar 19 2009 Konstantin Baev <kipruss@altlinux.org> 4.2.1-alt1
- Fix bug Eter#3638 (solve some DKMS troubles)
- update sources/2.6.27 (up to 2.6.27.20)
- update sources/2.6.28 (up to 2.6.28.8)

* Thu Mar 10 2009 Konstantin Baev <kipruss@altlinux.org> 4.2.0-alt1
- Send SMB flush in cifs_fsync [Backport from CIFS devel git]
- Remove oplock part of Etersoft patches
- Fix bug Eter#3239 (problem while mkdir -p d1/d2)
- Fix bug Eter#3626 (cifs kmem_cache_destroy problem)

* Wed Feb 11 2009 Konstantin Baev <kipruss@altlinux.org> 4.1.2-alt1
- CIFS_VERSION in module replaced by version of etercifs package
- update sources/2.6.27 (up to 2.6.27.15)
- update sources/2.6.28 (up to 2.6.28.4)

* Mon Jan 19 2009 Konstantin Baev <kipruss@altlinux.org> 4.1.1-alt1
- remove deprecated code from legacy sources
- add sources/2.6.16 from SLES10SP2 kernel with Etersoft patches (Eter#3249)
- add checking availability GNU make utility (Eter#3265)
- update sources/2.6.28 (up to 2.6.28.1)

* Mon Jan 12 2009 Konstantin Baev <kipruss@altlinux.org> 4.1.0-alt1
- add sources/2.6.28

* Fri Dec 26 2008 Konstantin Baev <kipruss@altlinux.org> 4.0.1-alt3
- fix build in kernels 2.6.18 - 2.6.24 (may be broken after adding option "forcemand")

* Thu Dec 18 2008 Konstantin Baev <kipruss@altlinux.org> 4.0.1-alt2
- minor design changes in sources code
- add docs

* Tue Dec 16 2008 Konstantin Baev <kipruss@altlinux.org> 4.0.1-alt1
- update all sources: add code, that fixing bug Eter#2929
- update sources/2.6.27 (up to 2.6.27.9)

* Tue Dec 09 2008 Konstantin Baev <kipruss@altlinux.org> 4.0.0-alt2
- update all sources: add mount option "forcemand"
- update sources/2.6.27 (up to 2.6.27.8)
- additional checking for existence etercifs kernel module sources for current kernel
- add symlinks for kernel sources 2.6.16 and 2.6.17
- fix RT ticket 7479 and bug Eter#2898
- add checking the kernel configuration

* Thu Dec 04 2008 Konstantin Baev <kipruss@altlinux.org> 4.0.0-alt1
- test build: add mount option "forcemandatorylock" aka "forcemand"

* Tue Nov 18 2008 Konstantin Baev <kipruss@altlinux.org> 3.8.0-alt7
- Minor bugfix

* Tue Nov 18 2008 Konstantin Baev <kipruss@altlinux.org> 3.8.0-alt6
- fixed bug Eter#2936

* Tue Nov 11 2008 Konstantin Baev <kipruss@altlinux.org> 3.8.0-alt5
- removed default parameter '-o mount' for mount fstab records

* Tue Nov 11 2008 Konstantin Baev <kipruss@altlinux.org> 3.8.0-alt4
- removed parameter (noreplace) for config file

* Tue Nov 11 2008 Konstantin Baev <kipruss@altlinux.org> 3.8.0-alt3
- add starting module after building (if module not exist)

* Fri Nov 07 2008 Konstantin Baev <kipruss@altlinux.org> 3.8.0-alt2
- fix building module on Ubuntu

* Thu Nov 06 2008 Konstantin Baev <kipruss@altlinux.org> 3.8.0-alt1
- fix building module with dkms
- add config file /etc/etercifs.conf

* Wed Nov 05 2008 Konstantin Baev <kipruss@altlinux.org> 3.7.0-alt2
- delete last change (building module on installing rpm)
- remove kernel_src.list and distr_vendor
- code refactoring near finction.sh and buildmodule.sh
- while fixing Eter#2782 added option 'testbuild' in rc-script:
  now able the command:
    service etercifs testbuild
- fix bug Eter#2783

* Thu Oct 30 2008 Konstantin Baev <kipruss@altlinux.org> 3.7.0-alt1
- Add building module on installing rpm

* Thu Oct 30 2008 Konstantin Baev <kipruss@altlinux.org> 3.6.1-alt1
- update sources/2.6.23 (Fixed bug Eter#2773)

* Mon Oct 27 2008 Konstantin Baev <kipruss@altlinux.org> 3.6-alt1
- update sources/2.6.27 (up to 2.6.27.4)

* Thu Oct 23 2008 Konstantin Baev <kipruss@altlinux.org> 3.5-alt1
- update sources/2.6.25 (up to 2.6.25.19)
- update sources/2.6.26 (up to 2.6.26.7)
- update sources/2.6.27 (up to 2.6.27.3)
- minor code refactoring

* Tue Oct 21 2008 Konstantin Baev <kipruss@altlinux.org> 3.4-alt1
- Fix error while building module in MOPSLinux
- update sources/2.6.27

* Fri Oct 10 2008 Konstantin Baev <kipruss@altlinux.org> 3.3-alt1
- move sources into etercifs rmp package
- delete Requires
- delete Spec part for ALT Linux with BuildRequires
- Url fixed
- update sources/2.6.25
- add sources/2.6.24
- add sources/2.6.23
- add sources/2.6.26
- add sources/2.6.27

* Thu Oct 09 2008 Konstantin Baev <kipruss@altlinux.org> 3.2-alt2
- remove Requires: rpm-build-compat
- add distr_vendor into package

* Wed Oct 08 2008 Konstantin Baev <kipruss@altlinux.org> 3.2-alt1
- remove disableing LinuxExtensions (bug Eter#2563)
- now package etercifs is not similar linux-cifs

* Wed Oct 08 2008 Konstantin Baev <kipruss@altlinux.org> 3.1-alt3
- Minor bugfix

* Wed Oct 08 2008 Konstantin Baev <kipruss@altlinux.org> 3.1-alt2
- Fixed part 2 of bug Eter#2553

* Tue Oct 07 2008 Konstantin Baev <kipruss@altlinux.org> 3.1-alt1
- Fixed part 1 of bug Eter#2553
- Added usage Generic for etercifs sources

* Wed Oct 01 2008 Konstantin Baev <kipruss@altlinux.org> 3.0-alt1
- Up version to 2.0
- changed flag in /fs/cifs/file.c
- changed package name and service name to etercifs
- added Conflicts

* Thu Sep 25 2008 Konstantin Baev <kipruss@altlinux.org> 2.0-alt1
- Up version to 2.0

* Thu Sep 25 2008 Konstantin Baev <kipruss@altlinux.org> 1:1.0-alt9
- Removed experimental code

* Wed Sep 24 2008 Konstantin Baev <kipruss@altlinux.org> 1:1.0-alt8
- For compatibility Serial replaced by Epoch

* Wed Sep 24 2008 Konstantin Baev <kipruss@altlinux.org> 1:1.0-alt7
- For compatibility with Ubuntu command service replaced by macros

* Fri Sep 19 2008 Konstantin Baev <kipruss@altlinux.org> 1:1.0-alt6
- Remove BuildRequires and  add requires - rpm-build-compat

* Tue Sep 16 2008 Konstantin Baev <kipruss@altlinux.org> 1:1.0-alt5
- Symlinks changed to local

* Fri Sep 05 2008 Konstantin Baev <kipruss@altlinux.org> 1:1.0-alt4
- Minor bugfix in spec

* Fri Sep 05 2008 Konstantin Baev <kipruss@altlinux.org> 1:1.0-alt3
- Added forgotten part (post and preun) of spec (and modified)

* Thu Sep 04 2008 Konstantin Baev <kipruss@altlinux.org> 1:1.0-alt2
- fixed build problem on kernel 2.6.18

* Wed Sep 03 2008 Konstantin Baev <kipruss@altlinux.org> 1:1.0-alt1
- sources changed - now it's with Etersoft patches
- source directory renamed to cifs
- sources will be packaged in separate kernel-source package,
  named kernel-source-etercifs-legacy-1.50c
- no more compiled module etercifs.ko in rpm, just install scripts and src
- one script builds etercifs module for several kerneld from other sources

* Thu Jan 31 2008 Vitaly Lipatov <lav@altlinux.ru> 1.50c-alt4
- fix build on Fedora 8 (2.6.18-53)

* Sun Jan 27 2008 Vitaly Lipatov <lav@altlinux.ru> 1.50c-alt3
- move modules placement
- move src files to name-version for dkms compatibility
- change module name to etercifs.ko

* Fri Dec 28 2007 Vitaly Lipatov <lav@altlinux.ru> 1.50c-alt2
- add fix for SLED10 kernel 2.6.16.46
- fix warnings, add missed access setting in reopen file func

* Tue Nov 06 2007 Vitaly Lipatov <lav@altlinux.ru> 1.50c-alt1
- update version
- fix spec according to Korinf build system

* Fri Oct 12 2007 Vitaly Lipatov <lav@altlinux.ru> 1.50-alt1
- update version

* Fri Sep 14 2007 Sergey Lebedev <barabashka@altlinux.ru> 1.50-alt0
- new version cifs 1.50

* Fri Jul 27 2007 Vitaly Lipatov <lav@altlinux.ru> 1.48a-alt7
- fix build on 2.6.22 kernels
- fix scripts for Debian/Ubuntu

* Tue Jun 26 2007 Vitaly Lipatov <lav@altlinux.ru> 1.48a-alt6
- WINE@Etersoft 1.0.7 bugfix release
- some start script fixes, install manually build first
- fix build for kernels in symlinked build dir
- fix build on ASP Linux 2.6.9-55 kernels

* Tue Jun 19 2007 Vitaly Lipatov <lav@altlinux.ru> 1.48a-alt5
- WINE@Etersoft 1.0.7 release
- fix build on ALT ovz-smp
- fix build with 2.6.9 and older kernel
- fix build on ALT Linux 2.4
- fix caching after oplock break (eterbug #477)
- fix build with 2.6.18 on CentOS/5 and Fedora

* Sun Jun 17 2007 Vitaly Lipatov <lav@altlinux.ru> 1.48a-alt4
- WINE@Etersoft 1.0.7 rc1
- script fixes

* Thu Jun 14 2007 Vitaly Lipatov <lav@altlinux.ru> 1.48a-alt3
- WINE@Etersoft 1.0.7 beta
- fix inode revalidate for read requests
- fix build module scripts

* Tue Jun 12 2007 Vitaly Lipatov <lav@altlinux.ru> 1.48a-alt2
- WINE@Etersoft 1.0.7 alpha

* Fri Jun 08 2007 Vitaly Lipatov <lav@altlinux.ru> 1.48a-alt1
- initial build for WINE@Etersoft project
