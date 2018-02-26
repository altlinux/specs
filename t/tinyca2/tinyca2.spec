# Spec file for TinyCA2 utility
# --with/--without options: 'ru'

%define with_ru 0
%if_with ru
  %define with_ru 1
%endif

Name: tinyca2
Version: 0.7.5
Release: alt2

Summary: graphical tool for managing a Certification Authority
Summary(ru_RU.UTF-8): графическая утилита для управления Certification Authority

License: GPL
Group: Security/Networking
URL: http://tinyca.sm-zone.net/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>
BuildArch: noarch

Provides: tinyca = %version
Obsoletes: tinyca

Source0: http://tinyca.sm-zone.net/%name-%version.tar
#Source1: %%name.png
Source2: %name.po

Source3: %name-16.png
Source4: %name-32.png
Source5: %name-48.png

Patch0: %name-0.7.0-alt-ru_po.patch
Patch1: %name-0.7.2-alt-Gtk2_init.patch
Patch2: %name-0.72-alt-desktop_l10n.patch
Patch3: %name-0.7.5-alt-fix_qw_parentheses.patch

AutoReqProv: perl, yes
BuildRequires: perl-devel, perl-Glib, perl-Gtk2, perl-Locale-gettext
Requires: openssl

%description
TinyCA2 is a graphical tool written in Perl/Gtk2 to manage a small
Certification Authority (CA) using openssl.

TinyCA2 supports
- creation and revocation of x509 - S/MIME certificates.
- PKCS#10 requests.
- exporting certificates as PEM, DER, TXT, and PKCS#12.
- server certificates for use in web servers, email servers, IPsec,
  and more.
- client certificates for use in web browsers, email clients, IPsec,
  and more.
- creation and management of SubCAs


%description -l ru_RU.UTF-8
TinyCA2  -  написанная на Perl/GTK2 графическая утилита для 
управления Certification Authority (CA) небольших размеров, 
с использованием openssl.

TinyCA2 поддерживает:
- создание и отзыв сертификатов x509 и S/MIME
- запросы PKCS#10
- экспорт сертификатов в форматах PEM, DER, TXT и PKCS#12
- управление серверными сертификатами для использования с серверами 
  web, email, с IPsec, и т.д.
- управление клиентскими сертификатами для использования в браузерах,
  почтовых клиентах, для IPsec и пр.
- создание и управление SubCA


%define libdir		%_datadir/TinyCA2/lib
%define templatesdir	%_datadir/TinyCA2/templates
%define localedir	%_datadir/locale

# Defining _perl_lib_path for correct work of AutoReqProv
%define _perl_lib_path %libdir

%prep
%setup

%if "%with_ru" == "1"
%patch0 -p1
%endif 

%patch1 -p1
%patch2
%patch3

%if "%with_ru" == "1"
  /bin/install -m 0644 %SOURCE2 po/ru.po
  /bin/mkdir -p locale/ru/LC_MESSAGES
%endif

%build
# Configure sources
%__subst 's@./lib@%libdir@g' %name
%__subst 's@./templates@%templatesdir@g' %name
%__subst 's@./locale@%localedir@g' %name
/usr//bin/make -C po

%install
%if "%with_ru" == "1"
  LANGUAGES="de es cs fr sv ru"
%else
  LANGUAGES="de es cs fr sv"
%endif

/bin/mkdir -p -- %buildroot%_bindir
/bin/mkdir -p -- %buildroot%libdir
/bin/mkdir -p -- %buildroot%libdir/GUI
/bin/mkdir -p -- %buildroot%templatesdir

