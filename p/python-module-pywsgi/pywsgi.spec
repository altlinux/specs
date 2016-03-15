%define oname pywsgi

%def_with python3

Name: python-module-%oname
Version: 0.9.0
Release: alt2.1
Summary: A high-level class-based API around WSGI, CGI, and mod_python
License: GPLv2
Group: Development/Python
Url: http://pypi.python.org/pypi/pywsgi/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname

%description
pywsgi provides the following features:

 - An abstraction from low-level gateway interface handlers like WSGI,
   CGI, and mod_python.
 - A consistent high-level, class-based interface.
 - Session handling.
 - Cookie handling.
 - GET/POST data handling.
 - Error handling.
 - A pywsgi.util namespace with useful tools.

%package -n python3-module-%oname
Summary: A high-level class-based API around WSGI, CGI, and mod_python
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
pywsgi provides the following features:

 - An abstraction from low-level gateway interface handlers like WSGI,
   CGI, and mod_python.
 - A consistent high-level, class-based interface.
 - Session handling.
 - Cookie handling.
 - GET/POST data handling.
 - Error handling.
 - A pywsgi.util namespace with useful tools.

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
%doc README
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc README
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.0-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Aug 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.0-alt2
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.0-alt1.1
- Rebuild with Python-2.7

* Wed Jul 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.0-alt1
- Initial build for Sisyphus

