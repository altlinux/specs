%def_without check

%define oname icalendar

Name: python3-module-%oname
Version: 5.0.11
Release: alt1

Summary: iCalendar parser/generator
License: GPLv2.1
Group: Development/Python3
Url: https://pypi.org/project/icalendar/

BuildArch: noarch

Source: %oname-%version.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-sphinx

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-dateutil
BuildRequires: python3-module-pytz
BuildRequires: python3-module-coverage
BuildRequires: python3-module-hypothesis
%endif

%description
iCalendar is a parser/generator of iCalendar files
(RFC 2445) for use with Python.

%prep
%setup -n %oname-%version

%build
%pyproject_build
PYTHONPATH=../src %make -C docs html BUILDDIR=build3 SPHINXBUILD=py3_sphinx-build

%install
%pyproject_install

%check
%pyproject_run_pytest src/icalendar/tests

%files
%doc docs/build3/html *.rst
%_bindir/*
%python3_sitelibdir_noarch/%oname
%python3_sitelibdir_noarch/%oname-%version.dist-info

%changelog
* Sun Nov 05 2023 Grigory Ustinov <grenka@altlinux.org> 5.0.11-alt1
- Automatically updated to 5.0.11 (Closes: #48334).

* Tue Apr 14 2020 Andrey Bychkov <mrdrew@altlinux.org> 4.0.3-alt2
- Build for python2 disabled.

* Mon Apr 29 2019 Fr. Br. George <george@altlinux.ru> 4.0.3-alt1
- Autobuild version bump to 4.0.3

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

