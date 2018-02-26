Name: postfix-control
Version: 1.6.1
Release: alt1

Summary: Postfix Mail Transport Agent facility control
License: GPL
Group: System/Servers
BuildArch: noarch
Packager: Dmitry V. Levin <ldv@altlinux.org>

Source0: postfix.control
Source1: postqueue.control

%description
This package contains control rules for the Postfix MTA facility.
See control(8) for details.

%install
install -pD -m755 %_sourcedir/postfix.control \
	%buildroot%_controldir/postfix
install -pD -m755 %_sourcedir/postqueue.control \
	%buildroot%_controldir/postqueue

%files
%config %_controldir/*

%changelog
* Wed Feb 28 2007 Dmitry V. Levin <ldv@altlinux.org> 1.6.1-alt1
- postfix control: Optimize; relax smtp regexp.

* Mon Feb 26 2007 Stanislav Ievlev <inger@altlinux.org> 1.6-alt1
- postfix control: New state set:
  local, server without content filter, server with content filter.

* Wed Feb 14 2007 Dmitry V. Levin <ldv@altlinux.org> 1.5-alt1
- postqueue control: Add /usr/libexec/postfix/postqueue support.

* Sat Dec 09 2006 Dmitry V. Levin <ldv@altlinux.org> 1.4-alt1
- Added summary to control files.

* Sat Oct 02 2004 Dmitry V. Levin <ldv@altlinux.org> 1.3-alt1
- Added help.

* Mon Apr 19 2004 Dmitry V. Levin <ldv@altlinux.org> 1.2-alt1
- postfix.control: optimized, to avoid unneeded config edits
  and server reloads.

* Wed Oct 22 2003 Dmitry V. Levin <ldv@altlinux.org> 1.1-alt1
- Added control(8) support for postqueue.

* Mon Oct 20 2003 Dmitry V. Levin <ldv@altlinux.org> 1.0-alt1
- Initial revision.
