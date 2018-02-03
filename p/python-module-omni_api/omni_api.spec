%define oname omni_api

%def_with python3

Name: python-module-%oname
Version: 0.3.1
Release: alt1.1
Summary: Omni API
License: Apache-2.0
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/omni_api/

# https://github.com/hivesolutions/omni_api.git
Source: %name-%version.tar

BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-appier
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-appier
%endif

%py_provides omni

%description
Simple rest api wrapper for the omni infra-structure.

%package -n python3-module-%oname
Summary: Omni API
Group: Development/Python3
%py3_provides omni

%description -n python3-module-%oname
Simple rest api wrapper for the omni infra-structure.

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
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.md src/examples
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md src/examples
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.3.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Oct 19 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.3.1-alt1
- Updated to upstream version 0.3.1.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.2-alt1.git20150101.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.2.2-alt1.git20150101.1
- NMU: Use buildreq for BR.

* Fri Jan 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.2-alt1.git20150101
- Version 0.2.2

* Tue Dec 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt1.git20141222
- Version 0.2.1

* Thu Dec 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.18-alt1.git20141210
- Initial build for Sisyphus

