Summary: eudev - an userspace implementation of devfs
Name: eudev
Version: 3.2.9
Release: alt3

Url: https://github.com/gentoo/eudev
Group: System/Configuration/Hardware
License: GPL-2

Packager: Alexey Gladkov <legion@altlinux.ru>

Source0: %name-%version.tar
Source1: udev.filetrigger
Source2: udev-hwdb.filetrigger
Source3: udevd.init

Patch0: 0001-Rename-udev-to-eudev.patch

Buildrequires: gperf
Buildrequires: util-linux
Buildrequires: libselinux-devel
Buildrequires: libkmod-devel
Buildrequires: libblkid-devel

%define _unpackaged_files_terminate_build 1

# We need a separate version of the utilities because they have less
# dependencies (see ALT#39444).
Requires: systemd-tmpfiles-standalone

%description
Starting with the 2.5 kernel, all physical and virtual devices in a
system are visible to userspace in a hierarchal fashion through
sysfs. /sbin/hotplug provides a notification to userspace when any
device is added or removed from the system. Using these two features,
a userspace implementation of a dynamic /dev is now possible that can
provide a very flexible device naming policy

%package -n libeudev
Summary: Shared library to access udev device information
Group: System/Libraries

%description -n libeudev
This package provides shared library to access eudev device information

%package -n libeudev-devel
Summary:  Development libraries for eudev
Group:    Development/C
Requires: libeudev = %version-%release
Conflicts: libudev-devel

%description -n libeudev-devel
Header and Library files for doing development with the eudev.

%prep
%setup -q
%patch0 -p1

%build
autoreconf -f -i -s

%configure \
	--prefix=/ \
	--bindir=/bin \
	--sbindir=/sbin \
	--libdir=/lib \
	--enable-split-usr \
	--enable-manpages \
	--enable-hwdb \
	--enable-rule-generator \
#

%make_build

%install
%make_install install DESTDIR=%buildroot

# rpm posttrans filetriggers
install -pD -m755 %SOURCE1 %buildroot/%_rpmlibdir/eudev.filetrigger
install -pD -m755 %SOURCE2 %buildroot/%_rpmlibdir/eudev-hwdb.filetrigger

# service
install -pD -m755 %SOURCE3 %buildroot/%_initdir/eudevd

# Move *.pc to better place
mkdir -p -- %buildroot/%_pkgconfigdir
mv -f -- \
    %buildroot/lib/pkgconfig/*.pc \
    %buildroot/%_datadir/pkgconfig/*.pc \
    %buildroot/%_pkgconfigdir/

# Rename
mv -f -- %buildroot/%_man5dir/udev.conf.5     %buildroot/%_man5dir/eudev-udev.conf.5
mv -f -- %buildroot/%_man7dir/udev.7          %buildroot/%_man7dir/eudev.7
mv -f -- %buildroot/%_man8dir/udevd.8         %buildroot/%_man8dir/eudevd.8
mv -f -- %buildroot/%_man8dir/udevadm.8       %buildroot/%_man8dir/eudevadm.8
mv -f -- %buildroot/%_pkgconfigdir/libudev.pc %buildroot/%_pkgconfigdir/libeudev.pc

mkdir -p -- \
	%buildroot/%_sysconfdir/eudev/rules.d \
	%buildroot/%_sysconfdir/eudev/hwdb.d

cat >>%buildroot/%_sysconfdir/eudev/udev.conf <<EOF
# tmpfs options. Note that size shouldn't be less than several
# megabytes due to insane format of current udev database
# (in /run/eudev)
runfs_options="size=5m"

# tmpfs options for /dev
udevfs_options="size=5m"
EOF

# Create ghost files
touch %buildroot%_sysconfdir/eudev/hwdb.bin

rm -rf -- \
	%buildroot/%_includedir/udev.h \
	%buildroot/%_pkgconfigdir/udev.pc \
	%buildroot/lib/*.la \
	%buildroot/lib/*.a

%pre
%_sbindir/groupadd -r -f cdrom >/dev/null 2>&1 ||:
%_sbindir/groupadd -r -f tape >/dev/null 2>&1 ||:
%_sbindir/groupadd -r -f dialout >/dev/null 2>&1 ||:
%_sbindir/groupadd -r -f input >/dev/null 2>&1 ||:
%_sbindir/groupadd -r -f video >/dev/null 2>&1 ||:
%_sbindir/groupadd -r -f render >/dev/null 2>&1 ||:

%post
%post_service eudevd

%preun
%preun_service eudevd

%files
%dir %_sysconfdir/eudev
%dir %_sysconfdir/eudev/rules.d
%dir %_sysconfdir/eudev/hwdb.d
%config(noreplace) %_sysconfdir/eudev/hwdb.d/*.hwdb
%config(noreplace) %_sysconfdir/eudev/*.conf
%ghost %_sysconfdir/eudev/hwdb.bin
%_initdir/eudevd
/bin/eudevadm
/sbin/eudevd
/sbin/eudevadm
/lib/eudev
%_rpmlibdir/eudev*.filetrigger
%_man5dir/eudev*
%_man7dir/eudev*
%_man8dir/eudev*

%files -n libeudev
/lib/libeudev.so.*

%files -n libeudev-devel
%_includedir/libudev.h
/lib/libeudev.so
%_pkgconfigdir/libeudev.pc

%changelog
* Fri Feb 05 2021 Alexey Gladkov <legion@altlinux.ru> 3.2.9-alt3
- Pull upstream fixes.
- Use standalone variant of systemd-tmpfiles.
- Update License tag.

* Sat Nov 28 2020 Alexey Gladkov <legion@altlinux.ru> 3.2.9-alt2
- Rename pkg-config file.

* Wed Sep 02 2020 Alexey Gladkov <legion@altlinux.ru> 3.2.9-alt1
- New version (3.2.9).

* Tue Jan 15 2019 Alexey Gladkov <legion@altlinux.ru> 3.2.7-alt1
- New version (3.2.7).
- Rewrite init-script.

* Fri Sep 28 2018 Alexey Gladkov <legion@altlinux.ru> 3.2.6-alt1
- initial build for ALTLinux
