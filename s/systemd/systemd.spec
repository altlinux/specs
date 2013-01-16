%define firmwaredir             /lib/firmware
%define _localstatedir %_var

%def_enable libcryptsetup
%def_enable logind
%def_enable vconsole
%def_enable readahead
%def_enable quotacheck
%def_enable randomseed
%def_disable coredump
%def_disable gcrypt
%def_disable qrencode
%def_disable microhttpd
%def_enable myhostname
%def_enable bootchart

Name: systemd
Version: 197
Release: alt1
Summary: A System and Session Manager
Url: http://www.freedesktop.org/wiki/Software/systemd
Group: System/Configuration/Boot and Init
License: LGPLv2.1+

Source:%name-%version.tar
Source2: rc-local.service
Source4: prefdm.service
Source6: altlinux-idetune.service
Source7: altlinux-update_chrooted.service
Source8: altlinux-clock-setup.service
Source14: systemd-bash3
Source15: network.service
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
Source29: tmpfile-systemd-startup-nologin.conf
Source30: systemd-vconsole-setup@.service
Source31: 60-raw.rules

# udev rule generator
Source41: rule_generator.functions
Source42: write_net_rules
Source43: 75-persistent-net-generator.rules
Source44: write_cd_rules
Source45: 75-cd-aliases-generator.rules
Source46: udev-bash3

Patch1: %name-snapshot.patch
Patch2: %name-alt-patches.patch

%define dbus_ver 1.4.6

BuildRequires: glibc-kernheaders
BuildRequires: intltool >= 0.40.0
BuildRequires: gperf
BuildRequires: libcap-devel libcap-utils
BuildRequires: libwrap-devel
BuildRequires: libpam-devel
BuildRequires: libacl-devel
BuildRequires: libattr-devel
BuildRequires: xsltproc
BuildRequires: docbook-style-xsl docbook-dtds
BuildRequires: libdbus-devel >= %dbus_ver
BuildRequires: libselinux-devel
BuildRequires: libaudit-devel
BuildRequires: glib2-devel >= 2.26 libgio-devel
BuildRequires: gobject-introspection-devel
BuildRequires: liblzma-devel
BuildRequires: kmod-devel >= 5
BuildRequires: python-devel
BuildRequires: quota
BuildRequires: gtk-doc
BuildRequires: libblkid-devel >= 2.20

%{?_enable_libcryptsetup:BuildRequires: libcryptsetup-devel}
BuildRequires: libgcrypt-devel
%{?_enable_qrencode:BuildRequires: libqrencode-devel}
%{?_enable_microhttpd:BuildRequires: libmicrohttpd-devel}

Requires: dbus >= %dbus_ver
Requires: udev = %version-%release
Requires: libudev1 = %version-%release
Requires: libnss-myhostname = %version-%release
Requires: filesystem >= 2.3.10-alt1
Requires: agetty
# Requires: selinux-policy >= 3.8.5

Requires: libsystemd-daemon = %version-%release
Requires: libsystemd-login = %version-%release
Requires: libsystemd-journal = %version-%release

# Copy from SysVinit
PreReq: coreutils
Requires: /sbin/sulogin
Requires: sysvinit-utils

Obsoletes: systemd-units < 43-alt1
Provides: systemd-units = %version-%release
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

%package -n libsystemd-daemon
Group: System/Libraries
Summary: Systemd Daemon Utility Library

%description -n libsystemd-daemon
The sd-daemon library provides a reference implementation of various
APIs for new-style daemons, as implemented by the systemd init system.


This package contains the development files.

%package -n libsystemd-login
Group: System/Libraries
Summary: Systemd Login Utility Library

%description -n libsystemd-login
The libsystemd-login library provides an interface for the
systemd-logind service which is used to track user sessions and seats.

%package -n libsystemd-id128
Group: System/Libraries
Summary: Systemd 128 Bit ID Utility Library

%description -n libsystemd-id128
The libsystemd-id128 library provides utility functions for generating 128 bit IDs.

%package -n libsystemd-journal
Group: System/Libraries
Summary: Systemd Journal Utility Library

