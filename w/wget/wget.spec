# -*- rpm-spec -*-
# $Id: wget,v 1.1 2004/03/19 10:48:41 grigory Exp $

%define beta %nil

Name: wget
Version: 1.13.4
Release: alt1

Summary: An utility for retrieving files using the HTTP, HTTPS or FTP protocols
License: GPLv3
Group: Networking/WWW

Url: http://www.gnu.org/software/wget/wget.html
Source: ftp://ftp.gnu.org/gnu/wget/%name-%version.tar
Patch1: %name-1.9.1-alt-texinfo.patch
Patch2: %name-1.6-mdk-passive_ftp.patch
Patch3: %name-1.7-alt-locale.patch
Patch10: wget-1.10.1-alt-ntlm-buffer.patch
Packager: Michael Shigorin <mike@altlinux.org>

# Automatically added by buildreq on Sun Sep 25 2011
# optimized out: libcom_err-devel libkrb5-devel perl-Encode perl-Pod-Escapes perl-Pod-Simple perl-podlators
BuildRequires: libidn-devel libssl-devel perl-Pod-Parser zlib-devel

Summary(es):	Cliente en lМnea de comando para bajar archivos WWW/FTP con recursiСn opcional
Summary(fr):	Un utilitaire pour recuperer des fichiers en utilisant les protocoles HTTP ou FTP
Summary(pl):	Wsadowy klient HTTP/FTP
Summary(pt_BR):	Cliente na linha de comando para baixar arquivos WWW/FTP com recursЦo opcional
Summary(ru_RU.KOI8-R):	Утилита для получения файлов по протоколам HTTP и FTP
Summary(uk_UA.KOI8-U):	Утил╕та для отримання файл╕в по протоколам HTTP та FTP
Summary(zh_CN):	[м╗я╤]╧╕дэг©╢С╣добтьЁлпР,ж╖Ёж╤о╣ЦпЬ╢╚

%description
GNU Wget is a file retrieval utility which can use either the HTTP,
HTTPS or FTP protocols.  Wget features include the ability to work
in the background while you're logged out, recursive retrieval of
directories, file name wildcard matching, remote file timestamp
storage and comparison, use of Rest with FTP servers and Range with
HTTP servers to retrieve files over slow or unstable connections,
support for Proxy servers, and configurability.

Install wget if you need to retrieve large numbers of files with HTTP,
HTTPS or FTP, or if you need a utility for mirroring web sites or FTP
directories.

%description -l es
GNU wget es una herramienta de red para bajar archivos usando HTTP y
FTP. Funciona en modo no interactivo, pudiendo trabajar en background.
Funciona muy bien, incluso en conexiones lentas o inestables, bajando
el archivo hasta que sea completamente recibido.

%description -l fr
GNU Wget est un utilitaire pour rИcupИrer des fichiers qui peut
utiliser indiffИremment les protocoles HTTP ou FTP. Parmi les
caractИristiques de Wget, citons la capacitИ Ю rИcupИrer des fichiers
en arriХre-plan alors que vous n'Йtes pas connectИ, la rИcupИration
rИcursive de rИpertoires, la capacitИ de rИcupИrer des fichiers en
appliquant un filtre sur le nom ou sur la date, la gestion de Rest
avec les serveurs FTP et de Range avec les serveurs HTTP pour
rИcupИrer des fichiers avec une connexion lente ou instable, le
support des serveurs Proxy... Wget est particuliХrement configurable.

