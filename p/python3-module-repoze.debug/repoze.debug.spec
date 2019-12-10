%define _unpackaged_files_terminate_build 1

%define oname repoze.debug

Name: python3-module-%oname
Version: 1.1
Release: alt3

Summary: WSGI middleware: debugging utilities
License: BSD
Group: Development/Python3
Url: https://github.com/repoze/repoze.debug

# https://github.com/repoze/repoze.debug.git
Source0: https://pypi.python.org/packages/94/41/12c9883799f8045b9f8b77363e0defc547324dbf1a04537f09fd722fd91d/%{oname}-%{version}.tar.gz
Patch0: fix-py3-import.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3 python3-module-sphinx

%py3_requires repoze threadframe paste webob


%description
Middleware which can help with in-production forensic debugging.

%package tests
Summary: Tests for repoze.debug
Group: Development/Python3
Requires: %name = %version-%release

%description tests
Middleware which can help with in-production forensic debugging.

This package contains tests for repoze.debug.

%package pickles
Summary: Pickles for repoze.debug
Group: Development/Python3

%description pickles
Middleware which can help with in-production forensic debugging.

This package contains pickles for repoze.debug.

%package docs
Summary: Documentation for repoze.debug
Group: Development/Documentation
BuildArch: noarch

%description docs
Middleware which can help with in-production forensic debugging.

This package contains documentation for repoze.debug.

%prep
%setup -q -n %{oname}-%{version}
%patch0 -p2

sed -i 's|sphinx-build|sphinx-build-3|' docs/Makefile

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

export PYTHONPATH=%buildroot%python3_sitelibdir
pushd docs
%make pickle
%make html
popd

install -d %buildroot%python3_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python3_sitelibdir/%oname/

%files
%doc *.txt
%_bindir/*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/%oname/pickle
%exclude %python3_sitelibdir/*/*/tests

%files tests
%exclude %python3_sitelibdir/*/*/tests

%files pickles
%python3_sitelibdir/%oname/pickle

%files docs
%doc docs/_build/html/*


%changelog
* Tue Dec 10 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.1-alt3
- build for python2 disabled

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1
- automated PyPI update

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.2-alt2.git20131220.1.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.2-alt2.git20131220.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.0.2-alt2.git20131220.1
- NMU: Use buildreq for BR.

* Tue Jul 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt2.git20131220
- Added module for Python 3

* Tue Jul 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt1.git20131220
- New snapshot

* Mon Sep 23 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt1.git20130702
- Version 1.0.2

* Thu Apr 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8-alt1.git20130130
- Version 0.8

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.7.2-alt1.git20110418.1.1
- Rebuild with Python-2.7

* Thu Jun 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.2-alt1.git20110418.1
- Added necessary requirements
- Excluded *.pth

* Wed Jun 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.2-alt1.git20110418
- Initial build for Sisyphus

