%define major 1.4
Name: geda-examples
Version: 1.4.2
Release: alt1
Serial: 1

Summary: Design Examples for gEDA/gaf project

License: GPL
Group: Video
Url: http://www.geda.seul.org

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://geda.seul.org/release/v%major/%version/%name-%version.tar.bz2

BuildArch: noarch

%description
Design Examples for gEDA/gaf project.

%prep
%setup -q

%build
%configure
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS ChangeLog NEWS README
%_docdir/geda-doc/examples/

%changelog
* Fri Dec 26 2008 Vitaly Lipatov <lav@altlinux.ru> 1:1.4.2-alt1
- new version (1.4.2)

* Sun Feb 17 2008 Vitaly Lipatov <lav@altlinux.ru> 1:1.4.0-alt1
- new version (1.4.0)

* Sun Jan 13 2008 Vitaly Lipatov <lav@altlinux.ru> 1:1.2.1-alt1
- new version (1.2.1)
- cleanup spec, fix doc install and placement

* Tue Sep 11 2007 Vitaly Lipatov <lav@altlinux.ru> 1:1.2.0-alt1
- new version (1.2.0)

* Fri Jun 08 2007 Vitaly Lipatov <lav@altlinux.ru> 20070526-alt1
- new version (20070526)

* Sat Apr 07 2007 Vitaly Lipatov <lav@altlinux.ru> 20070216-alt1
- new version (20070216)

* Sun Sep 10 2006 Vitaly Lipatov <lav@altlinux.ru> 20060906-alt0.1
- new version (20060906)

* Sun Jun 11 2006 Vitaly Lipatov <lav@altlinux.ru> 20060123-alt0.1
- new version (20060123)

* Wed Sep 14 2005 Vitaly Lipatov <lav@altlinux.ru> 20050820-alt0.1
- new version

* Sat Feb 05 2005 Vitaly Lipatov <lav@altlinux.ru> 20041228-alt0.1
- first build for ALT Linus Sisyphus

