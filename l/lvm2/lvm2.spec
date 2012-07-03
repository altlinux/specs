%define lvm2version 2.02.96
%define dmversion 1.02.75

%def_disable cluster
%def_enable selinux

Summary: Userland logical volume management tools
Name: lvm2
Version: %lvm2version
Release: alt1
License: GPL

Group: System/Base
Url: http://sources.redhat.com/lvm2
Source: %name-%version.tar

Source1: dmcontrol_update
Source3: lvm2-monitor.init

Patch3: device-mapper.1.02.64-alt-verbose.patch
Patch4: device-mapper.1.02.54-alt-LIB_VERSION.patch

Patch11: lvm2-2.02.73-alt-dmeventd-lvm-weak.patch
Patch14: lvm2-2.02.95-alt-systemd-units.patch

Conflicts: liblvm

Requires: dmsetup  >= %{dmversion}-%{release}
Requires: dmeventd >= %{dmversion}-%{release}
Requires: liblvm2  = %{lvm2version}-%{release}

%define _sbindir /sbin
%def_enable static

BuildRequires: libreadline-devel, libtinfo-devel libudev-devel
%{?_enable_static:BuildRequires: libreadline-devel-static libtinfo-devel-static}
%{?_enable_cluster:BuildRequires: libcman-devel libdlm-devel}
%{?_enable_selinux:BuildRequires: libselinux-devel}

%description
LVM2 includes all of the support for handling read/write operations
on physical volumes (hard disks, RAID-Systems, magneto optical, etc.,
multiple devices (MD), see mdadd(8) or even loop devices, see losetup(8)),
creating volume groups (kind of virtual disks) from one or more physical
volumes and creating one or more logical volumes (kind of logical
partitions) in volume groups.

%package static
Summary: Statically linked userland logical volume management tool
Group: System/Base
Requires: %name = %lvm2version-%release

%description static
This package contains statically linked LVM2 tool.

%package -n clvm
Summary: Cluster LVM daemon for LVM2
Group: System/Base
Requires: %name = %lvm2version-%release

%description -n clvm
Extensions to LVM2 to support clusters.

### liblvm* subpackages go here.

%package -n liblvm2
Summary: LVM2 shared libraries
License: LGPLv2
Group: System/Libraries
Requires: libdevmapper = %dmversion-%release
Requires: libdevmapper-event = %dmversion-%release

%description -n liblvm2
This package contains shred lvm2 libraries for applications.

%package -n liblvm2-devel
Summary: LVM2 development libraries and headers
Group: System/Libraries
License: LGPLv2
Requires: lvm2 = %lvm2version-%release
Requires: liblvm2 = %lvm2version-%release
Requires: libdevmapper-devel = %dmversion-%release

%description -n liblvm2-devel
This package contains files needed to develop applications that use
the lvm2 libraries.

### device-mapper subpackages go here.

%package -n libdevmapper
Version: %dmversion
Summary: Library of routines for device-mapper management
Group: System/Libraries

%package -n libdevmapper-devel
Version: %dmversion
Summary: Header file for libdevmapper
Group: System/Libraries
Requires: libdevmapper = %dmversion-%release

%package -n libdevmapper-devel-static
Version: %dmversion
Summary: Static version of libdevmapper
Group: System/Libraries
Requires: libdevmapper-devel = %dmversion-%release

%package -n dmsetup
Version: %dmversion
Summary: Utilities for low level logical volume management
Group: System/Kernel and hardware
Requires: libdevmapper = %dmversion-%release
Requires: udev >= 150-alt4

%package -n dmeventd
Version: %dmversion
Summary: Device-mapper event daemon
Group: System/Base
Requires: dmsetup = %dmversion-%release
Requires: libdevmapper-event = %dmversion-%release

%package -n libdevmapper-event
Summary: Device-mapper event daemon shared library
Version: %dmversion
License: LGPLv2
Group: System/Libraries
Requires: liblvm2  = %{lvm2version}-%{release}
Requires: libdevmapper = %dmversion-%release

