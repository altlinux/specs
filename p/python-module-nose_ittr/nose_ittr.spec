%define oname nose_ittr

%def_without python3

Name: python-module-%oname
Version: 0.0.4
Release: alt1.git20141202.1
Summary: nose extension for supporting parametrized testing
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/nose_ittr
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/taykey/nose-ittr.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-nose python-modules-logging
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-nose
%endif

%py_provides %oname

%description
Allows developer to run the same test over and over again using
different values.

Main Features:

* Very easy to integrate with existing tests
* Saves a lot of boilerplate code, and code replication
* Work with all nose plugins (including multiprocessing)

%if_with python3
%package -n python3-module-%oname
Summary: nose extension for supporting parametrized testing
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Allows developer to run the same test over and over again using
different values.

Main Features:

* Very easy to integrate with existing tests
* Saves a lot of boilerplate code, and code replication
* Work with all nose plugins (including multiprocessing)
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
%doc *.txt *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%python3_sitelibdir/*
%endif

# TODO: enable test_ittr_params_to_setup

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.0.4-alt1.git20141202.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Mar 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.4-alt1.git20141202
- Version 0.0.4

* Fri Nov 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.3-alt1.git20141127
- Version 0.0.3

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.2-alt1.git20141127
- Version 0.0.2

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt1.git20141126
- Initial build for Sisyphus

