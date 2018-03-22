Name: python-module-icalendar
Version: 4.0.1
Release: alt1
Summary: iCalendar parser/generator
License: GPLv2.1
Group: Development/Python
BuildArch: noarch
%setup_python_module icalendar
Source: icalendar-%version.tar.gz
Url: http://pypi.python.org/pypi/icalendar

# Automatically added by buildreq on Mon Mar 26 2018
# optimized out: python-base python-devel python-module-OpenSSL python-module-PyStemmer python-module-Pygments python-module-SQLAlchemy python-module-asn1crypto python-module-babel python-module-backports.ssl_match_hostname python-module-cffi python-module-chardet python-module-cryptography python-module-cssselect python-module-docutils python-module-enum34 python-module-idna python-module-imagesize python-module-ipaddress python-module-jinja2 python-module-lxml python-module-markupsafe python-module-ndg-httpsclient python-module-ntlm python-module-py python-module-pycparser python-module-pytest python-module-pytz python-module-requests python-module-setuptools python-module-simplejson python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinxcontrib python-module-typing python-module-urllib3 python-module-webencodings python-module-whoosh python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-xml python3 python3-base python3-module-OpenSSL python3-module-Pygments python3-module-SQLAlchemy python3-module-asn1crypto python3-module-babel python3-module-cffi python3-module-chardet python3-module-cryptography python3-module-docutils python3-module-genshi python3-module-html5lib python3-module-idna python3-module-imagesize python3-module-jinja2 python3-module-lxml python3-module-markupsafe python3-module-ndg-httpsclient python3-module-ntlm python3-module-py python3-module-pytest python3-module-pytz python3-module-requests python3-module-setuptools python3-module-six python3-module-sphinx python3-module-urllib3 python3-module-webencodings python3-module-whoosh xz
BuildRequires: ctags python-module-alabaster python-module-dateutil python-module-html5lib python-module-jinja2-tests python-module-sphinx_rtd_theme python-module-sphinxcontrib-websupport python3-dev python3-module-alabaster python3-module-dateutil python3-module-jinja2-tests python3-module-sphinx_rtd_theme python3-module-sphinxcontrib-websupport time

%description
iCalendar is a parser/generator of iCalendar files
(RFC 2445) for use with Python.

%package -n python3-module-%modulename
Group: Development/Python
Summary: iCalendar parser/generator
%description -n python3-module-%modulename
iCalendar is a parser/generator of iCalendar files
(RFC 2445) for use with Python3.

%prep
%setup -n %modulename-%version

%build
%python_build -b build2
PYTHONPATH=../src %make -C docs html BUILDDIR=build2
%python3_build -b build3
PYTHONPATH=../src %make -C docs html BUILDDIR=build3 SPHINXBUILD=py3_sphinx-build

%install
rm -f build && ln -sf build2 build
%python_install
rm -f build && ln -sf build3 build
%python3_install

%files
%doc docs/build2/html *.rst
%python_sitelibdir_noarch/%modulename
%python_sitelibdir_noarch/%modulename-*

%files -n python3-module-%modulename
%doc docs/build3/html *.rst
%python3_sitelibdir_noarch/%modulename
%python3_sitelibdir_noarch/%modulename-*
%_bindir/*

%changelog
* Thu Mar 22 2018 Fr. Br. George <george@altlinux.ru> 4.0.1-alt1
- Autobuild version bump to 4.0.1
- Python3 module introdice

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

