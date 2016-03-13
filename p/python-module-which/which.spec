%define oname which

%def_with python3

Name: python-module-%oname
Version: 1.1.0
Release: alt1.1
Summary: A portable GNU which replacement implemented in Python
License: MIT
Group: Development/Python
Url: http://code.google.com/p/which/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildPreReq: python-tools-2to3
%endif

%description
which.py is a small GNU-which replacement. It has the following
features:

* it is portable (Windows, Linux, Mac OS X, Un*x);
* it understands PATHEXT and "App Paths" registration on Windows (i.e.
  it will find everything that start does from the command shell);
* it can print all matches on the PATH;
* it can note "near misses" on the PATH (e.g. files that match but may
  not, say, have execute permissions); and
* it can be used as a Python module.

%if_with python3
%package -n python3-module-%oname
Summary: A portable GNU which replacement implemented in Python
Group: Development/Python3

%description -n python3-module-%oname
which.py is a small GNU-which replacement. It has the following
features:

* it is portable (Windows, Linux, Mac OS X, Un*x);
* it understands PATHEXT and "App Paths" registration on Windows (i.e.
  it will find everything that start does from the command shell);
* it can print all matches on the PATH;
* it can note "near misses" on the PATH (e.g. files that match but may
  not, say, have execute permissions); and
* it can be used as a Python module.
%endif

%prep
%setup
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
find -type f -name '*.py' -exec 2to3 -w '{}' +
sed -i 's|#!/usr/bin/env python|#!/usr/bin/python3|' which.py
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
%doc *.txt
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1.0-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Sep 17 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1
- Initial build for Sisyphus

