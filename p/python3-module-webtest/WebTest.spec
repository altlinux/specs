%define _unpackaged_files_terminate_build 1
%define oname webtest

%def_with check

Name: python3-module-%oname
Version: 3.0.1
Release: alt1
Summary: Helper to test WSGI applications
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/WebTest/
Vcs: https://github.com/Pylons/webtest.git

Source: %name-%version.tar
Patch0: %name-%version-alt.patch
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3(bs4)
BuildRequires: python3(mock)
BuildRequires: python3(PasteDeploy)
BuildRequires: python3(pytest)
BuildRequires: python3(waitress)
BuildRequires: python3(webob)
BuildRequires: python3(wsgiproxy)
BuildRequires: python3(pyquery)
%endif

%description
This wraps any WSGI application and makes it easy to send test
requests to that application, without starting up an HTTP server.

This provides convenient full-stack testing of applications written
with any WSGI-compatible framework.

This is based on ``paste.fixture.TestApp``.

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -v

%files
%python3_sitelibdir/webtest/
%python3_sitelibdir/WebTest-%version.dist-info

%changelog
* Fri Aug 30 2024 Anton Vyatkin <toni@altlinux.org> 3.0.1-alt1
- New version 3.0.1.

* Fri Jan 26 2024 Anton Vyatkin <toni@altlinux.org> 3.0.0-alt1
- New version 3.0.0.

* Wed Apr 14 2021 Stanislav Levin <slev@altlinux.org> 2.0.35-alt1
- 2.0.19 -> 2.0.35.

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 2.0.19-alt1.dev0.git20150724.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0.19-alt1.dev0.git20150724.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.0.19-alt1.dev0.git20150724.1
- NMU: Use buildreq for BR.

* Sat Aug 29 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.19-alt1.dev0.git20150724
- New snapshot

* Tue Mar 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.19-alt1.dev0.git20150208
- Version 2.0.19.dev0

* Wed Jul 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.16-alt1.dev0.git20140629
- Version 2.0.16.dev0

* Mon Dec 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.11-alt1.dev0.git20131122
- Version 2.0.11.dev0

* Sun Mar 03 2013 Aleksey Avdeev <solo@altlinux.ru> 2.0-alt1
- Version 2.0

* Tue May 08 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.4-alt1.hg20120506
- Version 1.3.4
- Added module for Python 3

* Mon Dec 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.3-alt1.hg20111208
- Version 1.3.3

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.3-alt2.hg20110422.1
- Rebuild with Python-2.7

* Tue May 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.3-alt2.hg20110422
- New snapshot

* Fri Nov 19 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.3-alt2.hg20101112
- Version 1.2.3

* Wed Jul 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.1-alt2.hg20100723
- New snapshot (svn -> hg)

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.1-alt1.svn20090922.1
- Rebuilt with python 2.6

* Tue Sep 29 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.1-alt1.svn20090922
- Initial build for Sisyphus
