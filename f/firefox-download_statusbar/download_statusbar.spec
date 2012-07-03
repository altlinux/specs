# SPEC file for Download Statusbar Firefox extension

%define rname	download_statusbar
%define version 0.9.10
%define release alt1
%define cid	\{D4DD63FA-01E4-46a7-B6B1-EDAB7D6AD389\}
%define ciddir	%firefox_noarch_extensionsdir/%cid

Name:		%firefox_name-%rname
Version:	%version
Release:	%release

Summary:	Download Statusbar plugin for Firefox
Summary(ru_RU.UTF-8):	расширение Download Statusbar для Firefox

License:	%mpl 1.1 / %gpl2plus / %lgpl2plus
Group:		Networking/WWW
#URL:		http://downloadstatusbar.mozdev.org/
URL: 		https://addons.mozilla.org/ru/firefox/addon/26
BuildArch:      noarch

Source0:	%rname.xpi
Packager:       Nikolay A. Fetisov <naf@altlinux.ru>

BuildRequires(pre):	rpm-build-firefox rpm-build-licenses
BuildRequires:		unzip

%description
Download Statusbar  extension for  Firefox browser allows to view
and manage downloads from a tidy statusbar - without the download
window getting in the way of your web browsing.

%description -l ru_RU.UTF-8
Расширение Download Statusbar для Firefox позволяет просматривать и
управлять загрузками из небольшой панели внизу окна браузера  - без 
необходимости открывать отдельное окно списка загрузок.

%prep
%setup -c

# RPM call unzip with -Lq keys, effectivly kills all mixed-case filenames in archive
rm -rf -- ./*
unzip -q %SOURCE0

%install
mkdir -p -- %buildroot/%ciddir
cp -r -- * %buildroot/%ciddir

%postun
if [ "$1" = 0 ]; then
  [ ! -d "%ciddir" ] || rm -rf "%ciddir"
fi

%files
%ciddir

%changelog
* Sun Feb 05 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.9.10-alt1
- New version (0.9.10)

* Thu Aug 04 2011 Alexey Gladkov <legion@altlinux.ru> 0.9.8-alt2
- Update maxVersion according to AMO.

* Tue Apr 12 2011 Alexey Gladkov <legion@altlinux.ru> 0.9.8-alt1
- New version (0.9.8)

* Thu Jun 04 2009 Alexey Gladkov <legion@altlinux.ru> 0.9.6.5-alt1
- New version (0.9.6.5)

* Sun Mar 15 2009 Nikolay A. Fetisov <naf@altlinux.ru> 0.9.6.4-alt1
- New version

* Thu Jul 10 2008 Nikolay A. Fetisov <naf@altlinux.ru> 0.9.6.3-alt1
- New version

* Sat Dec 15 2007 Nikolay A. Fetisov <naf@altlinux.ru> 0.9.5.2-alt2
- Rebuild for Firefox 2.0.0.11

* Fri Nov 09 2007 Nikolay A. Fetisov <naf@altlinux.ru> 0.9.5.2-alt1
- New version:
  - Added new translations: sr-YU
  - Updated translations: ru-RU, zh-TW

* Fri Oct 26 2007 Nikolay A. Fetisov <naf@altlinux.ru> 0.9.5.1-alt1
- Revives from orphaned
- New version: a lot of feature enhancements
- Rename package following upstream
- Spec file cleanup

* Thu Jun 15 2006 Alexey Gladkov <legion@altlinux.ru> 1:0.9.4-alt4
- rebuild with firefox 1.5.0.4

* Mon May 15 2006 Alexey Gladkov <legion@altlinux.ru> 1:0.9.4-alt3
- rebuild with firefox 1.5.0.3

* Mon Feb 20 2006 Alexey Gladkov <legion@altlinux.ru> 1:0.9.4-alt2
- rebuild with firefox 1.5.0.1

* Tue Dec 20 2005 Alexey Gladkov <legion@altlinux.ru> 1:0.9.4-alt1
- new version.

* Thu Nov 10 2005 Konstantin A Lepikhov (L.A. Kostis) <lakostis@altlinux.ru> 1:0.9.3.1-alt4.1
- rebuild with new firefox.

* Thu Oct 13 2005 Konstantin A Lepikhov (L.A. Kostis) <lakostis@altlinux.ru> 1:0.9.3.1-alt4
- rebuild with new firefox.

* Fri Aug 26 2005 Alexey Gladkov <legion@altlinux.ru> 1:0.9.3.1-alt3
- bugfix rebuild.

* Tue Aug 16 2005 Alexey Gladkov <legion@altlinux.ru> 1:0.9.3.1-alt2
- bugfix rebuild.

* Mon Aug 08 2005 Alexey Gladkov <legion@altlinux.ru> 1:0.9.3.1-alt1
- new version.

* Mon Jun 27 2005 Alexey Gladkov <legion@altlinux.ru> 1:0.9.2-alt4
- update for new firefox;

* Wed Apr 27 2005 Alexey Gladkov <legion@altlinux.ru> 1:0.9.2-alt3
- requires fix;

* Sat Mar 05 2005 Alexey Gladkov <legion@altlinux.ru> 1:0.9.2-alt2.1
- postscript bugfix;

* Fri Jan 19 2005 Alexey Gladkov <legion@altlinux.ru> 1:0.9.2-alt2
- rebuild with new firefox.
- Requires to firefox package was relaxed.

* Fri Jan 07 2005 Alexey Gladkov <legion@altlinux.ru> 1:0.9.2-alt1
- new version;
- new extension scheme;

* Wed Oct 27 2004 Alexey Gladkov <legion@altlinux.ru> 1:0.9.1-alt2
- new version;
- Spec changes;

* Fri Feb 13 2004 Alexey Gladkov <legion@altlinux.ru> 0.82-alt1
- Mozilla Firebird becomes Mozilla Firefox. Mozilla's next 
  generation browser has changed names (again);
- New version;

* Thu Dec 04 2003 Alexey Gladkov <legion@altlinux.ru> 0.8-alt1
- first build for ALT Linux.
