%define firmwaredir /lib/firmware
%define _localstatedir %_var

%def_enable elfutils
%def_enable libcryptsetup
%def_enable logind
%def_enable vconsole
%def_enable quotacheck
%def_enable randomseed
%def_enable coredump
%def_disable gcrypt
%def_disable qrencode
%def_enable microhttpd
%def_enable gnutls
%def_enable libcurl
%def_enable libidn
%def_enable bootchart
%def_enable polkit
%def_enable efi
%def_enable networkd
%def_enable timesyncd
%def_enable resolved
%def_disable terminal
%def_disable kdbus
%def_enable utmp
%def_with python
%def_enable gtk_doc
%def_enable xz
%def_enable lz4

%def_disable smack
%def_disable seccomp
%def_disable ima
%def_enable selinux
%def_disable apparmor


%def_disable sysusers
%def_disable ldconfig
%def_disable firstboot

%if_enabled sysusers
%def_enable ldconfig
%def_enable firstboot
%endif

%ifarch ia64 %ix86 ppc64 x86_64
%define mmap_min_addr 65536
%else
%define mmap_min_addr 32768
%endif

Name: systemd
# Epoch 1 is when systemd and journalctl are split.
# (Without it, we cannot specify the conflicts correctly
# for pkgs both from p7/t7 and Sisyphus
# so that older systemd from p7/t7 can be installed along with newer journalctl.)
Epoch: 1
Version: 217
Release: alt2
Summary: A System and Session Manager
Url: http://www.freedesktop.org/wiki/Software/systemd
Group: System/Configuration/Boot and Init
License: LGPLv2.1+

Packager: Alexey Shabalin <shaba@altlinux.ru>

Source:%name-%version.tar
Source4: altlinux-openresolv.path
Source5: altlinux-openresolv.service
Source6: altlinux-libresolv.path
Source7: altlinux-libresolv.service
Source8: altlinux-clock-setup.service
Source15: systemd-logind-launch
Source16: altlinux-kmsg-loglevel.service
Source17: altlinux-save-dmesg.service
Source18: altlinux-save-dmesg
Source19: udevd.init
Source20: udevd-final.init
Source21: 40-ignore-remove.rules
Source22: scsi_id.config
Source23: var-lock.mount
Source24: var-run.mount
Source27: altlinux-first_time.service
Source28: systemd-tmpfiles.filetrigger
Source30: 49-coredump-null.conf
Source31: 60-raw.rules
Source33: udev.filetrigger
# ALTLinux's default preset policy
Source34: 85-display-manager.preset
Source35: 90-default.preset
Source36: 99-default-disable.preset
Source37: 85-networkd.preset
Source38: 85-timesyncd.preset

# udev rule generator
Source41: rule_generator.functions
Source42: write_net_rules
Source43: 75-persistent-net-generator.rules
Source44: write_cd_rules
Source45: 75-cd-aliases-generator.rules

Patch1: %name-snapshot.patch
Patch2: %name-alt-patches.patch

# bash3 completions
Source51: hostnamectl-bash3
Source52: journalctl-bash3
Source53: localectl-bash3
Source54: loginctl-bash3
Source55: systemctl-bash3
Source56: systemd-analyze-bash3
Source57: coredumpctl-bash3
Source58: timedatectl-bash3
Source59: udevadm-bash3
Source60: bootctl-bash3
Source61: busctl-bash3
Source62: machinectl-bash3
Source63: systemd-delta-bash3
Source64: systemd-cat-bash3
Source65: systemd-cgls-bash3
Source66: systemd-cgtop-bash3
Source67: systemd-detect-virt-bash3


%define dbus_ver 1.4.6

BuildRequires: glibc-kernheaders
BuildRequires: intltool >= 0.40.0
BuildRequires: gperf
BuildRequires: libcap-devel libcap-utils
BuildRequires: libpam-devel
BuildRequires: libacl-devel acl
BuildRequires: xsltproc
BuildRequires: docbook-style-xsl docbook-dtds
BuildRequires: libdbus-devel >= %dbus_ver
%{?_enable_seccomp:BuildRequires: pkgconfig(libseccomp) >= 1.0.0}
%{?_enable_selinux:BuildRequires: pkgconfig(libselinux) >= 2.1.9}
%{?_enable_apparmor:BuildRequires: pkgconfig(libapparmor)}
%{?_enable_elfutils:BuildRequires: elfutils-devel >= 0.158}
BuildRequires: libaudit-devel
BuildRequires: glib2-devel >= 2.26 libgio-devel
BuildRequires: gobject-introspection-devel
%{?_enable_xz:BuildRequires: liblzma-devel}
%{?_enable_lz4:BuildRequires: liblz4-devel}
BuildRequires: libkmod-devel >= 15 kmod
BuildRequires: kexec-tools
%{?_with_python:BuildRequires: python-devel python-module-sphinx}
BuildRequires: quota
BuildRequires: gtk-doc
BuildRequires: libblkid-devel >= 2.20

%{?_enable_libcryptsetup:BuildRequires: libcryptsetup-devel >= 1.6.0}
BuildRequires: libgcrypt-devel
%{?_enable_qrencode:BuildRequires: libqrencode-devel}
%{?_enable_microhttpd:BuildRequires: pkgconfig(libmicrohttpd) >= 0.9.33}
%{?_enable_gnutls:BuildRequires: pkgconfig(gnutls) >= 3.1.4}
%{?_enable_libcurl:BuildRequires: pkgconfig(libcurl)}
%{?_enable_libidn:BuildRequires: pkgconfig(libidn)}
%{?_enable_terminal:BuildRequires: pkgconfig(libevdev) >= 1.2 pkgconfig(xkbcommon) >= 0.4  pkgconfig(libdrm) >= 2.4}

Requires: dbus >= %dbus_ver
Requires: udev = %epoch:%version-%release
Requires: filesystem >= 2.3.10-alt1
Requires: agetty
Requires: acl
Requires: util-linux >= 2.25

# Requires: selinux-policy >= 3.8.5

Requires: %name-utils = %epoch:%version-%release
Requires: %name-services = %epoch:%version-%release
Requires: pam_%name = %epoch:%version-%release
Requires: journalctl = %epoch:%version-%release

# /*bin/journalctl is in a subpackage.
# We want to be able to install a new journalctl and use the old (stable) systemd.
Conflicts: journalctl < %epoch:%version-%release

# Copy from SysVinit
PreReq: coreutils
Requires: /sbin/sulogin
Requires: sysvinit-utils

Obsoletes: systemd-units < 0:43-alt1
Provides: systemd-units = %epoch:%version-%release
Provides: syslogd-daemon

%description
systemd is a system and session manager for Linux, compatible with
SysV and LSB init scripts. systemd provides aggressive parallelization
capabilities, uses socket and D-Bus activation for starting services,
offers on-demand starting of daemons, keeps track of processes using
Linux cgroups, supports snapshotting and restoring of the system
state, maintains mount and automount points and implements an
elaborate transactional dependency-based service control logic. It can
work as a drop-in replacement for sysvinit.

%package -n libsystemd
Group: System/Libraries
Summary: Systemd Library

Provides: libsystemd-daemon = %epoch:%version-%release
Provides: libsystemd-login = %epoch:%version-%release
Provides: libsystemd-id128 = %epoch:%version-%release
Provides: libsystemd-journal = %epoch:%version-%release

Obsoletes: libsystemd-daemon < %epoch:%version-%release
Obsoletes: libsystemd-login < %epoch:%version-%release
Obsoletes: libsystemd-id128 < %epoch:%version-%release
Obsoletes: libsystemd-journal < %epoch:%version-%release

%description -n libsystemd
The libsystemd library provides a reference implementation of various
APIs for new-style daemons, as implemented by the systemd init system.


%package -n libsystemd-devel
Group: Development/C
Summary: Development headers for systemd Library
License: LGPLv2+ and MIT

Requires: libsystemd = %epoch:%version-%release

Provides: libsystemd-daemon-devel = %epoch:%version-%release
Provides: libsystemd-journal-devel = %epoch:%version-%release
Provides: libsystemd-login-devel = %epoch:%version-%release
Provides: libsystemd-id128-devel = %epoch:%version-%release

Obsoletes: libsystemd-daemon-devel < %epoch:%version-%release
Obsoletes: libsystemd-journal-devel < %epoch:%version-%release
Obsoletes: libsystemd-login-devel < %epoch:%version-%release
Obsoletes: libsystemd-id128-devel < %epoch:%version-%release

%description -n libsystemd-devel
The libsystemd library provides a reference implementation of various
APIs for new-style daemons, as implemented by the systemd init system.

%package -n libnss-myhostname
Group: System/Libraries
Summary: nss-myhostname provide hostname resolution for the locally configured system hostname
Requires(pre): chrooted >= 0.3.5-alt1 chrooted-resolv sed
Requires(postun): chrooted >= 0.3.5-alt1 sed

%description -n libnss-myhostname
nss-myhostname is a plugin for the GNU Name Service Switch (NSS)
functionality of the GNU C Library (glibc) providing host name
resolution for the locally configured system hostname as returned by
gethostname(2). Various software relies on an always resolvable local
host name. When using dynamic hostnames this is usually achieved by
patching /etc/hosts at the same time as changing the host name. This
however is not ideal since it requires a writable /etc file system and
is fragile because the file might be edited by the administrator at
the same time. nss-myhostname simply returns all locally configure
public IP addresses, or -- if none are configured -- the IPv4 address
127.0.0.2 (wich is on the local loopback) and the IPv6 address ::1
(which is the local host) for whatever system hostname is configured
locally. Patching /etc/hosts is thus no longer necessary.

It is necessary to change "hosts" in /etc/nsswitch.conf to
hosts: files myhostname

%package -n libnss-mymachines
Group: System/Libraries
Summary: libnss-mymachines is plugin for local system host name resolution
Requires(pre): chrooted >= 0.3.5-alt1 chrooted-resolv sed
Requires(postun): chrooted >= 0.3.5-alt1 sed
Requires: dbus >= %dbus_ver
Requires: %name-services = %epoch:%version-%release

%description -n libnss-mymachines
nss-mymachines for automatically resolves the names
of all local registered containers to their respective IP addresses.

It is necessary to change "hosts" in /etc/nsswitch.conf to
hosts: files mymachines

%package -n libnss-resolve
Group: System/Libraries
Summary: nss-resolve is plugin for resolve hostnames via systemd-resolved
Requires(pre): chrooted >= 0.3.5-alt1 chrooted-resolv sed
Requires(postun): chrooted >= 0.3.5-alt1 sed
Requires: dbus >= %dbus_ver
Requires: %name-networkd = %epoch:%version-%release

%description -n libnss-resolve
NSS module "nss-resolve" has been added which can be used
instead of glibc's own "nss-dns" to resolve hostnames via
systemd-resolved. Hostnames, addresses and arbitrary RRs may
be resolved via systemd-resolved D-Bus APIs. In contrast to
the glibc internal resolver systemd-resolved is aware of
multi-homed system, and keeps DNS server and caches separate
and per-interface.

It is necessary to change "hosts" in /etc/nsswitch.conf to
hosts: files resolve

%package -n pam_%name
Group: System/Base
Summary: Register user sessions in the systemd login manager
Requires: dbus >= %dbus_ver
Conflicts: %name < 1:216-alt1

%description -n pam_%name
pam_systemd registers user sessions with the systemd login manager
systemd-logind.service, and hence the systemd control group hierarchy.

%package devel
Group: Development/C
Summary: Development headers for systemd
License: LGPLv2.1+ MIT
BuildArch: noarch

%description devel
Development headers and library files for developing applications for systemd.

