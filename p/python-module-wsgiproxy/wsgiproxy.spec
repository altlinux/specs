%define oname wsgiproxy

%def_with python3

Name: python-module-%oname
Version: 0.2.2
Release: alt2.1
Summary: HTTP proxying tools for WSGI apps
License: MIT
Group: Development/Python
Url: http://pypi.python.org/pypi/WSGIProxy/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%description
WSGIProxy gives tools to proxy arbitrary(ish) WSGI requests to other
processes over HTTP.

This will encode the WSGI request CGI-style environmental variables
(which must be strings), plus a configurable set of other variables. It
also sends values like HTTP_HOST and wsgi.url_scheme which are often
obscured by the proxying process, as well as values like SCRIPT_NAME. On
the receiving end, a WSGI middleware fixes up the environment to
represent the state of the original request. This makes HTTP more like
FastCGI or SCGI, which naturally preserve these values.

%package -n python3-module-%oname
Summary: HTTP proxying tools for WSGI apps
Group: Development/Python3

%description -n python3-module-%oname
WSGIProxy gives tools to proxy arbitrary(ish) WSGI requests to other
processes over HTTP.

This will encode the WSGI request CGI-style environmental variables
(which must be strings), plus a configurable set of other variables. It
also sends values like HTTP_HOST and wsgi.url_scheme which are often
obscured by the proxying process, as well as values like SCRIPT_NAME. On
the receiving end, a WSGI middleware fixes up the environment to
represent the state of the original request. This makes HTTP more like
FastCGI or SCGI, which naturally preserve these values.

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
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.2-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Jul 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.2-alt2
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2.2-alt1.1
- Rebuild with Python-2.7

* Thu Jun 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.2-alt1
- Initial build for Sisyphus

