Name: makeself
Version: 2.1.5
Release: alt1

Summary: It's a small shell script that generates a self-extractable tar.gz archive from a directory
Summary(ru_RU.KOI8-R): Скрипт для создания самораспаковывающихся архивов tar.gz

License: GPL

Group: Archiving/Compression
Packager: Ilya Mashkin <oddity@altlinux.ru>

Url:  http://www.megastep.org/makeself
Source: http://www.megastep.org/makeself/%name-%version.tar.bz2

%description
Makeself.sh is a small shell script that generates a self-extractable tar.gz archive from a directory. 
The resulting file appears as a shell script (many of those have a .run suffix), and can be launched as is. 
The archive will then uncompress itself to a temporary directory and an optional arbitrary command will be 
executed (for example an installation script).

%prep
%setup -q

%install
%__install -D -m0755 makeself.sh  %buildroot%_bindir/makeself.sh
%__install -D -m0755 makeself-header.sh  %buildroot%_bindir/makeself-header.sh


%files
%doc README TODO
%_bindir/*


%changelog
* Mon Dec 07 2009 Ilya Mashkin <oddity@altlinux.ru> 2.1.5-alt1
- 2.1.5

* Fri Feb 17 2006 Alexander Plikus <plik@altlinux.ru> 2.1.4-alt1
- initial build for ALT Linux