%package sysvinit
Group: System/Configuration/Boot and Init
Summary: systemd System V init tools
Requires: %name = %epoch:%version-%release
# Obsoletes: SysVinit
Provides: SysVinit = 2.88-alt0.1
#Obsoletes:      upstart
Conflicts: upstart
Conflicts: SysVinit
BuildArch: noarch

%description sysvinit
Drop-in replacement for the System V init tools of systemd.

%package utils
Group: System/Configuration/Boot and Init
Summary: systemd utils
Conflicts: %name < %epoch:%version-%release

%description utils
This package contains utils from systemd:
 - systemd-binfmt
 - systemd-modules-load
 - systemd-sysctl
 - systemd-tmpfiles

%package services
Group: System/Configuration/Boot and Init
Summary: systemd services
Conflicts: %name < %epoch:%version-%release
Requires: pam_%name = %epoch:%version-%release
Requires: %name-utils = %epoch:%version-%release
Requires: dbus >= %dbus_ver
Conflicts: service <= 0.5.25-alt1
Conflicts: chkconfig <= 1.3.59-alt3

%description services
This package contains dbus services and utils from systemd:
 - systemd-hostnamed and hostnamectl
 - systemd-localed and localectl
 - systemd-logind and loginctl
 - systemd-machine and machinectl
 - systemd-timedated and timedatectl

%package networkd
Group: System/Base
Summary: System service that manages networks
Conflicts: %name < 1:214-alt13
Requires: %name = %epoch:%version-%release
Requires: iproute2
Provides: network-config-subsystem

%description networkd
systemd-networkd is a system service that manages networks.
It detects and configures network devices as they appear,
as well as creating virtual network devices.

%package timesyncd
Group: System/Configuration/Other
Summary: Network Time Synchronization
Conflicts: %name < 1:214-alt13
Requires: %name-networkd = %epoch:%version-%release
Provides: ntp-client

%description timesyncd
systemd-timesyncd is a system service that may be used
to synchronize the local system clock with a Network Time Protocol Server.

%package analyze
Group: System/Configuration/Boot and Init
Summary: Analyze tool for systemd.
Requires: %name = %epoch:%version-%release

%description analyze
Analyze tool for systemd.

%package journal-gateway
Group: System/Servers
Summary: Journal Gateway Daemon
Requires: %name = %epoch:%version-%release

%description journal-gateway
This service provides access to the journal via HTTP and JSON.

%package -n journalctl
Group: System/Configuration/Boot and Init
Summary: Tool to query the journal from systemd.
Provides: /bin/journalctl
Provides: /sbin/journalctl
# File conflict with the releases before splitting out journalctl.
# 0:208-alt3 was the first release when the pkg was split in Sisyphus.
# The split pkgs for p7/t7 have lesser releases, so they couldn't coexist
# with newer journalctl due to this conflict. But Epoch helps us:
# there will be split pkgs for p7/t7 with Epoch 1, and hecne
# this conflict declaration won't apply!
Conflicts: %name < 0:208-alt3

%description -n journalctl
Tool to query the journal from systemd.

%package coredump
Group: System/Servers
Summary: systemd-coredump and coredumpctl utils
Requires: %name = %epoch:%version-%release

%description coredump
systemd-coredump and coredumpctl utils.

%package stateless
Group: System/Servers
Summary: systems that boot up with an empty /etc directory
Requires: %name = %epoch:%version-%release

%description stateless
This package contains:
 - systemd-sysusers util and unit
 - systemd-firstboot util and unit
 - ldconfig unit
 - systemd-update-done unit

systemd-sysusers tool creates system users and groups in /etc/passwd and
/etc/group, based on static declarative system user/group
definitions in /lib/sysusers.d/. This is useful to
enable factory resets and volatile systems that boot up with
an empty /etc directory, and thus need system users and
groups created during early boot. systemd now also ships
with two default sysusers.d/ files for the most basic
users and groups systemd and the core operating system
require.

%package -n bash-completion-%name
Summary: Bash completion for systemd utils
Group: Shells
BuildArch: noarch
Requires: bash-completion
Requires: %name = %epoch:%version-%release
# Not to loose it on upgrades after the split.
Requires: bash-completion-journalctl = %epoch:%version-%release

%description -n bash-completion-%name
Bash completion for %name.

%package -n zsh-completion-%name
Summary: Zsh completion for systemd utils
Group: Shells
BuildArch: noarch
Requires: %name = %epoch:%version-%release
Requires: zsh-completion-journalctl = %epoch:%version-%release

%description -n zsh-completion-%name
Zsh completion for %name.

%package -n bash-completion-journalctl
Summary: Bash completion for journalctl from systemd
Group: Shells
BuildArch: noarch
Requires: bash-completion
Requires: journalctl = %epoch:%version-%release
Conflicts: journalctl < %epoch:%version-%release
# File conflict with the releases before splitting out journalctl.
# 0:208-alt3 was the first release when the pkg was split in Sisyphus.
Conflicts: bash-completion-%name < 0:208-alt3

%description -n bash-completion-journalctl
Bash completion for journalctl from systemd.

%package -n zsh-completion-journalctl
Summary: Zsh completion for journalctl from systemd
Group: Shells
BuildArch: noarch
Requires: journalctl = %epoch:%version-%release
Conflicts: zsh-completion-%name < 1:214-alt14

%description -n zsh-completion-journalctl
Zsh completion for journalctl from systemd

%package -n python-module-%name
Summary: Python Bindings for systemd
License: LGPLv2+
Group: Development/Python
Requires: libsystemd = %epoch:%version-%release

%description -n python-module-%name
This package contains python binds for systemd APIs

%package -n udev
Group: System/Configuration/Hardware
Summary: udev - an userspace implementation of devfs
License: GPLv2+
PreReq: shadow-utils dmsetup kmod >= 15 util-linux >= 2.20 losetup >= 2.19.1
PreReq: udev-rules = %epoch:%version-%release
PreReq: udev-hwdb = %epoch:%version-%release
PreReq: systemd-utils = %epoch:%version-%release
Provides: hotplug = 2004_09_23-alt18
Obsoletes: hotplug
Conflicts: systemd < %epoch:%version-%release
Conflicts: util-linux <= 2.22-alt2
Conflicts: DeviceKit

%description -n udev
Starting with the 2.5 kernel, all physical and virtual devices in a
system are visible to userspace in a hierarchal fashion through
sysfs. /sbin/hotplug provides a notification to userspace when any
device is added or removed from the system. Using these two features,
a userspace implementation of a dynamic /dev is now possible that can
provide a very flexible device naming policy

%package -n udev-extras
Summary: Extra rules and tools for udev
Group: System/Configuration/Hardware
License: GPLv2+
Requires: udev = %epoch:%version-%release

%description -n udev-extras
The udev-extras package contains an additional rules and tools
to create and identify devices

%package -n udev-rules
Summary: Rule files for udev
Group: System/Configuration/Hardware
License: GPLv2+
Provides: %_sysconfdir/udev/rules.d /lib/udev/rules.d
Conflicts: udev < %epoch:%version-%release
BuildArch: noarch

%description -n udev-rules
This package contains the default set of rule files used by udev,
which control names and permission of device files in /dev.  Rule
files which have corresponding symlinks in /lib/udev/initramfs-rules.d
are also used by the make-initrd package when creating initramfs images

%package -n udev-hwdb
Summary: Hardware database for udev
Group: System/Configuration/Hardware
License: GPLv2+
Provides: %_sysconfdir/udev/hwdb.d /lib/udev/hwdb.d
Conflicts: udev < %epoch:%version-%release
BuildArch: noarch

%description -n udev-hwdb
This package contains internal hardware database for udev.

%package -n udev-rule-generator-cdrom
Summary: CD rule generator for udev
Group: System/Configuration/Hardware
License: GPLv2+
BuildArch: noarch
PreReq: udev-rules = %epoch:%version-%release
Provides: udev-rule-generator = %epoch:%version-%release
Obsoletes: udev-rule-generator < %epoch:%version-%release

%description -n udev-rule-generator-cdrom
This package contains CD rule generator for udev

%package -n udev-rule-generator-net
Summary: Net rule generator for udev
Group: System/Configuration/Hardware
License: GPLv2+
BuildArch: noarch
PreReq: udev-rules = %epoch:%version-%release

%description -n udev-rule-generator-net
This package contains Net rule generator for udev

%package -n bash-completion-udev
Summary: Bash completion for udev utils
Group: Shells
BuildArch: noarch
Requires: bash-completion
Requires: udev = %epoch:%version-%release

%description -n bash-completion-udev
Bash completion for udev.

%package -n zsh-completion-udev
Summary: Zsh completion for udev utils
Group: Shells
BuildArch: noarch
Requires: udev = %epoch:%version-%release
Conflicts: zsh-completion-%name < 1:214-alt14

%description -n zsh-completion-udev
Zsh completion for udev.

%package -n libudev1
Summary: Shared library to access udev device information
Group: System/Libraries
License: LGPLv2.1+
Conflicts: libudev < 0:181-alt5

%description -n libudev1
This package provides shared library to access udev device information

%package -n libudev-devel
Summary: Libraries and headers for libudev
Group: Development/C
License: LGPLv2.1+
Requires: libudev1 = %epoch:%version-%release

%description -n libudev-devel
Shared library and headers for libudev

%package -n libudev-devel-doc
Summary: Development documentaion for libudev
Group: Development/Documentation
BuildArch: noarch
Conflicts: libudev-devel < %version

%description -n libudev-devel-doc
This package provides development documentations for libudev.

%package -n libgudev
Summary: GObject bindings for libudev
Group: System/Libraries
Requires: libudev1 = %epoch:%version-%release

%description -n libgudev
This package provides shared library to access udev device information

%package -n libgudev-gir
Summary: GObject introspection data for the GUdev library
Group: System/Libraries
Requires: libgudev = %epoch:%version-%release

%description -n libgudev-gir
GObject introspection data for the GUdev library

%package -n libgudev-devel
Summary: Libraries and headers for libgudev
Group: Development/C
Requires: libgudev = %epoch:%version-%release

%description -n libgudev-devel
Shared library and headers for libgudev

%package -n libgudev-devel-doc
Summary: Development documentaion for gudev
Group: Development/Documentation
BuildArch: noarch
Conflicts: libgudev-devel < %version

%description -n libgudev-devel-doc
This package provides development documentations for gudev.

%package -n libgudev-gir-devel
Summary: GObject introspection devel data for the GUdev library
Group: System/Libraries
BuildArch: noarch
Requires: libgudev-gir = %epoch:%version-%release libgudev-devel = %epoch:%version-%release

%description -n libgudev-gir-devel
GObject introspection devel data for the GUdev library

%prep
%setup -q
%patch1 -p1
%patch2 -p1

%build
export QUOTAON="/sbin/quotaon"
export QUOTACHECK="/sbin/quotacheck"
export KILL="/bin/kill"
export KMOD="/bin/kmod"
export KEXEC="/sbin/kexec"
export CHKCONFIG="/sbin/chkconfig"

