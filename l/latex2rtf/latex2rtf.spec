Name: latex2rtf
Version: 1.9.19
Release: alt1

Summary: Convert a LaTeX file to an RTF file
Summary(ru_RU.KOI8-R): Преобразователь файлов LaTeX в формат RTF

License: LGPL
Group: Text tools
Url: http://sourceforge.net/projects/latex2rtf/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://prdownloads.sourceforge.net/%name/%name-%version.tar.bz2
Patch: %name-link.patch

%description
This package contains the latex2rtf command converts a LaTeX file 
into RTF text format. The text and much of the formatting 
information is translated to RTF.

%description -l ru_RU.KOI8-R
Этот пакет содержит команду latex2rtf, которая преобразует
файл LaTeX в формат текстового файла RTF. Текст и большая
часть информации о форматировании переводится в RTF.

%prep
%setup -q
%patch
%__subst "s|^PREFIX=.*|PREFIX=\$(prefix)|" Makefile
%__subst "s|^MAN_INSTALL=\$(PREFIX)/man/man1|MAN_INSTALL=\$(PREFIX)/share/man/man1|" Makefile
%__subst "s|^INFO_INSTALL=\$(PREFIX)/info|INFO_INSTALL=\$(PREFIX)/share/info|" Makefile
%__subst "s|^SUPPORT_INSTALL=\$(PREFIX)/share/latex2rtf|SUPPORT_INSTALL=\$(PREFIX)/share/doc/latex2rtf-%version|" Makefile
%__subst "s|^CFG_INSTALL=\$(PREFIX)/share/latex2rtf/cfg|CFG_INSTALL=\$(PREFIX)/share/latex2rtf|" Makefile
%__subst 's|CFGDIR=\\"\$(CFG_INSTALL)\\"|CFGDIR=\\"/usr/share/latex2rtf\\"|' Makefile

%__subst "s|\$(MKDIR) \$(CFG_INSTALL)|\$(MKDIR) \$(CFG_INSTALL) \$(MKDIR) \$(SUPPORT_INSTALL)|" Makefile

%build
%make_build

%install
%makeinstall

%files
%_bindir/*
%_datadir/%name
%_mandir/man1/*
%_docdir/%name-%version

%changelog
* Wed Jul 02 2008 Vitaly Lipatov <lav@altlinux.ru> 1.9.19-alt1
- new version 1.9.19 (with rpmrb script)

* Wed Oct 24 2007 Vitaly Lipatov <lav@altlinux.ru> 1.9.18-alt1
- new version 1.9.18 (with rpmrb script)

* Thu Dec 09 2004 Vitaly Lipatov <lav@altlinux.ru> 1.9.16a-alt1
- new version
- fix cfg dir

* Thu Jun 03 2004 Vitaly Lipatov <lav@altlinux.ru> 1.9.15-alt1
- new version

* Mon Oct 06 2003 Vitaly Lipatov <lav@altlinux.ru> 1.9.14-alt1
- packaged for ALT Linux Sisyphus from scratch

