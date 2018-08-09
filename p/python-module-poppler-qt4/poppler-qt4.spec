%define oname poppler-qt4

%def_with python3

Name: python-module-%oname
Version: 0.24.0
Release: alt2.git20150218
Summary: A Python binding to Poppler-Qt4
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/python-poppler-qt4/

# https://github.com/wbsoft/python-poppler-qt4.git
Source: %name-%version.tar

BuildRequires: libpoppler-qt4-devel gcc-c++ libqt4-devel
BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-sip-devel python-module-PyQt4-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-sip-devel python3-module-PyQt4-devel
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

# compatibility with new poppler version
find . -type f | xargs sed -i -e 's:<qt4/poppler:<poppler:g'

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
* Thu Aug 09 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.24.0-alt2.git20150218
- Rebuilt with new poppler.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.24.0-alt1.git20150218.1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.24.0-alt1.git20150218.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.24.0-alt1.git20150218.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Wed Feb 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.24.0-alt1.git20150218
- Initial build for Sisyphus

