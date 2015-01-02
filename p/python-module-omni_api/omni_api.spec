%define oname omni_api

%def_with python3

Name: python-module-%oname
Version: 0.2.2
Release: alt1.git20150101
Summary: Omni API
License: GPLv3
Group: Development/Python
Url: https://pypi.python.org/pypi/omni_api/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/hivesolutions/omni_api.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-appier
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-appier
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
* Fri Jan 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.2-alt1.git20150101
- Version 0.2.2

* Tue Dec 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt1.git20141222
- Version 0.2.1

* Thu Dec 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.18-alt1.git20141210
- Initial build for Sisyphus

