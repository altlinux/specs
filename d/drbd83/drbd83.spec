Name: drbd83
Summary: Distributed Redundant Block Device
Packager: Vitaly Kuznetsov <vitty@altlinux.ru>
Version: 8.3.8
Release: alt3
Source0: %name-%version.tar
License: GPL
Group: System/Kernel and hardware
Url: http://www.drbd.org/

BuildRequires: docbook-style-xsl docbook-utils xsltproc flex

%description
Drbd is a distributed replicated block device. It mirrors a
block device over the network to another machine. Think of it
as networked raid 1. It is a building block for setting up
high availability (HA) clusters.

This package contains the programs that will control the drbd kernel module
provided in kernel-source-drbd. You will need a clustering service (such as
heartbeat) to fully implement it.

Authors:
--------
    Philipp Reisner <philipp.reisner at linbit dot com>
    Lars Ellenberg  <l.g.e at web dot de>

%package tools
Group: System/Kernel and hardware
Conflicts: drbd-tools drbd8-tools
Summary: Distributed Redundant Block Device utilities

%description tools
Drbd is a distributed replicated block device. It mirrors a
block device over the network to another machine. Think of it
as networked raid 1. It is a building block for setting up
high availability (HA) clusters.

This package contains the programs that will control the drbd kernel module
provided in kernel-source-drbd. You will need a clustering service (such as
heartbeat) to fully implement it.

Authors:
--------
    Philipp Reisner <philipp.reisner at linbit dot com>
    Lars Ellenberg  <l.g.e at web dot de>

%package -n kernel-source-%name-%version
Summary: Kernel source for DRBD
Group: Development/Kernel

BuildRequires(pre): kernel-build-tools

%description -n kernel-source-%name-%version
This is the source of the kernel-dependant driver for DRBD.

%package udev
Summary: udev integration scripts for DRBD
Group: System/Kernel and hardware
Requires: %{name}-tools = %{version}-%{release}, udev

%description udev
This package contains udev helper scripts for DRBD, managing symlinks to
DRBD devices in /dev/drbd/by-res and /dev/drbd/by-disk.

%package heartbeat
Summary: Heartbeat resource agent for DRBD
Group: System/Kernel and hardware
Requires: %{name}-tools = %{version}-%{release}
License: GPLv2

%description heartbeat
This package contains the DRBD resource agents for the Heartbeat cluster
resource manager (in v1 compatibility mode).

%prep
%setup -q -n %name-%version
%__cp -a drbd kernel-source-%name-%version
%__tar -cj -f kernel-source-%name-%version.tar.bz2 \
    kernel-source-%name-%version

%build
# No networking operations during build
subst 's!--xinclude!--xinclude --novalid!g' documentation/Makefile.in

./autogen.sh
%configure \
    --with-utils \
    --with-udev \
    --with-heartbeat \
    --without-km \
    --localstatedir=/var \
    --with-initdir=%{_initddir}

VERSION=%version-%release make drbd/drbd_buildtag.c
for dir in user scripts documentation; do
  make CFLAGS="%optflags -I../drbd" PREFIX=%buildroot/ MANDIR=%_mandir -C "$dir"
done

make PREFIX=%buildroot/ MANDIR=%_mandir doc

%install
mkdir -p %kernel_srcdir
install -p -m644 kernel-source-%name-%version.tar.bz2 %kernel_srcdir/

for dir in user scripts documentation; do
    %__make DESTDIR=%buildroot/ MANDIR=%_mandir -C "$dir" install
done


# and I only want to install a hint to the example conf
#
cat <<EOF > %buildroot%_sysconfdir/drbd.conf
#
# please have a a look at the example configuration file in
# %_docdir/%name-utils-%version/
#
include "drbd.d/global_common.conf";
include "drbd.d/*.res";
EOF

%__mkdir_p %buildroot%_sysconfdir/sysconfig
cat <<EOF > %buildroot%_sysconfdir/sysconfig/drbd
DEFAULTFILE="%_sysconfdir/sysconfig/drbd"
DRBDADM="/sbin/drbdadm"
PROC_DRBD="/proc/drbd"
MODPROBE="/sbin/modprobe"
RMMOD="/sbin/rmmod"
UDEV_TIMEOUT=10
ADD_MOD_PARAM=""
EOF

%__mkdir_p %buildroot%_localstatedir/drbd

