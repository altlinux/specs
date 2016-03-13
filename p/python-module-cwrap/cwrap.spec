%define oname cwrap

%def_with python3

Name: python-module-%oname
Version: 0.0.0
Release: alt2.git20110510.1
Summary: Automatical generate Cython wrappers from C header files
License: Free
Group: Development/Python
Url: https://github.com/enthought/cwrap
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/enthought/cwrap.git
Source: %name-%version.tar

BuildPreReq: python-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python-tools-2to3
%endif

BuildArch: noarch

Requires: gccxml

%description
Automatical generate Cython wrappers from C header files.

%package -n python3-module-%oname
Summary: Automatical generate Cython wrappers from C header files
Group: Development/Python3
Requires: gccxml

%description -n python3-module-%oname
Automatical generate Cython wrappers from C header files.

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
%doc examples/test/*
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc examples/test/*
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.0-alt2.git20110510.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Aug 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.0-alt2.git20110510
- Added module for Python3

* Fri Dec 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.0-alt1.git20110510
- Initial build for Sisyphus

