%define oname zope.hookable
%define fname python3-module-%oname
%define descr \
Support the efficient creation of hookable objects, which are callable \
objects that are meant to be replaced by other callables, at least \
optionally. \
\
The idea is you create a function that does some default thing and make \
it hookable. Later, someone can modify what it does by calling its \
sethook method and changing its implementation.  All users of the \
function, including those that imported it, will see the change.

Name: %fname
Version: 5.0.0
Release: alt1

%if ""==""
Summary: Hookable object support
Group: Development/Python3
%else
Summary: Documentation for %oname
Group: Development/Documentation
%endif

License: ZPL-2.1
Url: http://pypi.python.org/pypi/zope.hookable/
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3 rpm-macros-sphinx

%py3_requires zope

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: elfutils python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python3 python3-base
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-objects.inv python3-devel python3-module-setuptools rpm-build-python3 time

%if ""!=""
Conflicts: %fname < %EVR
Conflicts: %fname > %EVR
BuildArch: noarch
%endif

%description
%descr

%if ""!=""
This package contains documentation for %oname.

%package -n %fname-pickles
Summary: Pickles for zope.hookable
Group: Development/Python

%description -n %fname-pickles
%descr

This package contains pickles for zope.hookable.
%else
%package -n %fname-tests
Summary: Tests for zope.hookable
Group: Development/Python
Requires: %name = %version-%release
%py3_requires zope.testing

%description -n %fname-tests
%descr

This package contains tests for zope.hookable.
%endif

%prep
%setup
%if ""!=""
%prepare_sphinx .
ln -s ../objects.inv docs/
%endif

%build
%if ""==""
%python3_build
%else
export PYTHONPATH=$PWD/src
%make -C docs pickle
%make -C docs html
%endif

%install
%if ""==""
%python3_install
%else
install -d %buildroot%python3_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python3_sitelibdir/%oname/
%endif

%if ""==""
%files
%doc *.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/*/tests

%files -n %fname-tests
%python3_sitelibdir/*/*/tests

%else

%files
%doc docs/_build/html/*

%files -n %fname-pickles
%python3_sitelibdir/*/pickle

%endif

%changelog
* Thu Jan 09 2020 Grigory Ustinov <grenka@altlinux.org> 5.0.0-alt1
- Build new version.
- Fix license.

* Mon Oct 29 2018 Grigory Ustinov <grenka@altlinux.org> 4.2.0-alt1
- Build new version.

* Thu May 10 2018 Grigory Ustinov <grenka@altlinux.org> 4.0.4-alt2
- Tranfer package to subst-packaging system.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 4.0.4-alt1.1.1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Fri Mar 18 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.4-alt1.1.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Fri Mar 18 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.4-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 4.0.4-alt1.1
- NMU: Use buildreq for BR.

* Thu Jul 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.4-alt1
- Version 4.0.4
- Added module for Python 3

* Tue Apr 09 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt1
- Version 4.0.1

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 3.4.1-alt2.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.4.1-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.1-alt2
- Added necessary requirements
- Excluded *.pth

* Tue May 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.1-alt1
- Initial build for Sisyphus

