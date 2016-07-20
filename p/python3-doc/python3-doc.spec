Name: python3-doc
Version: 3.5.2
Release: alt1

Summary: Documentation for the Python 3 programming language
Summary(ru_RU.UTF-8): Документация по языку программирования Python.

Packager: Python Development Team <python@packages.altlinux.org>

License: PSF
Group: Development/Python3
Url: http://docs.python.org/3/

BuildArch: noarch
AutoReqProv: no

Source: python-%version-docs-html.tar.bz2

%description
Documentation for the Python 3 programming language, interpreter,
and bundled module library in the HTML format.

%description -l ru_RU.UTF-8
Документация по языку программирования Python 3, его интерпретатору
и распространяемой с ним библиотеке модулей, в формате HTML.

%prep
%setup -n python-%version-docs-html

%files
%doc *

%changelog
* Wed Jul 20 2016 Fr. Br. George <george@altlinux.ru> 3.5.2-alt1
- Autobuild version bump to 3.5.2

* Sat Oct 10 2015 Fr. Br. George <george@altlinux.ru> 3.4.2-alt2
- Change group

* Wed Oct 22 2014 Fr. Br. George <george@altlinux.ru> 3.4.2-alt1
- Autobuild version bump to 3.4.2

* Sat Sep 27 2014 Fr. Br. George <george@altlinux.ru> 3.4.1-alt1
- Autobuild version bump to 3.4.1

* Wed Apr 09 2014 Fr. Br. George <george@altlinux.ru> 3.4.0-alt1
- Autobuild version bump to 3.4.0

* Tue Feb 18 2014 Fr. Br. George <george@altlinux.ru> 3.3.4-alt1
- Autobuild version bump to 3.3.4

* Wed Jan 15 2014 Fr. Br. George <george@altlinux.ru> 3.3.3-alt1
- Autobuild version bump to 3.3.3

* Mon May 20 2013 Fr. Br. George <george@altlinux.ru> 3.3.2-alt1
- Autobuild version bump to 3.3.2

* Mon Nov 26 2012 Fr. Br. George <george@altlinux.ru> 3.3.0-alt1
- Autobuild version bump to 3.3.0

