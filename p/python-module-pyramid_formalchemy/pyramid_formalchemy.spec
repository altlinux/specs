%define oname pyramid_formalchemy

%def_with python3

Name: python-module-%oname
Version: 0.4.4
Release: alt2
Summary: FormAlchemy plugins and helpers for Pyramid
License: Free
Group: Development/Python
Url: http://pypi.python.org/pypi/pyramid_formalchemy/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools python-module-babel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools python3-module-babel
BuildPreReq: python-tools-2to3
%endif

%py_requires pyramid

%description
This module provide a set of utilities for using FormAlchemy with
Pyramid.

%package -n python3-module-%oname
Summary: FormAlchemy plugins and helpers for Pyramid
Group: Development/Python3
%py3_requires pyramid

%description -n python3-module-%oname
This module provide a set of utilities for using FormAlchemy with
Pyramid.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
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
* Thu Jul 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.4-alt2
- Added module for Python 3

* Thu Sep 19 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.4-alt1
- Version 0.4.4

* Tue Apr 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.3-alt1
- Version 0.4.3

* Mon Dec 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.2-alt1
- Version 0.4.2

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4.1-alt1.1
- Rebuild with Python-2.7

* Tue Jul 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt1
- Initial build for Sisyphus

