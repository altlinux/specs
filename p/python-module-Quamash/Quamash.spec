%define oname Quamash

%def_without python2
%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.5.1
Release: alt1.git20150118.1
Summary: Implementation of the PEP 3156 event-loop (tulip) api using the Qt Event-Loop
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/Quamash/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/harvimt/quamash.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: xvfb-run
%if_with python2
#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-asyncio python-module-pathlib
#BuildPreReq: python-module-PyQt4 xvfb-run
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-asyncio python3-module-pathlib
#BuildPreReq: python3-module-PyQt4
%endif

%py_provides quamash
%py_requires asyncio

# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: fontconfig libqt4-core libqt4-gui python-base python3 python3-base python3-module-setuptools python3-module-sip
BuildRequires: python3-module-PyQt4 python3-module-asyncio python3-module-pathlib python3-module-pytest rpm-build-python3

%description
Implementation of the PEP 3156 Event-Loop with Qt.

Quamash requires Python 3.4 and either PyQt4, PyQt5 or PySide.

%package -n python3-module-%oname
Summary: Implementation of the PEP 3156 event-loop (tulip) api using the Qt Event-Loop
Group: Development/Python3
%py3_provides quamash
%py3_requires asyncio

%description -n python3-module-%oname
Implementation of the PEP 3156 Event-Loop with Qt.

Quamash requires Python 3.4 and either PyQt4, PyQt5 or PySide.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%if_with python2
%python_build_debug
%endif

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%if_with python2
%python_install
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
%if_with python2
xvfb-run py.test -vv
python setup.py test
%endif
%if_with python3
pushd ../python3
python3 setup.py test
xvfb-run py.test-%_python3_version -vv
popd
%endif

%if_with python2
%files
%doc *.rst
%python_sitelibdir/*
%endif

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Wed Jan 27 2016 Mikhail Efremov <sem@altlinux.org> 0.5.1-alt1.git20150118.1
- NMU: Use buildreq for BR.

* Mon Jan 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.1-alt1.git20150118
- Version 0.5.1

* Sun Jan 11 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt1.git20150109
- Initial build for Sisyphus

