%define oname WSGIProxy2

%def_with check

Name:    python3-module-wsgiproxy2
Version: 0.5.1
Release: alt1

Summary: WSGI Proxy that supports several HTTP backends

License: MIT
Group: Development/Python3
Url: https://pypi.org/project/WSGIProxy2/
Vcs: https://github.com/gawel/WSGIProxy2.git

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-build-intro >= 2.2.5
%if_with check
BuildRequires: python3-module-webob
BuildRequires: python3-module-webtest
BuildRequires: python3-module-urllib3
BuildRequires: python3-module-requests
%endif

Provides: python3-module-%oname

%py3_provides wsgiproxy
Conflicts: python3-module-wsgiproxy

%description
A WSGI Proxy with various http client backends.

%prep
%setup

%build
%python3_build

%install
%python3_install
%python3_prune

%check
%tox_check

%files
%doc *.rst COPYING
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test_*


%changelog
* Fri Apr 14 2023 Anton Vyatkin <toni@altlinux.org> 0.5.1-alt1
- New version 0.5.1.

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
