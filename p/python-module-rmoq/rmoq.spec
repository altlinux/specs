%define oname rmoq

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.2.5
Release: alt1.git20150118
Summary: A simple request-mocker that will download
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/rmoq/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/relekang/rmoq.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-mock python-module-six
BuildPreReq: python-module-requests python-modules-json
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-mock python3-module-six
BuildPreReq: python3-module-requests
%endif

%py_provides %oname
%py_requires mock six requests

%description
A simple request mocker that caches requests responses to files.

%package -n python3-module-%oname
Summary: A simple request-mocker that will download
Group: Development/Python3
%py3_provides %oname
%py3_requires mock six requests

%description -n python3-module-%oname
A simple request mocker that caches requests responses to files.

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
export LC_ALL=en_US.UTF-8
python setup.py test
py.test -vv
%if_with python3
pushd ../python3
python3 setup.py test
py.test-%_python3_version -vv
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
* Mon Jan 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.5-alt1.git20150118
- Initial build for Sisyphus

