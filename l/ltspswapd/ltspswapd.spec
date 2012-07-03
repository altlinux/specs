%define cvs 20070117

Name: ltspswapd
Version: 0
Release: alt5.%cvs

Summary: LTSP.org's %name
License: GPL
Group: System/Configuration/Hardware

Url: http://www.altlinux.org/LTSP
# see also:
# http://www.archivesat.com/post1251692.htm
# http://www.archivesat.com/post1293963.htm
Source0: %name-%cvs.tar.bz2
# CVSROOT=:pserver:anonymous@cvs.ltsp.org:/usr/local/cvsroot cvs co lbussd
Source1: %name.init
# RHL: http://marc.theaimsgroup.com/?l=ltsp-discuss&m=115770699211895&w=3
Source2: %name.sysconfig
Packager: Michael Shigorin <mike@altlinux.org>

%description
LTSP.org's %name (for networked swap support)

See http://ltsp4.2.revamp-it.ch/twiki/bin/view/ltsp/Swap
regarding configuration

%prep
%setup -n %name

%build
%configure
%make

%install
%makeinstall bindir=%buildroot%_sbindir
install -pDm755 %SOURCE1 %buildroot%_initdir/%name
install -pDm644 %SOURCE2 %buildroot%_sysconfdir/sysconfig/%name
mkdir -p %buildroot%_spooldir/ltspswap

%files
%_sbindir/* 
%_initdir/*
%attr(700,root,root) %_spooldir/ltspswap
%_sysconfdir/sysconfig/%name

%post
%post_service %name

%preun
%preun_service %name

%changelog
* Wed Mar 07 2012 Michael Shigorin <mike@altlinux.org> 0-alt5.20070117
- dropped default swap size down to 64M (as was documented anyways)
  since it's plenty of space for ramzswap's compressed backing dev

* Wed Apr 11 2007 Michael Shigorin <mike@altlinux.org> 0-alt4.20070117
- split variables in sysconfig file (led@'s proposal)

* Mon Mar 26 2007 Michael Shigorin <mike@altlinux.org> 0-alt3.20070117
- uncommented ARGS in default configuration file (I've missed somehow
  that it wouldn't even start without explicit values)

* Thu Jan 18 2007 Michael Shigorin <mike@altlinux.org> 0-alt2.20070117
- added missing initscript (oops; still adapted/rewritten one)
- added spool directory
- added sysconfig file
- how did I manage to miss all of these compared to ltsp-server-pkg-fedora?
  (probably not even trying to use the package right away does help)

* Wed Jan 17 2007 Michael Shigorin <mike@altlinux.org> 0-alt1.20070117
- built for ALT Linux
- today's CVS off cvs.ltsp.org
- put binary to %_sbindir, not %_bindir