%description -n libsystemd-journal
The libsystemd-journal library provides an interface for the systemd journal service.

%package -n libsystemd-daemon-devel
Group: Development/C
Summary: Development headers for systemd Daemon Utility Library
License: MIT
Requires: libsystemd-daemon = %version-%release

%description -n libsystemd-daemon-devel
The sd-daemon library provides a reference implementation of various
APIs for new-style daemons, as implemented by the systemd init system.

%package -n libsystemd-login-devel
Group: Development/C
Summary: Development headers for systemd Login Utility Library
Requires: libsystemd-login = %version-%release

%description -n libsystemd-login-devel
The libsystemd-login library provides an interface for the
systemd-logind service which is used to track user sessions and seats.

This package contains the development files.

%package -n libsystemd-id128-devel
Group: Development/C
Summary: Development headers for systemd 128 Bit ID Utility Library
Requires: libsystemd-id128 = %version-%release

%description -n libsystemd-id128-devel
The libsystemd-id128 library provides utility functions for generating 128 bit IDs.

This package contains the development files.

%package -n libsystemd-journal-devel
Group: Development/C
Summary: Development headers for systemd Journal Utility Library
Requires: libsystemd-journal = %version-%release
Requires: libsystemd-id128-devel = %version-%release

%description -n libsystemd-journal-devel
The libsystemd-journal library provides an interface for the systemd journal service.

This package contains the development files.

%package -n libnss-myhostname
Group: System/Libraries
Summary: glibc plugin for local system host name resolution
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
Requires: %name = %version-%release
# Obsoletes: SysVinit
Provides: SysVinit = 2.88-alt0.1
#Obsoletes:      upstart
Conflicts: upstart
Conflicts: SysVinit
BuildArch: noarch

%description sysvinit
Drop-in replacement for the System V init tools of systemd.

%package analyze
Group: System/Configuration/Boot and Init
Summary: Analyze tool for systemd.
Requires: %name = %version-%release
BuildArch: noarch

%description analyze
Analyze tool for systemd.

%package -n bash-completion-%name
Summary: Bash completion for systemd utils
Group: Shells
BuildArch: noarch
Requires: bash-completion
Requires: systemd = %version-%release

%description -n bash-completion-%name
Bash completion for %name.

%package -n zsh-completion-%name
Summary: Zsh completion for systemd utils
Group: Shells
BuildArch: noarch

%description -n zsh-completion-%name
Zsh completion for %name.

%package -n python-module-%name
Summary: Python Bindings for systemd
License: LGPLv2+
Group: Development/Python
Requires: libsystemd-journal = %version-%release

%description -n python-module-%name
This package contains python binds for systemd APIs

%package -n udev
Group: System/Configuration/Hardware
Summary: udev - an userspace implementation of devfs
License: GPLv2+
PreReq: shadow-utils dmsetup kmod >= 5 util-linux >= 2.20 losetup >= 2.19.1
PreReq: udev-rules = %version-%release
PreReq: udev-hwdb = %version-%release
Requires: libudev1 = %version-%release
Requires: udev-rule-generator = %version-%release
Provides: hotplug = 2004_09_23-alt18
Obsoletes: hotplug
Conflicts: systemd < %version-%release
Conflicts: util-linux <= 2.22-alt2
Conflicts: hal DeviceKit

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
Requires: udev = %version-%release
Requires: libudev1 = %version-%release

%description -n udev-extras
The udev-extras package contains an additional rules and tools
to create and identify devices

%package -n udev-rules
Summary: Rule files for udev
Group: System/Configuration/Hardware
License: GPLv2+
Provides: %_sysconfdir/udev/rules.d /lib/udev/rules.d
Conflicts: udev < %version-%release
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
Conflicts: udev < %version-%release
BuildArch: noarch

%description -n udev-hwdb
This package contains internal hardware database for udev.

%package -n udev-rule-generator
Summary: CD/Net rule generator for udev
Group: System/Configuration/Hardware
License: GPLv2+
BuildArch: noarch
Requires: udev-rules = %version-%release

