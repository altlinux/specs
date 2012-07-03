Name: fwbuilder
Version: 5.1.0.3599
Release: alt1

Summary: Firewall Builder
License: GPLv2+
Group: Security/Networking

Url: http://www.fwbuilder.org/
Source0: http://downloads.sourceforge.net/fwbuilder/fwbuilder-%version.tar.gz
Source1: fwbuilder.desktop

Obsoletes: fwbuilder-doc fwbuilder-devel
# libfwbuilder merged into fwbuilder package
Obsoletes: libfwbuilder

# Historically ipt is a separate subpackage but required by main package.
# This makes little sense, probably we should just merge it to main package
# (so fwbuilder will contain iptables compiler by default).
# This is only matter of package size, separated compilers contains no
# additional runtime deps.
Requires: fwbuilder-ipt = %version-%release

# Automatically added by buildreq on Thu Mar 18 2010
BuildRequires: cppunit-devel gcc-c++ libnet-snmp-devel libqt4-devel libxslt-devel

%description
Firewall Builder consists of a GUI and set of policy compilers for various
firewall platforms. It helps users maintain a database of objects and allows
policy editing using simple drag-and-drop operations. GUI generates firewall
description in the form of XML file, which compilers then interpret and generate
platform-specific code. Several algorithms are provided for automated network
objects discovery and bulk import of data. The GUI and policy compilers are
completely independent, this provides for a consistent abstract model and the
same GUI for different firewall platforms.

%package pf
Summary: Policy compiler for OpenBSD pf
Group: Security/Networking
Requires: %name = %version-%release

%description pf
Policy compiler for OpenBSD PF.

%package ipf
Summary: Policy compiler for ipfilter
Group: Security/Networking
Requires: %name = %version-%release

%description ipf
Policy compiler for ipfilter.

%package ipfw
Summary: Policy compiler for ipfw
Group: Security/Networking
Requires: %name = %version-%release

%description ipfw
Policy compiler for ipfw.

%package ipt
Summary: Policy compiler for iptables
Group: Security/Networking
Requires: %name = %version-%release

%description ipt
Policy compiler for iptables.

%package cisco
Summary: Policy compiler for Cisco routers/firewalls
Group: Security/Networking
Requires: %name = %version-%release

%description cisco
Policy compiler for Cisco routers/firewalls.

%package procurve
Summary: Policy compiler for HP ProCurve ACL
Group: Security/Networking
Requires: %name = %version-%release

%description procurve
Policy compiler for HP ProCurve ACL.

%prep
%setup

%build
libtoolize --force --copy --install
aclocal
autoconf
%configure --with-templatedir=%_datadir/%name
%make_build

%install
%make INSTALL_ROOT=%buildroot install
# freedesktop menu entry
install -pD -m644 %SOURCE1 %buildroot%_desktopdir/%name.desktop

install -pm644 doc/transfer_secuwall.1 %buildroot%_man1dir/

# No, thanks...
rm -rf %buildroot%_defaultdocdir

