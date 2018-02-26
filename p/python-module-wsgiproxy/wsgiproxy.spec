%define oname wsgiproxy
Name: python-module-%oname
Version: 0.2.2
Release: alt1.1
Summary: HTTP proxying tools for WSGI apps
License: MIT
Group: Development/Python
Url: http://pypi.python.org/pypi/WSGIProxy/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-distribute

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

%prep
%setup

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2.2-alt1.1
- Rebuild with Python-2.7

* Thu Jun 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.2-alt1
- Initial build for Sisyphus

