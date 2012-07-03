Name: python-doc
Version: 2.6
Release: alt1

Summary: Documentation for the Python programming language
Summary(ru_RU.UTF-8): Документация по языку программирования Python.

Packager: Python Development Team <python@packages.altlinux.org>

License: PSF
Group: Development/Python
Url: http://www.python.org/doc/current/

BuildArch: noarch
AutoReqProv: no

#%define python_infofiles python-{api,ext,lib,ref,tut}.info

Source: http://docs.python.org/ftp/python/doc/%version/python-docs-html.tar.bz2
#Source1: python-info-%version.tar.bz2

%description
Documentation for the Python programming language, interpreter,
and bundled module library in the HTML format.

%description -l ru_RU.UTF-8
Документация по языку программирования Python, его интерпретатору
и распространяемой с ним библиотеке модулей, в формате HTML.

%prep
%setup -q -n python-docs-html

%files
%doc *

%changelog
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
