%define oname poppler-qt4

%def_with python3

Name: python-module-%oname
Version: 0.24.0
Release: alt1.git20150218.1.1
Summary: A Python binding to Poppler-Qt4
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/python-poppler-qt4/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/wbsoft/python-poppler-qt4.git
Source: %name-%version.tar

BuildPreReq: libpoppler-qt4-devel gcc-c++ libqt4-devel
BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-sip-devel python-module-PyQt4-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-sip-devel python3-module-PyQt4-devel
%endif

%description
A Python binding for libpoppler-qt4 that aims for completeness and for
being actively maintained.

%package -n python3-module-%oname
Summary: A Python binding to Poppler-Qt4
Group: Development/Python3

%description -n python3-module-%oname
A Python binding for libpoppler-qt4 that aims for completeness and for
being actively maintained.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug build_ext

%if_with python3
pushd ../python3
%python3_build_debug build_ext
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
%doc ChangeLog TODO *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc ChangeLog TODO *.rst
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.24.0-alt1.git20150218.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.24.0-alt1.git20150218.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Wed Feb 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.24.0-alt1.git20150218
- Initial build for Sisyphus

