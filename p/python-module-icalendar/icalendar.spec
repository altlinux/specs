Name: python-module-icalendar
Version: 2.2
Release: alt1
Summary: iCalendar parser/generator
License: GPLv2.1
Group: Development/Python
BuildArch: noarch
%setup_python_module icalendar
Source: icalendar-%version.tar.gz
Url: http://pypi.python.org/pypi/icalendar

# Automatically added by buildreq on Tue Nov 08 2011
# optimized out: python-base python-devel python-module-BeautifulSoup python-module-Pygments python-module-docutils python-module-genshi python-module-jinja2 python-module-setuptools python-module-simplejson python-modules python-modules-compiler python-modules-email python-modules-encodings python-modules-logging
BuildRequires: python-module-jinja2-tests python-module-sphinx time

%description
iCalendar is a parser/generator of iCalendar files
(RFC 2445) for use with Python.

%prep
%setup -n %modulename-%version

%build
%python_build
%make -C docs html

%install
%python_install

%files
%doc docs/_build/html *.txt
%python_sitelibdir_noarch/%modulename
%python_sitelibdir_noarch/%modulename-*

%changelog
* Tue Nov 08 2011 Fr. Br. George <george@altlinux.ru> 2.2-alt1
- Autobuild version bump to 2.2

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.1-alt1.1
- Rebuild with Python-2.7

* Mon Jul 04 2011 Fr. Br. George <george@altlinux.ru> 2.1-alt1
- Autobuild version bump to 2.1

