%define oname geventhttpclient

%def_with check

Name: python3-module-%oname
Version: 2.0.8
Release: alt1

Summary: http client library for gevent
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/geventhttpclient/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-gevent
BuildRequires: python3-module-six
BuildRequires: python3-module-brotlipy
BuildRequires: python3-module-dpkt
BuildRequires: python3-module-urllib3
BuildRequires: python3-module-certifi
%endif

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

%build
%python3_build_debug

%install
%python3_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
py.test-3 -m 'not online' -k 'not test_brotli_response'

%files
%doc PKG-INFO
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-*.egg-info

%changelog
* Wed Mar 01 2023 Anton Vyatkin <toni@altlinux.org> 2.0.8-alt1
- new version 2.0.8

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.0-alt1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1.0-alt1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Mon Aug 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1
- Initial build for Sisyphus

