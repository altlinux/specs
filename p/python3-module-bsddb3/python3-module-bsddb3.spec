%define pypi_name bsddb3
%def_disable check

Name: python3-module-%pypi_name
Version: 6.2.9
Release: alt1.1

Summary: Python bindings for BerkleyDB
Group: Development/Python3
License: BSD-3-Clause
Url: https://pypi.python.org/pypi/bsddb3/

Source: https://pypi.io/packages/source/b/%pypi_name/%pypi_name-%version.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(wheel) python3(setuptools)
BuildRequires: libdb4-devel python3-devel
BuildRequires: chrpath
%{?_enable_check:BuildRequires: /proc python3-test}

%description
This package provides Python 3 wrappers for Berkeley DB                                          .

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install
chrpath -d %buildroot%python3_sitelibdir/%pypi_name/*.so

%check
%__python3 test.py

%files
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%exclude %python3_sitelibdir/%pypi_name/tests/
%exclude %_includedir/python*/%pypi_name/bsddb.h

%changelog
* Mon Mar 25 2024 Yuri N. Sedunov <aris@altlinux.org> 6.2.9-alt1.1
- fixed build

* Fri Nov 27 2020 Yuri N. Sedunov <aris@altlinux.org> 6.2.9-alt1
- 6.2.9

* Fri Nov 20 2020 Yuri N. Sedunov <aris@altlinux.org> 6.2.8-alt1
- 6.2.8 (python3-only)

* Thu Feb 13 2020 Yuri N. Sedunov <aris@altlinux.org> 6.2.7-alt1
- 6.2.7
- made python2 build optional
- fixed License tag

* Wed Jul 11 2018 Yuri N. Sedunov <aris@altlinux.org> 6.2.6-alt1
- 6.2.6

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 6.2.5-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Fri Sep 15 2017 Yuri N. Sedunov <aris@altlinux.org> 6.2.5-alt1
- 6.2.5

* Sat Jan 28 2017 Yuri N. Sedunov <aris@altlinux.org> 6.2.4-alt1
- 6.2.4

* Wed Jun 01 2016 Yuri N. Sedunov <aris@altlinux.org> 6.2.1-alt1
- 6.2.1

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 6.1.1-alt1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Fri Feb 19 2016 Yuri N. Sedunov <aris@altlinux.org> 6.1.1-alt1
- 6.1.1

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 6.0.1-alt1.1
- NMU: Use buildreq for BR.

* Sun Jul 06 2014 Yuri N. Sedunov <aris@altlinux.org> 6.0.1-alt1
- first build for Sisyphus

