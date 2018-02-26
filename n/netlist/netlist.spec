Name: netlist
Version: 2.1
Release: alt2

Summary: A program to list active Internet connections and sockets
License: BSD-style
Group: System/Base
Url: ftp://ftp.openwall.com/pub/patches/linux/contrib
Packager: Dmitry V. Levin <ldv@altlinux.org>

# netlist-%version.tar.gz
Source: netlist-%version.tar

%description
When run by a non-privileged user, netlist lists active Internet
connections and listening sockets of that user.

When run by root or a user with group access privileges for /proc,
netlist lists all active TCP, UDP, and raw sockets on the system.

netlist was created to oppose restrictive tendencies in security.
Your use of netlist must be in accordance with this intent.  Please see
the LICENSE for information on this and other licensing conditions.

%prep
%setup -q

%build
%make_build CFLAGS="%optflags -fno-strict-aliasing"

%install
%make_install install \
	DESTDIR=%buildroot \
	BINDIR=%_bindir \
	MANDIR=%_mandir \
	#

%files
%attr(2711,root,proc) %_bindir/netlist
%_man1dir/*
%doc LICENSE

%changelog
* Tue Apr 10 2007 Dmitry V. Levin <ldv@altlinux.org> 2.1-alt2
- Disabled gcc optimization based on strict aliasing rules.

* Thu Mar 30 2006 Dmitry V. Levin <ldv@altlinux.org> 2.1-alt1
- Updated to 2.1.

* Sun Mar 12 2006 Dmitry V. Levin <ldv@altlinux.org> 2.0-alt4
- Updated for 2.6.x kernels.

* Thu Oct 10 2002 Dmitry V. Levin <ldv@altlinux.org> 2.0-alt3
- Rebuilt in new environment.

* Tue Nov 13 2001 Dmitry V. Levin <ldv@alt-linux.org> 2.0-alt2
- Added Url (thanks to Solar for the hint).

* Mon Nov 12 2001 Dmitry V. Levin <ldv@alt-linux.org> 2.0-alt1
- ALT adaptions.

* Wed Nov 07 2001 Solar Designer <solar@owl.openwall.com>
- Wrote the man page, Makefile, and this spec file.
