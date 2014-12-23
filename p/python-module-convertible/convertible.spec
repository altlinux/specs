%define oname convertible

%def_with python3

Name: python-module-%oname
Version: 0.12
Release: alt1.git20141223
Summary: Python library for converting object into dictionary/list structures and json
License: GPLv3
Group: Development/Python
Url: https://pypi.python.org/pypi/convertible/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/syncloud/convertible.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-jsonpickle python-module-pytest-cov
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-jsonpickle python3-module-pytest-cov
%endif

%py_provides %oname

%description
Python library for converting object into dictionary/list structures and
json.

%package -n python3-module-%oname
Summary: Python library for converting object into dictionary/list structures and json
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Python library for converting object into dictionary/list structures and
json.

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
py.test
#if_with python3
%if 0
pushd ../python3
python3 setup.py test
py.test-%_python3_version
popd
%endif

%files
%doc *.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%endif

%changelog
* Tue Dec 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.12-alt1.git20141223
- Initial build for Sisyphus

