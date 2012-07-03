%define cvs 20070117

Name: lbussd
Version: 0
Release: alt1.%cvs.4

Summary: LTSP.org's %name
License: LGPL 2.1+
Group: System/Configuration/Hardware

Url: http://www.ltsp.org
# see also:
# http://www.archivesat.com/post1251692.htm
# http://www.archivesat.com/post1293963.htm
Source: %name-%cvs.tar.bz2
# CVSROOT=:pserver:anonymous@cvs.ltsp.org:/usr/local/cvsroot cvs co lbussd
Patch0: %name-start.patch
Patch1: %name-icons.patch
Requires: fuse ltspfs

# Automatically added by buildreq on Mon Aug 06 2007 (-bi)
BuildRequires: perl-X11-Protocol

BuildArch: noarch
Autoreq: yes, noshell

%description
LTSP.org's %name (for local devices support).


%prep
%setup -n %name
%patch0 -p1
%patch1 -p1


%install
# %_x11sysconfdir undefined on M30
install -d -m 0755 %buildroot{%_sbindir,%_sysconfdir/X11/xinit.d}
install -m 0755 %name %buildroot%_sbindir/%name
install -m 0755 lbus_event_handler.sh %buildroot%_sbindir/lbus_event_handler.sh
install -m 0755 lbus-start %buildroot%_sysconfdir/X11/xinit.d/lbus-start
install -m 0644 ltsp-localdev.conf %buildroot%_sysconfdir/ltsp-localdev.conf


%files
%_sbindir/*
%config(noreplace) %_sysconfdir/ltsp-localdev.conf
%_sysconfdir/X11/xinit.d/lbus-start


%changelog
* Wed May 07 2008 Led <led@altlinux.ru> 0-alt1.20070117.4
- updated %name-icons.patch

* Wed May 07 2008 Led <led@altlinux.ru> 0-alt1.20070117.3
- updated %name-icons.patch

* Tue May 06 2008 Led <led@altlinux.ru> 0-alt1.20070117.2
- added %name-icons.patch

* Mon Aug 06 2007 Led <led@altlinux.ru> 0-alt1.20070117.1
- added %name-start.patch
- fixed %_sysconfdir/X11/xinit.d/lbus-start for correct detecting local
  DISPLAY
- fixed %%files
- fixed BuildRequires

* Wed Jan 17 2007 Michael Shigorin <mike@altlinux.org> 0-alt1.20070117
- built for ALT Linux
- today's CVS off cvs.ltsp.org