%package -n libdevmapper-event-devel
Summary: Development libraries and headers for the device-mapper event daemon
Version: %dmversion
License: LGPLv2
Group: System/Libraries
Requires: libdevmapper-event = %dmversion-%release
Requires: libdevmapper-devel = %dmversion-%release

%description
This package contains the library and set of utilites for creating and
managing of device-mapper logical volumes.

%description -n libdevmapper
Library of routines for device-mapper management.

%description -n libdevmapper-devel
Header files for libdevmapper.

%description -n libdevmapper-devel-static
Static version of libdevmapper.

%description -n dmsetup
Utilities for low level logical volume management.

%description -n dmeventd
This package contains the dmeventd daemon for monitoring the state
of device-mapper devices.

%description -n libdevmapper-event
This package contains the device-mapper event daemon shared library,
libdevmapper-event.

%description -n libdevmapper-event-devel
This package contains files needed to develop applications that use
the device-mapper event library.

%prep
%setup

%patch3 -p2
%patch4 -p2
%patch11 -p2
%patch14 -p1
%__subst -p 's/ncurses/tinfo &/' configure*

%build
%autoreconf
export ac_cv_path_MODPROBE_CMD=/sbin/modprobe

%if_enabled static
%configure \
	--disable-readline \
	--disable-selinux \
	--disable-nls \
	--enable-jobs=%__nprocs \
	--enable-lvm1_fallback \
	--enable-static_link \
	ac_cv_lib_dl_dlopen=no \
	--with-optimisation="%optflags -Os" \
	--with-group= \
	--with-staticdir=/sbin \
	--with-user= \
	--disable-pkgconfig \
	--with-device-uid=0 \
	--with-device-gid=6 \
	--with-device-mode=0660 \
	--with-dmeventd-path="/sbin/dmeventd" \
	LDFLAGS="-lc_stubs"
	#
%__make libdm
%__make lib
%__make -C tools lvm.static
mv tools/lvm.static .
mv libdm/ioctl/libdevmapper.a .
%__make clean
%endif # static

# dynamic

%configure \
	%{subst_enable selinux} \
	--disable-static_link \
	--enable-jobs=%__nprocs \
	--enable-lvm1_fallback \
	--enable-readline \
	--with-group= \
	--with-user= \
	--enable-pkgconfig \
	--with-device-uid=0 \
	--with-device-gid=6 \
	--with-device-mode=0660 \
%if_enabled cluster
	--with-clvmd=cman \
%endif
	--enable-applib \
	--enable-cmdlib \
	--with-usrlibdir=%_libdir \
	--enable-dmeventd \
	--with-udevdir=/lib/udev/rules.d \
	--enable-udev_sync \
	--with-dmeventd-path="/sbin/dmeventd"
	#
%__make

%install
%make_install install DESTDIR=%buildroot
chmod -R u+rwX %buildroot
%{?_enable_static:install -pm755 lvm.static %buildroot/sbin/}

mkdir -p %buildroot/%_lib
mkdir -p %buildroot/etc/lvm/{archive,backup}
mkdir -p %buildroot/var/lock/lvm
install -m700 /dev/null %buildroot/etc/lvm/.cache

### device-mapper part

install -pm755 %_sourcedir/dmcontrol_update %buildroot%_sbindir/

%{?_enable_static:install -pm755 libdevmapper.a %buildroot%_libdir/}

# Relocate shared library from %_libdir/ to /%_lib/.
for f in `ls %buildroot%_libdir/libdevmapper.so`; do
	t=`objdump -p "$f" |awk '/SONAME/ {print $2}'`
	[ -n "$t" ]
	ln -sf ../../%_lib/"$t" "$f"
done

mv %buildroot%_libdir/libdevmapper.so.1.00 %buildroot/%_lib/

mv %buildroot%_libdir/libdevmapper-event.so.1.00 %buildroot/%_lib/

pushd %buildroot%_libdir
rm -f libdevmapper-event.so
ln -sf ../../%_lib/libdevmapper-event.so.1.00 ./libdevmapper-event.so
popd

