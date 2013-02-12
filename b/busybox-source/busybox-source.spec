%define bname busybox
Name: %bname-source
Version: 1.21.0
Release: alt4
Summary: Sources of %bname
License: GPLv2
Group: Development/Other
URL: http://%bname.net
Source: %bname-%version.tar
Patch: %bname-%version-%release.patch
BuildArch: noarch
Provides: %_usrsrc/%bname-%version.tar.xz
AutoReq: no
AutoProv: no

%description
BusyBox combines tiny versions of many common UNIX utilities into a single small
executable. It provides minimalist replacements for most of the utilities you
usually find in bzip2, coreutils, dhcp, diffutils, e2fsprogs, file, findutils,
gawk, grep, inetutils, less, modutils, net-tools, procps, sed, shadow, sysklogd,
sysvinit, tar, util-linux, and vim. The utilities in BusyBox often have fewer
options than their full-featured cousins; however, the options that are included
provide the expected functionality and behave very much like their larger
counterparts.
BusyBox has been written with size-optimization and limited resources in mind,
both to produce small binaries and to reduce run-time memory usage. Busybox is
also extremely modular so you can easily include or exclude commands (or
features) at compile time. This makes it easy to customize embedded systems; to
create a working system, just add /dev, /etc, and a Linux kernel. Busybox has
also been used as a component of "thin client" desktop systems, live-CD
distributions, rescue disks, installers, and so on.
BusyBox provides a fairly complete POSIX environment for any small system, both
embedded environments and more full featured systems concerned about space.
Busybox is slowly working towards implementing the full Single Unix Specification
V3 (http://www.opengroup.org/onlinepubs/009695399/), but isn't there yet (and for
size reasons will probably support at most UTF-8 for internationalization).

This package contains sources of %bname.


%prep
%setup -q -n %bname-%version
%patch -p1


%install
install -d -m 0755 %buildroot%_usrsrc
tar -chJf %buildroot%_usrsrc/%bname-%version.tar.xz .


%files
%_usrsrc/*


%changelog
* Tue Feb 12 2013 Led <led@altlinux.ru> 1.21.0-alt4
- fdisk: upstream fixes

* Fri Feb 08 2013 Led <led@altlinux.ru> 1.21.0-alt3
- upstream updates and fixes

* Wed Jan 30 2013 Led <led@altlinux.ru> 1.21.0-alt2
- upstream updates and fixes

* Sun Jan 27 2013 Led <led@altlinux.ru> 1.21.0-alt1
- 1.21.0

* Sat Nov 17 2012 Led <led@altlinux.ru> 1.20.2-alt2
- cpio: enabled some long options
- added Url

* Fri Nov 16 2012 Led <led@altlinux.ru> 1.20.2-alt1
- 1.20.2
- modprobe: add /lib/modprobe.d and /run/modprobe.d as config dirs

* Sun Jul 01 2012 Led <led@massivesolutions.co.uk> 1.20.1-alt1
- 1.20.1
