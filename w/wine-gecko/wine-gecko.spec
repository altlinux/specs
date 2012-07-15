%define geckodir %_datadir/wine/gecko
%ifarch x86_64
%define curarch x86_64
%else
%define curarch x86
%endif

Name: wine-gecko
Version: 1.6
Release: alt1

Summary: Custom version of Mozilla's Gecko Layout Engine for Wine

License: MPL
Group: Office
Url: http://wiki.winehq.org/Gecko

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source0: http://prdownloads.sourceforge.net/wine/wine_gecko-%version-x86.msi
Source1: http://prdownloads.sourceforge.net/wine/wine_gecko-%version-x86_64.msi

ExclusiveArch: %{ix86} x86_64

%description
Wine implements its own version of Internet Explorer. The implementation
is based on a custom version of Mozilla's Gecko Layout Engine.
When your application tries to display a web page, it loads Wine's
custom Gecko from the file wine_gecko-%version-%curarch.msi
Wine looks for this file first in /usr/share/wine/gecko/

%install
mkdir -p %buildroot%geckodir
%ifarch x86_64
install -m 644 %SOURCE1 %buildroot%geckodir
%else
install -m 644 %SOURCE0 %buildroot%geckodir
%endif

%files
%dir %_datadir/wine/
%dir %geckodir/
%geckodir/wine_gecko-%version-%curarch.msi

%changelog
* Sun Jul 15 2012 Vitaly Lipatov <lav@altlinux.ru> 1.6-alt1
- new version 1.6 (use with wine 1.5.7 or later)

* Mon May 28 2012 Vitaly Lipatov <lav@altlinux.ru> 1.5-alt1
- new version 1.5 (use with wine 1.5.0 or later)

* Tue Dec 06 2011 Vitaly Lipatov <lav@altlinux.ru> 1.4-alt1
- new version 1.4 (use with wine 1.3.33 or later)

* Fri Aug 26 2011 Vitaly Lipatov <lav@altlinux.ru> 1.3-alt1
- new version 1.3 (use with wine 1.3.26 and later)

* Sat Mar 19 2011 Vitaly Lipatov <lav@altlinux.ru> 1.2.0-alt1
- new version 1.2.0 (use with wine 1.3.16 and later)

* Wed Dec 22 2010 Vitaly Lipatov <lav@altlinux.ru> 1.1.0-alt1
- new version 1.1.0

* Sun Dec 06 2009 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt1
- initial build for ALT Linux Sisyphus