gtkdocize --docdir docs/
intltoolize --force --automake
%autoreconf
%configure  \
	--disable-static \
	%{subst_with python} \
	--with-rootprefix="" \
	--with-rootlibdir=/%_lib \
	--with-pamlibdir=/%_lib/security \
	--enable-split-usr \
	--with-sysvinit-path=/etc/rc.d/init.d \
	--with-sysvrcnd-path=/etc/rc.d \
	--with-rc-local-script-path-start=/etc/rc.d/rc.local \
	--with-debug-shell=/bin/bash \
	--enable-compat-libs \
	--with-kbd-loadkeys=/bin/loadkeys \
	--with-kbd-setfont=/bin/setfont \
	--with-telinit=/sbin/telinit \
	--with-system-uid-max=499 \
	--with-system-gid-max=499 \
	--with-tty-gid=5 \
	%{subst_enable elfutils} \
	%{subst_enable xz} \
	%{subst_enable lz4} \
	%{subst_enable libcryptsetup} \
	%{subst_enable logind} \
	%{subst_enable vconsole} \
	%{subst_enable quotacheck} \
	%{subst_enable randomseed} \
	%{subst_enable coredump} \
	%{subst_enable smack} \
	%{subst_enable gcrypt} \
	%{subst_enable qrencode} \
	%{subst_enable microhttpd} \
	%{subst_enable gnutls} \
	%{subst_enable libcurl} \
	%{subst_enable libidn} \
	%{subst_enable bootchart} \
	%{subst_enable polkit} \
	%{subst_enable efi} \
	%{subst_enable networkd} \
	%{subst_enable resolved} \
	%{subst_enable timesyncd} \
	%{subst_enable sysusers} \
	%{subst_enable ldconfig} \
	%{subst_enable firstboot} \
	%{subst_enable terminal} \
	%{subst_enable kdbus} \
	%{subst_enable seccomp} \
	%{subst_enable ima} \
	%{subst_enable selinux} \
	%{subst_enable apparmor} \
	%{subst_enable utmp} \
	%{?_enable_gtk_doc:--enable-gtk-doc} \
	--enable-introspection

%make_build GCC_COLORS="" V=1

%install
%make DESTDIR=%buildroot install

%find_lang %name

# Make sure these directories are properly owned
mkdir -p %buildroot%_unitdir/{basic,default,dbus,graphical,poweroff,rescue,reboot}.target.wants

ln -s rc-local.service %buildroot%_unitdir/local.service
install -m644 %SOURCE4 %buildroot%_unitdir/altlinux-openresolv.path
install -m644 %SOURCE5 %buildroot%_unitdir/altlinux-openresolv.service
install -m644 %SOURCE6 %buildroot%_unitdir/altlinux-libresolv.path
ln -s ../altlinux-libresolv.path %buildroot%_unitdir/multi-user.target.wants
install -m644 %SOURCE7 %buildroot%_unitdir/altlinux-libresolv.service
ln -s ../altlinux-libresolv.service %buildroot%_unitdir/multi-user.target.wants
install -m644 %SOURCE8 %buildroot%_unitdir/altlinux-clock-setup.service
ln -s ../altlinux-clock-setup.service %buildroot%_unitdir/sysinit.target.wants
ln -s altlinux-clock-setup.service %buildroot%_unitdir/clock.service
install -m644 %SOURCE16 %buildroot%_unitdir/altlinux-kmsg-loglevel.service
ln -s ../altlinux-kmsg-loglevel.service %buildroot%_unitdir/sysinit.target.wants
install -m755 %SOURCE18 %buildroot/lib/systemd/altlinux-save-dmesg
install -m644 %SOURCE17 %buildroot%_unitdir/altlinux-save-dmesg.service
ln -s ../altlinux-save-dmesg.service %buildroot%_unitdir/basic.target.wants
install -m644 %SOURCE27 %buildroot%_unitdir/altlinux-first_time.service
ln -s ../altlinux-first_time.service %buildroot%_unitdir/basic.target.wants
ln -s systemd-random-seed.service %buildroot%_unitdir/random.service
ln -s systemd-reboot.service %buildroot%_unitdir/reboot.service
ln -s systemd-halt.service %buildroot%_unitdir/halt.service

# restore bind-mounts /var/run -> run and /var/lock -> /run/lock
# we don't have those directories symlinked
install -m644 %SOURCE23 %buildroot%_unitdir/var-lock.mount
install -m644 %SOURCE24 %buildroot%_unitdir/var-run.mount
ln -r -s %buildroot%_unitdir/var-lock.mount %buildroot%_unitdir/local-fs.target.wants
ln -r -s %buildroot%_unitdir/var-run.mount %buildroot%_unitdir/local-fs.target.wants

# turn off tmp.mount by default (ALT#29066)
rm -f %buildroot%_unitdir/tmp.mount
rm -f %buildroot%_unitdir/local-fs.target.wants/tmp.mount

install -m755 %SOURCE15 %buildroot/lib/systemd/systemd-logind-launch

find %buildroot \( -name '*.a' -o -name '*.la' \) -exec rm {} \;
mkdir -p %buildroot/{sbin,bin}
ln -r -s %buildroot/lib/systemd/systemd %buildroot/sbin/init
ln -r -s %buildroot/lib/systemd/systemd %buildroot/sbin/systemd
ln -r -s %buildroot/sbin/systemctl %buildroot/sbin/reboot
ln -r -s %buildroot/sbin/systemctl %buildroot/sbin/halt
ln -r -s %buildroot/sbin/systemctl %buildroot/sbin/poweroff
ln -r -s %buildroot/sbin/systemctl %buildroot/sbin/shutdown
ln -r -s %buildroot/sbin/systemctl %buildroot/sbin/telinit
ln -r -s %buildroot/sbin/systemctl %buildroot/sbin/runlevel

ln -r -s %buildroot/lib/systemd/systemd-{binfmt,modules-load,sysctl} %buildroot/sbin/
ln -r -s %buildroot/sbin/systemctl %buildroot/bin/
# for compatibility with older systemd pkgs which expected it at /bin/:
ln -r -s %buildroot/sbin/journalctl %buildroot/bin/

rm -rf %buildroot%_docdir/systemd

# add defaults services
ln -r -s %buildroot%_unitdir/remote-fs.target %buildroot%_unitdir/multi-user.target.wants
ln -r -s %buildroot%_unitdir/systemd-quotacheck.service %buildroot%_unitdir/local-fs.target.wants
ln -r -s %buildroot%_unitdir/quotaon.service %buildroot%_unitdir/local-fs.target.wants

# create drop-in to prevent tty1 to be cleared
mkdir -p %buildroot%_unitdir/getty@tty1.service.d
cat > %buildroot%_unitdir/getty@tty1.service.d/noclear.conf << EOF
[Service]
# ensure tty1 isn't cleared
TTYVTDisallocate=no
EOF

# Temporary workaround for update runlevel
ln -r -s %buildroot%_unitdir/systemd-update-utmp-runlevel.service %buildroot%_unitdir/poweroff.target.wants/
ln -r -s %buildroot%_unitdir/systemd-update-utmp-runlevel.service %buildroot%_unitdir/rescue.target.wants/
ln -r -s %buildroot%_unitdir/systemd-update-utmp-runlevel.service %buildroot%_unitdir/multi-user.target.wants/
ln -r -s %buildroot%_unitdir/systemd-update-utmp-runlevel.service %buildroot%_unitdir/graphical.target.wants/
ln -r -s %buildroot%_unitdir/systemd-update-utmp-runlevel.service %buildroot%_unitdir/reboot.target.wants/

# don't enable wall ask password service, it spams every console
rm -f %buildroot%_unitdir/multi-user.target.wants/systemd-ask-password-wall.path

# disable legacy services
ln -s /dev/null %buildroot%_unitdir/fbsetfont.service
ln -s /dev/null %buildroot%_unitdir/keytable.service
ln -s /dev/null %buildroot%_unitdir/killall.service
ln -s /dev/null %buildroot%_unitdir/single.service
ln -s /dev/null %buildroot%_unitdir/netfs.service

# Use mingetty as default
#%__subst 's,/sbin/agetty,/sbin/mingetty,'  %buildroot%_unitdir/getty@.service

