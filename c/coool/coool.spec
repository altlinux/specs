Name: coool
Version: 1.1
Release: alt1.2.1

Summary: It checks OpenOffice.org documents for broken Links

License: GPL
Group: Office
Url: http://free-electrons.com/community/tools/utils/coool/en

BuildArch: noarch
Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://free-electrons.com/pub/utils/coool/coool-1.1

%description
The package contains coool utility.
It checks OpenOffice.org documents for broken Links.

%install
install -D -m0755 %SOURCE0 %buildroot/%_bindir/coool

%files
%_bindir/*

%changelog
* Tue Oct 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1-alt1.2.1
- Rebuild with Python-2.7

* Tue Dec 01 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1.2
- Rebuilt with python 2.6

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 1.1-alt1.1
- Rebuilt with python-2.5.

* Sat Oct 13 2007 Vitaly Lipatov <lav@altlinux.ru> 1.1-alt1
- new version (1.1)

* Sat Oct 15 2005 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt0.1beta
- first build for ALT Linux Sisyphus