%description -n udev-rule-generator
This package contains CD/Net rule generator for udev

%package -n bash-completion-udev
Summary: Bash completion for udev utils
Group: Shells
BuildArch: noarch
Requires: bash-completion
Requires: udev = %version-%release

%description -n bash-completion-udev
Bash completion for udev.

%package -n libudev1
Summary: Shared library to access udev device information
Group: System/Libraries
License: LGPLv2.1+
Conflicts: libudev < 181-alt5

%description -n libudev1
This package provides shared library to access udev device information

%package -n libudev-devel
Summary: Libraries and headers for libudev
Group: Development/C
License: LGPLv2.1+
Requires: libudev1 = %version-%release

%description -n libudev-devel
Shared library and headers for libudev

%package -n libgudev
Summary: GObject bindings for libudev
Group: System/Libraries
Requires: libudev1 = %version-%release

%description -n libgudev
This package provides shared library to access udev device information

%package -n libgudev-gir
Summary: GObject introspection data for the GUdev library
Group: System/Libraries
Requires: libgudev = %version-%release

%description -n libgudev-gir
GObject introspection data for the GUdev library

%package -n libgudev-devel
Summary: Libraries and headers for libgudev
Group: Development/C
Requires: libgudev = %version-%release

%description -n libgudev-devel
Shared library and headers for libgudev

%package -n libgudev-gir-devel
Summary: GObject introspection devel data for the GUdev library
Group: System/Libraries
BuildArch: noarch
Requires: libgudev-gir = %version-%release libgudev-devel = %version-%release

%description -n libgudev-gir-devel
GObject introspection devel data for the GUdev library

%prep
%setup -q
%patch1 -p1
%patch2 -p1

%build
export QUOTAON="/sbin/quotaon"
export QUOTACHECK="/sbin/quotacheck"
export SETCAP="/sbin/setcap"
export KILL="/bin/kill"
export CHKCONFIG="/sbin/chkconfig"

gtkdocize --docdir docs/
intltoolize --force --automake
%autoreconf
%configure  \
	--disable-static \
	--with-rootprefix="" \
	--with-rootlibdir=/%_lib \
	--with-pamlibdir=/%_lib/security \
	--enable-split-usr \
	--with-sysvinit-path=/etc/rc.d/init.d \
	--with-rc-local-script-path-start=/etc/rc.d/rc.local \
	--with-kbd-loadkeys=/bin/loadkeys \
	--with-kbd-setfont=/bin/setfont \
	%{subst_enable libcryptsetup} \
	%{subst_enable logind} \
	%{subst_enable vconsole} \
	%{subst_enable readahead} \
	%{subst_enable quotacheck} \
	%{subst_enable randomseed} \
	%{subst_enable coredump} \
	%{subst_enable gcrypt} \
	%{subst_enable qrencode} \
	%{subst_enable microhttpd} \
	%{subst_enable myhostname} \
	%{subst_enable bootchart} \
	--enable-introspection

%make_build

%install
%make DESTDIR=%buildroot install
install -m644 %SOURCE2 %buildroot%_unitdir/rc-local.service
ln -s rc-local.service %buildroot%_unitdir/local.service
install -m644 %SOURCE4 %buildroot%_unitdir/prefdm.service
ln -s prefdm.service %buildroot%_unitdir/dm.service
ln -s prefdm.service %buildroot%_unitdir/display-manager.service
ln -s ../display-manager.service %buildroot%_unitdir/graphical.target.wants
install -m644 %SOURCE6 %buildroot%_unitdir/altlinux-idetune.service
ln -s ../altlinux-idetune.service %buildroot%_unitdir/sysinit.target.wants
install -m644 %SOURCE7 %buildroot%_unitdir/altlinux-update_chrooted.service
ln -s ../altlinux-update_chrooted.service %buildroot%_unitdir/sysinit.target.wants
install -m644 %SOURCE8 %buildroot%_unitdir/altlinux-clock-setup.service
ln -s ../altlinux-clock-setup.service %buildroot%_unitdir/sysinit.target.wants
ln -s altlinux-clock-setup.service %buildroot%_unitdir/clock.service
install -m644 %SOURCE15 %buildroot%_unitdir/network.service
ln -s ../network.service %buildroot%_unitdir/multi-user.target.wants
install -m644 %SOURCE16 %buildroot%_unitdir/altlinux-kmsg-loglevel.service
ln -s ../altlinux-kmsg-loglevel.service %buildroot%_unitdir/sysinit.target.wants
install -m755 %SOURCE18 %buildroot/lib/systemd/altlinux-save-dmesg
install -m644 %SOURCE17 %buildroot%_unitdir/altlinux-save-dmesg.service
ln -s ../altlinux-save-dmesg.service %buildroot%_unitdir/basic.target.wants
install -m644 %SOURCE27 %buildroot%_unitdir/altlinux-first_time.service
ln -s ../altlinux-first_time.service %buildroot%_unitdir/basic.target.wants

