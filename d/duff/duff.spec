Name: duff
Version: 0.5.2
Release: alt1

Summary: Utility for identifying duplicates in a given set of files
Summary(ru_RU.KOI8-R): Программа для определения одинаковых файлов (по контрольной сумме)
Packager: Ilya Mashkin <oddity@altlinux.ru>

License: GPL
Group: File tools
Url:  http://duff.sourceforge.net/ 

Source: http://dl.sf.net/%name/%name-%version.tar.bz2

%description
Duff is a command-line utility for identifying duplicates in a given set of
files.  It attempts to be usably fast, and uses SHA1 checksums as a part of
the comparisons.

%prep
%setup -q

%build
%configure
 
%install
%makeinstall

%find_lang %name

%files -f %name.lang
%doc README.SHA
%_bindir/*
%_man1dir/*
%_datadir/%name/*

%changelog
* Sun Feb 12 2012 Ilya Mashkin <oddity@altlinux.ru> 0.5.2-alt1
- 0.5.2

* Sun Jan 29 2012 Ilya Mashkin <oddity@altlinux.ru> 0.5.1-alt1
- 0.5.1

* Sun Jul 10 2011 Ilya Mashkin <oddity@altlinux.ru> 0.5-alt1
- 0.5

* Mon Dec 07 2009 Ilya Mashkin <oddity@altlinux.ru> 0.4-alt1
- 0.4

* Mon Dec 12 2005 Alexander  Plikus <plik@altlinux.ru> 0.3-alt1
- initial build for AltLinux


