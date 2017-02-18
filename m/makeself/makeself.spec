Name: makeself
Version: 2.3.0
Release: alt1

Summary: It's a small shell script that generates a self-extractable archive from a directory
Summary(ru_RU.UTF-8): Скрипт для создания самораспаковывающихся архивов

License: GPLv2+
Group: Archiving/Compression
Url:  http://www.megastep.org/makeself

Packager: Ilya Mashkin <oddity@altlinux.ru>

BuildArch: noarch

# Source-url: https://github.com/megastep/makeself/archive/release-%version.tar.gz
Source: %name-%version.tar

%description
Makeself.sh is a small shell script that generates
a self-extractable archive from a directory.
The resulting file appears as a shell script
(many of those have a .run suffix), and can be launched as is.
The archive will then uncompress itself to a temporary directory
and an optional arbitrary command will be
executed (for example an installation script).

%prep
%setup

%install
install -D -m0755 makeself.sh %buildroot%_bindir/makeself.sh
install -D -m0755 makeself-header.sh %buildroot%_bindir/makeself-header.sh
install -D -m0644 makeself.1 %buildroot%_man1dir/makeself.1

%files
%doc README.md makeself.lsm
%_bindir/makeself.sh
%_bindir/makeself-header.sh
%_man1dir/*

%changelog
* Sat Feb 18 2017 Vitaly Lipatov <lav@altlinux.ru> 2.3.0-alt1
- new version 2.3.0 (with rpmrb script)

* Tue Aug 27 2013 Vitaly Lipatov <lav@altlinux.ru> 2.2.0-alt1
- new version 2.2.0 (with rpmrb script)

* Mon Jan 21 2013 Vitaly Lipatov <lav@altlinux.ru> 2.1.5-alt2
- cleanup spec
- pack man page and makeself.lsm (ALT bug #9206)
- set noarch

* Mon Dec 07 2009 Ilya Mashkin <oddity@altlinux.ru> 2.1.5-alt1
- 2.1.5

* Fri Feb 17 2006 Alexander Plikus <plik@altlinux.ru> 2.1.4-alt1
- initial build for ALT Linux
