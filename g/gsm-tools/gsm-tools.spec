# -*- rpm-spec -*-
# $Id: gsm-tools.spec,v 1.7 2004/07/22 06:19:03 grigory Exp $

Name: gsm-tools
Version: 0.0.4
Release: alt6

Summary: gsm-tools - Tcl/Tk tools for work with GSM phones
License: GPL
Group: Communications
URL: http://gsm-tools.sourceforge.net/

BuildArch: noarch
Source0: %name-%version.tar.bz2

Requires: bwidget tk >= 8.4.0-alt1
BuildRequires: rpm-build >= 4.0.4-alt0.7 rpm-build-tcl tcl

%description
Main functions:
    Sending/recieving SMS
    Working with phone book
    Make calls, answer and busy

%prep
%setup -q -c

%build

%install 
%__mkdir_p %buildroot{%_tcldatadir/%name/,%_bindir}
%__install -m 0755 %name.tcl %buildroot%_bindir/%name
%__install -m 0644 *.tcl %buildroot%_tcldatadir/%name/
%__rm -f %buildroot%_tcldatadir/%name/%name.tcl

%files
%doc COPYING README TODO VERSION doc/config
%_bindir/*
%_tcldatadir/%{name}*

%changelog
* Mon Nov 12 2007 Grigory Milev <week@altlinux.ru> 0.0.4-alt6
- fix buildreq

* Thu Jul 22 2004 Grigory Milev <week@altlinux.ru> 0.0.4-alt5
- fixed bug #2557

* Wed Jul 30 2003 Grigory Milev <week@altlinux.ru> 0.0.4-alt4
- added configuration example to documentation

* Wed May  7 2003 Grigory Milev <week@altlinux.ru> 0.0.4-alt3
- lib_simens moved to lib_siemens (sorry, typo bug)

* Wed Mar  5 2003 Grigory Milev <week@altlinux.ru> 0.0.4-alt2
- call function fixed in lib_simens (ME45 etc.) 

* Fri Feb 28 2003 Grigory Milev <week@altlinux.ru> 0.0.4-alt1
- added bluetooth phones support (like t86)
- added auto reconect for bluetooth and IR phones

* Thu Oct 17 2002 Grigory Milev <week@altlinux.ru> 0.0.3-alt1
- initial release
