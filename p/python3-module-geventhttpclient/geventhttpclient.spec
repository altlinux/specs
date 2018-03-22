%define oname geventhttpclient
Name: python3-module-%oname
Version: 1.1.0
Release: alt1.1.1
Summary: http client library for gevent
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/geventhttpclient/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3

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
%setup
find -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build_debug

%install
%python3_install

%files
%doc PKG-INFO
%python3_sitelibdir/*

%changelog
* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.0-alt1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1.0-alt1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Mon Aug 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1
- Initial build for Sisyphus

