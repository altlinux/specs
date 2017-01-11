%define _unpackaged_files_terminate_build 1
%define oname geventhttpclient
Name: python-module-%oname
Version: 1.3.1
Release: alt1
Summary: http client library for gevent
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/geventhttpclient/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/35/41/33b552d780c1fef6427cbb314a69e8303a59e51b6aac25e07ded46aef6fa/%{oname}-%{version}.tar.gz

BuildPreReq: python-devel python-module-setuptools

Requires: python-module-backports.ssl_match_hostname

%description
A high performance, concurrent HTTP client library for python using
gevent.

geventhttpclient use a fast http parser, written in C, originating from
nginx, extracted and modified by Joyent.

geventhttpclient has been specifically designed for high concurrency,
streaming and support HTTP 1.1 persistent connections. More generally it
is designed for efficiently pulling from REST APIs and streaming API's
like Twitter's.

Safe SSL support is provided by default.

%prep
%setup -q -n %{oname}-%{version}

%build
%python_build_debug

%install
%python_install

%files
%doc PKG-INFO
%python_sitelibdir/*

%changelog
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.3.1-alt1
- automated PyPI update

* Fri Jul 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1
- Initial build for Sisyphus