# Fix pkgconfig file.
%__subst '/^Version:/ s/"\([^[:space:]]\+\)[^"]*"/\1/' %buildroot%_pkgconfigdir/*

# provide a symlink for devmapper.pc
ln -sf devmapper.pc %buildroot%_pkgconfigdir/libdevmapper.pc

### cluster stuff
%if_enabled cluster
install -pm755 scripts/lvmconf.sh %buildroot/sbin/lvmconf
%endif

### lvm2-monitor init script

mkdir -p %buildroot%_initdir
install -m 0755 %SOURCE3 %buildroot%_initdir/lvm2-monitor

%make install_systemd_units DESTDIR=%buildroot
%make install_tmpfiles_configuration DESTDIR=%buildroot

%post
%post_service lvm2-monitor

%preun
%preun_service lvm2-monitor

%files
%doc README WHATS_NEW udev/12-dm-permissions.rules
/sbin/*
%exclude /sbin/dmsetup
%exclude /sbin/dmcontrol_update
%if_enabled cluster
%exclude /sbin/lvmconf
%endif
%exclude /sbin/dmeventd
%{?_enable_static:%exclude /sbin/*.static}
%_mandir/man?/*
%exclude %_mandir/man8/dmsetup*
%if_enabled cluster
%exclude %_mandir/man8/clvm*
%endif
%config(noreplace) /etc/lvm/lvm.conf
%_initdir/lvm2-monitor
%_unitdir/lvm2-monitor.service
%config(noreplace) %_sysconfdir/tmpfiles.d/%name.conf
%dir /etc/lvm/
%defattr(600,root,root,700)
/etc/lvm/backup/
/etc/lvm/archive/
/var/lock/lvm/
%ghost %verify(not md5 size mtime) %config(missingok,noreplace) /etc/lvm/.cache

%if_enabled static
%files static
/sbin/*.static
%endif # static

%if_enabled cluster
%files -n clvm
/usr/sbin/clvmd
#%_initdir/clvmd
%_man8dir/clvmd*
%_sbindir/lvmconf
%endif

%files -n liblvm2
%_libdir/liblvm2app.so.*
%_libdir/liblvm2cmd.so.*

%files -n liblvm2-devel
%_libdir/liblvm2app.so
%_libdir/liblvm2cmd.so

%_includedir/lvm2app.h
%_includedir/lvm2cmd.h
%_pkgconfigdir/lvm2app.pc

%files -n libdevmapper
/%_lib/libdevmapper.so.*

%files -n libdevmapper-devel
%_libdir/libdevmapper.so
%_includedir/libdevmapper.h
%_pkgconfigdir/*devmapper.*

%files -n libdevmapper-devel-static
%_libdir/libdevmapper.a

%files -n dmsetup
%doc WHATS_NEW_DM
%_man8dir/dmsetup*
%_sbindir/dmsetup
%_sbindir/dmcontrol_update
/lib/udev/rules.d/*

%files -n dmeventd
%_sbindir/dmeventd
%_unitdir/dm-event.service
%_unitdir/dm-event.socket

%files -n libdevmapper-event
/%_lib/libdevmapper-event.so.*
%_libdir/libdevmapper-event-lvm2.so*
%_libdir/libdevmapper-event-lvm2mirror.so
%_libdir/libdevmapper-event-lvm2raid.so
%_libdir/libdevmapper-event-lvm2snapshot.so
%_libdir/device-mapper/libdevmapper-event-lvm2mirror.so*
%_libdir/device-mapper/libdevmapper-event-lvm2raid.so*
%_libdir/device-mapper/libdevmapper-event-lvm2snapshot.so*

%files -n libdevmapper-event-devel
%_libdir/libdevmapper-event.so
%_includedir/libdevmapper-event.h
%_pkgconfigdir/devmapper-event.pc

%changelog
* Wed Jun 20 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 2.02.96-alt1
- 2.02.96

* Tue Jun 05 2012 Alexey Shabalin <shaba@altlinux.ru> 2.02.95-alt2
- add systemd unit dm-event, but not enable by default.
- use systemd units from upstream.
- adapt systemd unit for ALTLinux.
- use pvscan --cache instead of vgscan in systemd units.
- add patch for build with libudev > 183.

* Mon Apr 02 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 2.02.95-alt1
- 2.02.95

* Tue Feb 07 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 2.02.90-alt1
- 2.02.90

* Tue Jan 31 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 2.02.89-alt1
- 2.02.89

* Tue Sep 13 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.02.88-alt1
- 2.02.88.

* Fri Aug 19 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.02.87-alt1
- 2.02.87.

* Wed Jul 27 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.02.86-alt1
- 2.02.86.

* Fri May 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.02.85-alt2
- shaba@:
    add lvm2-monitor.service

* Tue May 03 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.02.85-alt1
- 2.02.85.

* Tue Feb 15 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.02.84-alt1
- 2.02.84.
- shaba@:
    add libs-cleanup.patch from debian
    shared build with selinux

* Mon Feb 07 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.02.83-alt3
- 2.02.83.

* Tue Jan 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.02.82-alt2
- bump release to alt2 to avoid dm version conflict

* Tue Jan 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.02.82-alt1
- 2.02.82.

* Mon Jan 17 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.02.81-alt1
- 2.02.81.

* Sun Jan 16 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.02.80-alt1
- 2.02.80.

* Tue Dec 21 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 2.02.79-alt1
- 2.02.79.

* Mon Dec 06 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 2.02.78-alt1
- 2.02.78.

* Tue Nov 23 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 2.02.77-alt1
- 2.02.77.

* Mon Nov 15 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 2.02.76-alt1
- 2.02.76.
- fix 'executable' parameter processing

* Fri Nov 05 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 2.02.75-alt3
- build with proper dmeventd path (ALT #24499)

* Sun Oct 31 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 2.02.75-alt2
- move libdevmapper-event.so.1.00 to /lib[64] (ALT #24458)

* Tue Oct 26 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 2.02.75-alt1
- 2.02.75.

* Thu Aug 26 2010 Konstantin Pavlov <thresh@altlinux.org> 2.02.73-alt1
- 2.02.73.

* Mon Mar 15 2010 Kirill A. Shutemov <kas@altlinux.org> 2.02.61-alt3
- Drop lvm2-2.02.54-alt-udev-rules.patch. udev sets property STARTUP=1
  for coldplug now.

* Fri Mar 05 2010 Kirill A. Shutemov <kas@altlinux.org> 2.02.61-alt2
- Reapply lvm2-2.02.54-alt-udev-rules.patch

* Tue Mar 02 2010 Konstantin Pavlov <thresh@altlinux.org> 2.02.61-alt1
- 2.02.61 (closes: #22939).
- Remove translated descriptions (closes: #22131).

* Tue Feb 16 2010 Dmitry V. Levin <ldv@altlinux.org> 2.02.54-alt3
- dmsetup: Placed udev rules to valid location (closes: #22968).

* Thu Dec 03 2009 Kirill A. Shutemov <kas@altlinux.org> 2.02.54-alt2
- Reenable udev synchronisation.
- Fix and cleanup requires.

* Wed Nov 18 2009 Pavlov Konstantin <thresh@altlinux.ru> 2.02.54-alt1
- 2.02.54.
- Disabled cluster support.

* Thu Oct 15 2009 Pavlov Konstantin <thresh@altlinux.ru> 2.02.53-alt1
- 2.02.53.
- Disable udev synchronisation.

* Thu Sep 24 2009 Pavlov Konstantin <thresh@altlinux.ru> 2.02.52-alt2
- Enable udev synchronisation code.
- Install default udev rules for dmsetup and lvm2.

* Thu Sep 24 2009 Pavlov Konstantin <thresh@altlinux.ru> 2.02.52-alt1
- 2.02.52.
- Introducing new subpackages:
  + dmeventd,
  + libdevmapper-event
  + libdevmapper-event-devel.
- Relocate liblvm2*.so to /%%_lib/.
- Monitor LV mirrors by default (using dmeventd).

* Fri Aug 28 2009 Pavlov Konstantin <thresh@altlinux.ru> 2.02.51-alt1
- 2.02.51.
- Add patches from fedora:
  + Fix pvcreate on a partition (2.02.51)
  + Fix global locking in PV reporting commands (2.02.49).
- Build with liblvm2app and liblvm2cmd.

* Thu Apr 16 2009 Pavlov Konstantin <thresh@altlinux.ru> 2.02.45-alt1
- 2.02.45.
- libdevmapper merged into lvm subtree.
- Create device-mapper devices with 0660 root:disk permissions.
- Build clvm against cman.

* Sun Nov 16 2008 Pavlov Konstantin <thresh@altlinux.ru> 2.02.43-alt1
- 2.02.43.

* Fri Jul 11 2008 Pavlov Konstantin <thresh@altlinux.ru> 2.02.39-alt1
- 2.02.39.
- Stricted build requires for libdevmapper-devel >= 1.02.27-alt1.

* Mon Jan 28 2008 Pavlov Konstantin <thresh@altlinux.ru> 2.02.31-alt1
- 2.02.31.
- Stricted build requires for libdevmapper-devel >= 1.02.24-alt1.

* Tue Aug 28 2007 Pavlov Konstantin <thresh@altlinux.ru> 2.02.28-alt1
- 2.02.28.

* Wed Jul 25 2007 Pavlov Konstantin <thresh@altlinux.ru> 2.02.27-alt1
- 2.02.27.

* Mon Jun 18 2007 Pavlov Konstantin <thresh@altlinux.ru> 2.02.26-alt1
- 2.02.26.

* Wed May 02 2007 Pavlov Konstantin <thresh@altlinux.ru> 2.02.25-alt1
- 2.02.25.
- Stricted build requires for libdevmapper-devel >= 1.02.19-alt1.

* Sun Mar 11 2007 Pavlov Konstantin <thresh@altlinux.ru> 2.02.23-alt1
- 2.02.23.

* Wed Feb 21 2007 Pavlov Konstantin <thresh@altlinux.ru> 2.02.22-alt1
- 2.02.22.

* Sun Jan 21 2007 Pavlov Konstantin <thresh@altlinux.ru> 2.02.19-alt1
- 2.02.19.
- Stricted build requires for libdevmapper-devel >= 1.02.15-alt1.

* Fri Dec 15 2006 Pavlov Konstantin <thresh@altlinux.ru> 2.02.17-alt1
- 2.02.17.

* Sat Nov 11 2006 Pavlov Konstantin <thresh@altlinux.ru> 2.02.14-alt1
- 2.02.14.

* Thu Oct 19 2006 Pavlov Konstantin <thresh@altlinux.ru> 2.02.12-alt1
- 2.02.12.
- Stricted build requires for libdevmapper-devel >= 1.02.12-alt1.

* Mon Feb 06 2006 Dmitry V. Levin <ldv@altlinux.org> 2.02.01-alt2
- Removed ncurses dependencies.
- Relocated utilities to /sbin/.
- Linked lvm.static without readline and packaged it
  in separate subpackage.
- Cleaned up specfile according to ALT packaging policy.

* Mon Jan 16 2006 Pavlov Konstantin <thresh@altlinux.ru> 2.02.01-alt1
- NMU.
- New development version.
- Added buildrequires: libdevmapper-devel-static >= 1.02.02.
- Added packager field.

* Fri Dec 30 2005 ALT QA Team Robot <qa-robot@altlinux.org> 2.01.14-alt1.1
- Rebuilt with libreadline.so.5.

* Wed Sep 14 2005 Anton Farygin <rider@altlinux.ru> 2.01.14-alt1
- 2.01.14

* Fri Jul 15 2005 Anton Farygin <rider@altlinux.ru> 2.01.09-alt2
- requires updated for lvmcompat package

* Fri Jun 24 2005 Anton Farygin <rider@altlinux.ru> 2.01.09-alt1
- first build for sisyphus, based on specfile from fedora project