# We create all wants links manually at installation time to make sure
# they are not owned and hence overriden by rpm after the used deleted
# them.
rm -r %buildroot%_sysconfdir/systemd/system/*.target.wants
rm -f %buildroot%_sysconfdir/systemd/system/display-manager.service

# And the default symlink we generate automatically based on inittab
rm -f %buildroot%_sysconfdir/systemd/system/default.target

# create modules.conf as a symlink to /etc/modules
mkdir -p %buildroot/lib/modules-load.d
mkdir -p %buildroot%_sysconfdir/modules-load.d
ln -r -s %buildroot%_sysconfdir/modules %buildroot%_sysconfdir/modules-load.d/modules.conf

# create /etc/sysctl.d/99-sysctl.conf as a symlink to /etc/sysctl.conf
mkdir -p %buildroot%_sysconfdir/sysctl.d
ln -r -s %buildroot%_sysconfdir/sysctl.conf %buildroot%_sysconfdir/sysctl.d/99-sysctl.conf

# Make sure directories in /var exist
mkdir -p %buildroot%_localstatedir/lib/systemd/coredump
mkdir -p %buildroot%_localstatedir/lib/systemd/catalog
mkdir -p %buildroot%_localstatedir/lib/systemd/backlight
mkdir -p %buildroot%_localstatedir/lib/systemd/rfkill
mkdir -p %buildroot%_localstatedir/log/journal
touch %buildroot%_localstatedir/lib/systemd/catalog/database
touch %buildroot%_sysconfdir/udev/hwdb.bin
touch %buildroot%_localstatedir/lib/systemd/random-seed
touch %buildroot%_localstatedir/lib/systemd/clock

# Add completion for bash3
mkdir -p %buildroot%_sysconfdir/bash_completion.d
rm -f %buildroot%_sysconfdir/bash_completion.d/*
rm -f %buildroot%_datadir/bash-completion/completions/*
install -m644 %SOURCE51 %buildroot%_sysconfdir/bash_completion.d/hostnamectl
install -m644 %SOURCE52 %buildroot%_sysconfdir/bash_completion.d/journalctl
install -m644 %SOURCE53 %buildroot%_sysconfdir/bash_completion.d/localectl
install -m644 %SOURCE54 %buildroot%_sysconfdir/bash_completion.d/loginctl
install -m644 %SOURCE55 %buildroot%_sysconfdir/bash_completion.d/systemctl
install -m644 %SOURCE56 %buildroot%_sysconfdir/bash_completion.d/systemd-analyze
install -m644 %SOURCE57 %buildroot%_sysconfdir/bash_completion.d/coredumpctl
install -m644 %SOURCE58 %buildroot%_sysconfdir/bash_completion.d/timedatectl
install -m644 %SOURCE59 %buildroot%_sysconfdir/bash_completion.d/udevadm
install -m644 %SOURCE60 %buildroot%_sysconfdir/bash_completion.d/bootctl
install -m644 %SOURCE61 %buildroot%_sysconfdir/bash_completion.d/busctl
install -m644 %SOURCE62 %buildroot%_sysconfdir/bash_completion.d/machinectl
install -m644 %SOURCE63 %buildroot%_sysconfdir/bash_completion.d/systemd-delta
install -m644 %SOURCE64 %buildroot%_sysconfdir/bash_completion.d/systemd-cat
install -m644 %SOURCE65 %buildroot%_sysconfdir/bash_completion.d/systemd-cgls
install -m644 %SOURCE66 %buildroot%_sysconfdir/bash_completion.d/systemd-cgtop
install -m644 %SOURCE67 %buildroot%_sysconfdir/bash_completion.d/systemd-detect-virt

# Make sure the ghost-ing below works
touch %buildroot%_sysconfdir/systemd/system/runlevel2.target
touch %buildroot%_sysconfdir/systemd/system/runlevel3.target
touch %buildroot%_sysconfdir/systemd/system/runlevel4.target
touch %buildroot%_sysconfdir/systemd/system/runlevel5.target


# Create new-style configuration files so that we can ghost-own them
touch %buildroot%_sysconfdir/hostname
touch %buildroot%_sysconfdir/vconsole.conf
touch %buildroot%_sysconfdir/locale.conf
touch %buildroot%_sysconfdir/machine-info

# fix pam.d/systemd-user for ALTLinux
%__subst 's,system-auth,common-login,g' %buildroot%_sysconfdir/pam.d/systemd-user

# Install ALTLinux default preset policy
mkdir -p %buildroot/lib/systemd/system-preset
mkdir -p %buildroot%_sysconfdir/systemd/system-preset
mkdir -p %buildroot/lib/systemd/user-preset
mkdir -p %buildroot%_sysconfdir/systemd/user-preset
mkdir -p %buildroot/usr/lib/systemd/user-preset
install -m 0644 %SOURCE34 %buildroot/lib/systemd/system-preset/
install -m 0644 %SOURCE35 %buildroot/lib/systemd/system-preset/
install -m 0644 %SOURCE36 %buildroot/lib/systemd/system-preset/
install -m 0644 %SOURCE37 %buildroot/lib/systemd/system-preset/
install -m 0644 %SOURCE38 %buildroot/lib/systemd/system-preset/

# The following services are currently installed by initscripts
#pushd %buildroot%_unitdir/graphical.target.wants && {
#	rm -f display-manager.service
#	rm -f dm.service
#popd
#}

# Set up the pager to make it generally more useful
mkdir -p %buildroot%_sysconfdir/profile.d
cat > %buildroot%_sysconfdir/profile.d/systemd.sh << EOF
export SYSTEMD_PAGER="/usr/bin/less -FR"
EOF
chmod 755 %buildroot%_sysconfdir/profile.d/systemd.sh

install -m644 %SOURCE30 %buildroot/lib/sysctl.d/49-coredump-null.conf
# rpm posttrans filetriggers
install -pD -m755 %SOURCE28 %buildroot%_rpmlibdir/systemd-tmpfiles.filetrigger
install -pD -m755 %SOURCE33 %buildroot%_rpmlibdir/udev.filetrigger

cat >>%buildroot/lib/sysctl.d/50-default.conf <<EOF
# Indicates the amount of address space which a user process will be
# restricted from mmaping.  Since kernel null dereference bugs could
# accidentally operate based on the information in the first couple of
# pages of memory userspace processes should not be allowed to write to
# them.  By default, this value in kernel is set to 0 and no protections
# will be enforced by the security module.  Setting this value to
# something >= 32k will allow the vast majority of applications to work
# correctly and provide defense in depth against future potential kernel
# bugs.  This value is somewhat architecture-dependent, though.
# Recommended default for x86_64 is 65536.
vm.mmap_min_addr = %mmap_min_addr
EOF

#######
# UDEV
#######
mkdir -p %buildroot%_initdir
install -p -m755 %SOURCE19 %buildroot%_initdir/udevd
#install -p -m755 %SOURCE20 %buildroot%_initdir/udevd-final

ln -s systemd-udevd.service %buildroot%_unitdir/udevd.service
#ln -s systemd-udev-settle.service %buildroot%_unitdir/udevd-final.service

# compatibility symlinks to udevd binary
ln -r -s %buildroot/lib/systemd/systemd-udevd %buildroot/lib/udev/udevd
ln -r -s %buildroot/lib/systemd/systemd-udevd %buildroot/sbin/udevd

install -p -m644 %SOURCE21 %buildroot/lib/udev/rules.d/40-ignore-remove.rules
install -p -m644 %SOURCE22 %buildroot%_sysconfdir/scsi_id.config

cat >>%buildroot%_sysconfdir/udev/udev.conf <<EOF
# Whether to mount a tmpfs filesystem to \$udev_root
udev_tmpfs="1"

# tmpfs options. Note that size shouldn't be less than several
# megabytes due to insane format of current udev database
# (in /dev/.udevdb)
tmpfs_options="size=5m"
EOF

mkdir -p %buildroot/lib/udev/devices

# Install symlinks for rules which are needed in initramfs
mkdir -p %buildroot/lib/udev/initramfs-rules.d
for f in \
	50-udev-default.rules \
	60-persistent-storage.rules \
	80-drivers.rules
do
	ln -s ../rules.d/"$f" \
		%buildroot/lib/udev/initramfs-rules.d/
done
# Create ghost files
touch %buildroot%_sysconfdir/udev/rules.d/70-persistent-net.rules
touch %buildroot%_sysconfdir/udev/rules.d/70-persistent-cd.rules
touch %buildroot%_sysconfdir/udev/hwdb.bin

# udev rule generator
install -p -m644 %SOURCE41 %buildroot/lib/udev/
install -p -m755 %SOURCE42 %buildroot/lib/udev/
install -p -m644 %SOURCE43 %buildroot/lib/udev/rules.d/
install -p -m755 %SOURCE44 %buildroot/lib/udev/
install -p -m644 %SOURCE45 %buildroot/lib/udev/rules.d/
ln -s /dev/null %buildroot%_sysconfdir/udev/rules.d/80-net-setup-link.rules


echo ".so man8/systemd-udevd.8" > %buildroot%_man8dir/udevd.8

install -p -m644 %SOURCE31 %buildroot%_sysconfdir/udev/rules.d/

%pre
%_sbindir/groupadd -r -f systemd-journal >/dev/null 2>&1 ||:

%_sbindir/groupadd -r -f systemd-bus-proxy >/dev/null 2>&1 ||:
%_sbindir/useradd -g systemd-bus-proxy -c 'systemd Bus Proxy' \
    -d /var/empty -s /dev/null -r -l -M systemd-bus-proxy >/dev/null 2>&1 ||:

%post
/sbin/systemctl daemon-reexec >/dev/null 2>&1 || :
/sbin/journalctl --update-catalog >/dev/null 2>&1 || :

# Move old stuff around in /var/lib
[ -d %_localstatedir/lib/systemd/random-seed ] && rm -rf %_localstatedir/lib/systemd/random-seed >/dev/null 2>&1 || :
[ -e %_localstatedir/lib/random-seed ] && mv %_localstatedir/lib/random-seed %_localstatedir/lib/systemd/random-seed >/dev/null 2>&1 || :
[ -e %_localstatedir/lib/backlight ] && mv %_localstatedir/lib/backlight %_localstatedir/lib/systemd/backlight >/dev/null 2>&1 || :

/lib/systemd/systemd-random-seed save >/dev/null 2>&1 || :

# rm symlinks for network.service
[ -L %_sysconfdir/systemd/system/network.target.wants/network.service ] && rm -f %_sysconfdir/systemd/system/network.target.wants/network.service  >/dev/null 2>&1 || :
[ -L %_sysconfdir/systemd/system/multi-user.target.wants/network.service ] && rm -f %_sysconfdir/systemd/system/multi-user.target.wants/network.service  >/dev/null 2>&1 || :

# rm symlinks for prefdm.service
[ -L %_sysconfdir/systemd/system/graphical.target.wants/prefdm.service ] && rm -f %_sysconfdir/systemd/system/graphical.target.wants/prefdm.service  >/dev/null 2>&1 || :

# Make sure new journal files will be owned by the "systemd-journal" group
chgrp systemd-journal /run/log/journal/ /run/log/journal/`cat /etc/machine-id 2> /dev/null` %_localstatedir/log/journal/ %_localstatedir/log/journal/`cat /etc/machine-id 2> /dev/null` >/dev/null 2>&1 || :
chmod g+s  /run/log/journal/ /run/log/journal/`cat /etc/machine-id 2> /dev/null` %_localstatedir/log/journal/ %_localstatedir/log/journal/`cat /etc/machine-id 2> /dev/null` >/dev/null 2>&1 || :

# Apply ACL to the journal directory
/usr/bin/setfacl -Rnm g:wheel:rx,d:g:wheel:rx,g:adm:rx,d:g:adm:rx %_localstatedir/log/journal/ >/dev/null 2>&1 || :

if [ $1 -eq 1 ] ; then
        # Enable the services we install by default
        /sbin/systemctl preset \
                remote-fs.target \
                getty@.service \
                serial-getty@.service \
                console-getty.service \
                console-shell.service \
                debug-shell.service \
                 >/dev/null 2>&1 || :
fi

%postun
if [ $1 -ge 1 ] ; then
	/sbin/systemctl daemon-reload > /dev/null 2>&1 || :
fi

%preun
if [ $1 -eq 0 ] ; then
        /sbin/systemctl disable \
                remote-fs.target \
                getty@.service \
                serial-getty@.service \
                console-getty.service \
                console-shell.service \
                debug-shell.service \
                 >/dev/null 2>&1 || :

        rm -f /etc/systemd/system/default.target > /dev/null 2>&1 || :
fi

%post utils
/sbin/systemd-machine-id-setup >/dev/null 2>&1 || :

%if_enabled networkd
%pre networkd
%_sbindir/groupadd -r -f systemd-network >/dev/null 2>&1 ||:
%_sbindir/useradd -g systemd-network -c 'systemd Network Management' \
    -d /var/empty -s /dev/null -r -l -M systemd-network >/dev/null 2>&1 ||:

%_sbindir/groupadd -r -f systemd-resolve >/dev/null 2>&1 ||:
%_sbindir/useradd -g systemd-resolve -c 'systemd Resolver' \
    -d /var/empty -s /dev/null -r -l -M systemd-resolve >/dev/null 2>&1 ||:

%post networkd
if [ $1 -eq 1 ] ; then
        # Enable the services we install by default
        /sbin/systemctl preset \
                systemd-networkd.service \
                systemd-networkd-wait-online.service \
                systemd-resolved.service \
                altlinux-openresolv.service \
                 >/dev/null 2>&1 || :
fi

%preun networkd
if [ $1 -eq 0 ] ; then
        /sbin/systemctl disable \
                systemd-networkd.service \
                systemd-networkd-wait-online.service \
                systemd-resolved.service \
                altlinux-openresolv.service \
                 >/dev/null 2>&1 || :
fi
%endif

%if_enabled timesyncd
%pre timesyncd
%_sbindir/groupadd -r -f systemd-timesync >/dev/null 2>&1 ||:
%_sbindir/useradd -g systemd-timesync -c 'systemd Time Synchronization' \
    -d /var/empty -s /dev/null -r -l -M systemd-timesync >/dev/null 2>&1 ||:

%post timesyncd
if [ $1 -eq 1 ] ; then
        # Enable the services we install by default
        /sbin/systemctl preset \
                systemd-timesyncd.service \
                 >/dev/null 2>&1 || :
fi

%preun timesyncd
if [ $1 -eq 0 ] ; then
        /sbin/systemctl disable \
                systemd-timesyncd.service \
                 >/dev/null 2>&1 || :
fi
%endif

%post -n libnss-myhostname
if [ "$1" = "1" ]; then
    grep -q '^hosts:[[:blank:]].\+myhostname' \
    /etc/nsswitch.conf || \
    sed -i.rpmorig 's/^\(hosts:.\+\)$/\1 myhostname/' /etc/nsswitch.conf >/dev/null 2>&1 || :
fi
update_chrooted all

%postun -n libnss-myhostname
if [ "$1" = "0" ]; then
    grep -q '^hosts:[[:blank:]].\+myhostname' \
        /etc/nsswitch.conf && \
    sed -i 's/ myhostname//' /etc/nsswitch.conf
fi
update_chrooted all

%if_enabled microhttpd
%pre journal-gateway
%_sbindir/groupadd -r -f systemd-journal-gateway ||:
%_sbindir/useradd -g systemd-journal-gateway -c 'Journal Gateway' \
    -d %_localstatedir/log/journal -s /dev/null -r -l systemd-journal-gateway >/dev/null 2>&1 ||:

%_sbindir/groupadd -r -f systemd-journal-remote ||:
%_sbindir/useradd -g systemd-journal-gateway -c 'Journal Remote' \
    -d %_localstatedir/log/journal/remote -s /dev/null -r -l systemd-journal-remote >/dev/null 2>&1 ||:

%if_enabled libcurl
%_sbindir/groupadd -r -f systemd-journal-upload ||:
%_sbindir/useradd -g systemd-journal-upload -c 'Journal Upload' \
    -d %_localstatedir/log/journal/upload -s /dev/null -r -l systemd-journal-upload >/dev/null 2>&1 ||:
%endif

%post journal-gateway
%post_service systemd-journal-gatewayd
%post_service systemd-journal-remote
%if_enabled libcurl
%post_service systemd-journal-upload
%endif

%preun journal-gateway
%preun_service systemd-journal-gatewayd
%preun_service systemd-journal-remote
%if_enabled libcurl
%preun_service systemd-journal-upload
%endif

%endif

%pre -n udev
%_sbindir/groupadd -r -f cdrom >/dev/null 2>&1 ||:
%_sbindir/groupadd -r -f tape >/dev/null 2>&1 ||:
%_sbindir/groupadd -r -f dialout >/dev/null 2>&1 ||:
%_sbindir/groupadd -r -f input >/dev/null 2>&1 ||:
%_sbindir/groupadd -r -f video >/dev/null 2>&1 ||:

%post -n udev
%post_service udevd
/sbin/udevadm hwdb --update >/dev/null 2>&1 || :

%preun -n udev
%preun_service udevd

%files -f %name.lang
%dir %_sysconfdir/systemd/system
%dir %_sysconfdir/systemd/user

%_sysconfdir/profile.d/systemd.sh

/lib/tmpfiles.d/systemd-nologin.conf
/lib/tmpfiles.d/systemd.conf

%_sysconfdir/xdg/systemd

%config(noreplace) %_sysconfdir/systemd/bootchart.conf
%config(noreplace) %_sysconfdir/systemd/journald.conf
%config(noreplace) %_sysconfdir/systemd/system.conf
%config(noreplace) %_sysconfdir/systemd/user.conf
%config(noreplace) %_sysconfdir/dbus-1/system.d/org.freedesktop.systemd1.conf

%ghost %config(noreplace) %_sysconfdir/systemd/system/runlevel2.target
%ghost %config(noreplace) %_sysconfdir/systemd/system/runlevel3.target
%ghost %config(noreplace) %_sysconfdir/systemd/system/runlevel4.target
%ghost %config(noreplace) %_sysconfdir/systemd/system/runlevel5.target

/sbin/systemctl
/bin/systemctl
/sbin/systemd
/sbin/systemd-ask-password
/sbin/systemd-inhibit

/sbin/systemd-notify
/sbin/systemd-tty-ask-password-agent
%_bindir/bootctl
%_bindir/busctl
%_bindir/systemd-cat
%_bindir/systemd-cgls
%_bindir/systemd-cgtop
%_bindir/systemd-delta
%_bindir/systemd-detect-virt
%_bindir/systemd-nspawn
%_bindir/systemd-path
%_bindir/systemd-run
%_bindir/systemd-stdio-bridge
/lib/systemd/systemd
/lib/systemd/systemd-ac-power
/lib/systemd/systemd-activate
/lib/systemd/systemd-bootchart
/lib/systemd/systemd-bus-proxyd
/lib/systemd/systemd-cgroups-agent
/lib/systemd/systemd-cryptsetup
/lib/systemd/systemd-fsck
/lib/systemd/systemd-initctl
/lib/systemd/systemd-journald
/lib/systemd/systemd-quotacheck
/lib/systemd/systemd-random-seed
/lib/systemd/systemd-remount-fs
/lib/systemd/systemd-reply-password
/lib/systemd/systemd-rfkill
/lib/systemd/systemd-shutdown
/lib/systemd/systemd-shutdownd
/lib/systemd/systemd-sleep
/lib/systemd/systemd-socket-proxyd
/lib/systemd/systemd-update-done
/lib/systemd/systemd-update-utmp
/lib/systemd/systemd-user-sessions
/lib/systemd/systemd-vconsole-setup
/lib/systemd/altlinux-save-dmesg

%dir %_unitdir
%_unitdir/*

%if_enabled networkd
%exclude %_unitdir/*networkd*
%exclude %_unitdir/*resolv*
%exclude %_unitdir/*/*resolv*
%endif
%if_enabled timesyncd
%exclude %_unitdir/*timesyncd*
%endif
%if_enabled microhttpd
%exclude %_unitdir/systemd-journal-gatewayd*
%endif
%if_enabled libcurl
%exclude %_unitdir/systemd-journal-upload*
%endif
%exclude %_unitdir/*udev*
%exclude %_unitdir/*/*udev*

