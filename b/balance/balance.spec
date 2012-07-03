Name: balance
Version: 3.54
Release: alt1

Summary: TCP load-balancing proxy server
License: GPLv2
Group: System/Servers
Url: https://www.inlab.de/balance.html
Source: %name-%version.tar.gz
Packager: Michael A. Kangin <prividen@altlinux.org>

%description
Balance is a simple but powerful generic tcp proxy with round robin
load balancing and failover mechanisms.  The program behaviour can
be controlled at runtime using a simple command line syntax.

%prep
%setup 

%build
%make_build

%install
mkdir -p %buildroot{%_sbindir,%_man1dir,%_runtimedir/%name}
install -m 0755 %name %buildroot%_sbindir/
install %name.1 %buildroot%_man1dir/

%files
%_sbindir/%name
%doc README COPYING %name.pdf
%_man1dir/*
%dir %_runtimedir/%name

%changelog
* Mon Jan 30 2012 Michael A. Kangin <prividen@altlinux.org> 3.54-alt1
- Build for ALTLinux

* Fri Dec 03 2010 T.Obermair > 3.54 
- update version

* Tue Apr 08 2008 T.Obermair > 3.42 
- update version

* Sat Nov 24 2007 T.Obermair > 3.40 
- update version

* Mon Jan 15 2007 T.Obermair > 3.35 
- update version

* Sat Mar 18 2006 T.Obermair > 3.34 
- update version

* Wed Oct 19 2005 T.Obermair > 3.28 
- update version

* Fri Oct 31 2003 Bojan Smojver <bojan at rexursive dot com> 3.11-1 
- update version

* Mon Sep  22 2003 Thomas Steudten <thomas at steudten dot com> 3.10-2 
- rebuild
- fix/expand specfile
