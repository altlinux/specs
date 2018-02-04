%define oname pluggy

%def_with python3

Name: python-module-%oname
Version: 0.3.0
Release: alt1.git20150528.2.1
Summary: Plugin and hook calling mechanisms for python
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pluggy/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/hpk42/pluggy.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildRequires: python-module-pytest
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildRequires: python3-module-pytest
%endif

%py_provides %oname

%description
This is the plugin manager as used by pytest but stripped of pytest
specific details.

%if_with python3
%package -n python3-module-%oname
Summary: Plugin and hook calling mechanisms for python
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
This is the plugin manager as used by pytest but stripped of pytest
specific details.
%endif

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
python setup.py test -v
py.test -vv
%if_with python3
pushd ../python3
python3 setup.py test -v
py.test3 -vv
popd
%endif

%files
%doc CHANGELOG *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc CHANGELOG *.rst
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.3.0-alt1.git20150528.2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Jul 13 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.3.0-alt1.git20150528.2
- Fixed build spec with py.test3

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.0-alt1.git20150528.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Jul 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt1.git20150528
- Initial build for Sisyphus