# restore bind-mounts /var/run -> run and /var/lock -> /run/lock
# we don't have those directories symlinked
install -m644 %SOURCE23 %buildroot%_unitdir/var-lock.mount
install -m644 %SOURCE24 %buildroot%_unitdir/var-run.mount
ln -s ../var-lock.mount %buildroot%_unitdir/local-fs.target.wants
ln -s ../var-run.mount %buildroot%_unitdir/local-fs.target.wants

ln -s systemd-random-seed-load.service %buildroot%_unitdir/random.service

find %buildroot \( -name '*.a' -o -name '*.la' \) -exec rm {} \;
mkdir -p %buildroot/sbin
ln -s ../lib/systemd/systemd %buildroot/sbin/init
ln -s ../lib/systemd/systemd %buildroot/bin/systemd
ln -s ../bin/systemctl %buildroot/sbin/reboot
ln -s ../bin/systemctl %buildroot/sbin/halt
ln -s ../bin/systemctl %buildroot/sbin/poweroff
ln -s ../bin/systemctl %buildroot/sbin/shutdown
ln -s ../bin/systemctl %buildroot/sbin/telinit
ln -s ../bin/systemctl %buildroot/sbin/runlevel
rm -rf %buildroot%_docdir/systemd

# add defaults services
ln -s ../remote-fs.target %buildroot%_unitdir/multi-user.target.wants
ln -s ../systemd-quotacheck.service %buildroot%_unitdir/local-fs.target.wants
ln -s ../quotaon.service %buildroot%_unitdir/local-fs.target.wants
mkdir -p %buildroot%_unitdir/getty.target.wants
ln -s ../getty@.service %buildroot%_unitdir/getty.target.wants/getty@tty1.service
ln -s ../getty@.service %buildroot%_unitdir/getty.target.wants/getty@tty2.service
ln -s ../getty@.service %buildroot%_unitdir/getty.target.wants/getty@tty3.service
ln -s ../getty@.service %buildroot%_unitdir/getty.target.wants/getty@tty4.service
ln -s ../getty@.service %buildroot%_unitdir/getty.target.wants/getty@tty5.service
ln -s ../getty@.service %buildroot%_unitdir/getty.target.wants/getty@tty6.service

install -m644 %SOURCE30 %buildroot%_unitdir/systemd-vconsole-setup@.service
ln -s ../systemd-vconsole-setup@.service %buildroot%_unitdir/getty.target.wants/systemd-vconsole-setup@tty1.service
ln -s ../systemd-vconsole-setup@.service %buildroot%_unitdir/getty.target.wants/systemd-vconsole-setup@tty2.service
ln -s ../systemd-vconsole-setup@.service %buildroot%_unitdir/getty.target.wants/systemd-vconsole-setup@tty3.service
ln -s ../systemd-vconsole-setup@.service %buildroot%_unitdir/getty.target.wants/systemd-vconsole-setup@tty4.service
ln -s ../systemd-vconsole-setup@.service %buildroot%_unitdir/getty.target.wants/systemd-vconsole-setup@tty5.service
ln -s ../systemd-vconsole-setup@.service %buildroot%_unitdir/getty.target.wants/systemd-vconsole-setup@tty6.service

