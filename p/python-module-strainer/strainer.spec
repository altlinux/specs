%define oname strainer

%def_with python3

Name: python-module-%oname
Version: 0.1.4
Release: alt2
Summary: Tools to allow developers to cleanup web objects (HTML, JSON, XHTML)
License: MIT
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/strainer/

Source: %name-%version.tar

BuildRequires: python-devel python-module-setuptools-tests
BuildRequires: python-module-simplejson python-module-nose
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools-tests
BuildRequires: python3-module-simplejson python3-module-nose
BuildRequires: python-tools-2to3
%endif

%py_provides %oname
%py_requires json

%description
Provides middleware for detecting and correcting errors in web pages
that are served via the standard WSGI protocol used by most Python web
frameworks. By default, validation errors are logged to the
"strainer.middleware" channel using the standard Python logging module.

%if_with python3
%package -n python3-module-%oname
Summary: Tools to allow developers to cleanup web objects (HTML, JSON, XHTML)
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Provides middleware for detecting and correcting errors in web pages
that are served via the standard WSGI protocol used by most Python web
frameworks. By default, validation errors are logged to the
"strainer.middleware" channel using the standard Python logging module.
%endif

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
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/*
%endif

%changelog
* Thu Dec 28 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.4-alt2
- Updated build dependencies.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.4-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1.4-alt1.1
- NMU: Use buildreq for BR.

* Fri Feb 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.4-alt1
- Initial build for Sisyphus

