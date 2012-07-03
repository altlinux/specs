#
# lxc: linux Container library
#
# (C) Copyright IBM Corp. 2007, 2008
#
# Authors:
# Daniel Lezcano <dlezcano at fr.ibm.com>
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
#
# Spec file adapted for ALT Linux.

Name: lxc
Version: 0.7.5
Release: alt3
Packager: Denis Pynkin <dans@altlinux.org>

URL: http://lxc.sourceforge.net
Source: http://dl.sourceforge.net/sourceforge/%name/%name-%{version}.tar
Patch: %name-%version-%release.patch

Summary: %name : Linux Container
Group: System/Configuration/Other
License: LGPL
Requires: libcap gzip-utils
BuildRequires: libcap-devel docbook-utils glibc-kernheaders

%add_findreq_skiplist %_libdir/%name/templates/*

%description

The package "%name" provides the command lines to create and manage
containers.  It contains a full featured container with the isolation
/ virtualization of the pids, the ipc, the utsname, the mount points,
/proc, /sys, the network and it takes into account the control groups.
It is very light, flexible, and provides a set of tools around the
container like the monitoring with asynchronous events notification,
or the freeze of the container. This package is useful to create
Virtual Private Server, or to run isolated applications like bash or
sshd.

%package devel
Summary: development library for %name
Group: Development/Other

%description devel
The %name-devel package contains header files and library needed for
development of the linux containers.

%prep
%setup
%patch -p1

%build
CFLAGS+=-I%_includedir/linux-default/include/
%autoreconf
%configure -disable-rpath --localstatedir=%_var --with-config-path=%_var/lib/lxc
%make_build

%install
%make_install DESTDIR=%buildroot install
mkdir -p %buildroot%_localstatedir/%name
mkdir -p %buildroot%_cachedir/%name

#find %buildroot -type f -name '*.la' -exec rm -f {} ';'

#post

%files
%defattr(-,root,root)
%_bindir/*
%_libdir/*.so.*
%dir %_libexecdir/%name
%attr(4711,root,root) %_libexecdir/%name/lxc-init
%dir %_libdir/%name
%dir %_libdir/%name/rootfs
%_libdir/%name/rootfs/*
%dir %_libdir/%name/templates
%_libdir/%name/templates/*
%_man1dir/*
%_man5dir/*
%_man7dir/*
%_docdir/%name/*
%dir %_localstatedir/%name
%dir %_cachedir/%name

%files devel
%defattr(-,root,root)
%dir %_includedir/%name
%_includedir/%name/*
%_datadir/pkgconfig/*
%_libdir/*.so

%changelog
* Fri May 11 2012 Denis Pynkin <dans@altlinux.org> 0.7.5-alt3
- Merged bc31b303c48c615c2cd15dd54831e55196b983f0 to fix 
  build with new autotools

* Mon Jan 02 2012 Denis Pynkin <dans@altlinux.org> 0.7.5-alt2
- Merged 1c41ddcb4af633ac906f1d7c9ef1dc7d121d7850 for rpath option

* Mon Oct 03 2011 Denis Pynkin <dans@altlinux.org> 0.7.5-alt1
- New version
- Template for ALTLinux by Alexey Shabalin

* Thu Jul 21 2011 Denis Pynkin <dans@altlinux.org> 0.7.4.2-alt1
- New version

* Sat Apr 30 2011 Denis Pynkin <dans@altlinux.ru> 0.7.4.1-alt1
- New version

* Sun Nov 07 2010 Denis Pynkin <dans@altlinux.ru> 0.7.3-alt1
- New version

* Sat Jul 31 2010 Denis Pynkin <dans@altlinux.ru> 0.7.2-alt1
- New version

* Fri May 28 2010 Denis Pynkin <dans@altlinux.ru> 0.6.5-alt2
- added zgrep in requirements
- added patch c08556c6ece8ad8308f7636adb0ad25b60e3a16d for lazy umount

* Fri Feb 19 2010 Denis Pynkin <dans@altlinux.ru> 0.6.5-alt1
- New version

* Sat Dec 12 2009 Denis Pynkin <dans@altlinux.ru> 0.6.4-alt1
- New version

* Wed Nov 11 2009 Denis Pynkin <dans@altlinux.ru> 0.6.3-alt2
- fixed #22235 (added dirs /var/lib/lxc and /var/cache/lxc)

* Sat Jul 25 2009 Denis Pynkin <dans@altlinux.ru> 0.6.3-alt1
- New version
- Patch for --as-needed

* Thu Jul 23 2009 Denis Pynkin <dans@altlinux.ru> 0.6.2-alt1
- Initial spec for ALT Linux

* Mon Mar 24 2009 Daniel Lezcano <daniel.lezcano@free.fr> - Version 0.6.1
- Removed capability setting, let the user to do that through "lxc-setcap"

* Mon Feb 16 2009 Daniel Lezcano <daniel.lezcano@free.fr> - Version 0.6.0
- Added more capabilities to the executables

* Sun Jan 25 2009 Daniel Lezcano <daniel.lezcano@free.fr> - Version 0.6.0
- Reduced spec file

* Sun Aug 3 2008 Daniel Lezcano <dlezcano@fr.ibm.com> - Version 0.1.0
- Initial RPM release.
