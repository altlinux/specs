%define pkgname ALT-bugzilla

Name: fortunes-%pkgname
Version: 20100629
Release: alt1

Summary: ALT Linux Team members' quotes from ALT Linux Bugzilla
Group: Games/Other
License: distributable
Url: http://bugzilla.altlinux.org/

Packager: Andrey Rahmatullin <wrar@altlinux.ru>

BuildArch: noarch

Source: %name

BuildPreReq: fortune-mod >= 1.0-ipl33mdk
PreReq: fortune-mod >= 1.0-ipl33mdk

%description
ALT Linux Team members' quotes from ALT Linux Bugzilla

%install
install -pD -m644 %SOURCE0 %buildroot%_gamesdatadir/fortune/%pkgname
strfile %buildroot%_gamesdatadir/fortune/%pkgname %buildroot%_gamesdatadir/fortune/%pkgname.dat

%files
%_gamesdatadir/fortune/%{pkgname}*

%changelog
* Tue Jun 29 2010 Andrey Rahmatullin <wrar@altlinux.ru> 20100629-alt1
- 19 new quotes

* Thu Aug 20 2009 Andrey Rahmatullin <wrar@altlinux.ru> 20090820-alt1
- 27 new quotes

* Tue Aug 05 2008 Andrey Rahmatullin <wrar@altlinux.ru> 20080805-alt1
- 51 new quotes

* Sun Nov 18 2007 Andrey Rahmatullin <wrar@altlinux.ru> 20071118-alt1
- 32 new quotes

* Thu Apr 12 2007 Andrey Rahmatullin <wrar@altlinux.ru> 20070412-alt1
- 38 new quotes

* Thu Sep 28 2006 Andrey Rahmatullin <wrar@altlinux.ru> 20060928-alt1
- 31 new quotes
- generate dat file at build time

* Fri Jan 27 2006 Andrey Rahmatullin <wrar@altlinux.ru> 20060127-alt1
- 25 new quotes

* Sun Sep 25 2005 Andrey Rahmatullin <wrar@altlinux.ru> 20050925-alt1
- 30 new quotes

* Fri Jul 22 2005 Andrey Rahmatullin <wrar@altlinux.ru> 20050722-alt1
- initial build

