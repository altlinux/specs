%define oname parse_type

%def_with python3

Name: python-module-%oname
Version: 0.3.5
Release: alt1.dev.git20140505.2.1
Summary: parse_type extends the parse module (opposite of string.format())
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/parse_type/

# https://github.com/jenisys/parse_type.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-parse python-module-six
BuildPreReq: python-module-enum34 python-module-coverage
BuildPreReq: python-module-pytest-cov python-module-pytest-runner
BuildPreReq: python-module-tox python-module-argparse
BuildPreReq: python-module-ordereddict
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-parse python3-module-six
BuildPreReq: python3-module-enum34 python3-module-coverage
BuildPreReq: python3-module-pytest-cov python3-module-pytest-runner
BuildPreReq: python3-module-tox python3-module-argparse
%endif

%py_provides %oname
%py_requires parse six enum34

%description
Simplifies to build parse types based on the parse module.

%package -n python3-module-%oname
Summary: parse_type extends the parse module (opposite of string.format())
Group: Development/Python3
%py3_provides %oname
%py3_requires parse six enum34

%description -n python3-module-%oname
Simplifies to build parse types based on the parse module.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
python setup.py test ||:
%if_with python3
pushd ../python3
python3 setup.py test ||:
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.3.5-alt1.dev.git20140505.2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Aug 14 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.3.5-alt1.dev.git20140505.2
- Fixed build.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.5-alt1.dev.git20140505.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Nov 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.5-alt1.dev.git20140505
- Initial build for Sisyphus

