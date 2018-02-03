%define oname canonicalize

%def_with python3

Name: python-module-%oname
Version: 1.3
Release: alt1.git20150212.1.1
Summary: Canonicalize a cluster of records
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/canonicalize/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/datamade/canonicalize.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-numpy python-module-affinegap
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-numpy python3-module-affinegap
%endif

%py_provides %oname
%py_requires numpy affinegap

%description
Canoicalize a Cluster of Records.

%if_with python3
%package -n python3-module-%oname
Summary: Canonicalize a cluster of records
Group: Development/Python3
%py3_provides %oname
%py3_requires numpy affinegap

%description -n python3-module-%oname
Canoicalize a Cluster of Records.
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
python setup.py test
export PYTHONPATH=$PWD
python tests/test_canonical.py -v
%if_with python3
pushd ../python3
python3 setup.py test
export PYTHONPATH=$PWD
python3 tests/test_canonical.py -v
popd
%endif

%files
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.3-alt1.git20150212.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3-alt1.git20150212.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Mar 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt1.git20150212
- Initial build for Sisyphus