%files
%_bindir/fwbuilder
%_bindir/fwbedit
%_datadir/%name
%_desktopdir/*.desktop
%_miconsdir/fwbuilder.png
%_niconsdir/fwbuilder.png
%_liconsdir/fwbuilder.png
%_iconsdir/hicolor/128x128/apps/fwbuilder.png
%_iconsdir/hicolor/24x24/apps/fwbuilder.png
%_iconsdir/hicolor/72x72/apps/fwbuilder.png
%_iconsdir/hicolor/256x256/apps/fwbuilder.png
%_iconsdir/hicolor/512x512/apps/fwbuilder.png
%_man1dir/fwbuilder.1*
%_man1dir/fwbedit.1*
%_man1dir/transfer_secuwall.1*

%files pf
%_bindir/fwb_pf
%_man1dir/fwb_pf.1*

%files ipf
%_bindir/fwb_ipf
%_man1dir/fwb_ipf.1*

%files ipfw
%_bindir/fwb_ipfw
%_man1dir/fwb_ipfw.1*

%files ipt
%_bindir/fwb_ipt
%_man1dir/fwb_ipt.1*

%files cisco
%_bindir/fwb_pix
%_bindir/fwb_iosacl
%_man1dir/fwb_pix*
%_man1dir/fwb_iosacl*

%files procurve
%_bindir/fwb_procurve_acl

%changelog
* Fri Mar 30 2012 Victor Forsiuk <force@altlinux.org> 5.1.0.3599-alt1
- 5.1.0.3599

* Tue Jan 03 2012 Victor Forsiuk <force@altlinux.org> 5.0.1.3592-alt1
- 5.0.1.3592

* Sun Jul 31 2011 Victor Forsiuk <force@altlinux.org> 5.0.0.3568-alt1
- 5.0.0.3568

* Sun Jun 19 2011 Victor Forsiuk <force@altlinux.org> 4.2.2.3541-alt1
- 4.2.2.3541

* Fri Dec 10 2010 Victor Forsiuk <force@altlinux.org> 4.1.3-alt1
- 4.1.3

* Mon Oct 18 2010 Victor Forsiuk <force@altlinux.org> 4.1.2-alt1
- 4.1.2

* Wed Sep 08 2010 Victor Forsiuk <force@altlinux.org> 4.1.1-alt1
- 4.1.1

* Tue Aug 10 2010 Victor Forsiuk <force@altlinux.org> 4.1.0-alt1
- 4.1.0

* Fri Jun 18 2010 Victor Forsiuk <force@altlinux.org> 4.0.2-alt1
- 4.0.2

* Thu Mar 18 2010 Victor Forsiuk <force@altlinux.org> 4.0.0-alt1
- 4.0.0

* Mon Sep 28 2009 Victor Forsyuk <force@altlinux.org> 3.0.7-alt1
- 3.0.7

* Thu Jul 09 2009 Victor Forsyuk <force@altlinux.org> 3.0.5-alt1
- 3.0.5

* Fri Dec 12 2008 Victor Forsyuk <force@altlinux.org> 3.0.3-alt1
- 3.0.3

* Sun Dec 24 2006 Valery Inozemtsev <shrek@altlinux.ru> 2.1.8-alt1
- 2.1.8

* Fri Nov 03 2006 Valery Inozemtsev <shrek@altlinux.ru> 2.1.7-alt2
- fixed compilers name

* Wed Nov 01 2006 Valery Inozemtsev <shrek@altlinux.ru> 2.1.7-alt1
- 2.1.7

* Sun May 07 2006 Valery Inozemtsev <shrek@altlinux.ru> 2.0.12-alt2
- updated build dependencies

* Sun Apr 23 2006 Valery Inozemtsev <shrek@altlinux.ru> 2.0.12-alt1
- 2.0.12

* Sun Apr 09 2006 Valery Inozemtsev <shrek@altlinux.ru> 2.0.11-alt1
- 2.0.11

* Fri Mar 31 2006 Valery Inozemtsev <shrek@altlinux.ru> 2.0.10-alt3
- rebuild with libbind-9.3.2

* Tue Jan 10 2006 Valery Inozemtsev <shrek@altlinux.ru> 2.0.10-alt2
- move to freedesktop menu

* Wed Nov 16 2005 Valery Inozemtsev <shrek@altlinux.ru> 2.0.10-alt1
- 2.0.10

* Sun Sep 18 2005 Valery Inozemtsev <shrek@altlinux.ru> 2.0.9-alt1
- 2.0.9

* Sun Jul 10 2005 Valery Inozemtsev <shrek@altlinux.ru> 2.0.8-alt1
- 2.0.8

* Sat May 14 2005 Valery Inozemtsev <shrek@altlinux.ru> 2.0.7-alt1
- 2.0.7

* Mon Feb 21 2005 Valery Inozemtsev <shrek@altlinux.ru> 2.0.6-alt1
- 2.0.6

* Mon Jan 17 2005 Valery Inozemtsev <shrek@altlinux.ru> 2.0.5-alt1
- 2.0.5

* Sat Dec 04 2004 Valery Inozemtsev <shrek@altlinux.ru> 2.0.4-alt1
- 2.0.4

* Fri Nov 12 2004 ALT QA Team Robot <qa-robot@altlinux.org> 2.0.3-alt1.1
- Removed libelf-devel from build dependencies.

* Sun Oct 03 2004 Valery Inozemtsev <shrek@altlinux.ru> 2.0.3-alt1
- 2.0.3

* Sat Sep 04 2004 Valery Inozemtsev <shrek@altlinux.ru> 2.0.2-alt1
- 2.0.2

* Fri Aug 13 2004 Valery Inozemtsev <shrek@altlinux.ru> 2.0.1-alt1
- bugfix release

* Wed Aug 11 2004 Valery Inozemtsev <shrek@altlinux.ru> 2.0.0-alt3
- fix spec file

* Thu Jul 29 2004 Valery Inozemtsev <shrek@altlinux.ru> 2.0.0-alt2
- 2.0.0 release

* Mon Jul 26 2004 Valery Inozemtsev <shrek@altlinux.ru> 2.0.0-alt1.20040726
- the latest nightly build 2004.07.25

* Sat Jul 03 2004 Valery Inozemtsev <shrek@altlinux.ru> 2.0.0-alt1.20040703
- the latest nightly build 2004.07.03

* Tue Jun 29 2004 Valery Inozemtsev <shrek@altlinux.ru> 2.0.0-alt1.20040629
- the latest nightly build 2004.06.29

* Sun Jun 27 2004 Valery Inozemtsev <shrek@altlinux.ru> 2.0.0-alt1.20040625
- the latest nightly build 2004.06.25

* Fri May 14 2004 Valery Inozemtsev <shrek@altlinux.ru> 1.1.2-alt2
- Rebuilt with openssl-0.9.7d

* Wed Feb 04 2004 Valery Inozemtsev <shrek@altlinux.ru> 1.1.2-alt1
- new version

* Sun Dec 14 2003 Valery Inozemtsev <shrek@altlinux.ru> 1.1.1-alt1
- New version

* Mon Nov 3 2003 Valery Inozemtsev <shrek@altlinux.ru> 1.0.11-alt1
- Build for ALT Linux Master 2.2
- Add menu entry

* Thu Jul 17 2003 Valery Inozemtsev <shrek@altlinux.ru> 1.0.10-alt1
- Add initialization script for firewall daemon

* Sun Jul 13 2003 Valery Inozemtsev <shrek@altlinux.ru> 1.0.10-alt0
- initial ALT Linux Master 2.2 build
