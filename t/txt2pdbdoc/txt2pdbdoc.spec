Summary: Palm Doc file format conversion
Summary(ru_RU.KOI8-R): Конвертор файлов в/из Palm Doc формат
Name: txt2pdbdoc
Version: 1.4.4
Release: alt2
Source: %name-%version.tar.gz
Group: Communications
License: GPL
Url: http://homepage.mac.com/pauljlucas/software/
Packager: Ilya Mashkin <oddity@altlinux.ru>

%description
 Converts plain text files to/from the Doc format used by Palm; also utilities to convert HTML files to Doc and vice versa.

%description -l ru_RU.KOI8-R
 Конвертор текстовых файлов в/из Doc формат используемый на Palm. Так же содержит утилиту для конвертации HTML в текст удобный для чтения на Palm.

%prep
%setup -q

%build
%configure
%make

%install
%makeinstall

%files
%doc README INSTALL.README AUTHORS COPYING ChangeLog
%_mandir/man?/*
%_bindir/*

%changelog
* Thu Jul 23 2009 Ilya Mashkin <oddity@altlinux.ru> 1.4.4-alt2
- fix build
- add Packager

* Sat Nov 13 2004 Vasya Borisov <vasy@altlinux.ru> 1.4.4-alt1
- New version 1.4.4:
  - This version adds the -D option to suppress checking of a Doc file's
type/creator.
  - This version also fixes a small bug in printing an error message (it printed
the wrong file name).
  - Removed -b as a decode option from usage message.
* Thu May 20 2004 Vasya Borisov <vasy@altlinux.ru> 1.4.3-alt1
- Spec clean
* Fri Nov 14 2003 Vasya Borisov <vasy@altlinux.ru> 1.4.3-alt2
- Add russian description
* Fri Oct 03 2003 Vasya Borisov <vasy@altlinux.ru> 1.4.3-alt1
- Initial release for Sisyphus
