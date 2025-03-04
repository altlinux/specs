%define oname geventhttpclient

%def_with check

Name: python3-module-%oname
Version: 2.3.3
Release: alt1

Summary: http client library for gevent
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/geventhttpclient

Source: %name-%version.tar
# Upstream didn't packaged them into source tarball on pypi
# So it can be nessesary to update them from github
# https://github.com/geventhttpclient/geventhttpclient
# While building from github repo is hard because of submodule
Source1: tests.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-gevent
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
tar -xvf %SOURCE1 tests

%build
%pyproject_build

%install
%pyproject_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
%pyproject_run_pytest -m 'not network'

%files
%doc PKG-INFO
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Tue Mar 04 2025 Grigory Ustinov <grenka@altlinux.org> 2.3.3-alt1
- Build new version.
- Build with check.

* Sat May 18 2024 Grigory Ustinov <grenka@altlinux.org> 2.3.1-alt1
- Build new version.

* Fri Apr 28 2023 Grigory Ustinov <grenka@altlinux.org> 2.0.9-alt1
- Build new version.
- Build without check for python3.11.

* Wed Mar 01 2023 Anton Vyatkin <toni@altlinux.org> 2.0.8-alt1
- new version 2.0.8

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.0-alt1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1.0-alt1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Mon Aug 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1
- Initial build for Sisyphus

