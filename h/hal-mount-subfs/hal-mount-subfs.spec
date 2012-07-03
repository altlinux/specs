%define fdidir %_datadir/hal/fdi/policy/20thirdparty

Name: hal-mount-subfs
Version: 0.1.9
Release: alt3
BuildArch: noarch

Group: System/Kernel and hardware
Summary: Auto Mounting of Removable Media via submount
Summary(ru_RU.UTF-8): Автоматическое монтирование сменных устройств через submount
Url: http://git.altlinux.org/people/prividen/packages/hal-mount-subfs.git
License: GPL
Packager: Michael A. Kangin <prividen@altlinux.org>

Requires: submount >= 0.9-alt5.1
Requires: hal >= 0.5.10-alt8
Requires: ntfs-3g
# need for initlog
Requires: service 

Source0: %name-%version.tgz

%description
Auto Mounting of Removable Media via submount

%description -l ru_RU.UTF-8
Когда вы подключаете сменное устройство, %name автоматически создает для него
точку монтирования и монтирует его туда через систему submount. При извлечении
устройства оно отмонтируется и точка монтирования уничтожается.

%prep
%setup -q

%build

%install

mkdir -p %buildroot%_datadir/hal/scripts
mkdir -p %buildroot%fdidir
mkdir -p %buildroot%_sysconfdir/sysconfig
install -m 0644 *.fdi %buildroot%fdidir/
install -m 0755 mount-hal-fs %buildroot%_datadir/hal/scripts/
install -m 0644 %name.sysconfig %buildroot%_sysconfdir/sysconfig/%name

%pre
echo "Warning!!! You MUST install kernel-modules-subfs package for your kernel."

%files
%_datadir/hal/scripts/mount-hal-fs
%fdidir/*.fdi
%config(noreplace) %_sysconfdir/sysconfig/%name
%doc docs/*

%changelog
* Wed Nov 17 2010 Michael A. Kangin <prividen@altlinux.org> 0.1.9-alt3
- Fix incorrect mountpoint name decoding
- New example 95-world-accessable.fdi (Closes: #23849)

* Tue Apr 28 2009 Michael A. Kangin <prividen@altlinux.org> 0.1.9-alt2
- ntfs-3g requires

* Sat Apr 25 2009 Michael A. Kangin <prividen@altlinux.org> 0.1.9-alt1
- Warnings about absent kernel-modules-subfs;
- Fix mount options for XFS (#19078);
- ntfs-3g support

* Wed Dec 10 2008 Michael A. Kangin <prividen@altlinux.org> 0.1.8-alt1
- Fix charset options for KOI8-R and vfat (#16722);
- Recognize LABEL= and UUID= in /etc/fstab entries (#18095);
- New example: customize device's mount options;
- FAQ

* Thu Aug 07 2008 Michael A. Kangin <prividen@altlinux.org> 0.1.7-alt1
- vfat's flush mountoption support

* Sun Aug 03 2008 Michael A. Kangin <prividen@altlinux.org> 0.1.6-alt1
- 0.1.6-alt1 release

* Sat Aug 02 2008 Michael A. Kangin <prividen@altlinux.org> 0.1.6-alt0
- change requires from submountd to submount;
- config file /etc/sysconfig/hal-mount/subfs;
- some new example config FDI;
- do not mount devices with SHOULD_MOUNT=false policy

* Thu Jul 03 2008 Michael A. Kangin <prividen@altlinux.org> 0.1.5-alt1
- add encodings support for UDF to example fdi files (Igor Vlasenko)

* Fri Apr 11 2008 Michael A. Kangin <prividen@altlinux.org> 0.1.4-alt1
- fix HAL properties for mounted volumes (KDE compatibility)

* Tue Mar 25 2008 Michael A. Kangin <prividen@altlinux.org> 0.1.3-alt1
- Fix processing mountpoints with spaces in name (Yura Kalinichenko);
- Mount filesystems with procuid option;
- UTF8 support by default;
- move .fdi to /usr/share/hal/fdi/policy/20thirdparty/
- build for Sisyphus

* Sat Jan 26 2008 Michael A. Kangin <mak@rsmu.ru> 0.1.2-alt1
- Ignore one of NTFS softraid partitions

* Fri Dec 28 2007 Michael A. Kangin <mak@rsmu.ru> 0.1.1-alt1
- add patch to no automounting noremovable volumes

* Thu Dec 20  2007 Michael A. Kangin <mak@rsmu.ru> 0.1.0-alt1
- New version, new logic, new program

* Fri Jul  7  2006 Sergey A. Sukiyazov <corwin@altlinux.ru> 0.0.1-alt1
- fix unmount algorithm for force unmount

* Mon Jun 12 2006 Sergey A. Sukiyazov <corwin@altlinux.ru> 0.0.1-alt0.3
- fix hal-mount-fs

* Wed Jun  7 2006 Sergey A. Sukiyazov <corwin@altlinux.ru> 0.0.1-alt0.1
- initial build for Sisyphus
- mount-subfs.c, hal-mount-fs and 91-mount-subfs.fdi from submount-0.9-alt4.3
