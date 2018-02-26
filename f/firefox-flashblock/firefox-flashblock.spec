# SPEC file for FlashBlock extension

%define rname	flashblock
%define version 1.5.15.1
%define release alt3
%define cid 	\{3d7eb24f-2740-49df-8937-200b1cc08f8a\}
%define ciddir	%firefox_noarch_extensionsdir/%cid

Name:		%firefox_name-%rname
Version:	%version
Release:	%release

Summary:	FlashBlock plugin for Firefox
Summary(ru_RU.UTF-8):	расширение FlashBlock для Firefox

License:	%mpl 1.1 / %gpl2plus / %lgpl2plus
Group:		Networking/WWW
URL:		http://flashblock.mozdev.org/
BuildArch:	noarch

Source0:	%rname-%version.xpi

Packager:       Nikolay A. Fetisov <naf@altlinux.ru>

BuildRequires(pre): rpm-build-firefox rpm-build-licenses
BuildRequires:  unzip

%description 	
FlashBlock is an extension for the Mozilla, Firefox,  and Netscape
browsers  that  takes  a   pessimistic  approach  to dealing  with 
Macromedia Flash content on a webpage and blocks ALL Flash content
from loading.   It then  leaves placeholders  on the  webpage that 
allow you to click to download and then view the Flash content. 

%description -l ru_RU.UTF-8
FlashBlock - расширение для браузеров семейства Mozilla-Firefox,
предназначенное для блокирования загрузки всех расположенных на
странице объектов Flash.  Вместо роликов Flash на страницу 
вставляются ссылки, позволяющие загрузить и просмотреть их.

%prep
%setup -c

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
* Wed Jan 25 2012 Mykola Grechukh <gns@altlinux.ru> 1.5.15.1-alt3
- Support for firefox 9.0+

* Thu Jan 19 2012 Alexey Gladkov <legion@altlinux.ru> 1.5.15.1-alt2
- Rebuilt with firefox-9.0.1

* Thu Aug 04 2011 Alexey Gladkov <legion@altlinux.ru> 1.5.15.1-alt1
- New version (1.5.15.1).

* Tue Apr 05 2011 Mykola Grechukh <gns@altlinux.ru> 1.5.14.2-alt1
- new version

* Wed Oct 21 2009 Nikolay A. Fetisov <naf@altlinux.ru> 1.5.11-alt1
- New version 1.5.11

* Thu Jun 04 2009 Alexey Gladkov <legion@altlinux.ru> 1.5.10-alt1
- New version 1.5.10

* Sun Mar 15 2009 Nikolay A. Fetisov <naf@altlinux.ru> 1.5.8-alt1
- New version

* Sun Dec 14 2008 Nikolay A. Fetisov <naf@altlinux.ru> 1.5.7.1-alt1
- New version 1.5.7.1

* Thu Jul 10 2008 Nikolay A. Fetisov <naf@altlinux.ru> 1.5.6-alt1
- New version

* Sat Dec 15 2007 Nikolay A. Fetisov <naf@altlinux.ru> 1.5.5-alt1
- New version
  - several bugfixes
  - adding bg-BG and uk-UA locales

* Fri Nov 09 2007 Nikolay A. Fetisov <naf@altlinux.ru> 1.5.4.1-alt3
- Rebuild for Firefox 2.0.0.9

* Fri Oct 26 2007 Nikolay A. Fetisov <naf@altlinux.ru> 1.5.4.1-alt2
- Rebuild for Firefox 2.0.0.8

* Thu Aug 30 2007 Nikolay A. Fetisov <naf@altlinux.ru> 1.5.4.1-alt1
- New version
  - Stop DDoSing flash heavy websites

* Fri Aug 03 2007 Nikolay A. Fetisov <naf@altlinux.ru> 1.5.4-alt2
- Rebuild for Firefox 2.0.0.6

* Sat Jul 21 2007 Nikolay A. Fetisov <naf@altlinux.ru> 1.5.4-alt1
- New version
  - New extension icons
  - several bugfixes

* Thu Jul 05 2007 Nikolay A. Fetisov <naf@altlinux.ru> 1.5.3-alt2
- Rebuild for Firefox 2.0.0.4

* Mon May 07 2007 Nikolay A. Fetisov <naf@altlinux.ru> 1.5.3-alt1
- New version
  - add 'Copy Flash Location' to the context menu
  - show the URI of the blocked flash in a tooltip
  - several bugfixes

* Wed Mar 14 2007 Nikolay A. Fetisov <naf@altlinux.ru> 1.5.2-alt2
- Rebuild for Firefox 2.0.0.2

* Mon Dec 04 2006 Nikolay A. Fetisov <naf@altlinux.ru> 1.5.2-alt1
- New version
  - several bugfixes
- Rebuild for Firefox 2.0
  - removes obsolete macros
  - replace 'set_firefox_noarch' macro with 'BuildArch' tag

* Sun Sep 24 2006 Nikolay A. Fetisov <naf@altlinux.ru> 1.5.1-alt4
- Rebuild for Firefox 1.5.0.7

* Wed Aug 09 2006 Nikolay A. Fetisov <naf@altlinux.ru> 1.5.1-alt3
- Rebuild with Firefox 1.5.0.6

* Tue Jun 20 2006 Nikolay A. Fetisov <naf@altlinux.ru> 1.5.1-alt2
- Rebuild with firefox 1.5.0.4

* Mon May 15 2006 Alexey Gladkov <legion@altlinux.ru> 1.5.1-alt1.1
- NMU: rebuild with firefox 1.5.0.3

* Mon Feb 20 2006 Alexey Gladkov <legion@altlinux.ru> 1.5.1-alt1
- NMU
- new version
- rebuild with firefox 1.5.0.1

* Tue Dec 20 2005 Alexey Gladkov <legion@altlinux.ru> 1.5-alt1
- new version
- rebuild with firefox-1.5
- spec changes:
  * BuildRequires fix;
  * new macros was used to fix multiarch problem.

* Tue Nov 22 2005 Nikolay A. Fetisov <naf@altlinux.ru> 1.3.2-alt1
- Initial build for ALTLinux Sisyphus

