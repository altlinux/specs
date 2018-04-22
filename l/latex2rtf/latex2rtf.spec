Name: latex2rtf
Version: 2.3.17
Release: alt1

Summary: Convert a LaTeX file to an RTF file
Summary(ru_RU.UTF8): Преобразователь файлов LaTeX в формат RTF

License: LGPL
Group: Text tools
Url: http://sourceforge.net/projects/latex2rtf/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://prdownloads.sourceforge.net/%name/%name-%version.tar

%description
This package contains the latex2rtf command converts a LaTeX file 
into RTF text format. The text and much of the formatting 
information is translated to RTF.

%description -l ru_RU.UTF8
Этот пакет содержит команду latex2rtf, которая преобразует
файл LaTeX в формат текстового файла RTF. Текст и большая
часть информации о форматировании переводится в RTF.

%prep
%setup

%build
%make_build DESTDIR=%prefix
make -C doc latex2rtf.html

%install
make install DESTDIR=%buildroot%prefix

# hack for 2.3.15
chmod 755 %buildroot%_bindir/latex2png

%files
%doc HACKING README
%_bindir/*
%_datadir/%name/
%_man1dir/*

%changelog
* Sun Apr 22 2018 Vitaly Lipatov <lav@altlinux.ru> 2.3.17-alt1
- new version 2.3.17 (with rpmrb script)

* Tue May 16 2017 Igor Vlasenko <viy@altlinux.ru> 2.3.16-alt1
- NMU: new version 2.3.16

* Tue May 09 2017 Igor Vlasenko <viy@altlinux.ru> 2.3.15-alt1
- NMU: new version 2.3.15
- added latex2rtf-cfg-ukrainian.patch

* Fri Aug 05 2016 Vitaly Lipatov <lav@altlinux.ru> 2.3.11a-alt1
- new version 2.3.11a (with rpmrb script)

* Tue Sep 02 2014 Vitaly Lipatov <lav@altlinux.ru> 2.3.8-alt1
- new version 2.3.8 (with rpmrb script)

* Tue Apr 01 2014 Vitaly Lipatov <lav@altlinux.ru> 2.3.6-alt1
- new version 2.3.6 (with rpmrb script)

* Sun Aug 04 2013 Vitaly Lipatov <lav@altlinux.ru> 2.3.3-alt1
- new version 2.3.3 (with rpmrb script)

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.9.19-alt1.qa1
- NMU: rebuilt for debuginfo.

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

