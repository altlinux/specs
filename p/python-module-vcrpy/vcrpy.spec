%define oname vcrpy

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 1.1.2
Release: alt1.git20141103
Summary: Automatically mock your HTTP interactions to simplify and speed up testing
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/vcrpy/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/kevin1024/vcrpy.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-yaml python-module-mock
BuildPreReq: python-module-six python-module-contextlib2
BuildPreReq: python-module-wrapt python-module-pytest-localserver
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-yaml python3-module-mock
BuildPreReq: python3-module-six python3-module-contextlib2
BuildPreReq: python3-module-wrapt python3-module-pytest-localserver
%endif

%py_provides vcr

%description
Automatically mock your HTTP interactions to simplify and speed up
testing.

%package -n python3-module-%oname
Summary: Automatically mock your HTTP interactions to simplify and speed up testing
Group: Development/Python3
%py3_provides vcr

%description -n python3-module-%oname
Automatically mock your HTTP interactions to simplify and speed up
testing.

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
%doc *.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%endif

%changelog
* Sat Nov 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.2-alt1.git20141103
- Initial build for Sisyphus

