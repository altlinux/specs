%define _unpackaged_files_terminate_build 1
%define oname genty

%def_with check

Name: python3-module-%oname
Version: 1.3.2
Release: alt3
Summary: Allows you to run a test with multiple data sets
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.python.org/pypi/genty/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/box/genty.git
Source0: https://pypi.python.org/packages/c9/bc/eee096fe9ecf1041944f1327cf6a2030fb2c59acd66580b692eb8b540233/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3(mock)
BuildRequires: python3(six)
%endif

%py3_provides %oname
%py3_requires six

%description
Genty, pronounced "gen-tee", stands for "generate tests". It promotes
generative testing, where a single test can execute over a variety of
input.

%prep
%setup -n %{oname}-%{version}

%build
%python3_build_debug

%install
%python3_install

%check
python3 setup.py test

%files
%doc *.rst
%python3_sitelibdir/*

%changelog
* Fri Oct 23 2020 Stanislav Levin <slev@altlinux.org> 1.3.2-alt3
- Dropped dependency on coveralls.

* Sat Aug 01 2020 Grigory Ustinov <grenka@altlinux.org> 1.3.2-alt2
- Drop python2 support.
- Fix license.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.3.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.3.2-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.2.0-alt1.git20150223.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.2.0-alt1.git20150223.1
- NMU: Use buildreq for BR.

* Tue Feb 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt1.git20150223
- Initial build for Sisyphus

