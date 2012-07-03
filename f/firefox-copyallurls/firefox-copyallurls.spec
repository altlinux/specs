# SPEC file for SessionSaver extension

%define rname	copyallurls
%define version 0.9.7
%define release alt1
%define cid 	\{960BE052-4847-422b-9AD6-8631D3D0A607\}
%define ciddir	%firefox_noarch_extensionsdir/%cid

Name:		%firefox_name-%rname
Version:	%version
Release: 	%release

Summary:	CopyAllUrls plugin for Firefox
Summary(ru_RU.UTF-8):	расширение CopyAllUrls для Firefox

License:	%mpl 1.1 / %gpl2plus / %lgpl2plus
Group:		Networking/WWW
URL:		http://www.plasser.net/code/xul/copyallurls/
BuildArch:	noarch

Source0:	%rname-%version.xpi

Packager:       Nikolay A. Fetisov <naf@altlinux.ru>

BuildRequires(pre):	rpm-build-firefox rpm-build-licenses
BuildRequires:	unzip

%description
CopyAllUrls is an extension for Mozilla-Firefox to copy all URLs
of a browser window to the clipboard and back again. It can copy
all URLs of open tabs in plain text or structured form (html  or
stx = structured text) to clipboard. Also You can take a list of
URLs (one per line) and open all at once.

%description -l ru_RU.UTF-8
CopyAllUrls - расширение для браузеров семейства Mozilla-Firefox,
предназначенное для копирования всех URL из окна браузера в буфер
обмена и обратно. Оно может копировать все URL из открытых  табов
в виде обычного текста или в форматированном виде  (как html  или
stx - структурированный текст)  в буфер обмена.  Также  Вы можете 
взять список URL'ов (по одному в строке) и открыть их все сразу.

%prep
%setup -c

%install
mkdir -p -- %buildroot/%ciddir
cp -r -- * %buildroot/%ciddir
touch %buildroot/%ciddir/chrome.manifest

%postun
if [ "$1" = 0 ]; then
  [ ! -d "%ciddir" ] || rm -rf "%ciddir"
fi

%files
%ciddir

%changelog
* Sun Feb 05 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.9.7-alt1
- New version

* Thu Oct 20 2011 Nikolay A. Fetisov <naf@altlinux.ru> 0.9.5-alt3
- Rebuild for Firefox 7.0

* Wed Aug 24 2011 Andrey Cherepanov <cas@altlinux.org> 0.9.5-alt2
- Rebuild for Firefox 6.0

* Sat Aug 13 2011 Nikolay A. Fetisov <naf@altlinux.ru> 0.9.5-alt1
- Rebuild for Firefox 5.0
- New version

* Tue Jan 26 2010 Alexey Gladkov <legion@altlinux.ru> 0.9.0-alt2
- Rebuild for Firefox 3.6

* Wed Oct 21 2009 Nikolay A. Fetisov <naf@altlinux.ru> 0.9.0-alt1
- New version

* Sat Jun 06 2009 Alexey Gladkov <legion@altlinux.ru> 0.8.1-alt3
- Rebuild for Firefox 3.5

* Sun Mar 15 2009 Nikolay A. Fetisov <naf@altlinux.ru> 0.8.1-alt2
- Rebuild for Firefox 3.1

* Thu Jul 10 2008 Nikolay A. Fetisov <naf@altlinux.ru> 0.8.1-alt1
- New version

* Sat Dec 15 2007 Nikolay A. Fetisov <naf@altlinux.ru> 0.7.1-alt8
- Rebuild for Firefox 2.0.0.11

* Fri Nov 09 2007 Nikolay A. Fetisov <naf@altlinux.ru> 0.7.1-alt7
- Rebuild for Firefox 2.0.0.9

* Fri Oct 26 2007 Nikolay A. Fetisov <naf@altlinux.ru> 0.7.1-alt6
- Rebuild for Firefox 2.0.0.8

* Fri Aug 03 2007 Nikolay A. Fetisov <naf@altlinux.ru> 0.7.1-alt5
- Rebuild for Firefox 2.0.0.6

* Sat Jul 21 2007 Nikolay A. Fetisov <naf@altlinux.ru> 0.7.1-alt4
- Rebuild for Firefox 2.0.0.5

* Thu Jul 05 2007 Nikolay A. Fetisov <naf@altlinux.ru> 0.7.1-alt3
- Rebuild for Firefox 2.0.0.4

* Wed Mar 14 2007 Nikolay A. Fetisov <naf@altlinux.ru> 0.7.1-alt2
- Rebuild for Firefox 2.0.0.2

* Mon Dec 04 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.7.1-alt1
- New version
  - major feature enhancement
- Rebuild for Firefox 2.0
  - removes obsolete macros
  - replace 'set_firefox_noarch' macro with 'BuildArch' tag

* Sun Sep 24 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.6.2-alt4
- Rebuild for Firefox 1.5.0.7

* Wed Aug 09 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.6.2-alt3
- Rebuild for Firefox 1.5.0.6

* Tue Jun 20 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.6.2-alt2
- Rebuild with firefox 1.5.0.4

* Tue May 23 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.6.2-alt1
- New version 0.6.2
  * New option for line breaks between url-entries

* Mon May 15 2006 Alexey Gladkov <legion@altlinux.ru> 0.4.1-alt1.1.1
- NMU: rebuild with firefox 1.5.0.3
  
* Tue Nov 15 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.4.1-alt1.1
- rebuild with firefox-1.0.7 .

* Thu Aug 25 2005 Nikolay A. Fetisov <naf@altlinux.ru> 0.4.1-alt1
- Initial build for ALTLinux Sisyphus

* Mon Aug 22 2005 Nikolay A. Fetisov <naf@altlinux.ru> 0.4.1-alt0
- Initial build