%_man1dir/bootctl.*
%_man1dir/busctl.*
%_man1dir/systemctl.*
%_mandir/*/systemd-ask-password*
%_mandir/*/*bootchart.*
%_man1dir/systemd-cat.*
%_man1dir/systemd-cgls.*
%_man1dir/systemd-cgtop.*
%_man1dir/systemd-delta.*
%_man1dir/systemd-detect-virt.*
%_man1dir/systemd-inhibit.*
%_man1dir/systemd-notify.*
%_man1dir/systemd-nspawn.*
%_man1dir/systemd-path.*
%_man1dir/systemd-run.*
%_mandir/*/systemd-tty-ask-password*
%_man1dir/systemd.*
%_man5dir/crypttab*
%_mandir/*/*cryptsetup*
%_mandir/*/*journald*
%_man5dir/localtime*
%_man5dir/os-release*
%_man5dir/systemd-sleep.conf*
%_man5dir/systemd-system.conf*
%_man5dir/systemd-user.conf*
%_man5dir/systemd.automount*
%_man5dir/systemd.exec*
%_man5dir/systemd.kill*
%_man5dir/systemd.mount*
%_man5dir/systemd.path*
%_man5dir/systemd.preset*
%_man5dir/systemd.resource-control*
%_man5dir/systemd.scope*
%_man5dir/systemd.service*
%_man5dir/systemd.slice*
%_man5dir/systemd.snapshot*
%_man5dir/systemd.socket*
%_man5dir/systemd.swap*
%_man5dir/systemd.target*
%_man5dir/systemd.timer*
%_man5dir/systemd.unit*
%_mandir/*/*vconsole*

%_man8dir/systemd-activate*
%_man8dir/systemd-debug-generator*
%_man8dir/systemd-efi-boot-generator*
%_man8dir/systemd-fsck*
%_man8dir/systemd-fstab-generator*
%_man8dir/systemd-getty-generator*
%_man8dir/systemd-gpt-auto-generator*
%_man8dir/systemd-hibernate*
%_man8dir/systemd*sleep*
%_man8dir/systemd-initctl*
%_man8dir/systemd-kexec*
%_man8dir/systemd-quota*
%_man8dir/systemd-random-seed*
%_man8dir/systemd-remount*
%_man8dir/systemd-rfkill*
%_man8dir/systemd-socket-proxyd*
%_man8dir/systemd-suspend*
%_man8dir/systemd-system-update-generator*
%_man8dir/systemd-update-utmp*
%_man8dir/systemd-user-sessions*
%_man8dir/systemd-update-done*
%_man8dir/systemd-halt*
%_man8dir/systemd-reboot*
%_man8dir/systemd-shutdown*
%_man8dir/systemd-poweroff*

%exclude %_mandir/*/systemd-firstboot*
%exclude %_mandir/*/*sysusers*
%exclude %_datadir/factory
%exclude /lib/tmpfiles.d/etc.conf

/usr/lib/systemd
/lib/systemd/system-generators

%dir /lib/systemd/system-preset
/lib/systemd/system-preset/85-display-manager.preset
/lib/systemd/system-preset/90-default.preset
/lib/systemd/system-preset/90-systemd.preset
/lib/systemd/system-preset/99-default-disable.preset


/lib/udev/rules.d/70-uaccess.rules
/lib/udev/rules.d/71-seat.rules
/lib/udev/rules.d/73-seat-late.rules
/lib/udev/rules.d/99-systemd.rules
%_man7dir/*
%exclude %_man7dir/udev*

%dir %_datadir/systemd
%_datadir/systemd/kbd-model-map
%_datadir/dbus-1/system-services/org.freedesktop.systemd1.service
%_datadir/dbus-1/services/org.freedesktop.systemd1.service

%if_enabled polkit
%_datadir/polkit-1/actions/org.freedesktop.systemd1.policy
%endif

%dir %_localstatedir/log/journal
%dir %_localstatedir/lib/systemd
%dir %_localstatedir/lib/systemd/catalog
%ghost %_localstatedir/lib/systemd/catalog/database
%ghost %_localstatedir/lib/systemd/random-seed
%ghost %_localstatedir/lib/systemd/clock

# %%_docdir/systemd
%doc DISTRO_PORTING LICENSE.LGPL2.1 README NEWS TODO
%_localstatedir/log/README
# may be need adapt for ALTLinux?
%exclude /usr/lib/kernel
%exclude %_bindir/kernel-install
%exclude %_man8dir/kernel-install.*

%files -n libsystemd
/%_lib/*.so.*
%exclude /%_lib/*udev*.so.*
%exclude /%_lib/libnss*

%files -n libsystemd-devel
%_libdir/*.so
%exclude %_libdir/*udev*.so
%_pkgconfigdir/*.pc
%exclude %_pkgconfigdir/*udev*.pc
%_includedir/systemd

%files -n libnss-myhostname
/%_lib/libnss_myhostname.so.*
%_man8dir/nss-myhostname.*

%files -n libnss-mymachines
/%_lib/libnss_mymachines.so.*

%files -n libnss-resolve
/%_lib/libnss_resolve.so.*

%files -n pam_%name
%config %_sysconfdir/pam.d/systemd-user
/%_lib/security/pam_systemd.so
%_man8dir/pam_systemd*

%files devel
%doc LICENSE.LGPL2.1 LICENSE.MIT
%_datadir/pkgconfig/systemd.pc
%_man3dir/*

%files sysvinit
/sbin/init
/sbin/reboot
/sbin/halt
/sbin/poweroff
/sbin/shutdown
/sbin/telinit
/sbin/runlevel
%_man1dir/init*
%_man8dir/halt*
%_man8dir/reboot*
%_man8dir/shutdown*
%_man8dir/poweroff*
%_man8dir/telinit*
%_man8dir/runlevel*
%_initdir/README

%files utils
%dir /lib/systemd

/sbin/systemd-escape
%_mandir/*/*escape*

/sbin/systemd-tmpfiles
%_mandir/*/*tmpfiles*
%_rpmlibdir/systemd-tmpfiles.filetrigger
/lib/tmpfiles.d/legacy.conf
/lib/tmpfiles.d/x11.conf
/lib/tmpfiles.d/tmp.conf
/lib/tmpfiles.d/var.conf


/lib/systemd/systemd-binfmt
/sbin/systemd-binfmt
%_mandir/*/*binfmt*

/lib/systemd/systemd-modules-load
%_sysconfdir/modules-load.d/modules.conf
/sbin/systemd-modules-load
%_mandir/*/*modules-load*

/lib/systemd/systemd-sysctl
/sbin/systemd-sysctl
%config(noreplace) %_sysconfdir/sysctl.d/99-sysctl.conf
/lib/sysctl.d/50-default.conf
/lib/sysctl.d/49-coredump-null.conf
%_mandir/*/*sysctl*

