%define oname WSGIProxy2

%def_without test

Name:    python3-module-wsgiproxy2
Version: 0.4.6
Release: alt2

Summary: WSGI Proxy that supports several HTTP backends

License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/WSGIProxy2/

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/gawel/WSGIProxy2.git
Source: %name-%version.tar

BuildArch:      noarch

BuildRequires(pre): rpm-build-intro >= 2.2.5
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-webob python3-module-six
BuildRequires: python3-module-http-parser
BuildRequires: python3-module-urllib3 python3-module-requests
BuildRequires: python3-module-nose

# optional (and stalled)
#BuildRequires: python3-module-restkit
%add_python3_req_skip restkit

%if_with test
BuildRequires: python3-module-webtest
BuildRequires: python3-module-coverage
%endif

Provides: python3-module-%oname

%py3_provides wsgiproxy
Conflicts: python3-module-wsgiproxy


%description
A WSGI Proxy with various http client backends.

%if_with test
%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
A WSGI Proxy with various http client backends.

This package contains tests for %oname.
%endif

%prep
%setup

%build
%python3_build

%install
%python3_install
%python3_prune

%check
nosetests3 -vv

%files
%doc README_fixt.py README.rst
%python3_sitelibdir/*
%if 0
%exclude %python3_sitelibdir/*/test_*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test_*
%endif

%changelog
* Mon Nov 23 2020 Vitaly Lipatov <lav@altlinux.ru> 0.4.6-alt2
- build python3 package only

* Thu Jun 04 2020 Pavel Vasenkov <pav@altlinux.org> 0.4.6-alt1
- Version 0.4.6

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.4.3-alt1.dev0.git20141227.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.3-alt1.dev0.git20141227.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jan 27 2016 Mikhail Efremov <sem@altlinux.org> 0.4.3-alt1.dev0.git20141227.1
- NMU: Use buildreq for BR.

* Sat Aug 29 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.3-alt1.dev0.git20141227
- Version 0.4.3.dev0

* Fri Oct 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.2-alt1.dev0.git20131221
- Initial build for Sisyphus
