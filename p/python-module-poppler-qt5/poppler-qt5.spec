%define oname poppler-qt5

%def_with python3

Name: python-module-%oname
Version: 0.24.2
Release: alt1.git20170214.1.1
Summary: A Python binding to Poppler-Qt5
License: LGPLv2.1+
Group: Development/Python
Url: https://pypi.python.org/pypi/python-poppler-qt5/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/wbsoft/python-poppler-qt5.git
# tag: v0.24.2
Source: %name-%version.tar

BuildPreReq: gcc-c++ qt5-base-devel libpoppler-qt5-devel
BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-sip-devel python-module-PyQt5-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-sip-devel python3-module-PyQt5-devel
%endif

%description
A Python binding for libpoppler-qt5 that aims for completeness and for
being actively maintained.

%package -n python3-module-%oname
Summary: A Python binding to Poppler-Qt5
Group: Development/Python3

%description -n python3-module-%oname
A Python binding for libpoppler-qt5 that aims for completeness and for
being actively maintained.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
export PATH=$PATH:%_qt5_bindir
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug --debug -j6
popd
%endif

%install
export PATH=$PATH:%_qt5_bindir
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
export PATH=$PATH:%_qt5_bindir
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc ChangeLog TODO *.rst demo.py
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc ChangeLog TODO *.rst demo.py
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.24.2-alt1.git20170214.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sat Oct 14 2017 Fr. Br. George <george@altlinux.ru> 0.24.2-alt1.git20170214.1
- Merge upstream updates

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.24.1-alt1.git20150224.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Fri Feb 27 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.24.1-alt1.git20150224
- Initial build for Sisyphus

