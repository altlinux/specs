%define _unpackaged_files_terminate_build 1
%define oname httpbin

%def_enable check

Name: python3-module-%oname
Version: 0.7.0
Release: alt3
Summary: HTTP Request and Response Service
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/httpbin/
# https://github.com/postmanlabs/httpbin
BuildArch: noarch

Source: %oname-%version.tar

BuildRequires(pre): rpm-build-python3

%if_enabled check
BuildRequires: python3-module-flask
BuildRequires: python3-module-six
BuildRequires: python3-module-werkzeug
BuildRequires: python3-module-raven
BuildRequires: python3-module-brotlipy
%endif


%py3_provides %oname

%description
Testing an HTTP Library can become difficult sometimes. PostBin.org is
fantastic for testing POST requests, but not much else. This exists to
cover all kinds of HTTP scenarios. Additional endpoints are being
considered.

All endpoint responses are JSON-encoded.

%prep
%setup -n %oname-%version

%build
%python3_build_debug

%install
%python3_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir/
python3 test_httpbin.py

%files
%doc AUTHORS *.md LICENSE
%python3_sitelibdir/*

%changelog
* Mon Sep 26 2022 Danil Shein <dshein@altlinux.org> 0.7.0-alt3
- NMU: Fix Werkzeug 2.1.x compatibility
  + enable tests

* Wed Sep 16 2020 Grigory Ustinov <grenka@altlinux.org> 0.7.0-alt2
- Fixed FTBFS.
- Fixed packaging.

* Tue Oct 01 2019 Anton Farygin <rider@altlinux.ru> 0.7.0-alt1
- 0.7.0
- built without python-2.7 support

* Fri Mar 30 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.6.2-alt1.1
- Fixed requires

* Wed Mar 28 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.6.2-alt1
- Updated version to 0.6.2

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.0-alt1.git20140826.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.2.0-alt1.git20140826.1
- NMU: Use buildreq for BR.

* Mon Nov 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1.git20140826
- Initial build for Sisyphus
