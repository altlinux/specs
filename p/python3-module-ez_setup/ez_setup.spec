%define oname ez_setup
Name: python3-module-%oname
Version: 0.9
Release: alt1.1
Summary: ez_setup.py and distribute_setup.py
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/ez_setup/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/ActiveState/ez_setup.git
Source0: https://pypi.python.org/packages/ba/2c/743df41bd6b3298706dfe91b0c7ecdc47f2dc1a3104abeb6e9aa4a45fa5d/ez_setup-%{version}.tar.gz
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools

%py3_provides %oname

%description
ez_setup.py and distribute_setup.py.

%prep
%setup -q -n ez_setup-%{version}

%build
%python3_build_debug

%install
%python3_install

%check
python3 setup.py test

%files
%doc *.txt *.rst
%python3_sitelibdir/*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.9-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Jan 06 2017 Igor Vlasenko <viy@altlinux.ru> 0.9-alt1
- automated PyPI update

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1-alt1.dev.git20101122.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Oct 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.dev.git20101122
- Initial build for Sisyphus