%files tools
/sbin/drbdsetup
/sbin/drbdadm
/sbin/drbdmeta
%_initddir/drbd
%_sbindir/drbd-overview
%config(noreplace) %_sysconfdir/drbd.conf
%config(noreplace) %_sysconfdir/sysconfig/drbd
%config(noreplace) %_sysconfdir/drbd.d/global_common.conf
%dir /usr/lib/drbd
/usr/lib/drbd/notify*
/usr/lib/drbd/outdate*
/usr/lib/drbd/snapshot*
/usr/lib/drbd/unsnapshot*
%_man8dir/*
%_man5dir/*
%doc scripts/drbd.conf.example
%doc COPYING
%doc README
%doc ChangeLog
%dir %_localstatedir/drbd
%dir %_sysconfdir/drbd.d

%files -n kernel-source-%name-%version
%_usrsrc/kernel/sources/kernel-source*.tar.bz2

%files udev
%config %_sysconfdir/udev/rules.d/65-drbd.rules*

%files heartbeat
%_sysconfdir/ha.d/resource.d/drbddisk
%_sysconfdir/ha.d/resource.d/drbdupper
/usr/lib/ocf/resource.d/linbit/drbd
/usr/lib/drbd/crm-*

%changelog
* Mon Feb 28 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 8.3.8-alt3
- avoid intersection with system packages (/usr/src/debug)

* Fri Nov 05 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 8.3.8-alt2
- fix drbd start/stop order (ALT #24504)

* Wed Aug 25 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 8.3.8-alt1
- 8.3.8

* Tue Jun 08 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 8.3.7-alt4
- fix typo in default config

* Fri Mar 05 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 8.3.7-alt3
- pack some forgotten stuff
- move /etc/default/drbd to /etc/sysconfig/drbd

* Thu Mar 04 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 8.3.7-alt2
- localestatedir fixed, thanks to misha@

* Sat Feb 27 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 8.3.7-alt1
- update to 8.3.7, -udev and -heartbeat subpackages added

* Tue Sep 09 2008 Eugene Prokopiev <enp@altlinux.ru> 8.2.6-alt2
- fix x86_64 build

* Mon Sep 08 2008 Eugene Prokopiev <enp@altlinux.ru> 8.2.6-alt1
- new version
- new repo scheme 
- some cleanup:
  + remove rpm-build-linux-ha support
  + use upstream initscript

* Sun May 18 2008 L.A. Kostis <lakostis@altlinux.ru> 0.7.25-alt1.git18022008
- use GIT fe0c05d shapshot.

* Sun May 18 2008 L.A. Kostis <lakostis@altlinux.ru> 0.7.25-alt1
- 0.7.25.

* Sat Dec 02 2006 L.A. Kostis <lakostis@altlinux.ru> 0.7.22-alt2
- add dependency to linux-ha-common.
- update ha resources.
- remove unwanted kernel version checks during -tools install.

* Fri Nov 10 2006 L.A. Kostis <lakostis@altlinux.ru> 0.7.22-alt1
- 0.7.22.

* Sun Sep 17 2006 L.A. Kostis <lakostis@altlinux.ru> 0.7.21-alt1
- 0.7.21.

* Sun Jul 09 2006 LAKostis <lakostis at altlinux.org> 0.7.20-alt1
- 0.7.20.

* Sun Jun 18 2006 LAKostis <lakostis at altlinux.org> 0.7.19-alt1.1
- imported .spec to git.

* Mon Jun 05 2006 LAKostis <lakostis at altlinux.org> 0.7.19-alt1
- 0.7.19.

* Tue May 09 2006 LAKostis <lakostis at altlinux.org> 0.7.18-alt1.1
- fixed typo in post (see #9534).

* Fri Apr 28 2006 LAKostis <lakostis at altlinux.org> 0.7.18-alt1
- 0.7.18.

* Mon Apr 24 2006 LAKostis <lakostis at altlinux.org> 0.7.17-alt2
- Add drbd nodes only for kernels < 2.6 due udev.

* Sat Apr 22 2006 LAKostis <lakostis at altlinux.org> 0.7.17-alt1.2
- Add condrestart/condreload to init.d script.

* Fri Apr 21 2006 LAKostis <lakostis at altlinux.org> 0.7.17-alt1.1
- Apply patch fixing drbd unconfigured state after startup
  when using udevd.

* Sun Apr 16 2006 LAKostis <lakostis at altlinux.org> 0.7.17-alt1
- 0.7.17.

* Fri Feb 24 2006 LAKostis <lakostis at altlinux.org> 0.7.16-alt1
- 0.7.16.

* Fri Jan 06 2006 LAKostis <lakostis at altlinux.org> 0.7.15-alt1
- 0.7.15.

* Sun Oct 30 2005 LAKostis <lakostis at altlinux.org> 0.7.14-alt1
- initial build for Sisyphus.
- add some defaults from debian package.
- spec based on template from source package.