# disable legacy services
ln -s /dev/null %buildroot%_unitdir/fbsetfont.service
ln -s /dev/null %buildroot%_unitdir/keytable.service
ln -s /dev/null %buildroot%_unitdir/killall.service
ln -s /dev/null %buildroot%_unitdir/halt.service
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
mkdir -p %buildroot%_sysconfdir/modules-load.d
ln -s ../modules %buildroot%_sysconfdir/modules-load.d/modules.conf

# add load rtc module at boot time
mkdir -p %buildroot/lib/modules-load.d

# Make sure the NTP units dir exists
mkdir -p %buildroot/lib/systemd/ntp-units.d
mkdir -p %buildroot%_sysconfdir/systemd/ntp-units.d

# Add completion for bash3
rm -f %buildroot%_sysconfdir/bash_completion.d/*
install -m644 %SOURCE14 %buildroot%_sysconfdir/bash_completion.d/systemd
# Add completion for zsh
install -D shell-completion/systemd-zsh-completion.zsh %buildroot%_datadir/zsh/Completion/Unix/_systemd

# Make sure the ghost-ing below works
touch %buildroot%_sysconfdir/systemd/system/runlevel2.target
touch %buildroot%_sysconfdir/systemd/system/runlevel3.target
touch %buildroot%_sysconfdir/systemd/system/runlevel4.target
touch %buildroot%_sysconfdir/systemd/system/runlevel5.target

# Make sure these directories are properly owned
mkdir -p %buildroot%_unitdir/basic.target.wants
mkdir -p %buildroot%_unitdir/default.target.wants
mkdir -p %buildroot%_unitdir/dbus.target.wants
mkdir -p %buildroot%_unitdir/syslog.target.wants

# Create new-style configuration files so that we can ghost-own them
touch %buildroot%_sysconfdir/hostname
touch %buildroot%_sysconfdir/vconsole.conf
touch %buildroot%_sysconfdir/locale.conf
touch %buildroot%_sysconfdir/os-release
touch %buildroot%_sysconfdir/machine-id
touch %buildroot%_sysconfdir/machine-info

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

# move libnss_myhostname to /lib
mv %buildroot%_libdir/libnss_myhostname.so.2 %buildroot/%_lib/libnss_myhostname.so.2

#######
# UDEV
#######
mkdir -p %buildroot%_initdir
install -p -m755 %SOURCE19 %buildroot%_initdir/udevd
#install -p -m755 %SOURCE20 %buildroot%_initdir/udevd-final

ln -s systemd-udevd.service %buildroot%_unitdir/udevd.service
#ln -s systemd-udev-settle.service %buildroot%_unitdir/udevd-final.service

# compatibility symlinks to udevd binary
ln -s ../systemd/systemd-udevd %buildroot/lib/udev/udevd
ln -s ../lib/systemd/systemd-udevd %buildroot/sbin/udevd

# move udevadm to /sbin
mv %buildroot%_bindir/udevadm %buildroot/sbin/udevadm
sed -i -e 's|/usr/bin/udevadm|/sbin/udevadm|g' \
	%buildroot/lib/udev/rules.d/71-seat.rules \
	%buildroot%_unitdir/systemd-udev-settle.service \
	%buildroot%_unitdir/systemd-udev-trigger.service

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
# firmware dirs
mkdir -p %buildroot%firmwaredir/updates
mkdir -p %buildroot/lib/mkinitrd/udev/%firmwaredir/updates
# Create ghost files
touch %buildroot%_sysconfdir/udev/rules.d/70-persistent-net.rules
touch %buildroot%_sysconfdir/udev/rules.d/70-persistent-cd.rules

# udev rule generator
install -p -m644 %SOURCE41 %buildroot/lib/udev/
#install -p -m755 %SOURCE42 %buildroot/lib/udev/
#install -p -m644 %SOURCE43 %buildroot/lib/udev/rules.d/
install -p -m755 %SOURCE44 %buildroot/lib/udev/
install -p -m644 %SOURCE45 %buildroot/lib/udev/rules.d/

# Add completion for bash3
install -m644 %SOURCE46 %buildroot%_sysconfdir/bash_completion.d/udev

echo ".so man8/systemd-udevd.8" > %buildroot%_man8dir/udevd.8

install -p -m644 %SOURCE31 %buildroot%_sysconfdir/udev/rules.d/

install -m644 %SOURCE29 %buildroot/lib/tmpfiles.d/systemd-startup-nologin.conf
# rpm posttrans filetriggers
install -pD -m755 %SOURCE28 %buildroot%_rpmlibdir/systemd-tmpfiles.filetrigger

%post
/bin/systemd-machine-id-setup >/dev/null 2>&1 || :
/lib/systemd/systemd-random-seed save >/dev/null 2>&1 || :
/bin/systemctl daemon-reexec >/dev/null 2>&1 || :
/bin/journalctl --update-catalog >/dev/null 2>&1 || :

if [ $1 -eq 1 ] ; then
        # Try to read default runlevel from the old inittab if it exists
        runlevel=$(/bin/awk -F ':' '$3 == "initdefault" && $1 !~ "^#" { print $2 }' /etc/inittab 2> /dev/null)
        if [ -z "$runlevel" ] ; then
                target="%_unitdir/graphical.target"
        else
                target="%_unitdir/runlevel$runlevel.target"
        fi

        # And symlink what we found to the new-style default.target
        /bin/ln -sf "$target" %_sysconfdir/systemd/system/default.target 2>&1 || :

        # Enable the services we install by default
        /bin/systemctl enable \
                getty@.service \
                remote-fs.target \
                systemd-readahead-replay.service \
                systemd-readahead-collect.service >/dev/null 2>&1 || :
fi

%postun
if [ $1 -ge 1 ] ; then
	/bin/systemctl daemon-reload > /dev/null 2>&1 || :
	/bin/systemctl try-restart systemd-logind.service >/dev/null 2>&1 || :
fi

%preun
if [ $1 -eq 0 ] ; then
        /bin/systemctl disable \
                getty@.service \
                remote-fs.target \
                systemd-readahead-replay.service \
                systemd-readahead-collect.service >/dev/null 2>&1 || :

        /bin/rm -f /etc/systemd/system/default.target > /dev/null 2>&1 || :
fi

%post -n libnss-myhostname
if [ "$1" = "1" ]; then
    grep -q '^hosts:[[:blank:]].\+myhostname' \
    /etc/nsswitch.conf || \
    sed -i.rpmorig 's/^\(hosts:.\+\)$/\1 myhostname/' /etc/nsswitch.conf
fi
update_chrooted all

%postun -n libnss-myhostname
if [ "$1" = "0" ]; then
    grep -q '^hosts:[[:blank:]].\+myhostname' \
        /etc/nsswitch.conf && \
    sed -i 's/ myhostname//' /etc/nsswitch.conf
fi
update_chrooted all

%pre -n udev
%_sbindir/groupadd -r -f video 2>/dev/null
%_sbindir/groupadd -r -f dialout 2>/dev/null
%_sbindir/groupadd -r -f tape 2>/dev/null

%post -n udev
%post_service udevd
/sbin/udevadm hwdb --update >/dev/null 2>&1 || :

%preun -n udev
%preun_service udevd

%files
%dir %_sysconfdir/systemd
%dir %_sysconfdir/systemd/system
%dir %_sysconfdir/systemd/user
%dir %_sysconfdir/systemd/ntp-units.d


%_sysconfdir/profile.d/systemd.sh
/lib/tmpfiles.d/*.conf
%_sysconfdir/modules-load.d/modules.conf
%_sysconfdir/xdg/systemd

%config(noreplace) %_sysconfdir/dbus-1/system.d/*.conf
%config(noreplace) %_sysconfdir/systemd/*.conf
%ghost %config(noreplace) %_sysconfdir/hostname
%ghost %config(noreplace) %_sysconfdir/vconsole.conf
%ghost %config(noreplace) %_sysconfdir/locale.conf
%ghost %config(noreplace) %_sysconfdir/os-release
%ghost %config(noreplace) %_sysconfdir/machine-id
%ghost %config(noreplace) %_sysconfdir/machine-info

# Make sure we don't remove runlevel targets from F14 alpha installs,
# but make sure we don't create then anew.
%ghost %config(noreplace) %_sysconfdir/systemd/system/runlevel2.target
%ghost %config(noreplace) %_sysconfdir/systemd/system/runlevel3.target
%ghost %config(noreplace) %_sysconfdir/systemd/system/runlevel4.target
%ghost %config(noreplace) %_sysconfdir/systemd/system/runlevel5.target

/bin/*
%dir /lib/systemd
/lib/systemd/*
%dir /usr/lib/systemd
/usr/lib/systemd/*
%_bindir/*
%exclude %_bindir/systemd-analyze
/lib/udev/rules.d/70-uaccess.rules
/lib/udev/rules.d/71-seat.rules
/lib/udev/rules.d/73-seat-late.rules
/lib/udev/rules.d/99-systemd.rules
/%_lib/security/pam_systemd.so
%_rpmlibdir/systemd-tmpfiles.filetrigger
%_man1dir/*
%exclude %_man1dir/init.*
%_man5dir/*
%_man7dir/*
%exclude %_man7dir/udev*
%_man8dir/*
%exclude %_man8dir/systemd-udevd*
%exclude %_man8dir/udevadm.*
%exclude %_man8dir/udevd.*
%exclude %_man8dir/halt.*
%exclude %_man8dir/reboot.*
%exclude %_man8dir/shutdown.*
%exclude %_man8dir/poweroff.*
%exclude %_man8dir/telinit.*
%exclude %_man8dir/runlevel.*
%if_enabled myhostname
%exclude %_man8dir/nss-myhostname.*
%endif
%_datadir/systemd
%_datadir/dbus-1/services/*.service
%_datadir/dbus-1/system-services/*.service
%_datadir/dbus-1/interfaces/*.xml
%_datadir/polkit-1/actions/*.policy
# %%_docdir/systemd
%doc DISTRO_PORTING LICENSE.LGPL2.1 README NEWS TODO
%_localstatedir/log/README
%exclude %_unitdir/*udev*
%exclude %_unitdir/*/systemd-udev*
%exclude /lib/systemd/systemd-udevd

