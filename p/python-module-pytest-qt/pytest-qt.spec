%define oname pytest-qt

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 1.2.2
Release: alt1.git20141105.1.1.1
Summary: pytest plugin for Qt (PyQt and PySide) application testing
License: LGPLv3
Group: Development/Python
Url: https://pypi.python.org/pypi/pytest-qt/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/nicoddemus/pytest-qt.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-PyQt4 python-module-PySide
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
#BuildPreReq: python3-module-PyQt4 python3-module-PySide
%endif

%py_provides pytestqt
%py_requires PyQt4 PySide

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-pytest python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base python3-module-pytest python3-module-setuptools
BuildRequires: python-module-setuptools python3-module-setuptools rpm-build-python3

%description
pytest-qt is a pytest plugin that allows programmers to write tests for
PySide and PyQt applications.

%package -n python3-module-%oname
Summary: pytest plugin for Qt (PyQt and PySide) application testing
Group: Development/Python3
%py3_provides pytestqt
%py3_requires PyQt4 PySide

%description -n python3-module-%oname
pytest-qt is a pytest plugin that allows programmers to write tests for
PySide and PyQt applications.

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
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst docs/*.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst docs/*.rst
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.2.2-alt1.git20141105.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.2.2-alt1.git20141105.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.2.2-alt1.git20141105.1
- NMU: Use buildreq for BR.

* Thu Nov 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.2-alt1.git20141105
- Initial build for Sisyphus

