Name: python-doc
Version: 2.7.17
Release: alt1

Summary: Documentation for the Python programming language
Summary(ru_RU.UTF-8): Документация по языку программирования Python.

Packager: Python Development Team <python@packages.altlinux.org>

License: PSF
Group: Development/Python
Url: http://docs.python.org/2/

BuildArch: noarch
AutoReqProv: no

#%define python_infofiles python-{api,ext,lib,ref,tut}.info

Source: python-%version-docs-html.tar.bz2
#Source1: python-info-%version.tar.bz2

%description
Documentation for the Python programming language, interpreter,
and bundled module library in the HTML format.

%description -l ru_RU.UTF-8
Документация по языку программирования Python, его интерпретатору
и распространяемой с ним библиотеке модулей, в формате HTML.

%prep
%setup -n python-%version-docs-html

%files
%doc *

%changelog
* Mon Nov 04 2019 Fr. Br. George <george@altlinux.ru> 2.7.17-alt1
- Autobuild version bump to 2.7.17

* Tue Feb 20 2018 Fr. Br. George <george@altlinux.ru> 2.7.14-alt1
- Autobuild version bump to 2.7.14

* Mon Mar 13 2017 Fr. Br. George <george@altlinux.ru> 2.7.13-alt1
- Autobuild version bump to 2.7.13

* Tue Jul 26 2016 Fr. Br. George <george@altlinux.ru> 2.7.12-alt1
- Autobuild version bump to 2.7.12

* Thu Dec 24 2015 Fr. Br. George <george@altlinux.ru> 2.7.11-alt1
- Autobuild version bump to 2.7.11

* Tue Jul 14 2015 Fr. Br. George <george@altlinux.ru> 2.7.10-alt1
- Autobuild version bump to 2.7.10

* Wed Jan 28 2015 Fr. Br. George <george@altlinux.ru> 2.7.9-alt1
- Autobuild version bump to 2.7.9

* Tue Aug 19 2014 Fr. Br. George <george@altlinux.ru> 2.7.8-alt1
- Autobuild version bump to 2.7.8

* Mon Jun 09 2014 Fr. Br. George <george@altlinux.ru> 2.7.7-alt1
- Autobuild version bump to 2.7.7

* Wed Jan 15 2014 Fr. Br. George <george@altlinux.ru> 2.7.6-alt1
- Autobuild version bump to 2.7.6

* Mon May 20 2013 Fr. Br. George <george@altlinux.ru> 2.7.5-alt1
- Autobuild version bump to 2.7.5

* Sun Nov 25 2012 Fr. Br. George <george@altlinux.ru> 2.7.3-alt1
- Autobuild version bump to 2.7.3

* Thu Jan 28 2010 Evgeny Sinelnikov <sin@altlinux.ru> 2.6-alt1
- new version for python 2.6 updated at October 02, 2008

* Thu May 01 2008 Vitaly Lipatov <lav@altlinux.ru> 2.5.2-alt1
- new version 2.5.2 (with rpmrb script)

* Sun Nov 12 2006 Vitaly Lipatov <lav@altlinux.ru> 2.4.4-alt0.1
- new version 2.4.4 (with rpmrb script)

* Tue Nov 01 2005 Vitaly Lipatov <lav@altlinux.ru> 2.4.2-alt1
- new version

* Sun Apr 17 2005 Vitaly Lipatov <lav@altlinux.ru> 2.4.1-alt1
- updated to 2.4.1

* Sat Feb 21 2004 Mikhail Zabaluev <mhz@altlinux.ru> 2.3.3-alt1
- Updated to 2.3.3

* Fri Dec 27 2002 Mikhail Zabaluev <mhz@altlinux.ru> 2.2.2-alt1
- 2.2.2

* Sun Nov 10 2002 Stanislav Ievlev <inger@altlinux.ru> 2.2-alt2
- rebuild

* Tue Jan 29 2002 Stanislav Ievlev <inger@altlinux.ru> 2.2-alt1
- renamed to doc

* Fri Jan 04 2002 Mikhail Zabaluev <mhz@altlinux.ru> 2.2-alt1
- New version

* Tue Sep 04 2001 Mikhail Zabaluev <mhz@altlinux.ru> 2.1.1-alt3
- Singled out from the python package
