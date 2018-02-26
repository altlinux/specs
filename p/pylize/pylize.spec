Name: pylize
Version: 1.3b
Release: alt3.1
License: GPL
BuildArch: noarch

URL: http://www.chrisarndt.de/en/software/pylize/
Source: http://chrisarndt.de/en/software/%name/download/%name-%version.tar.bz2

Summary: On-Screen presentation generation tool
Summary(ru_RU.UTF-8): Создание серии слайдов по специально размеченной HTML-странице
Group: Office
Patch0: pylize.install.py.patch
Patch1: pylize.ru.patch

BuildRequires: python-module-em python-devel
Requires: python-module-em

%description
Pylize is a Python script that generates a set of HTML files that
make up an on-screen presentation from a master file. The HTML files
can be viewed with any CSS-aware browser. The master file contains
the text for all the slides and some additional information like
title, author etc. pylize can also create a template master file for
you.

%description -l ru_RU.UTF-8
Pylize -- это сценарий на языке Python, который преобразует в презентацию
исходную HTML-страницу, размеченную по определённым правилам (заголовки кадров,
информацию об авторе и т. п.). Презентация -- это серия слайдов, HTML-страниц,
которые можно просмотреть с помощью любого навигатора, поддерживающего CSS.
Pylize может сгенерировать загатовку для исходного файла, останется только
вписать содержательную часть.

%prep
%setup -q
%patch0
%patch1

%build

%install
python install.py --root=$RPM_BUILD_ROOT --optimize=2 --record=INSTALLED_FILES

%files -f INSTALLED_FILES
%defattr(-,root,root)
%doc doc/*
%doc PKG-INFO TODO README README.empy

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.3b-alt3.1
- Rebuild with Python-2.7

* Tue Apr 12 2011 Fr. Br. George <george@altlinux.ru> 1.3b-alt3
- Clean up spec a little

* Fri Nov 20 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3b-alt2.2
- Rebuilt with python 2.6

* Sat Nov 14 2009 Repocop Q. A. Robot <repocop@altlinux.org> 1.3b-alt2.1.qa1
- NMU (by repocop): the following fixes applied:
  * vendor-tag for pylize
  * postclean-05-filetriggers for spec file

* Fri Jan 25 2008 Grigory Batalov <bga@altlinux.ru> 1.3b-alt2.1
- Rebuilt with python-2.5.

* Tue Mar 13 2007 Fr. Br. George <george@altlinux.ru> 1.3b-alt2
- GEAR adapted with some trivial spec fixes

* Mon Nov 21 2005 Fr. Br. George <george@altlinux.ru> 1.3b-alt1
- Initial ALT build


