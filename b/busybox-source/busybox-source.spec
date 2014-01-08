%define bname busybox
Name: %bname-source
Version: 1.22.0
Release: alt1
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
* Wed Jan 08 2014 Led <led@altlinux.ru> 1.22.0-alt1
- 1.22.0

* Sat Dec 21 2013 Led <led@altlinux.ru> 1.21.1-alt26
- upstream fixes

* Thu Dec 19 2013 Led <led@altlinux.ru> 1.21.1-alt25
- upstream updates and fixes

* Thu Dec 12 2013 Led <led@altlinux.ru> 1.21.1-alt24
- upstream updates for ntpd applet

* Sun Dec 01 2013 Led <led@altlinux.ru> 1.21.1-alt23
- upstream updates and fixes

* Thu Nov 28 2013 Led <led@altlinux.ru> 1.21.1-alt22
- upstream updates and fixes

* Wed Nov 20 2013 Led <led@altlinux.ru> 1.21.1-alt21
- upstream updates and fixes
- modprobe: add more options for compatibility reason

* Tue Nov 12 2013 Led <led@altlinux.ru> 1.21.1-alt20
- upstream fixes

* Mon Nov 11 2013 Led <led@altlinux.ru> 1.21.1-alt19
- upstream updates and fixes

* Thu Nov 07 2013 Led <led@altlinux.ru> 1.21.1-alt18
- find: made '-wholename' key don't depends on ENABLE_DESKTOP

* Thu Nov 07 2013 Led <led@altlinux.ru> 1.21.1-alt17
- find: fixed using "." if PATH unspecified

* Sun Nov 03 2013 Led <led@altlinux.ru> 1.21.1-alt16
- upstream updates and fixes

* Thu Sep 12 2013 Led <led@altlinux.ru> 1.21.1-alt15
- upstream updates and fixes

* Sat Sep 07 2013 Led <led@altlinux.ru> 1.21.1-alt14
- upstream updates and fixes

* Tue Aug 20 2013 Led <led@altlinux.ru> 1.21.1-alt13
- upstream updates and fixes
- find: use "." if PATH unspecified

* Sun Aug 18 2013 Led <led@altlinux.ru> 1.21.1-alt12
- upstream updates and fixes

* Sun Aug 11 2013 Led <led@altlinux.ru> 1.21.1-alt11
- upstream updates

* Wed Aug 07 2013 Led <led@altlinux.ru> 1.21.1-alt10
- upstream updates

* Sun Aug 04 2013 Led <led@altlinux.ru> 1.21.1-alt9
- config: add FEATURE_VOLUMEID_F2FS

* Sun Aug 04 2013 Led <led@altlinux.ru> 1.21.1-alt8
- volume_id: add f2fs detection

* Thu Aug 01 2013 Led <led@altlinux.ru> 1.21.1-alt7
- upstream fixes:
  + awk: Fix handling of functions with empty body

* Mon Jul 29 2013 Led <led@altlinux.ru> 1.21.1-alt6
- upstream updates and fixes

* Mon Jul 08 2013 Led <led@altlinux.ru> 1.21.1-alt5
- upstream fixes

* Sat Jul 06 2013 Led <led@altlinux.ru> 1.21.1-alt4
- upstream fixes

* Wed Jul 03 2013 Led <led@altlinux.ru> 1.21.1-alt3
- upstream fixes

* Tue Jul 02 2013 Led <led@altlinux.ru> 1.21.1-alt2
- upstream fixes

* Mon Jul 01 2013 Led <led@altlinux.ru> 1.21.1-alt1
- 1.21.1

* Thu Jun 20 2013 Led <led@altlinux.ru> 1.21.0-alt15
- upstream fixes

* Thu May 23 2013 Led <led@altlinux.ru> 1.21.0-alt14
- upstream updates and fixes

* Mon May 20 2013 Led <led@altlinux.ru> 1.21.0-alt13
- reverts for fix build 'find' applet

* Mon May 20 2013 Led <led@altlinux.ru> 1.21.0-alt12
- upstream updates and fixes

* Wed May 15 2013 Led <led@altlinux.ru> 1.21.0-alt11
- upstream updates and fixes

* Mon May 13 2013 Led <led@altlinux.ru> 1.21.0-alt10
- upstream updates and fixes

* Fri Apr 19 2013 Led <led@altlinux.ru> 1.21.0-alt9
- upstream updates and fixes

* Wed Mar 06 2013 Led <led@altlinux.ru> 1.21.0-alt8
- upstream updates and fixes

* Sun Mar 03 2013 Led <led@altlinux.ru> 1.21.0-alt7
- upstream updates and fixes

* Thu Feb 28 2013 Led <led@altlinux.ru> 1.21.0-alt6
- upstream updates and fixes
- find: implemented '-execdir' option

* Thu Feb 21 2013 Led <led@altlinux.ru> 1.21.0-alt5
- rpm: upstream updates

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