%files -n libsystemd-daemon
/%_lib/libsystemd-daemon.so.*

%files -n libsystemd-login
/%_lib/libsystemd-login.so.*

%files -n libsystemd-id128
/%_lib/libsystemd-id128.so.*

%files -n libsystemd-journal
/%_lib/libsystemd-journal.so.*

%if_enabled myhostname
%files -n libnss-myhostname
/%_lib/libnss_myhostname.so.2
%_man8dir/nss-myhostname.*
%endif

%files devel
%doc LICENSE.LGPL2.1 LICENSE.MIT
%_includedir/systemd/sd-shutdown.h
%_datadir/pkgconfig/systemd.pc
%_man3dir/*

%files -n libsystemd-daemon-devel
%doc LICENSE.MIT
%_libdir/libsystemd-daemon.so
%_pkgconfigdir/libsystemd-daemon.pc
%_includedir/systemd/sd-daemon.h

%files -n libsystemd-login-devel
%_libdir/libsystemd-login.so
%_pkgconfigdir/libsystemd-login.pc
%_includedir/systemd/sd-login.h

%files -n libsystemd-id128-devel
%_libdir/libsystemd-id128.so
%_pkgconfigdir/libsystemd-id128.pc
%_includedir/systemd/sd-id128.h

%files -n libsystemd-journal-devel
%_libdir/libsystemd-journal.so
%_pkgconfigdir/libsystemd-journal.pc
%_includedir/systemd/sd-journal.h
%_includedir/systemd/sd-messages.h

%files sysvinit
/sbin/init
/sbin/reboot
/sbin/halt
/sbin/poweroff
/sbin/shutdown
/sbin/telinit
/sbin/runlevel
%_man1dir/init.*
%_man8dir/halt.*
%_man8dir/reboot.*
%_man8dir/shutdown.*
%_man8dir/poweroff.*
%_man8dir/telinit.*
%_man8dir/runlevel.*
%_initdir/README

%files analyze
%_bindir/systemd-analyze

%files -n bash-completion-%name
%_sysconfdir/bash_completion.d/systemd

%files -n zsh-completion-%name
%_datadir/zsh/Completion/Unix/_systemd

%files -n python-module-%name
%python_sitelibdir/%name

%files -n bash-completion-udev
%_sysconfdir/bash_completion.d/udev

%files -n libudev1
/%_lib/libudev.so.*

%files -n libudev-devel
%_includedir/libudev.h
%_libdir/libudev.so
%_pkgconfigdir/libudev.pc
%_datadir/pkgconfig/udev.pc

%files -n libgudev
%_libdir/libgudev-*.so.*

%files -n libgudev-devel
%_includedir/gudev-1.0
%_libdir/libgudev-*.so
%_pkgconfigdir/gudev-*.pc

%files -n libgudev-gir
%_libdir/girepository-1.0/*.typelib

%files -n libgudev-gir-devel
%_datadir/gir-1.0/*.gir

%files -n udev
%doc README TODO NEWS LICENSE.GPL2
%dir %_sysconfdir/udev
%config(noreplace) %_sysconfdir/udev/*.conf
%config %_sysconfdir/scsi_id.config
%_initdir/udev*
%_unitdir/*udev*
%_unitdir/*/systemd-udev*
%dir %firmwaredir
%dir %firmwaredir/updates
%dir /lib/udev
%dir /lib/udev/devices
/lib/udev/udevd
/lib/udev/ata_id
/lib/udev/cdrom_id
/lib/udev/mtd_probe
/lib/udev/scsi_id
/sbin/udevadm
/sbin/udevd
/lib/systemd/systemd-udevd
%_man8dir/udevadm*
%_man8dir/systemd-udevd*
%_man8dir/udevd*
%_man7dir/udev*

