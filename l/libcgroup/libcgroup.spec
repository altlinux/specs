%define soversion 1.0.38
%define soversion_major 1

Name: libcgroup
Summary: Libraries for allow to control and monitor control groups
Group: System/Libraries
Version: 0.38.0
Release: alt1
License: LGPLv2+
Url: http://libcg.sourceforge.net/
Packager: Alexey Shabalin <shaba@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: flex gcc-c++ libpam-devel

%description
Control groups infrastructure.

This library allows applications to manipulate, control, administrate and
monitor control groups and the associated controllers.

%package -n pam_cgroup
Summary: A Pluggable Authentication Module for libcgroup
Group: System/Base
Requires: libcgroup = %version-%release

%description -n pam_cgroup
Linux-PAM module, which allows administrators to classify the user's login
processes to pre-configured control group.

%package -n cgroup
Summary: Tools to control and monitor control groups
Group: System/Configuration/Other
Requires: libcgroup = %version-%release

%description -n cgroup
Control groups infrastructure.

These tools help manipulate, control, administrate and monitor control groups
and the associated controllers.

%package devel
Summary: Development libraries to develop applications that utilize control groups
Group: Development/C
Requires: libcgroup = %version-%release

%description devel
It provides API to create/delete and modify cgroup nodes. It will also in the
future allow creation of persistent configuration for control groups and
provide scripts to manage that configuration.

%prep
%setup
%patch -p1

%build
%autoreconf
%configure \
	--bindir=/bin \
	--sbindir=/sbin \
	--libdir=%_libdir \
	--enable-initscript-install \
	--enable-pam-module-dir=/%_lib/security \
	--enable-opaque-hierarchy=name=systemd

%make_build

%install
%make DESTDIR=%buildroot install

# install config files
mkdir -p %buildroot/%_sysconfdir/sysconfig
cp samples/cgred.conf %buildroot/%_sysconfdir/sysconfig/cgred
cp samples/cgconfig.sysconfig %buildroot/%_sysconfdir/sysconfig/cgconfig
cp samples/cgconfig.conf %buildroot/%_sysconfdir/cgconfig.conf
cp samples/cgrules.conf %buildroot/%_sysconfdir/cgrules.conf
cp samples/cgsnapshot_blacklist.conf %buildroot/%_sysconfdir/cgsnapshot_blacklist.conf

rm -f %buildroot/%_lib/security/pam_cgroup.la

# move the libraries  to /
mkdir -p %buildroot/%_lib
mv -f %buildroot/%_libdir/libcgroup.so.%soversion %buildroot/%_lib
rm -f %buildroot/%_libdir/libcgroup.so.%soversion_major
ln -sf libcgroup.so.%soversion %buildroot/%_lib/libcgroup.so.%soversion_major
ln -sf ../../%_lib/libcgroup.so.%soversion %buildroot/%_libdir/libcgroup.so
rm -f %buildroot/%_libdir/*.la

# install unit and sysconfig files
install -d %buildroot%systemd_unitdir
install -m 644 cgconfig.service %buildroot%systemd_unitdir/
install -m 644 cgred.service %buildroot%systemd_unitdir/

%pre -n cgroup
%_sbindir/groupadd -r -f cgred 2> /dev/null ||:

%post -n cgroup
%post_service cgred
%post_service cgconfig

%preun -n cgroup
%preun_service cgred
%preun_service cgconfig

%files
/%_lib/libcgroup.so.*

%files -n cgroup
%doc COPYING INSTALL README README_daemon README_systemd
%config(noreplace) %_sysconfdir/sysconfig/cgred
%config(noreplace) %_sysconfdir/sysconfig/cgconfig
%config(noreplace) %_sysconfdir/cgconfig.conf
%config(noreplace) %_sysconfdir/cgrules.conf
%config(noreplace) %_sysconfdir/cgsnapshot_blacklist.conf
%attr(2711, root, cgred) /bin/cgexec
/bin/cgclassify
/bin/cgcreate
/bin/cgget
/bin/cgset
/bin/cgdelete
/bin/lscgroup
/bin/lssubsys
/bin/cgsnapshot
/sbin/*
%_man1dir/*
%_man5dir/*
%_man8dir/*
%config %_initdir/cgconfig
%config %_initdir/cgred
%systemd_unitdir/cgconfig.service
%systemd_unitdir/cgred.service

%files -n pam_cgroup
%_pam_modules_dir/pam_cgroup.so

%files devel
%doc COPYING INSTALL
%_includedir/libcgroup.h
%dir %_includedir/libcgroup
%_includedir/libcgroup/*.h
%_libdir/libcgroup.*
%_pkgconfigdir/libcgroup.pc

%changelog
* Mon Mar 12 2012 Alexey Shabalin <shaba@altlinux.ru> 0.38.0-alt1
- 0.38 release

* Mon Mar 12 2012 Alexey Shabalin <shaba@altlinux.ru> 0.38.0-alt0.rc1
- 0.38.rc1
- add systemd unit files

* Thu Aug 18 2011 Alexey Shabalin <shaba@altlinux.ru> 0.37.1-alt3.7f564
- upstream git snapshot 7f5641d9b2e8d073466f0511a17e669438dbaea7

* Thu May 19 2011 Alexey Shabalin <shaba@altlinux.ru> 0.37.1-alt2
- fix pid file of cgred service
- ignore systemd hierarchy
- use -avoid-version instead of messing with pam module renaming
- backported from upstream snapshot:
  + Fixed parsing of mount options
  + Fix cgclear to continue unmounting on error

* Thu Mar 03 2011 Alexey Shabalin <shaba@altlinux.ru> 0.37.1-alt1
- 0.37.1
- Fix buffer overflow when processing list of controllers from command line (CVE-2011-1006)

* Thu Dec 16 2010 Alexey Shabalin <shaba@altlinux.ru> 0.37-alt1
- 0.37
- defined startup_failure in cgconfig init script (ALT #24596)

* Sun Sep 19 2010 Alexey Shabalin <shaba@altlinux.ru> 0.36.2-alt3.git20100906
- git snapshot af53a11e8e5f27593f31a34739756d41a08b5416
- fix init scripts
- mount tmpfs to /sys/fs/cgroup from init cgconfig (/sys/fs/cgroup exist in kernel 2.6.35-un-def-alt4.2)

* Thu Aug 26 2010 Alexey Shabalin <shaba@altlinux.ru> 0.36.2-alt2
- change default mount point from /var/run/cgroup/system to /sys/fs/cgroup/system

* Wed Jul 07 2010 Alexey Shabalin <shaba@altlinux.ru> 0.36.2-alt1
- initial build for ALTLinux
