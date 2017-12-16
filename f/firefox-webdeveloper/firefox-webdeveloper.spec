%define rname	webdeveloper
%define cid	\{c45c406e-ab73-11d8-be73-000a95be3b12\}
%define ciddir 	%firefox_noarch_extensionsdir/%cid

Name:		%firefox_name-%rname
Version:	2.0.1
Release:	alt1
Summary:	The Web Developer extension for Mozilla Firefox

License:	GPLv3
Group:		Networking/WWW
Url:		http://chrispederick.com/work/web-developer/

Source0:	web_developer-%version-fx+sm.xpi

BuildArch:	noarch
BuildRequires:	rpm-build-firefox unzip
Serial:		1

Packager: Sergey Kurakin <kurakin@altlinux.org>

%description 
The Web Developer extension for Mozilla Firefox and Mozilla 
adds a menu and a toolbar to the browser with various web developer tools.

%prep
%setup -c

%install
%__mkdir_p %buildroot/%ciddir
%__cp -r * %buildroot/%ciddir

%postun
if [ "$1" = 0 ]; then
  [ ! -d "%ciddir" ] || rm -rf "%ciddir"
fi

%files
%ciddir

%changelog
* Sat Dec 16 2017 Nikolay A. Fetisov <naf@altlinux.org> 1:2.0.1-alt1
- New version

* Thu Jan 07 2016 Nikolay A. Fetisov <naf@altlinux.ru> 1:1.2.5-alt3
- Signed version to work with Firefox >= 43.x

* Thu Nov 21 2013 Andrey Cherepanov <cas@altlinux.org> 1:1.2.5-alt2
- Adapt for Firefox 24.1.x

* Tue Nov 05 2013 Andrey Cherepanov <cas@altlinux.org> 1:1.2.5-alt1
- New version
- Adapt for Firefox 24.x and Seamonkey 2.22.x

* Thu Dec 20 2012 Andrey Cherepanov <cas@altlinux.org> 1:1.2.2-alt1
- New version 1.2.2

* Thu Jan 28 2010 Alexey Gladkov <legion@altlinux.ru> 1:1.1.8-alt2
- Rebuilt with firefox-3.6.

* Thu Jul  2 2009 Sergey Kurakin <kurakin@altlinux.org> 1:1.1.8-alt1
- 1.1.8
  + native support for Firefox 3.5
  + bugfixes

* Sat Jun  6 2009 Sergey Kurakin <kurakin@altlinux.org> 1:1.1.6-alt3
- allow using with Firefox 3.5

* Wed May 27 2009 Sergey Kurakin <kurakin@altlinux.org> 1:1.1.6-alt2
- some changes in upstream, not reflected in version number
  (added pt_PT translation and so on)
- allow using with Firefox 3.1
- Url corrected

* Fri Jun 13 2008 Igor Zubkov <icesik@altlinux.org> 1:1.1.6-alt1
- 1.1.5 -> 1.1.6

* Fri Apr 04 2008 Igor Zubkov <icesik@altlinux.org> 1:1.1.5-alt1
- 1.1.4 -> 1.1.5

* Thu Sep 27 2007 Igor Zubkov <icesik@altlinux.org> 1:1.1.4-alt4
- rebuild

* Thu Aug 02 2007 Igor Zubkov <icesik@altlinux.org> 1:1.1.4-alt3
- rebuild with firefox 2.0.0.6-alt1

* Fri Jul 20 2007 Igor Zubkov <icesik@altlinux.org> 1:1.1.4-alt2
- rebuild with firefox 2.0.0.5-alt1

* Fri Jul 06 2007 Igor Zubkov <icesik@altlinux.org> 1:1.1.4-alt1
- 1.0.2 -> 1.1.4 (closes #12229)

* Tue Jul 03 2007 Igor Zubkov <icesik@altlinux.org> 1:1.0.2-alt6
- rebuild with firefox 2.0.0.4-alt1

* Fri Apr 13 2007 Igor Zubkov <icesik@altlinux.org> 1:1.0.2-alt5
- rebuild with firefox 2.0.0.2-alt1

* Fri Nov 24 2006 Alexey Gladkov <legion@altlinux.ru> 1:1.0.2-alt4.1
- NMU: Fix macros for firefox-2.0.

* Wed Nov 22 2006 Igor Zubkov <icesik@altlinux.org> 1:1.0.2-alt4
- rebuild with firefox 1.5.0.7
- add packager tag

* Thu Jun 15 2006 Alexey Gladkov <legion@altlinux.ru> 1:1.0.2-alt3
- rebuild with firefox 1.5.0.4

* Mon May 15 2006 Alexey Gladkov <legion@altlinux.ru> 1:1.0.2-alt2
- rebuild with firefox 1.5.0.3
- localization added

* Mon Feb 20 2006 Alexey Gladkov <legion@altlinux.ru> 1:1.0.2-alt1
- new version.

* Mon Dec 19 2005 Alexey Gladkov <legion@altlinux.ru> 1:0.9.4-alt1
- new version.

* Thu Nov 10 2005 Konstantin A Lepikhov (L.A. Kostis) <lakostis@altlinux.ru> 1:0.9.3-alt10.1
- rebuild with new firefox.

* Thu Oct 13 2005 Konstantin A Lepikhov (L.A. Kostis) <lakostis@altlinux.ru> 1:0.9.3-alt10
- rebuild with new firefox.

* Fri Aug 26 2005 Alexey Gladkov <legion@altlinux.ru> 1:0.9.3-alt9
- bugfix rebuild.

* Tue Aug 16 2005 Alexey Gladkov <legion@altlinux.ru> 1:0.9.3-alt7
- bugfix rebuild.

* Mon Aug 08 2005 Alexey Gladkov <legion@altlinux.ru> 1:0.9.3-alt6
- update for new firefox;

* Mon Jun 27 2005 Alexey Gladkov <legion@altlinux.ru> 1:0.9.3-alt5
- update for new firefox;

* Wed Apr 27 2005 Alexey Gladkov <legion@altlinux.ru> 1:0.9.3-alt4
- requires fix;

* Sat Mar 05 2005 Alexey Gladkov <legion@altlinux.ru> 1:0.9.3-alt3.1
- postscript bugfix;

* Fri Feb 25 2005 Alexey Gladkov <legion@altlinux.ru> 1:0.9.2-alt3
- spec bugfix;

* Fri Jan 19 2005 Alexey Gladkov <legion@altlinux.ru> 1:0.9.2-alt2
- rebuild with new firefox.
- Requires to firefox package was relaxed.

* Thu Jan 06 2005 Alexey Gladkov <legion@altlinux.ru> 1:0.9.2-alt1
- New version 0.9.2

* Wed Oct 27 2004 Alexey Gladkov <legion@altlinux.ru> 1:0.8-alt2
- New Version 0.8;
- Spec changes;
- New Extension scheme.

* Fri Feb 13 2004 Alexey Gladkov <legion@altlinux.ru> 0.61-alt1
- Mozilla Firebird becomes Mozilla Firefox. Mozilla's next 
  generation browser has changed names (again);
- New version;

* Sun Dec 28 2003 Alexey Gladkov <legion@altlinux.ru> 0.5-alt1
- new version.

* Thu Dec 04 2003 Alexey Gladkov <legion@altlinux.ru> 0.4-alt1
- first build for ALT Linux.