%files -n udev-extras
%doc src/udev/keymap/README.keymap.txt
/lib/udev/accelerometer
/lib/udev/keymaps
/lib/udev/findkeyboards
/lib/udev/keymap
/lib/udev/keyboard-force-release.sh
/lib/udev/v4l_id
/lib/udev/collect
/lib/udev/rules.d/61-accelerometer.rules
/lib/udev/rules.d/75-*-description.rules
/lib/udev/rules.d/78-sound-card.rules
/lib/udev/rules.d/95-keyboard-force-release.rules
/lib/udev/rules.d/95-keymap.rules

%files -n udev-rules
%dir %_sysconfdir/udev/rules.d
%config(noreplace) %_sysconfdir/udev/rules.d/*
/lib/udev/initramfs-rules.d
/lib/udev/rules.d
# rule-generator
%exclude %_sysconfdir/udev/rules.d/70-persistent-*.rules
%exclude /lib/udev/rules.d/75-*-generator.rules
# extras
%exclude /lib/udev/rules.d/61-accelerometer.rules
%exclude /lib/udev/rules.d/75-*-description.rules
%exclude /lib/udev/rules.d/78-sound-card.rules
%exclude /lib/udev/rules.d/95-keyboard-force-release.rules
%exclude /lib/udev/rules.d/95-keymap.rules
# systemd
%exclude /lib/udev/rules.d/70-uaccess.rules
%exclude /lib/udev/rules.d/71-seat.rules
%exclude /lib/udev/rules.d/73-seat-late.rules
%exclude /lib/udev/rules.d/99-systemd.rules


%files -n udev-hwdb
%dir %_sysconfdir/udev/hwdb.d
/lib/udev/hwdb.d

%files -n udev-rule-generator
%config(noreplace,missingok) %verify(not md5 size mtime) %ghost %_sysconfdir/udev/rules.d/70-persistent-*.rules
/lib/udev/rules.d/75-*-generator.rules
/lib/udev/rule_generator.functions
/lib/udev/write_*_rules

%changelog
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
