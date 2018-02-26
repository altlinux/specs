%define LANG_DE de
%define LANG_ES es
%define LANG_FR fr
%define LANG_IT it
%define LANG_PT pt_BR
%define LANG_RU ru
%define LANG_SK sk
%define LANG_SR sr
%define LANG_UK uk

Name: micq
Version: 0.5.0.3
Release: alt2.1

License: GPL
Url: http://micq.ukeer.de/
Packager: Aleksandr Blokhin (Sass) <sass@altlinux.ru>
Summary: A clone of the Mirabilis ICQ online messaging program
Summary(ru_RU.UTF-8): Клон программы передачи сообщений Mirabilis ICQ
Group: Networking/Instant messaging

Source: %name-%version.tar.bz2

# Automatically added by buildreq on Sat Dec 11 2004
BuildRequires: libgnutls-devel libssl-devel zlib-devel

%description
Micq is a clone of the Mirabilis ICQ online messaging/conferencing program.

%description -l ru_RU.UTF-8
Micq явялется клоном программы передачи сообщений Mirabilis ICQ.

%package -n man-pages-%name
Summary: Manual pages for %name in Spanish, German, French, and Brazilian Portuguese languages
Summary(ru_RU.UTF-8): Документация   для   программы   Micq   на  испанском,  немецком, французском и бразильском португальском языках
License: distributable
Group: System/Internationalization
PreReq: %name

%description -n man-pages-%name
Manual pages for %name in Spanish, German, French, and Brazilian Portuguese languages.

%description -l ru_RU.UTF-8 -n man-pages-%name
Документация   для   программы   Micq   на  испанском,  немецком,
французском и бразильском португальском языках.

%prep
%setup -q

%build
%configure --enable-ssl=gnutls,openssl 
%make_build

%install
%makeinstall -C src
%__mkdir_p $RPM_BUILD_ROOT%_docdir/%name
%__install -p -m644 AUTHORS FAQ README COPYING COPYING-GPLv2 \
     NEWS ChangeLog doc/{icq091.txt,icqv7.txt,README.*} \
     $RPM_BUILD_ROOT%_docdir/%name

