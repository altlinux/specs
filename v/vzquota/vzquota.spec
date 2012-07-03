Name: vzquota
Version: 3.0.12
Release: alt2

Summary: OpenVZ disk quota control utilities
License: GPL
Group: System/Configuration/Other
Url: http://openvz.org/
Packager: Dmitry V. Levin <ldv@altlinux.org>

# http://download.openvz.org/utils/%name/%version/src/%name-%version.tar.bz2
Source: %name-%version-%release.tar

%description
OpenVZ is an OS-level server virtualization solution, built on Linux.
OpenVZ creates isolated, secure virtual private servers on a single
physical server enabling better server utilization and ensuring that
applications do not conflict.  Each container performs and executes
exactly like a stand-alone server; containers can be rebooted
independently and have root access, users, IP addresses, memory,
processes, files, applications, system libraries and configuration files.

This package contains utilities to manipulate disk quotas for containers.

%prep
%setup -q -n %name-%version-%release

%build
export CFLAGS="%optflags"
%make_build VARDIR=/var/lib

%install
make install DESTDIR=%buildroot MANDIR=%_mandir VARDIR=/var/lib

%files
%_sbindir/*
/var/lib/*
%_man8dir/*
%doc doc/*

%changelog
* Tue May 19 2009 Dmitry V. Levin <ldv@altlinux.org> 3.0.12-alt2
- Fixed build with fresh toolchain.

* Tue Nov 11 2008 Dmitry V. Levin <ldv@altlinux.org> 3.0.12-alt1
- Updated to 3.0.12.

* Thu Aug 16 2007 Dmitry V. Levin <ldv@altlinux.org> 3.0.11-alt1
- Updated to 3.0.11.

* Mon Oct 09 2006 Dmitry V. Levin <ldv@altlinux.org> 3.0.9-alt1
- Updated to 3.0.9.

* Thu Jun 15 2006 Dmitry V. Levin <ldv@altlinux.org> 3.0.8-alt1
- Adopted for Sisyphus.

* Tue Apr 18 2006 Kir Kolyshkin <kir-at-openvz.org> 3.0.0-5
- fixed license in man pages

* Wed Mar 15 2006 Andrey Mirkin <amirkin-at-sw.ru> 3.0.0-3
- added new function to reload 2nd level quota

* Mon Feb  6 2006 Kir Kolyshkin <kir-at-openvz.org> 3.0.0-2
- fixed gcc4 compilation issue

* Fri Sep 09 2005 Dmitry Mishin <dim_at_sw.ru> 2.7.0-7
- fixes to use new vzkernel headers provisioning scheme

* Thu Aug 11 2005 Dmitry Mishin <dim_at_sw.ru> 2.7.0-5
- reworked hard links check
- mans fixes

* Sat Aug 06 2005 Dmitry Mishin <dim_at_sw.ru> 2.7.0-4
- adopted for new vzctl_quota ioctls
