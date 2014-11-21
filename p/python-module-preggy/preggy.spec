%define oname preggy

%def_with python3

Name: python-module-%oname
Version: 1.1.3
Release: alt1.git20141002
Summary: preggy is an assertion library for Python. (What were you ``expect()``ing?)
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/preggy/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/heynemann/preggy.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests python-module-six
BuildPreReq: python-module-unidecode python-module-nose
BuildPreReq: python-module-yanc python-module-coverage
BuildPreReq: python-module-tox
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-module-setuptools-tests python3-module-six
BuildPreReq: python3-module-unidecode python3-module-nose
BuildPreReq: python3-module-yanc python3-module-coverage
BuildPreReq: python3-module-tox
%endif

%py_provides %oname

%description
preggy is a collection of expectations for python applications,
extracted from the pyVows project.

%package -n python3-module-%oname
Summary: preggy is an assertion library for Python. (What were you ``expect()``ing?)
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
preggy is a collection of expectations for python applications,
extracted from the pyVows project.

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
%if_with python3
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
* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.3-alt1.git20141002
- Initial build for Sisyphus

