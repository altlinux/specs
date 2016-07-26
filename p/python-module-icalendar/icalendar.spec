Name: python-module-icalendar
Version: 3.10
Release: alt1
Summary: iCalendar parser/generator
License: GPLv2.1
Group: Development/Python
BuildArch: noarch
%setup_python_module icalendar
Source: icalendar-%version.tar.gz
Url: http://pypi.python.org/pypi/icalendar

# Automatically added by buildreq on Wed Apr 22 2015
# optimized out: python-base python-devel python-module-BeautifulSoup python-module-PyStemmer python-module-docutils python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest
BuildRequires: ctags python-module-Pygments python-module-cssselect python-module-html5lib python-module-pytz python-module-sphinx_rtd_theme time

%description
iCalendar is a parser/generator of iCalendar files
(RFC 2445) for use with Python.

%prep
%setup -n %modulename-%version

%build
%python_build
PYTHONPATH=../src %make -C docs html

%install
%python_install

%files
%doc docs/_build/html *.rst
%python_sitelibdir_noarch/%modulename
%python_sitelibdir_noarch/%modulename-*

%changelog
* Tue Jul 26 2016 Fr. Br. George <george@altlinux.ru> 3.10-alt1
- Autobuild version bump to 3.10

* Wed Nov 18 2015 Fr. Br. George <george@altlinux.ru> 3.9.1-alt1
- Autobuild version bump to 3.9.1

* Wed Apr 22 2015 Fr. Br. George <george@altlinux.ru> 3.9.0-alt1
- Autobuild version bump to 3.9.0
- Fix documentation build

* Mon Feb 02 2015 Fr. Br. George <george@altlinux.ru> 3.8.4-alt1
- Autobuild version bump to 3.8.4

* Sat Sep 27 2014 Fr. Br. George <george@altlinux.ru> 3.8.3-alt1
- Autobuild version bump to 3.8.3

* Tue Aug 19 2014 Fr. Br. George <george@altlinux.ru> 3.8.2-alt1
- Autobuild version bump to 3.8.2

* Mon Jun 09 2014 Fr. Br. George <george@altlinux.ru> 3.7-alt1
- Autobuild version bump to 3.7

* Wed Jan 15 2014 Fr. Br. George <george@altlinux.ru> 3.6.1-alt1
- Autobuild version bump to 3.6.1

* Thu Aug 22 2013 Fr. Br. George <george@altlinux.ru> 3.5-alt1
- Autobuild version bump to 3.5

* Thu Feb 14 2013 Fr. Br. George <george@altlinux.ru> 3.3-alt1
- Autobuild version bump to 3.3

* Tue Nov 08 2011 Fr. Br. George <george@altlinux.ru> 2.2-alt1
- Autobuild version bump to 2.2

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.1-alt1.1
- Rebuild with Python-2.7

* Mon Jul 04 2011 Fr. Br. George <george@altlinux.ru> 2.1-alt1
- Autobuild version bump to 2.1

