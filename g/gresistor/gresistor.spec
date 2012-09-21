Summary: Identify resistors
Name: gresistor
Version: 0.0.1
Release: alt3.1.1.qa1
License: GPL
Group: Sciences/Physics
URL: http://www.minipop.org/index.php?file=progs/gresistor/gresistor.tpl
Packager: Mikhail Pokidko <pma@altlinux.org>
Source: %name-%{version}.tar.gz
#Patch1: %name.python2.5.patch

BuildArch: noarch

#BuildRequires: python

# Automatically added by buildreq on Wed Sep 13 2006
BuildRequires: python-devel python-modules-encodings
BuildRequires: desktop-file-utils

%description
To allow for identification, resistors are usually marked with colored bands. 
Often referred to as color codes, these markings are indicative of their 
resistance, tolerance, and temperature coefficient. gResistror is a great 
program that will help you translate resistor color codes into a readable 
value. All you have to do is watch the colors on the resistor and then 
enter them in the program. As you enter, you'll see that the resistor 
value is changing according to the selected color.

%prep
%setup
#patch1 -p1

%build
python setup.py build

%install
python setup.py install --prefix %buildroot%_prefix
desktop-file-install --dir %buildroot%_desktopdir \
	--remove-category=Utility \
	--remove-category=gResistor \
	--add-category=Engineering \
	--add-category=Electronics \
	--remove-key=Version \
	%buildroot%_desktopdir/gresistor.desktop

%files
%doc README
%_bindir/%name
%_datadir/%name/
%_datadir/applications/%name.desktop
#python_sitelibdir/SimpleGladeApp.py*
%python_sitelibdir/*

%changelog
* Fri Sep 21 2012 Repocop Q. A. Robot <repocop@altlinux.org> 0.0.1-alt3.1.1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for gresistor
  * postclean-03-private-rpm-macros for the spec file

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.0.1-alt3.1.1
- Rebuild with Python-2.7

* Wed Dec 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt3.1
- Rebuilt with python 2.6

* Thu Apr 03 2008 Mikhail Pokidko <pma@altlinux.org> 0.0.1-alt3
- repocop fixes

* Sat Feb 02 2008 Grigory Batalov <bga@altlinux.ru> 0.0.1-alt2.1
- Rebuilt with python-2.5.

* Sat Feb 02 2008 Grigory Batalov <bga@altlinux.ru> 0.0.1-alt2
- Build as noarch.
- Use python_sitelibdir macro while packaging.

* Mon Sep 11 2006 Mikhail Pokidko <pma@altlinux.org> 0.0.1-alt1
- Initial package.
