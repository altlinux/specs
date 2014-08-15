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
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
#
# Spec file adapted for ALT Linux.

%global with_systemd 1
%define init_script systemd

Name: lxc
Version: 1.0.5
Release: alt1
Packager: Denis Pynkin <dans@altlinux.org>

URL: https://linuxcontainers.org/
Source: %name-%version.tar
Patch: %name-%version-%release.patch

Summary: %name : Linux Container
Group: System/Configuration/Other
License: LGPL
Requires: libcap gzip-utils
BuildRequires: libcap-devel docbook-utils glibc-kernheaders
BuildRequires: docbook2X xsltproc
BuildRequires: rpm-macros-alternatives

# Needed to disable auto requirements from distro templates
%add_findreq_skiplist %_datadir/%name/*

Requires: openssl rsync
BuildRequires: libcap libcap-devel docbook2X graphviz

BuildRequires: systemd-devel

%description
Containers are insulated areas inside a system, which have their own namespace
for filesystem, network, PID, IPC, CPU and memory allocation and which can be
created using the Control Group and Namespace features included in the Linux
kernel.

This package provides the lxc-* tools, which can be used to start a single
daemon in a container, or to boot an entire "containerized" system, and to
manage and debug your containers.

%package	libs
Summary:	Shared library files for %{name}
Group:		System/Configuration/Other
%description	libs
The %{name}-libs package contains libraries for running %{name} applications.

%package	python3
Summary:	Python 3 bindings to %{name}
Group:		System/Configuration/Other
Requires: python3
BuildRequires: python3-devel
BuildRequires: rpm-build-python3
%description	python3
The %{name}-python package contains %{name} bindings for Python 3.

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
%configure -disable-rpath \
    --localstatedir=%_var \
    --with-config-path=%_var/lib/lxc \
    --enable-python \
    --disable-lua \
    --with-init-script=%{init_script}

%make_build

%install
%make_install DESTDIR=%buildroot install
mkdir -p %buildroot%_localstatedir/%name
mkdir -p %buildroot%_cachedir/%name

#find %buildroot -type f -name '*.la' -exec rm -f {} ';'

# rename python version of lxc-ls and install legacy one
%__mv %buildroot%{_bindir}/lxc-ls %buildroot%{_bindir}/lxc-ls.py
%__install -m 0755 src/lxc/legacy/lxc-ls %buildroot%{_bindir}/lxc-ls.sh

# add alternatives
install -d %buildroot//etc/alternatives/packages.d
cat >%buildroot%_altdir/%name-legacy <<__EOF__
%{_bindir}/lxc-ls	%{_bindir}/lxc-ls.sh	100
__EOF__

cat >%buildroot%_altdir/%name <<__EOF__
%{_bindir}/lxc-ls	%{_bindir}/lxc-ls.py	1000
__EOF__

#post

%files
%defattr(-,root,root)
%exclude %{_bindir}/lxc-ls.py
%exclude %{_bindir}/lxc-start-ephemeral
%exclude %{_bindir}/lxc-device
%{_bindir}/*
%{_mandir}/man1/lxc*
%{_mandir}/man5/lxc*
%{_mandir}/man7/lxc*
%{_mandir}/ja/man1/lxc*
%{_mandir}/ja/man5/lxc*
%{_mandir}/ja/man7/lxc*
%{_datadir}/doc/*
%{_datadir}/lxc/*
%{_sysconfdir}/bash_completion.d/*
%config(noreplace) %{_sysconfdir}/lxc/*
%{_unitdir}/lxc.service
%config %_altdir/%name-legacy

%files libs
%defattr(-,root,root)
%{_sbindir}/*
%{_libdir}/*.so.*
%{_libdir}/%{name}
%{_localstatedir}/*
%{_libexecdir}/%{name}
%attr(4111,root,root) %{_libexecdir}/%{name}/lxc-user-nic

%if %{with_systemd}
%attr(555,root,root) %{_libexecdir}/%{name}/lxc-devsetup
%attr(555,root,root) %{_libexecdir}/%{name}/lxc-autostart-helper
%endif

%files python3
%defattr(-,root,root)
%{_bindir}/lxc-ls.py
%{_bindir}/lxc-start-ephemeral
%{_bindir}/lxc-device
%{python3_sitelibdir}/_lxc*
%{python3_sitelibdir}/lxc/*
%config %_altdir/%name

%files devel
%defattr(-,root,root)
%{_includedir}/%{name}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*


%changelog
* Fri Aug 15 2014 Denis Pynkin <dans@altlinux.org> 1.0.5-alt1
- New version

* Fri Aug 15 2014 Denis Pynkin <dans@altlinux.org> 1.0.4-alt2
- Fixed: #30154 #30119
- New subpackage lxc-python3
- Build both lxc-ls -- legacy and python.
  Correct version is selected via alternatives
- Fixed: #30158 #30159
- Updated template for ALTLinux
- Now used default list of packages in case
  if /etc/lxc/profiles/default is absent


* Sat Jun 14 2014 Denis Pynkin <dans@altlinux.org> 1.0.4-alt1
- New version

* Sun Nov 24 2013 Denis Pynkin <dans@altlinux.org> 0.9.0-alt3
- Fixed rebuild problem

* Mon Jul 01 2013 Denis Pynkin <dans@altlinux.org> 0.9.0-alt2
- 0.9.0 release
- fixed #29113, Thanks to legion@.

* Sun Mar 10 2013 Denis Pynkin <dans@altlinux.org> 0.9.0-alt1.alpha3
- New version

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
