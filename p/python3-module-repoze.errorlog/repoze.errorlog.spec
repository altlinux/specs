%define _unpackaged_files_terminate_build 1

%define oname repoze.errorlog

Name: python3-module-%oname
Version: 1.1
Release: alt2
Summary: WSGI middleware: intercept / log / browse exceptions
License: BSD
Group: Development/Python3
Url: https://github.com/repoze/repoze.errorlog

# https://github.com/repoze/repoze.errorlog.git
Source0: https://pypi.python.org/packages/f9/a0/cac87efb7ac8098d03760df3ffa6a71333db7d0e4bb26a15a9c1d2706957/%{oname}-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3

%py3_requires repoze meld3 paste


%description
This package implements a WSGI middleware filter which intercepts
exceptions and writes them to a Python logging module channel (or the
``wsgi.errors`` filehandle, if no channel is configured).  It also
allows the browsing of limited exception history via a browser UI.

%package tests
Summary: Tests for repoze.errorlog
Group: Development/Python3
Requires: %name = %version-%release

%description tests
This package implements a WSGI middleware filter which intercepts
exceptions and writes them to a Python logging module channel (or the
``wsgi.errors`` filehandle, if no channel is configured).  It also
allows the browsing of limited exception history via a browser UI.

This package contains tests for repoze.errorlog.

%prep
%setup -q -n %{oname}-%{version}

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build

%install
%python3_install

%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
    %buildroot%python3_sitelibdir/
%endif

%files
%doc *.txt *.rst docs/*.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/tests.*

%files tests
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/*/tests.*


%changelog
* Tue Dec 10 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.1-alt2
- build for python2 disabled

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1
- automated PyPI update

* Tue Jun 07 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.0-alt1.dev0.git20150207.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.0-alt1.dev0.git20150207.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Feb 14 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.dev0.git20150207
- Version 1.0.0.dev0

* Mon Jul 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.2-alt2.git20120329
- Added module for Python 3

* Thu Apr 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.2-alt1.git20120329
- Version 0.9.2

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.1-alt1.git20110322.1.1
- Rebuild with Python-2.7

* Thu Jun 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.1-alt1.git20110322.1
- Added necessary requirements
- Excluded *.pth

* Fri Jun 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.1-alt1.git20110322
- Initial build for Sisyphus

