%define _unpackaged_files_terminate_build 1

%define pypi_name WebOb

%def_with check

Name: python3-module-webob
Version: 1.8.8
Release: alt1

Summary: WSGI request and response object
License: MIT
Group: System/Libraries
Url: https://pypi.org/project/WebOb
Vcs: https://github.com/Pylons/webob

Source0: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3(pytest)
%endif

%description
WebOb provides wrappers around the WSGI request environment, and an object to
help create WSGI responses. The objects map much of the specified behavior of
HTTP, including header parsing and accessors for other standard parts of the
environment.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -v

%files
%doc README.rst
%python3_sitelibdir_noarch/webob/
%python3_sitelibdir_noarch/%pypi_name-%version.dist-info

%changelog
* Wed Aug 14 2024 Anton Vyatkin <toni@altlinux.org> 1.8.8-alt1
- New version 1.8.8.

* Fri Jan 26 2024 Anton Vyatkin <toni@altlinux.org> 1.8.7-alt2
- Fixed FTBFS.

* Tue Mar 29 2022 Stanislav Levin <slev@altlinux.org> 1.8.7-alt1
- 1.8.6 -> 1.8.7.

* Fri Jul 23 2021 Grigory Ustinov <grenka@altlinux.org> 1.8.6-alt2
- Drop python2 support.

* Tue Mar 31 2020 Igor Vlasenko <viy@altlinux.ru> 1.8.6-alt1
- new version

* Wed Jan 09 2019 Alexey Shabalin <shaba@altlinux.org> 1.8.5-alt1
- new version

* Wed Mar 14 2018 Igor Vlasenko <viy@altlinux.ru> 1.7.4-alt1_3
- new version

* Wed Jan 18 2017 Igor Vlasenko <viy@altlinux.ru> 1.7.1-alt1
- automated PyPI update

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.7.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.5.0-alt1.a0.git20150731.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.5.0-alt1.a0.git20150731.1
- NMU: Use buildreq for BR.

* Sat Aug 29 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt1.a0.git20150731
- Version 1.5.0a0

* Fri Feb 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.1-alt1.dev.git20150127
- Version 1.4.1dev

* Wed Jul 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4-alt1
- Version 1.4

* Thu Jan 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt1
- Version 1.3.1

* Sun Mar 03 2013 Aleksey Avdeev <solo@altlinux.ru> 1.2.3-alt1
- Version 1.2.3

* Sat May 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.b3.git20120504
- Version 1.2b3
- Added module for Python 3

* Mon Dec 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.b2.git20111206
- Version 1.2b2

* Mon Dec 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt1.hg20110917
- Version 1.1.1

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.7-alt1.hg20110430.1
- Rebuild with Python-2.7

* Tue May 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.7-alt1.hg20110430
- Version 1.0.7

* Fri Nov 19 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.hg20101031
- Version 1.0

* Thu Jul 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.8.post1-alt1.hg20100714
- Version 0.9.8.post1

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.7-alt1.svn20090902.1
- Rebuilt with python 2.6

* Mon Sep 28 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.7-alt1.svn20090902
- Initial build for Sisyphus

