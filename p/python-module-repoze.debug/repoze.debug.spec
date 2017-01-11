%define _unpackaged_files_terminate_build 1
# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt1
%define oname repoze.debug

%def_with python3

Name: python-module-%oname
Version: 1.1
#Release: alt2.git20131220.1.1
Summary: WSGI middleware: debugging utilities
License: BSD
Group: Development/Python
Url: https://github.com/repoze/repoze.debug
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/repoze/repoze.debug.git
Source0: https://pypi.python.org/packages/94/41/12c9883799f8045b9f8b77363e0defc547324dbf1a04537f09fd722fd91d/%{oname}-%{version}.tar.gz

#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
#BuildPreReq: python-tools-2to3
%endif

%py_requires repoze threadframe paste webob

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-tools-2to3 python3 python3-base
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-objects.inv python3-module-setuptools rpm-build-python3 time

%description
Middleware which can help with in-production forensic debugging.

%package -n python3-module-%oname
Summary: WSGI middleware: debugging utilities
Group: Development/Python3
%py3_requires repoze threadframe paste webob

%description -n python3-module-%oname
Middleware which can help with in-production forensic debugging.

%package -n python3-module-%oname-tests
Summary: Tests for repoze.debug
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
Middleware which can help with in-production forensic debugging.

This package contains tests for repoze.debug.

%package tests
Summary: Tests for repoze.debug
Group: Development/Python
Requires: %name = %version-%release

%description tests
Middleware which can help with in-production forensic debugging.

This package contains tests for repoze.debug.

%package pickles
Summary: Pickles for repoze.debug
Group: Development/Python

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

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install
%if "%python_sitelibdir_noarch" != "%python_sitelibdir"
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

export PYTHONPATH=%buildroot%python_sitelibdir
pushd docs
%make pickle
%make html
popd

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%files
%doc *.txt
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/%oname/pickle
%exclude %python_sitelibdir/*/*/tests

%files tests
%exclude %python_sitelibdir/*/*/tests

%files pickles
%python_sitelibdir/%oname/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests
%endif

%changelog
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

