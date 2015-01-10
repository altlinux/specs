%define oname sse

%def_with python3

Name: python-module-%oname
Version: 1.2
Release: alt1.git20130701
Summary: Server-Sent Events protocol implemetation
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/sse/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/niwibe/sse.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
%endif

%py_provides %oname

%description
Server Sent Events protocol implemetation on python2 and python3 in the
same codebase.

%package -n python3-module-%oname
Summary: Server-Sent Events protocol implemetation
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Server Sent Events protocol implemetation on python2 and python3 in the
same codebase.

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
python tests.py -v
%if_with python3
pushd ../python3
python3 tests.py -v
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
* Sat Jan 10 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.git20130701
- Initial build for Sisyphus

