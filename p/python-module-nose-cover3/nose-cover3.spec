%define oname nose-cover3

%def_with python3

Name: python-module-%oname
Version: 0.1.0
Release: alt1.git20110913.1
Summary: Coverage 3.x support for Nose
License: LPGLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/nose-cover3/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/ask/nosecover3.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
Coverage 3.x support for Nose.

%package -n python3-module-%oname
Summary: Coverage 3.x support for Nose
Group: Development/Python3

%description -n python3-module-%oname
Coverage 3.x support for Nose.

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

%files
%doc *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.0-alt1.git20110913.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Sep 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1.git20110913
- Initial build for Sisyphus