/lib/systemd/systemd-backlight
%_mandir/*/*backlight*
%ghost %dir %_localstatedir/lib/systemd/backlight

/sbin/systemd-machine-id-setup
%ghost %config(noreplace) %_sysconfdir/machine-info
%ghost %config(noreplace) %_sysconfdir/hostname
%ghost %config(noreplace) %_sysconfdir/vconsole.conf
%ghost %config(noreplace) %_sysconfdir/locale.conf

%files services
%dir %_sysconfdir/systemd
%config(noreplace) %_sysconfdir/systemd/logind.conf
%config(noreplace) %_sysconfdir/dbus-1/system.d/org.freedesktop.*.conf
%exclude %_sysconfdir/dbus-1/system.d/org.freedesktop.systemd1.conf
%_datadir/dbus-1/system-services/org.freedesktop.*.service
%exclude %_datadir/dbus-1/system-services/org.freedesktop.systemd1.service
%exclude %_datadir/dbus-1/system-services/org.freedesktop.resolve1.service
%if_enabled polkit
%_datadir/polkit-1/actions/*.policy
%exclude %_datadir/polkit-1/actions/org.freedesktop.systemd1.policy
%endif


/sbin/loginctl
/lib/systemd/systemd-logind
/lib/systemd/systemd-logind-launch
/sbin/machinectl
/lib/systemd/systemd-machined
%_bindir/hostnamectl
/lib/systemd/systemd-hostnamed
%_bindir/localectl
/lib/systemd/systemd-localed
%_bindir/timedatectl
/lib/systemd/systemd-timedated

%_mandir/*/*login*
%exclude %_man3dir/*
%_mandir/*/*machine*
%_mandir/*/*hostname*
%exclude %_mandir/*/nss-myhostname*
%_mandir/*/*locale*
%_mandir/*/*timedate*

%if_enabled networkd
%files networkd
/sbin/networkctl
%config(noreplace) %_sysconfdir/systemd/resolved.conf
/lib/systemd/system-preset/85-networkd.preset
/lib/systemd/systemd-networkd
/lib/systemd/systemd-networkd-wait-online
/lib/systemd/systemd-resolved
/lib/systemd/systemd-resolve-host
/lib/tmpfiles.d/systemd-network.conf
%_unitdir/systemd-networkd.service
%_unitdir/systemd-networkd-wait-online.service
%_unitdir/*resolv*
%_unitdir/*/*resolv*
/lib/systemd/network/*.network
%_mandir/*/*network*
%_mandir/*/*netdev*
%_mandir/*/*resolved*
%endif

%if_enabled timesyncd
%files timesyncd
%config(noreplace) %_sysconfdir/systemd/timesyncd.conf
/lib/systemd/system-preset/85-timesyncd.preset
/lib/systemd/systemd-timesyncd
%_unitdir/systemd-timesyncd.service
%_mandir/*/*timesyncd*
%endif

%files analyze
%_bindir/systemd-analyze
%_man1dir/systemd-analyze.*

%if_enabled microhttpd
%files journal-gateway
%dir %_localstatedir/log/journal/remote
%config(noreplace) %_sysconfdir/systemd/journal-remote.conf
/lib/systemd/systemd-journal-gatewayd
/lib/systemd/systemd-journal-remote
%_unitdir/systemd-journal-gatewayd.*
%_datadir/systemd/gatewayd
/lib/tmpfiles.d/systemd-remote.conf
%_man8dir/systemd-journal-gatewayd.*
%_man8dir/systemd-journal-remote.*

%if_enabled sysusers
/lib/sysusers.d/systemd-remote.conf
%endif

%if_enabled libcurl
%config(noreplace) %_sysconfdir/systemd/journal-upload.conf
/lib/systemd/systemd-journal-upload
%_unitdir/systemd-journal-upload.service
%_man8dir/systemd-journal-upload*
%endif
%endif

%if_enabled coredump
%files coredump
%config(noreplace) %_sysconfdir/systemd/coredump.conf
/lib/systemd/systemd-coredump
%_bindir/*coredumpctl
/lib/sysctl.d/50-coredump.conf
%_man1dir/*coredumpctl.*
%_man5dir/coredump.conf.*
%_man8dir/systemd-coredump.*
%dir %_localstatedir/lib/systemd/coredump
%endif

%if_enabled sysuser
%files stateless
/sbin/systemd-sysusers
%dir /lib/sysusers.d
%dir %_datadir/factory
%_datadir/factory/*
%_unitdir/systemd-sysusers.service
%_unitdir/sysinit.target.wants/systemd-sysusers.service
/lib/sysusers.d/systemd.conf
/lib/sysusers.d/basic.conf
/lib/tmpfiles.d/etc.conf
%_mandir/*/*sysusers*

%if_enabled firstboot
/sbin/systemd-firstboot
%_unitdir/systemd-firstboot.service
%_unitdir/sysinit.target.wants/systemd-firstboot.service
%endif
%if_enabled ldconfig
%_unitdir/ldconfig.service
%_unitdir/sysinit.target.wants/ldconfig.service
%endif
%endif