/bin/install -m 0644 -- lib/*.pm %buildroot%libdir/
/bin/install -m 0644 -- lib/GUI/*.pm %buildroot%libdir/GUI/
/bin/install -m 0644 -- templates/openssl.cnf %buildroot%templatesdir/
/bin/install -m 0755 -- %name %buildroot%_bindir/

for LANG in $LANGUAGES; do
   /bin/mkdir -p -- %buildroot%localedir/$LANG/LC_MESSAGES/
   /bin/install -D -m 0644 -- locale/$LANG/LC_MESSAGES/%name.mo %buildroot%localedir/$LANG/LC_MESSAGES/%name.mo
done

/bin/mkdir -p -- %buildroot%_desktopdir
/bin/install -m 0644 -- %name.desktop %buildroot%_desktopdir

/bin/mkdir -p -- %buildroot%_miconsdir %buildroot%_liconsdir %buildroot%_niconsdir
/bin/install -m 0644 -- %SOURCE3 %buildroot%_miconsdir/%name.png
/bin/install -m 0644 -- %SOURCE4 %buildroot%_niconsdir/%name.png
/bin/install -m 0644 -- %SOURCE5 %buildroot%_liconsdir/%name.png

%find_lang %name

%files -f %name.lang
%doc CHANGES INSTALL

%_bindir/%name
%_datadir/TinyCA2*
%_desktopdir/%name.desktop
%_miconsdir/%{name}*
%_niconsdir/%{name}*
%_liconsdir/%{name}*

%changelog
* Fri Nov 04 2011 Nikolay A. Fetisov <naf@altlinux.ru> 0.7.5-alt2
- Fix build with perl 5.14

* Sat Dec 13 2008 Nikolay A. Fetisov <naf@altlinux.ru> 0.7.5-alt1
- New version 0.7.5
- Removing obsolete %%update_menus calls
- Adding pre-scaled icons
- Fix repocop issues on .desktop file

* Fri Jun 30 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.7.4-alt1
- New version 0.7.4
  * Invalid filename encoding with German umlauts in base64 has been fixed. 
  * Corrupted display of UTF-8 characters in the GUI has been fixed.

* Mon May 29 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.7.3-alt1
- New version 0.7.3
  * Enhanced version detection
  * Changed command for openssl due to changed openssl behavior
  * Added "friendly name" to PKCS#12 export
  * Corrected exit call
- Change name from tinyca to tinyca2 according to mainstream
- Use png icon instead xpm
- Adding russian localisation to desktop file

* Sun Jun 05 2005 Nikolay A. Fetisov <naf@altlinux.ru> 0.6.8-alt2
- Support for openssl>0.9.7e (#7006)
- Fix font selection for work with russian fonts

* Mon Feb 21 2005 Nikolay A. Fetisov <naf@altlinux.ru> 0.6.8-alt1
- new version 0.6.8
- added detection for openssl 0.9.8
- removed crlDistributionPoint for Root-CA
- added patch for multiple OUs
- added patch for multiple subjectAltName extensions

* Mon Feb 07 2005 Nikolay A. Fetisov <naf@altlinux.ru> 0.6.7-alt1
- new version 0.6.7
- spec file cleanup
- adding icon to the menu entry
- First build for ALT Linux
* Tue Oct 5 2004 - Nikolay A. Fetisov <naf@naf.net.ru>
- First build for Sisyphus
* Fri Aug 13 2004 - sm@sm-zone.net
- czech translation
* Sun Jun 13 2004 - sm@sm-zone.net
- gui polishing
- code cleanup
- some usability improvements
* Wed Jun  2 2004 - sm@sm-zone.net
- gui polishing
- GUI module splitted to several files
* Fri Oct  3 2003 - sm@sm-zone.net
- added a lot of configuration options
- correctly import/show details of requests without extensions
  (thanks to James.Leavitt@anywaregroup.com)
* Mon Sep  1 2003 - sm@sm-zone.net
- added renewal of certificates
* Wed Aug 13 2003 - sm@sm-zone.net
- rewite, now using perl-Gtk
* Sat Jul  5 2003 - sm@sm-zone.net
- added german translation
* Tue Jul  1 2003 - sm@sm-zone.net
- convert index.txt if openssl changed from 0.9.6x to 0.9.7x
* Fri Jun 27 2003 - sm@sm-zone.net
- added export into zip-file
  thanks to ludwig.nussel@suse.de
* Mon Jun 23 2003 - sm@sm-zone.net
- some tiny usability improvements
  thanks to ludwig.nussel@suse.de again
* Thu Jun 19 2003 - sm@sm-zone.net
- some usability improvements
  thanks to ludwig.nussel@suse.de
- some more configuration options
* Fri Oct  4 2002 - sm@sm-zone.net
- Fixed bug exporting keys in PEM format
- Fixed possible empty lines in cert/key/reqlist
  thanks to waldemar.mertke@gmx.de
* Fri Sep 27 2002 - sm@sm-zone.net
- fixed some minor bugs and typos (e.g. concerning openssl 0.9.7)
  thanks to iebgener@yahoo.com and waldemar.mertke@gmx.de
* Wed Aug 21 2002 - sm@sm-zone.net
- fixed revocation
- added some colors
- thanks to curly@e-card.bg
* Sun Aug 18 2002 - sm@sm-zone.net
- new version 0.4.0
- works independent of OpenCA modules now
- some enhancements to functionality (e.g. export of key without
  passwd)
- some smaller bugfixes in usability
- new specfile (thanks to oron@actcom.co.il)
* Thu Jun  6 2002 - Oron Peled <oron@actcom.co.il>
- Cleaned .spec file
* Mon Jun  3 2002 - sm@sm-zone.net
- fixed wrong templatedir when creating new CA
* Sun Jun  2 2002 - sm@sm-zone.net
- fixed some minor bugs and typos
* Sat May 11 2002 - sm@sm-zone.net
- Added parser for x509 extensions
* Fri May 03 2002 - sm@sm-zone.net
- added possibility to view requests/certificates
* Thu Apr 18 2002 - sm@sm-zone.net
- added configuration
* Sun Apr  7 2002 - sm@sm-zone.net
- improved usability
* Sun Mar 31 2002 - sm@sm-zone.net
- added function to delete ca
* Sat Mar 30 2002 - sm@sm-zone.net
- allow import of pkcs#10 requests
* Thu Mar 21 2002 - sm@sm-zone.et
- use different listboxes
* Mon Mar 18 2002 - sm@sm-zone.net
- initial package

