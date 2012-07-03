# test new macroses
%define python_build CFLAGS="%optflags" %__python setup.py build
%define python_install %__python setup.py install --root %buildroot

Name: pybackpack
Version: 0.5.4
Release: alt1.1.1

Summary: User oriented backup and restore application

License: GPL
Group: File tools
Url: http://andrewprice.me.uk/projects/pybackpack/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://andrewprice.me.uk/projects/pybackpack/download/%name-%version.tar.bz2

Requires: rdiff-backup >= 1.0
BuildArch: noarch

# Automatically added by buildreq on Fri Apr 06 2007
BuildRequires: python-devel python-modules-encodings rdiff-backup

%description
A GTK+ tool written in Python to backup files.

%prep
%setup -q

%build
%python_build

%install
%python_install

%files
%doc COPYING CHANGELOG INSTALL
%_bindir/pybackpack
%dir %python_sitelibdir/pybackpack/
%python_sitelibdir/pybackpack/*.py*
%python_sitelibdir/pybackpack/*.glade
%_pixmapsdir/*.png
%_man1dir/*
%_desktopdir/pybackpack.desktop

%changelog
* Tue Oct 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.4-alt1.1.1
- Rebuild with Python-2.7

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.4-alt1.1
- Rebuilt with python 2.6

* Thu Jun 19 2008 Vitaly Lipatov <lav@altlinux.ru> 0.5.4-alt1
- new version 0.5.4 (with rpmrb script)

* Wed Oct 24 2007 Vitaly Lipatov <lav@altlinux.ru> 0.5.1-alt1
- new version 0.5.1 (with rpmrb script)

* Thu Apr 05 2007 Vitaly Lipatov <lav@altlinux.ru> 0.4.5-alt1
- initial build for ALT Linux Sisyphus

* Sat Jan 06 2007 Andy Price <andy@andrewprice.me.uk> - 0.4.5-1
- Updated RPM to 0.4.5
* Mon Nov 20 2006 Andy Price <andy@andrewprice.me.uk> - 0.4.4-1
- Updated RPM to 0.4.4
* Tue Nov 14 2006 Andy Price <andy@andrewprice.me.uk> - 0.4.3-1
- Updated RPM to 0.4.3
* Sat Apr 22 2006 Dave Arter <davea@sucs.org> - 0.4.2-1
- Updated RPM to 0.4.2
* Sun Sep 18 2005 Dave Arter <davea@sucs.org> - 0.4.1-1
- Initial package attempt, using Jeff Spaleta's spec file
