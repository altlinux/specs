Name: convmv
Version: 1.15
Release: alt1

Summary: convmv converts file names from one encoding to another
Summary(ru_RU.UTF-8): convmv перекодирует названия файлов

License: GPL
Group: File tools
Url: http://freshmeat.net/projects/convmv/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://j3e.de/linux/%name/%name-%version.tar

BuildArchitectures: noarch

# Automatically added by buildreq on Thu Dec 16 2004 (-bi)
BuildRequires: perl-Encode perl-Unicode-Normalize

%description
convmv converts filenames (not file content), directories, 
and even whole filesystems to a different encoding.

%description -l ru_RU.UTF-8
convmv перекодирует названия файлов (не содержимое файлов),
каталогов, и даже целые файловые системы из одной
кодировки в другую.

%prep
%setup

%build

%make PREFIX=%_prefix

%install
%makeinstall_std PREFIX=%_prefix

%files
%doc Changes CREDITS
%_bindir/%name
%_mandir/man1/*

%changelog
* Mon Aug 22 2011 Vitaly Lipatov <lav@altlinux.ru> 1.15-alt1
- new version 1.15 (with rpmrb script)

* Fri Dec 12 2008 Vitaly Lipatov <lav@altlinux.ru> 1.14-alt1
- new version 1.14 (with rpmrb script)

* Tue Dec 02 2008 Vitaly Lipatov <lav@altlinux.ru> 1.13-alt1
- new version 1.13 (with rpmrb script)

* Thu Jan 24 2008 Vitaly Lipatov <lav@altlinux.ru> 1.12-alt1
- new version 1.12 (with rpmrb script)

* Tue Jan 22 2008 Vitaly Lipatov <lav@altlinux.ru> 1.11-alt1
- new version 1.11 (with rpmrb script)

* Sun Sep 03 2006 Vitaly Lipatov <lav@altlinux.ru> 1.10-alt0.1
- new version 1.10 (with rpmrb script)

* Thu Dec 15 2005 Vitaly Lipatov <lav@altlinux.ru> 1.09-alt1
- new version

* Thu Dec 16 2004 Vitaly Lipatov <lav@altlinux.ru> 1.08-alt1.1
- fix spec and buildreq

* Sat Sep 04 2004 Vitaly Lipatov <lav@altlinux.ru> 1.08-alt1
- new version

* Mon May 17 2004 Vitaly Lipatov <lav@altlinux.ru> 1.07-alt1.1
- rebuild with glibc 2.3

* Tue Jan 06 2004 Vitaly Lipatov <lav@altlinux.ru> 1.07-alt1
- first build for Sisyphus
