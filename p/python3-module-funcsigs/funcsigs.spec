%define _unpackaged_files_terminate_build 1
%define oname funcsigs

Name: python3-module-%oname
Version: 1.0.2
Release: alt4
Summary: Python function signatures from PEP362 for Python 2.6, 2.7 and 3.2+
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.python.org/pypi/funcsigs/

# https://github.com/aliles/funcsigs.git
Source0: https://pypi.python.org/packages/94/4a/db842e7a0545de1cdb0439bb80e6e42dfe82aaeaadd4072f2263a4fbed23/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-module-unittest2 python3-module-coverage
BuildPreReq: python3-module-flake8 python3-module-wheel

%py3_provides %oname

%description
funcsigs is a backport of the PEP 362 function signature features from
Python 3.3's inspect module. The backport is compatible with Python 2.6,
2.7 as well as 3.2 and up.

%prep
%setup -n %{oname}-%{version}

%build
%python3_build

%install
%python3_install

%check
python3 setup.py test
flake8 --exit-zero funcsigs tests

%files
%doc CHANGELOG *.rst docs/*.rst
%python3_sitelibdir/*

%changelog
* Wed Jul 28 2021 Grigory Ustinov <grenka@altlinux.org> 1.0.2-alt4
- Drop python2 support.

* Mon Oct 19 2020 Stanislav Levin <slev@altlinux.org> 1.0.2-alt3
- Disabled Python2 testing.

* Wed Jan 30 2019 Mikhail Gordeev <obirvalger@altlinux.org> 1.0.2-alt2
- Fix build with flake8

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4-alt1.git20131220.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1.git20131220
- Initial build for Sisyphus

