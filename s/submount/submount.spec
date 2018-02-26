%define rsuffix		%nil
%define pkgsuffix	%nil

Name: submount
Version: 0.9
Release: alt5.2
%define module_name     subfs
%define module_version  %version
%define module_release  %release

Group: System/Kernel and hardware
Summary: Auto Mounting of Removable Media
Url: http://submount.sourceforge.net/
License: GPL

Provides: submountd = %version-%release
Obsoletes: submountd
Conflicts: hal <= 0.5.3-alt4

BuildPreReq: kernel-build-tools, rpm-build

Source0: %name%rsuffix-%version.tar.bz2
Source1: Makefile.modules
Source2: mount-subfs.c


# SuSE
Patch1: submount.diff
Patch2: resmgr.diff
Patch3: disable-statfs.diff
Patch4: floppyfss-types.diff
Patch5: fix-oops.diff
Patch6: fix-sig11.diff
Patch7: remove-trailing-comma-in-options.diff
Patch8: hard-autodetect.diff

# ALT
Patch100: alt-mandir.patch
Patch101: alt-message.patch

%description
Submount is a system for automatically mounting and unmounting
removable media drives like CD-ROMs and floppy disk drives. Once
installed, it allows removable media drives to be accessed as if they
were permanently mounted.

You must install kernel-modules-%module_name-* package
for your kernel.

Example line for a CD-ROM drive in /etc/fstab:
/dev/cdrom /mnt/cdrom subfs fs=cdfss,ro 0 0

Example line for a floppy drive in /etc/fstab:
/dev/floppy /mnt/floppy subfs fs=floppyfss,sync 0 0

Example line for a NFS in /etc/fstab:
host:/share_name /mnt/share_name subfs fs=nfs,program=/sbin/net-submountd%pkgsuffix 0 0

Authors:
--------
    Eugene S. Weiss <eweiss@sbclobal.net>

%package -n kernel-source-%module_name%pkgsuffix
Group: Development/Kernel
Summary: %module_name module sources for Linux kernel

%description -n kernel-source-%module_name%pkgsuffix
%module_name module sources for Linux kernel

%prep
%setup -q -n %name%rsuffix-%version
pushd subfs*
%patch1 -p1
#%patch2 -p1
#%patch3 -p1
%patch5 -p1
#
%patch101 -p1
install -m0644 %SOURCE1 Makefile
popd
pushd submountd*
%patch2 -p1
%patch4 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
#
%patch100 -p1
popd

pushd submountd*
%__aclocal
%__autoconf
%__automake -a
popd

%build
pushd submountd*
export CFLAGS="%optflags"
%configure \
    --sbindir=/sbin \
    --enable-resmgr
%make
popd

%install
pushd submountd*
%make DESTDIR=%buildroot install
popd

for f in submountd net-submountd
do
    [ -e "%buildroot/sbin/$f"%pkgsuffix ] \
	|| mv -f "%buildroot/sbin/$f" "%buildroot/sbin/$f"%pkgsuffix
done

# kernel module sources
[ -d kernel-source-%module_name%pkgsuffix-%module_version ] || mv %module_name%rsuffix-%module_version kernel-source-%module_name%pkgsuffix-%module_version
%__mkdir_p %buildroot/%kernel_src
%__tar cfz \
    %buildroot/%kernel_src/kernel-source-%module_name%pkgsuffix-%module_version.tar.gz \
    kernel-source-%module_name%pkgsuffix-%module_version


%files
%doc COPYING README
%_mandir/*/*
#
/sbin/submountd%pkgsuffix
/sbin/net-submountd%pkgsuffix

%files -n kernel-source-%module_name%pkgsuffix
%attr(0644,root,root) %kernel_src/kernel-source-%module_name%pkgsuffix-%module_version.tar.*

%changelog
* Thu Jan 27 2011 Michael Shigorin <mike@altlinux.org> 0.9-alt5.2
- rebuilt (see #24924)

* Wed Apr 22 2009 Michael A. Kangin <prividen@altlinux.org> 0.9-alt5.1
- Patch for ability to unmount ntfs-3g file system 

* Mon Jun 19 2006 Sergey V Turchin <zerg at altlinux dot org> 0.9-alt5
- removed policy and script for hal

* Fri Jul 22 2005 Anton Farygin <rider@altlinux.ru> 0.9-alt4.2
- hal policy: disabled unmounting subfs cdroms and floppy
- mount-hal-fs: do not mount already mounted filesystem

* Thu Jul 21 2005 Anton Farygin <rider@altlinux.ru> 0.9-alt4.1
- added policy and script for hal

* Wed Jun 01 2005 Sergey V Turchin <zerg at altlinux dot org> 0.9-alt4
- merge patches with SuSE

* Wed Jul 14 2004 Sergey V Turchin <zerg at altlinux dot org> 0.9-alt3
- fix package description

* Tue May 11 2004 Sergey V Turchin <zerg at altlinux dot org> 0.9-alt2
- initial spec
- add patches from SuSE
- bump release