%files -n bash-completion-%name
%_sysconfdir/bash_completion.d/*
%exclude %_sysconfdir/bash_completion.d/udevadm
%exclude %_sysconfdir/bash_completion.d/journalctl

%files -n zsh-completion-%name
%_datadir/zsh/site-functions/*
%exclude %_datadir/zsh/site-functions/_udevadm
%exclude %_datadir/zsh/site-functions/_journalctl

%if_with python
%files -n python-module-%name
%python_sitelibdir/%name
%endif

%files -n journalctl
/bin/journalctl
/sbin/journalctl
%_man1dir/journalctl.*

%files -n bash-completion-journalctl
%_sysconfdir/bash_completion.d/journalctl

%files -n zsh-completion-journalctl
%_datadir/zsh/site-functions/_journalctl

%files -n bash-completion-udev
%_sysconfdir/bash_completion.d/udevadm
#%_datadir/bash-completion/completions/udevadm

%files -n zsh-completion-udev
%_datadir/zsh/site-functions/_udevadm

%files -n libudev1
/%_lib/libudev.so.*

%files -n libudev-devel
%_includedir/libudev.h
%_libdir/libudev.so
%_pkgconfigdir/libudev.pc
%_datadir/pkgconfig/udev.pc

%files -n libudev-devel-doc
%_datadir/gtk-doc/html/libudev

%files -n libgudev
%_libdir/libgudev-*.so.*

%files -n libgudev-devel
%_includedir/gudev-1.0
%_libdir/libgudev-*.so
%_pkgconfigdir/gudev-*.pc

%files -n libgudev-devel-doc
%_datadir/gtk-doc/html/gudev

%files -n libgudev-gir
%_libdir/girepository-1.0/*.typelib

%files -n libgudev-gir-devel
%_datadir/gir-1.0/*.gir

%files -n udev
%doc README TODO NEWS LICENSE.GPL2
%dir %_sysconfdir/udev
%config(noreplace) %_sysconfdir/udev/*.conf
%ghost %_sysconfdir/udev/hwdb.bin
%config(noreplace) %_sysconfdir/scsi_id.config
%_initdir/udev*
%_unitdir/*udev*
%_unitdir/*/*udev*
%dir /lib/udev
%dir /lib/udev/devices
%dir /lib/systemd/network
/lib/systemd/network/*.link
/lib/udev/udevd
/lib/udev/ata_id
/lib/udev/cdrom_id
/lib/udev/mtd_probe
/lib/udev/scsi_id
/sbin/udevadm
/sbin/udevd
/lib/systemd/systemd-udevd
%_rpmlibdir/udev.filetrigger
%_mandir/*/*udev*
%_mandir/*/*link*
%_man5dir/systemd.device*

%files -n udev-extras
/lib/udev/accelerometer
/lib/udev/v4l_id
/lib/udev/collect
/lib/udev/rules.d/61-accelerometer.rules
/lib/udev/rules.d/78-sound-card.rules

%files -n udev-rules
%dir %_sysconfdir/udev/rules.d
%config(noreplace) %_sysconfdir/udev/rules.d/*
/lib/udev/initramfs-rules.d
/lib/udev/rules.d
# rule-generator
/lib/udev/rule_generator.functions

%exclude %_sysconfdir/udev/rules.d/70-persistent-*.rules
%exclude %_sysconfdir/udev/rules.d/80-net-setup-link.rules
%exclude /lib/udev/rules.d/75-*-generator.rules
# extras
%exclude /lib/udev/rules.d/61-accelerometer.rules
%exclude /lib/udev/rules.d/78-sound-card.rules
# systemd
%exclude /lib/udev/rules.d/70-uaccess.rules
%exclude /lib/udev/rules.d/71-seat.rules
%exclude /lib/udev/rules.d/73-seat-late.rules
%exclude /lib/udev/rules.d/99-systemd.rules

%files -n udev-hwdb
%dir %_sysconfdir/udev/hwdb.d
/lib/udev/hwdb.d

%files -n udev-rule-generator-cdrom
%config(noreplace,missingok) %verify(not md5 size mtime) %ghost %_sysconfdir/udev/rules.d/70-persistent-cd.rules
/lib/udev/rules.d/75-cd-aliases-generator.rules
/lib/udev/write_cd_rules

%files -n udev-rule-generator-net
%config(noreplace,missingok) %verify(not md5 size mtime) %ghost %_sysconfdir/udev/rules.d/70-persistent-net.rules
%_sysconfdir/udev/rules.d/80-net-setup-link.rules
/lib/udev/rules.d/75-persistent-net-generator.rules
/lib/udev/write_net_rules

%changelog
* Wed Nov 12 2014 Alexey Shabalin <shaba@altlinux.ru> 1:217-alt2
- udev hwdb: Change error message regarding missing hwdb.bin back to debug.

* Wed Oct 29 2014 Alexey Shabalin <shaba@altlinux.ru> 1:217-alt1
- 217

* Tue Sep 23 2014 Alexey Shabalin <shaba@altlinux.ru> 1:216-alt4
- backport fixes for timesyncd from upstream master
- backport many fixes for mem leak from upstream master

* Mon Sep 15 2014 Alexey Shabalin <shaba@altlinux.ru> 1:216-alt3
- move systemd-machine-id-setup to systemd-utils
- move configs /etc/{machine-info,hostname,vconsole.conf,locale.conf} to systemd-utils
- move all units files frorm systemd-utils,systemd-services to systemd

* Mon Sep 15 2014 Alexey Shabalin <shaba@altlinux.ru> 1:216-alt2
- move systemd-{halt,poweroff,reboot,shutdown} man pages to systemd package

* Fri Sep 05 2014 Alexey Shabalin <shaba@altlinux.ru> 1:216-alt1
- 216
- drop use /proc/sys/kernel/hotplug in init script (ALT#30275)
- split zsh completions for systemd, journalctl, udev (ALT#29698)
- update altlinux-openresolv units
- run first_time before display-manager (ALT#29200)
- add systemd-logind shell wrapper
- revert aloow copy to /etc/localtime (Debian patch)
- make hostnamed/localed/logind/machined/timedated D-Bus activatable (Debian patch)
- split systemd-network support from main tmpfiles.d/systemd.conf
- move hostnamed/localed/logind/machined/timedated and *ctl utils to systemd-service package
- split pam_systemd to separate package
- add libnss-mymachines, libnss-resolve packages

* Fri Aug 15 2014 Alexey Shabalin <shaba@altlinux.ru> 1:214-alt14
- add altlinux-openresolv unit to networkd package

* Fri Aug 15 2014 Alexey Shabalin <shaba@altlinux.ru> 1:214-alt13
- fixed networkd and timesyncd preset

* Thu Aug 14 2014 Alexey Shabalin <shaba@altlinux.ru> 1:214-alt12
- split networkd and timesyncd into a separate packages

* Tue Aug 05 2014 Alexey Shabalin <shaba@altlinux.ru> 1:214-alt11
- set default polling interval on removable devices as well
- sysv: order initscripts which provide $network before network.target
- sysv-generator: do not generate 'Wants' symlinks to generated service files that will be shadowed by a native unit
- altlinux-update_chrooted.service -> altlinux-libresolv.path

* Tue Jul 08 2014 Alexey Shabalin <shaba@altlinux.ru> 1:214-alt10
- backport patches for generator from upstream master
- fix preun journal-gateway
- drop detect and set default.target
- update presets services
- skip log_parse_environment for initrd

* Wed Jul 02 2014 Alexey Shabalin <shaba@altlinux.ru> 1:214-alt9
- add alias for halt and reboot services
- don't do automatic cleanup in $XDG_RUNTIME_DIR

* Tue Jul 01 2014 Alexey Shabalin <shaba@altlinux.ru> 1:214-alt8
- drop prefdm.service
- add preset for display managers

* Mon Jun 30 2014 Alexey Shabalin <shaba@altlinux.ru> 1:214-alt7
- update ALTLinux units

* Mon Jun 30 2014 Alexey Shabalin <shaba@altlinux.ru> 1:214-alt6
- units: networkd - don't order wait-online.service before network.target
- libudev: queue - watch entire directory to allow the re-use of the watch descriptor

* Sat Jun 28 2014 Alexey Shabalin <shaba@altlinux.ru> 1:214-alt5
- backport fixes from upstream master branch

* Fri Jun 27 2014 Alexey Shabalin <shaba@altlinux.ru> 1:214-alt3
- revert "add systemd-vconsole-setup@.service for another way localize ttyX"
- revert "start systemd-ask-password-wall.service after getty@tty1.service"
- revert "increase RestartSec to 5 sec for getty services"

* Fri Jun 27 2014 Alexey Shabalin <shaba@altlinux.ru> 1:214-alt2
- snapshot v214-stable branch
- fixed sysv generator
- don't create symlinks /var/run, /var/lock (ALT#30138)

* Mon Jun 23 2014 Alexey Shabalin <shaba@altlinux.ru> 1:214-alt1
- switch to v214-stable branch

* Thu May 08 2014 Alexey Shabalin <shaba@altlinux.ru> 1:210-alt8
- increase RestartSec to 5 sec for getty services (ALT#30061)

* Thu Apr 24 2014 Alexey Shabalin <shaba@altlinux.ru> 1:210-alt7
- v210-stable snapshot (1ba98e163ed872d8744ff644e3d255b4be171bc6)
- fixed typo, /lib/systemd/network should work fine
- revert patch "udev always rename network"
- start systemd-sysctl.service after systemd-module-load.service
- start systemd-ask-password-wall.service after getty@tty1.service
- drop default enabled getty.target.wants/getty@tty*.service
- add systemd-vconsole-setup@.service for another way localize ttyX
- add config with "TTYVTDisallocate=no" for getty@tty1.service
- apply 1003-udev-netlink-null-rules.patch from opensuse
- drop network.service unit - use sysvinit script
- rename 99-default.preset to 99-default-disable.preset
- add 90-default.preset

* Mon Apr 14 2014 Sergey V Turchin <zerg@altlinux.org> 1:210-alt4.2
- NMU: don't disable getty for tty1 because prefdm have conflict
- NMU: don't disable plymouth-quit for xdm-like

* Wed Apr 09 2014 Sergey V Turchin <zerg@altlinux.org> 1:210-alt4.1
- NMU: disable getty for tty1 by default (ALT#29959)
- NMU: don't run prefdm before plymouth-quit

* Thu Mar 20 2014 Alexey Shabalin <shaba@altlinux.ru> 1:210-alt4
- v210-stable snapshot (28be65e12016d365783ac9646bf588ec68352b75)

* Wed Mar 19 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 1:210-alt3
- systemd-tmpfiles.filetrigger:
 + Skip filetrigger if root is fake (e.g. in hasher) (ALT#29895).
 + Move to utils subpackage.

* Fri Mar 07 2014 Alexey Shabalin <shaba@altlinux.ru> 1:210-alt2
- snapshot of systemd-stable/v210-stable
- update bash3 completions
- new distribution-agnostic configs should be redefine old configs

* Tue Feb 25 2014 Alexey Shabalin <shaba@altlinux.ru> 1:210-alt1
- 210
- build systemd-networkd
- drop systemd-startup-nologin.conf tmpfile, used upstream systemd-nologin.conf
- add and define conditions for seccomp(disabled), IMA(disabled), selinux(enabled), apparmor(disabled)
- updated bash3 completions
- all systemd-* libraries moved to libsystemd package
- update %post
- renamed 80-net-name-slot.rules to 80-net-setup-link.rules
- give systemd-logind access to /proc when it's mounted with hidepid option
- /boot -> /boot/efi in efi-boot-generator
- return time zone setup from /etc/sysconfig/clock
- return hostname setup from /etc/sysconfig/network
- build python module
- build gtk-doc packages (libudev-devel-doc, libgudev-devel-doc)
- delete old dir /var/lib/systemd/random-seed

* Thu Jan  2 2014 Ivan Zakharyaschev <imz@altlinux.org> 1:208-alt4
- declare the file conflicts with systemd pkgs before the split of journalctl
  (Epoch 1 for the split pkg, so that the new split journalctl from Sisyphus 
  or any branches conflicts with Epoch 0 old pkgs)
- declare shaba@ as the maintainer

* Thu Jan  2 2014 Ivan Zakharyaschev <imz@altlinux.org> 208-alt3
- split journalctl into a separate pkg
  (to be used for querying without systemd) (ALT#29674)

* Thu Oct 17 2013 Alexey Shabalin <shaba@altlinux.ru> 208-alt2
- update udev.init for create static inodes for SysV

* Wed Oct 02 2013 Alexey Shabalin <shaba@altlinux.ru> 208-alt1
- 208

* Tue Oct 01 2013 Alexey Shabalin <shaba@altlinux.ru> 207-alt3.git.a0f70805
- fixed post install (ALT#29411)

* Mon Sep 30 2013 Alexey Shabalin <shaba@altlinux.ru> 207-alt2.git.a0f70805
- fixed mount /usr (ALT#29407)
- default kernel.sysrq = 1 (ALT#29366)
- fixed error about /var/lib/systemd/random-seed

* Mon Sep 23 2013 Alexey Shabalin <shaba@altlinux.ru> 207-alt1.git.a0f70805
- upstream git snapshot a0f708053ba42c8289caed1107f498bbf332e204

* Wed Jul 24 2013 Alexey Shabalin <shaba@altlinux.ru> 206-alt1
- 206

* Fri Jul 05 2013 Alexey Shabalin <shaba@altlinux.ru> 205-alt1
- 205
- add udev.filetrigger for reload udev rules

* Thu Jun 13 2013 Sergey V Turchin <zerg@altlinux.org> 204-alt5
- turn off tmp.mount by default (ALT#29066)

* Wed May 29 2013 Alexey Shabalin <shaba@altlinux.ru> 204-alt4
- fix permition of /run/lock/serial (ALT#29032)
- move tmpfiles.d/{tmp.conf,x11.conf} to systemd-utils

* Mon May 27 2013 Alexey Shabalin <shaba@altlinux.ru> 204-alt3
- move /etc/modules-load.d/modules.conf from systemd to systemd-utils

* Fri May 17 2013 Alexey Shabalin <shaba@altlinux.ru> 204-alt2
- fix permitions for ALTLinux in /lib/tmpfiles.d/legacy.conf
- move sysctl  and tmpfiles configs to systemd-utils
- use /sbin/systemd-tmpfiles for create static inodes in SysV init script
- add systemd-coredump package

* Thu May 16 2013 Michael Shigorin <mike@altlinux.org> 204-alt1.1
- NMU: apply F18 patch to revert upstream breakage of ethX/ethY
  renaming, see also RH#896135, FDO#53837, FDO#56929

* Sun May 12 2013 Alexey Shabalin <shaba@altlinux.ru> 204-alt1
- 204
- add symlink /bin/systemctl -> /sbin/systemctl

* Wed May 08 2013 Alexey Shabalin <shaba@altlinux.ru> 203-alt1
- 203
- move root utils to /sbin
- split systemd-bash3 completion to several files
- disable build python module
- add systemd-utils package

* Tue Apr 09 2013 Alexey Shabalin <shaba@altlinux.ru> 201-alt1
- 201

* Mon Apr 08 2013 Alexey Shabalin <shaba@altlinux.ru> 200-alt3
- run systemd-vconsole-setup before getty.target

* Mon Apr 08 2013 Alexey Shabalin <shaba@altlinux.ru> 200-alt2
- fixed custom font in console
- remove conflict with hal for udev

* Fri Apr 05 2013 Alexey Shabalin <shaba@altlinux.ru> 200-alt1
- 200

* Tue Mar 12 2013 Alexey Shabalin <shaba@altlinux.ru> 198-alt1
- 198
- add systemd-journal-gateway package

* Tue Feb 12 2013 Alexey Shabalin <shaba@altlinux.ru> 197-alt6
- revert --action=add in systemd-udev-trigger.service

* Mon Feb 11 2013 Alexey Shabalin <shaba@altlinux.ru> 197-alt5
- mask 80-net-name-slot.rules in udev-rule-generator-net

* Thu Feb 07 2013 Alexey Shabalin <shaba@altlinux.ru> 197-alt4
- revert persistent net generator
- split package udev-rule-generator to udev-rule-generator-cdrom and udev-rule-generator-net
- add more preset dirs
- only enforce ALTLinux's disable-by-default policy

* Wed Feb 06 2013 Alexey Shabalin <shaba@altlinux.ru> 197-alt3
- move 75-net-description.rules and 75-tty-description.rules from udev-extras to udev-rules
- add default preset policy

* Tue Jan 29 2013 Alexey Shabalin <shaba@altlinux.ru> 197-alt2
- add --action=add to udevadm trigger in udevd.init
- add strict inter-package dependencies

* Wed Jan 16 2013 Alexey Shabalin <shaba@altlinux.ru> 197-alt1
- 197
- drop 75-persistent-net-generator.rules and write_net_rules
- revert support ALTLinux configuration files for console,locale,hostname
- build libnss-myhostname as separate package
- enable build bootchart
- fixed /etc/firsttime.d support

* Thu Nov 29 2012 Alexey Shabalin <shaba@altlinux.ru> 196-alt1
- 196
- move completion to separate noarch packages:
  bash-completion-systemd, bash-completion-udev, zsh-completion-systemd
- provide syslogd-daemon because the journal is fine as a syslog implementation
- add udev-hwdb package

* Thu Nov 22 2012 Alexey Shabalin <shaba@altlinux.ru> 195-alt3
- drop altlinux-storage-init.service,altlinux-wait-storage.service,altlinux-storage-init-late.service

* Thu Nov 22 2012 Alexey Shabalin <shaba@altlinux.ru> 195-alt2
- drop rtc.conf from modules-load.d

* Tue Oct 23 2012 Alexey Shabalin <shaba@altlinux.ru> 195-alt1
- 195

* Mon Oct 08 2012 Alexey Shabalin <shaba@altlinux.ru> 194-alt2
- add 60-raw.rules from util-linux

* Thu Oct 04 2012 Alexey Shabalin <shaba@altlinux.ru> 194-alt1
- 194

* Mon Oct 01 2012 Alexey Shabalin <shaba@altlinux.ru> 193-alt2
- drop altlinux-swap.service
- add /etc/profile.d/systemd.sh and export
  SYSTEMD_PAGER="/usr/bin/less -FR" (ALT#27784)

* Fri Sep 28 2012 Alexey Shabalin <shaba@altlinux.ru> 193-alt1
- 193
- add support build with microhttpd, but disable

* Thu Sep 27 2012 Alexey Shabalin <shaba@altlinux.ru> 192-alt1
- 192

* Fri Sep 21 2012 Alexey Shabalin <shaba@altlinux.ru> 190-alt1
- 190
- mask legacy services: halt, single, netfs
- fix load font on tty1-6 - add and autorun systemd-vconsole-setup@.service
- add package contains python binds for systemd APIs

* Tue Sep 18 2012 Alexey Shabalin <shaba@altlinux.ru> 189-alt4
- exclude run tmpfiles systemd-startup-nologin.conf from filetrigger
  for upgrade systemd. (ALT#27749)
- move create /run/nologin to separate file systemd-startup-nologin.conf.

* Fri Sep 14 2012 Alexey Shabalin <shaba@altlinux.ru> 189-alt3
- because initrd drop udev db, need full rebuild with udevadm trigger

* Wed Sep 12 2012 Alexey Shabalin <shaba@altlinux.ru> 189-alt2
- move libsystemd-journal,libsystemd-id128{-devel} to separate packages
- systemd-devel as noarch without any requires;
  many packages require pkgconfig/systemd.pc only

* Tue Aug 28 2012 Alexey Shabalin <shaba@altlinux.ru> 189-alt1
- snapshot fe1fed02c7637a2c18cd575f78be7fda27972148
- build without FSS (gcrypt and qrencode)

* Thu Aug 09 2012 Alexey Shabalin <shaba@altlinux.ru> 188-alt1
- 188
- update prefdm.service
- fix rule_generator.functions for udev > 185

* Wed Aug 08 2012 Alexey Shabalin <shaba@altlinux.ru> 187-alt5
- add rtc.conf to modules-load.d for load rtc kernel module at boot time
- drop altlinux-loadmodules.service
  add symlink /etc/modules-load.d/modules.conf -> /etc/modules
- add export SYSTEMD_LOG_TARGET=syslog in udev init script for don't log to kmsg (ALT#27610)

* Wed Aug 08 2012 Alexey Shabalin <shaba@altlinux.org> 187-alt4
- call multipath and kpartx with -u
- fix typo in altlinux-storage-init

* Wed Aug 08 2012 Alexey Shabalin <shaba@altlinux.org> 187-alt3
- run prefdm after getty.target
- add rpm filetrigger for create tmpfiles
- add Conflicts: DeviceKit (ALT#27612)
- add ploop devices to skip rules (ALT#27083)

* Wed Aug 01 2012 Alexey Shabalin <shaba@altlinux.ru> 187-alt2
- update network.service
- add a storage setup after cryptsetup.target
- cleanup spec
- update ALTLinux specific unit files
- add unit file for run scripts from /etc/firsttime.d after install distro
- add unit for update /etc/issue and /etc/issue.net files
- add systemd-rc-local-generator for ALTLinux
- add Conflicts: hal

* Fri Jul 20 2012 Alexey Shabalin <shaba@altlinux.ru> 187-alt1
- 187

* Mon Jul 16 2012 Alexey Shabalin <shaba@altlinux.ru> 186-alt1
- 186
- fix path to udev binary in init script (ALT#27471)
- change Obsoletes to Conflicts for libudev

* Wed Jun 20 2012 Alexey Shabalin <shaba@altlinux.ru> 185-alt3
- fix install - add Obsoletes: libudev < 185-alt3 (ALT#27472)

* Wed Jun 20 2012 Alexey Shabalin <shaba@altlinux.org> 185-alt2
- rename libudev to libudev1.
- return cd rule generator (ALT#26389).
- run setsysfont as ExecStartPre for getty instead of fbsetfont
  service.
- units: avoid redundant VT clearing by agetty (thx Michal Schmidt).
- ALTLinux support: Don't set LANG to "C" by default. (thx Mikhail Efremov) (ALT#27408).

* Tue Jun 05 2012 Alexey Shabalin <shaba@altlinux.ru> 185-alt1
- 185
- add udev subpackages
- drop gtk subpackage (move to systemd-ui)

* Fri Mar 16 2012 Alexey Shabalin <shaba@altlinux.ru> 44-alt1
- v44

* Mon Mar 05 2012 Alexey Shabalin <shaba@altlinux.ru> 43-alt2
- split libsystemd-daemon(-devel) and libsystemd-login(-devel) packages

* Wed Feb 22 2012 Alexey Shabalin <shaba@altlinux.ru> 43-alt1
- v43
- merge units into the main package

* Fri Jan 13 2012 Alexey Shabalin <shaba@altlinux.ru> 37-alt3
- adapt for filesystem-2.3.10-alt1

* Mon Nov 14 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 37-alt2.1
- Rebuild with Python-2.7

* Tue Nov 01 2011 Alexey Shabalin <shaba@altlinux.ru> 37-alt2
- rebuild with libcryptsetup-1.4.0

* Wed Oct 12 2011 Alexey Shabalin <shaba@altlinux.ru> 37-alt1
- v37
- mask SYSV plymouth service

* Fri Sep 23 2011 Alexey Shabalin <shaba@altlinux.ru> 36-alt1
- v36

* Thu Sep 01 2011 Alexey Shabalin <shaba@altlinux.ru> 35-alt1
- v35

* Mon Aug 29 2011 Alexey Shabalin <shaba@altlinux.ru> 34-alt1
- v34

* Mon Aug 22 2011 Alexey Shabalin <shaba@altlinux.ru> 33-alt2.gite1915
- fix ABRT on service file reloading

* Mon Aug 08 2011 Alexey Shabalin <shaba@altlinux.ru> 33-alt1
- v33

* Thu Jul 28 2011 Alexey Shabalin <shaba@altlinux.ru> 31-alt1
- v31
- add devel package

* Thu Jun 16 2011 Alexey Shabalin <shaba@altlinux.ru> 29-alt1
- v29

* Fri Jun 10 2011 Alexey Shabalin <shaba@altlinux.ru> 28-alt3
- allow enable/disable symlinks for ALTLinux
- enable chkconfig support in systemctl for ALTLinux

* Sun Jun 05 2011 Alexey Shabalin <shaba@altlinux.ru> 28-alt2
- rebuild with new libnotify

* Sun May 29 2011 Alexey Shabalin <shaba@altlinux.ru> 28-alt1
- v28

* Sun May 22 2011 Alexey Shabalin <shaba@altlinux.ru> 27-alt2
- backported fixes from upstream

* Fri May 20 2011 Alexey Shabalin <shaba@altlinux.ru> 27-alt1
- v27
- mask /etc/init.d/killall
- add Requires: libnss-myhostname
- drop previus patch for pull rpcbind.target to multi-user.target,
  nfs services must requires rpcbind.target

* Sat May 14 2011 Alexey Shabalin <shaba@altlinux.ru> 26-alt3
- update network.service
- pull rpcbind.target to multi-user.target

* Sat May 07 2011 Alexey Shabalin <shaba@altlinux.ru> 26-alt2
- move systemd-analyze(python) tool to subpackage

* Wed May 04 2011 Alexey Shabalin <shaba@altlinux.ru> 26-alt1
- v26
- /var/lock and /var/run on tmpfs
- add altlinux-kmsg-loglevel.service
- add altlinux-save-dmesg.service

* Tue Mar 22 2011 Alexey Shabalin <shaba@altlinux.ru> 20-alt3
- disable legacy services: fbsetfont and keytable

* Mon Mar 21 2011 Alexey Shabalin <shaba@altlinux.ru> 20-alt2
- disable swap enable by systemd, use altlinux-swap.service
- disable "SysVConsole" legacy output to console

* Wed Mar 09 2011 Alexey Shabalin <shaba@altlinux.ru> 20-alt1
- v20

* Fri Mar 04 2011 Alexey Shabalin <shaba@altlinux.ru> 19-alt3.git20110301
- add workaround Conflicts: SysVinit < 2.86-alt2 in sysvinit-utils

* Wed Mar 02 2011 Alexey Shabalin <shaba@altlinux.ru> 19-alt2.git20110301
- upstream snapshot 20110301

* Tue Mar 01 2011 Alexey Shabalin <shaba@altlinux.ru> 19-alt1
- v19
- add condstop, condreload for compatibility with ALTLinux

* Mon Feb 28 2011 Alexey Shabalin <shaba@altlinux.ru> 18-alt2.git20110225
- upstream snapshot 20110225
- modify altlinux-clock for run only when /etc/adjtime is missing, and use hwclock-load
- add support mount /proc with gid=proc
- add network.service

* Thu Feb 17 2011 Alexey Shabalin <shaba@altlinux.ru> 18-alt1
- v18

* Tue Feb 15 2011 Alexey Shabalin <shaba@altlinux.ru> 17-alt9.20110213
- add one altlinux-storage-init service (with altlinux-storage-init script) instead of altlinux-lvm, altlinux-multipath, altlinux-raid services

* Tue Feb 15 2011 Alexey Shabalin <shaba@altlinux.ru> 17-alt8.20110213
- fix run clock service
- add altlinux-swap service
- add altlinux-lvm, altlinux-multipath, altlinux-raid services

* Mon Feb 14 2011 Alexey Shabalin <shaba@altlinux.ru> 17-alt7.20110213
- adapt completion for bash3; thx to iv@
- add altlinux-clock service
- fix work with plymoth
- package dir /etc/modules-load.d and add example
- add quota services to local-fs.target
- build with libcryptsetup support

* Wed Feb 09 2011 Alexey Shabalin <shaba@altlinux.ru> 17-alt6.20110209
- upstream snapshot
- plymouth support
- drop multipath and evms services

* Mon Feb 07 2011 Alexey Shabalin <shaba@altlinux.ru> 17-alt5
- add multipath service
- add update_chrooted service
- add idetune service
- add evms service to git (but not install)

* Fri Feb 04 2011 Alexey Shabalin <shaba@altlinux.ru> 17-alt4
- add load legacy module configuration from /etc/modules
- use hwclock-load.service instead init.d/clock
- use systemd-random-seed-load.service instead init.d/random

* Thu Feb 03 2011 Alexey Shabalin <shaba@altlinux.ru> 17-alt3
- don't use sysinit
- fix symlink path for rc-local

* Tue Feb 01 2011 Alexey Shabalin <shaba@altlinux.ru> 17-alt2
- add prefdm service
- fix syslog name service
- add Before=sysinit.target to sysinit.service
- use mingetty instead of agetty

* Tue Jan 25 2011 Alexey Shabalin <shaba@altlinux.ru> 17-alt1
- version 17

* Fri Jan 14 2011 Alexey Shabalin <shaba@altlinux.ru> 16-alt1
- version 16

* Fri Nov 19 2010 Alexey Shabalin <shaba@altlinux.ru> 13-alt1
- version 13

* Sun Sep 19 2010 Alexey Shabalin <shaba@altlinux.ru> 10-alt1
- version 10 + snapshot Sep 22 2010

* Thu Sep 09 2010 Alexey Shabalin <shaba@altlinux.ru> 9-alt1
- version 9

* Thu Aug 26 2010 Alexey Shabalin <shaba@altlinux.ru> 8-alt1
- version 8
- build with libaudit

* Wed Aug 25 2010 Alexey Shabalin <shaba@altlinux.ru> 7-alt1
- version 7
- build with selinux

* Fri Jul 09 2010 Alexey Shabalin <shaba@altlinux.ru> 2-alt1
- version 2

* Wed Jul 07 2010 Alexey Shabalin <shaba@altlinux.ru> 1-alt1
- initial build for ALTLinux
