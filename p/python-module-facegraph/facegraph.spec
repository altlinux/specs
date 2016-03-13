%define oname facegraph

%def_with python3

Name: python-module-%oname
Version: 0.0.36
Release: alt1.git20140108.1
Summary: A client library for the Facebook Graph API
License: Free
Group: Development/Python
Url: https://pypi.python.org/pypi/pyfacegraph/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/colinhowe/pyFaceGraph.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%description
pyFaceGraph is a Python client library for the Facebook Graph API.

%package -n python3-module-%oname
Summary: A client library for the Facebook Graph API
Group: Development/Python3

%description -n python3-module-%oname
pyFaceGraph is a Python client library for the Facebook Graph API.

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

%files
%doc *.md UNLICENSE
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md UNLICENSE
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.36-alt1.git20140108.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Sep 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.36-alt1.git20140108
- Initial build for Sisyphus