%description -l ja
GNU wget ╓о HTTP ╓╚ FTP ╔в╔М╔х╔Ё╔К╓н╓и╓а╓И╓╚╓Р╩хмя╓╧╓К╓Ё╓х╓╛╓г╓╜╓К
╔у╔║╔╓╔К╓Р╪Хфю╓╧╓К╔Ф║╪╔ф╔ё╔Й╔ф╔ё╓г╓╧║ёwget ╓о╔М╔╟╔╒╔╕╔х╓╥╓ф╓╓╓К
╢ж╓к╔п╔ц╔╞╔╟╔И╔╕╔С╔и╓гф╞╓╞фцд╖╓Р╓Б╓ц╓ф╓╓╓К╓Ё╓х║╒╔г╔ё╔Л╔╞╔х╔Й╓н╨ф╣╒е╙
╪Хфю║╒╔у╔║╔╓╔К╔м║╪╔Ю╓н╔О╔╓╔К╔и╔╚║╪╔и╔ч╔ц╔а╔С╔╟║╒╔у╔║╔╓╔К╓н╔©╔╓╔Ю╔╧╔©╔С╔в╓н
йщб╦╓ххФЁс║╒цы╓╞ит╟бдЙ╓йюэбЁ╓г FTP ╔╣║╪╔п╓н Rest ╓х HTTP ╔╣║╪╔п╓н
Range ╓н╩хмя║╒╔в╔М╔╜╔╥║╪╔╣║╪╔п╓н╔╣╔щ║╪╔х╓хюъдЙ╓нмф╟в╓╣╓Р╢ч╓С╓юфцд╖╓Р
╓Б╓ц╓ф╓╓╓ч╓╧║ё

%description -l pl
Wget jest klientem FTP/HTTP przeznaczonym do ╤ci╠gania zasobСw
wsadowo. Umo©liwia ╤ci╠ganie zasobСw z podkatalogami, a tak©e ma opcje
umo©liwiaj╠ce wykonanie lokalnej kopii zasobСw (mirror). W razie
niemo©no╤ci dostania siЙ do zasobСw lub gdy poЁ╠czenie z serwerem
FTP/HTTP zostanie zerwane, mo©e automatycznie ponawiaФ prСby
kopiowania. Jest tak©e dobrze przystosowany do tego, ©eby uruchamiaФ
go jako zadanie z crona.

%description -l pt_BR
O GNU wget И uma ferramenta de rede para baixar arquivos usando HTTP e
FTP. Ele funciona em modo nЦo interativo, podendo trabalhar em
background. Funciona muito bem, mesmo em conexУes lentas ou instАveis,
baixando o arquivo atИ que ele seja completamente recebido.

%description -l ru_RU.KOI8-R
GNU Wget - это утилита командной строки для получения файлов по
протоколам FTP и HTTP. Среди возможностей Wget - работа в фоновом
режиме после выхода из системы, рекурсивное извлечение каталогов,
выбор файлов по шаблону, сравнение времени удаленных и локальных
файлов, сохранение времени удаленных файлов при загрузке,
использование REST с FTP серверами и Range с HTTP серверами для
загрузки файлов по медленным или нестабильным каналам, поддержка 
прокси-серверов, конфигурируемость.

%description -l uk_UA.KOI8-U
GNU Wget - це утил╕та командного рядка для отримання файл╕в по
протоколам FTP та HTTP. Серед можливостей Wget - робота в фоновому
режим╕ п╕сля виходу ╕з системи, рекурсивне отримання каталог╕в,
виб╕р файл╕в по шаблону, пор╕вняння часу в╕ддалених та локальних
файл╕в, збереження часу в╕ддалених файл╕в при завантаженн╕,
використання REST з FTP серверами та Range з HTTP серверами для
завантаження файл╕в по пов╕льним чи нестаб╕льним каналам, п╕дтримка
прокс╕-сервер╕в, налаштовуван╕сть.

%prep
%setup -n %name-%version