%__mkdir_p $RPM_BUILD_ROOT%_datadir/%name/contrib
%__install -p -m644 contrib/*.tcl $RPM_BUILD_ROOT%_datadir/%name/contrib

%__mkdir_p $RPM_BUILD_ROOT%_mandir/{man1,man5,man7}
%__cp doc/%name.1 $RPM_BUILD_ROOT%_man1dir
%__cp doc/micqrc.5 $RPM_BUILD_ROOT%_man5dir
%__cp doc/%name.7 $RPM_BUILD_ROOT%_man7dir

%__mkdir_p $RPM_BUILD_ROOT%_mandir/%LANG_RU/{man1,man5,man7}
%__cp doc/ru/%name.1 $RPM_BUILD_ROOT%_mandir/%LANG_RU/man1
%__cp doc/ru/micqrc.5 $RPM_BUILD_ROOT%_mandir/%LANG_RU/man5
%__cp doc/ru/%name.7 $RPM_BUILD_ROOT%_mandir/%LANG_RU/man7

%__mkdir_p $RPM_BUILD_ROOT%_mandir/%LANG_DE/{man1,man5,man7}
%__cp doc/de/%name.1 $RPM_BUILD_ROOT%_mandir/%LANG_DE/man1
%__cp doc/de/micqrc.5 $RPM_BUILD_ROOT%_mandir/%LANG_DE/man5
%__cp doc/de/%name.7 $RPM_BUILD_ROOT%_mandir/%LANG_DE/man7

%__mkdir_p $RPM_BUILD_ROOT%_mandir/%LANG_ES/{man1,man5,man7}
%__cp doc/es/%name.1 $RPM_BUILD_ROOT%_mandir/%LANG_ES/man1
%__cp doc/es/micqrc.5 $RPM_BUILD_ROOT%_mandir/%LANG_ES/man5
%__cp doc/es/%name.7 $RPM_BUILD_ROOT%_mandir/%LANG_ES/man7

%__mkdir_p $RPM_BUILD_ROOT%_mandir/%LANG_FR/{man1,man5,man7}
%__cp doc/fr/%name.1 $RPM_BUILD_ROOT%_mandir/%LANG_FR/man1
%__cp doc/fr/micqrc.5 $RPM_BUILD_ROOT%_mandir/%LANG_FR/man5
%__cp doc/fr/%name.7 $RPM_BUILD_ROOT%_mandir/%LANG_FR/man7

%__mkdir_p $RPM_BUILD_ROOT%_mandir/%LANG_IT/man1
%__cp doc/it/%name.1 $RPM_BUILD_ROOT%_mandir/%LANG_IT/man1

%__mkdir_p $RPM_BUILD_ROOT%_mandir/%LANG_PT/{man1,man5,man7}
%__cp doc/pt_BR/%name.1 $RPM_BUILD_ROOT%_mandir/%LANG_PT/man1
%__cp doc/pt_BR/micqrc.5 $RPM_BUILD_ROOT%_mandir/%LANG_PT/man5
%__cp doc/pt_BR/%name.7 $RPM_BUILD_ROOT%_mandir/%LANG_PT/man7

#%__mkdir_p $RPM_BUILD_ROOT%_mandir/%LANG_SK/man1
#%__cp doc/sk/%name.1 $RPM_BUILD_ROOT%_mandir/%LANG_SK/man1

%__mkdir_p $RPM_BUILD_ROOT%_mandir/%LANG_SR/{man1,man5,man7}
%__cp doc/sr/%name.1 $RPM_BUILD_ROOT%_mandir/%LANG_SR/man1
%__cp doc/sr/micqrc.5 $RPM_BUILD_ROOT%_mandir/%LANG_SR/man5
%__cp doc/sr/%name.7 $RPM_BUILD_ROOT%_mandir/%LANG_SR/man5

%__mkdir_p $RPM_BUILD_ROOT%_mandir/%LANG_UK/{man1,man7}
%__cp doc/uk/%name.1 $RPM_BUILD_ROOT%_mandir/%LANG_UK/man1
%__cp doc/uk/%name.7 $RPM_BUILD_ROOT%_mandir/%LANG_UK/man7

%files
%dir %_docdir/%name
%dir %_datadir/%name
%dir %_datadir/%name/contrib
%_docdir/%name/*
%_bindir/%name
%_mandir/man?/*
%_mandir/%LANG_RU/man?/*
%_datadir/%name/*

%files -n man-pages-%name
%_mandir/%LANG_DE/man?/*
%_mandir/%LANG_ES/man?/*
%_mandir/%LANG_FR/man?/*
%_mandir/%LANG_PT/man?/*
%_mandir/%LANG_IT/man?/*
%_mandir/%LANG_SR/man?/*
%_mandir/%LANG_UK/man?/*

%changelog
* Tue Dec 07 2010 Igor Vlasenko <viy@altlinux.ru> 0.5.0.3-alt2.1
- rebuild with new openssl and/or boost by request of git.alt administrator

* Sat Nov 21 2009 Afanasov Dmitry <ender@altlinux.org> 0.5.0.3-alt2
- rebuild with gnutls 2.8.5

* Sat Aug 09 2008 ALT QA Team Robot <qa-robot@altlinux.org> 0.5.0.3-alt1.1.1
- Automated rebuild due to libssl.so.6 -> libssl.so.7 soname change.

* Fri Dec 29 2006 ALT QA Team Robot <qa-robot@altlinux.org> 0.5.0.3-alt1.1
- Rebuilt due to libcrypto.so.4 -> libcrypto.so.6 soname change.

* Sun May 29 2005 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 0.5.0.3-alt1
- 0.5.0.3

* Sat Dec 11 2004 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 0.4.99.9-alt0.1
- 0.4.99.9 beta release
- with ssl enabled
- with tls enabled

* Mon Nov 15 2004 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 0.4.12-alt1
- 0.4.12
- Added man-pages in italian, slovakian, serbian and ukrainian languages.
- Updated spec.

* Sat Jan 17 2004 Aleksandr Blokhin (Sass) <sass@altlinux.ru> 0.4.11-alt1
- 0.4.11

* Wed Nov 19 2003 Aleksandr Blokhin (Sass) <sass@altlinux.ru> 0.4.10.5-alt1
- 0.4.10.5

* Fri May 16 2003 Aleksandr Blokhin (Sass) <sass@altlinux.ru> 0.4.10.3-alt1
- 0.4.10.3
- fixed typo in spec

* Wed Mar 12 2003 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 0.4.10.2-alt1
- 0.4.10.2

* Thu Nov 14 2002 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 0.4.9.4-alt2
- Updated section %%install.
- Added Packager tag.
- Translated russian description in UTF-8 encoding.
- Changed licence to GPL.

* Mon Oct 07 2002 Aleksandr Blokhin (Sass) <sass@altlinux.ru> 0.4.9.4-alt1
- 0.4.9.4
- remove micq-russian-recode-fix patch
- builded additional package with manual pages in multiple languages

* Fri Sep 14 2001 Kostya Timoshenko <kt@altlinux.ru> 0.4.7-alt1
- 0.4.7
- remove old patch
- add micq-russian-recode-fix patch

* Mon Feb 19 2001 Kostya Timoshenko <kt@petr.kz> 0.4.6-ipl4mdk
- change tag Group (Networking/Instant messaging)

* Fri Feb  9  2001 Kostya Timoshenko <kt@petr.kz> 0.4.6-ipl3mdk
- change tag Group (Networking/ICQ)

* Thu Jan 25 2001 Kostya Timoshenko <kt@petr.kz>
- add micq-0.4.6-buf-ov.patch.bz2
- add micq-0.4.6-queued.patch.bz2

* Tue Jan 23 2001 Kostya Timoshenko <kt@petr.kz>
- initial RPM
