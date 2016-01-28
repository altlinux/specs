%define oname strainer

%def_with python3

Name: python-module-%oname
Version: 0.1.4
Release: alt1.1
Summary: Tools to allow developers to cleanup web objects (HTML, JSON, XHTML)
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/strainer/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-modules-json
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
%py_requires json

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-pytest python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-logging python-modules-unittest python-tools-2to3 python3 python3-base python3-module-pytest python3-module-setuptools
BuildRequires: python-module-setuptools-tests python3-module-setuptools-tests rpm-build-python3 time

%description
Provides middleware for detecting and correcting errors in web pages
that are served via the standard WSGI protocol used by most Python web
frameworks. By default, validation errors are logged to the
"strainer.middleware" channel using the standard Python logging module.

%package -n python3-module-%oname
Summary: Tools to allow developers to cleanup web objects (HTML, JSON, XHTML)
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Provides middleware for detecting and correcting errors in web pages
that are served via the standard WSGI protocol used by most Python web
frameworks. By default, validation errors are logged to the
"strainer.middleware" channel using the standard Python logging module.

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

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc PKG-INFO
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc PKG-INFO
%python3_sitelibdir/*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1.4-alt1.1
- NMU: Use buildreq for BR.

* Fri Feb 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.4-alt1
- Initial build for Sisyphus