# Fix docs and samples.
rm -f doc/*.info*
find doc -type f -print0 |
	xargs -r0 grep -FZl /usr/local/ -- |
	xargs -r0 sed -i 's,/usr/local/,/,g' --

%patch1 -p1
%patch10 -p1

%build
%configure --with-ssl=openssl
# https://bugzilla.altlinux.org/show_bug.cgi?id=14239
(cd po; make update-po)
%make_build

%install
%makeinstall

%find_lang %name

%files -f %name.lang
%config(noreplace) %_sysconfdir/%{name}rc
%_bindir/*
%_mandir/man?/*
%_infodir/*.info*
%doc AUTHORS MAILING-LIST NEWS README*

# TODO:
# - consider switching to gnutls build
#   (double-check with ca-certificates or whatever);
#   so far it's a bit too churny

%changelog
* Sun Sep 25 2011 Michael Shigorin <mike@altlinux.org> 1.13.4-alt1
- 1.13.4 (NB: moved to gnutls by default)
- built with openssl specifically
- enabled IDN support
- spec cleanup
- buildreq

* Mon Jan 17 2011 Timur Aitov <timonbl4@altlinux.org> 1.12-alt2
- fix manual build

* Tue Oct 12 2010 Michael Shigorin <mike@altlinux.org> 1.12-alt1.1
- rebuilt against openssl-1.0.0a

* Wed Sep 23 2009 Michael Shigorin <mike@altlinux.org> 1.12-alt1
- 1.12
  + fixes security problem outlined in RH#520454:
    SSL certificate name vs. host name verification bypass
    via NUL ('\0') character embedded in X509 certificate's
    CommonName or subjectAltName
  + thanks ldv@ for heads-up

* Sun Jul 26 2009 Michael Shigorin <mike@altlinux.org> 1.11.4-alt2
- applied repocop patch

* Fri Oct 31 2008 Michael Shigorin <mike@altlinux.org> 1.11.4-alt1
- 1.11.4 (1.11.2 should have fixed #17676)

* Sat Aug 09 2008 ALT QA Team Robot <qa-robot@altlinux.org> 1.11.1-alt1.1
- Automated rebuild due to libssl.so.6 -> libssl.so.7 soname change.

* Fri Mar 28 2008 Michael Shigorin <mike@altlinux.org> 1.11.1-alt1
- 1.11.1

* Mon Feb 11 2008 Michael Shigorin <mike@altlinux.org> 1.11.1-alt0.b2092
- 1.1.11-b2092

* Wed Jan 30 2008 Michael Shigorin <mike@altlinux.org> 1.11-alt2
- added workaround for #14239 (crash in ru_RU.UTF-8 while
  all OK in C, ru_RU.KOI8-R, uk_UA.UTF-8); that is, removed
  translations till 1.11.1: https://savannah.gnu.org/bugs/?22161

* Sun Jan 27 2008 Michael Shigorin <mike@altlinux.org> 1.11-alt1
- 1.11
  + License: changed to GPLv3
  + see announce here:
    http://www.mail-archive.com/wget%%40sunsite.dk/msg10768.html

* Thu Nov 01 2007 Michael Shigorin <mike@altlinux.org> 1.10.2-alt3
- fixed #13241, thanks inger@

* Tue May 22 2007 Michael Shigorin <mike@altlinux.org> 1.10.2-alt2
- added ru/uk package description charsets (#11848)
- spec macro abuse cleanup

* Fri Dec 29 2006 ALT QA Team Robot <qa-robot@altlinux.org> 1.10.2-alt1.1
- Rebuilt due to libcrypto.so.4 -> libcrypto.so.6 soname change.

* Sat Oct 15 2005 Michael Shigorin <mike@altlinux.org> 1.10.2-alt1
- 1.10.2
- security fix for CAN-2005-3185 (NTLM buffer overflow)
  provided by upstream vendor
- disabled patch2

* Thu Oct 13 2005 Michael Shigorin <mike@altlinux.org> 1.10.1-alt2
- security fix: NTLM buffer overflow
  + patch by Sergey Ryabchun (sr@)
  + thanks to Dmitry V.Levin (ldv@) for alerting

* Mon Aug 29 2005 Michael Shigorin <mike@altlinux.org> 1.10.1-alt1
- 1.10.1 (#7789, #7512)
- removed patch3 (merged upstream with minor changes)

* Wed Jun 29 2005 Michael Shigorin <mike@altlinux.org> 1.10-alt1
- 1.10 (thanks Grigory Fateyev <greg anastasia.ru> for testing)
- merged description translations from PLD's 1.9.1-19 spec
- updated buildrequires

* Mon May 10 2004 ALT QA Team Robot <qa-robot@altlinux.org> 1.9.1-alt1.1
- Rebuilt with openssl-0.9.7d.

* Fri Mar 19 2004 Grigory Milev <week@altlinux.ru> 1.9.1-alt1
- new version released
- remove unneeded putches due changes in release

* Wed Aug 06 2003 Alexey Voinov <voins@altlinux.ru> 1.8.2-alt4
- updated rh-filename patch.
- fixup wrong fix for directory traversal bug
- fixed buffer overflow (rh-segv patch)

* Wed Dec 11 2002 Dmitry V. Levin <ldv@altlinux.org> 1.8.2-alt3
- Merged RH patches:
  * Sat Oct 05 2002 Karsten Hopp <karsten@redhat.de> 1.8.2-5
  - fix directory traversal bug
  * Thu Jul 25 2002 Trond Eivind GlomsrЬd <teg@redhat.com> 1.8.2-3
  - Don't segfault when downloading URLs A-B-A (A-A-B worked) #49859

* Fri Nov 15 2002 Stanislav Ievlev <inger@altlinux.ru> 1.8.2-alt2
- rebuild

* Thu Jun 06 2002 Dmitry V. Levin <ldv@altlinux.org> 1.8.2-alt1
- 1.8.2
- Fixed .netrc quotation parsing (mdk).

* Tue Feb 05 2002 Dmitry V. Levin <ldv@alt-linux.org> 1.8.1-alt1
- 1.8.1

* Tue Dec 18 2001 Dmitry V. Levin <ldv@alt-linux.org> 1.8-alt1
- 1.8

* Tue Nov 20 2001 Dmitry V. Levin <ldv@alt-linux.org> 1.7.1-alt1
- 1.7.1

* Mon Oct 08 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.7-alt2
- Shutup output to screen when using quiet with batch mode (rh).

* Fri Jun 15 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.7-alt1
- 1.7
- Merged some MDK and RH paches.
- Resurrected manpage.

* Fri Apr 06 2001 Sergie Pugachev <fd_rag@altlinux.ru> 1.6-alt2
- New version 1.6
- Fixed texinfo.patch
- Fixed encdec.patch
- Fixed i18n

* Sat Dec 09 2000 Dmitry V. Levin <ldv@fandra.org> 1.5.3gold-ipl2
- Fixed texinfo documentation.
- Fix bug: the characters ";/?=&+" must retain their encoded/decodedstatus.
  (from Anon Sricharoenchai <ans@beethoven.cpe.ku.ac.th>)

* Fri Jun 30 2000 Dmitry V. Levin <ldv@fandra.org> 1.5.3gold-ipl1
- RE and Fandra adaptions.

* Mon Jun 26 2000 Soenke J. Peters <soenke+rpm@simprovement.com>
- included some stuff from CVS tree
- HTTPS support

* Thu Aug 26 1999 Jeff Johnson <jbj@redhat.com>
- don't permit chmod 777 on symlinks (#4725).

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 4)

* Fri Dec 18 1998 Bill Nottingham <notting@redhat.com>
- build for 6.0 tree
- add Provides

* Sat Oct 10 1998 Cristian Gafton <gafton@redhat.com>
- strip binaries
- version 1.5.3

* Sat Jun 27 1998 Jeff Johnson <jbj@redhat.com>
- updated to 1.5.2

* Thu Apr 30 1998 Cristian Gafton <gafton@redhat.com>
- modified group to Applications/Networking

* Wed Apr 22 1998 Cristian Gafton <gafton@redhat.com>
- upgraded to 1.5.0
- they removed the man page from the distribution (Duh!) and I added it back
  from 1.4.5. Hey, removing the man page is DUMB!

* Fri Nov 14 1997 Cristian Gafton <gafton@redhat.com>
- first build against glibc


