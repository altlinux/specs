%define oname zope.hookable
%define descr \
Support the efficient creation of hookable objects, which are callable \
objects that are meant to be replaced by other callables, at least \
optionally. \
\
The idea is you create a function that does some default thing and make \
it hookable. Later, someone can modify what it does by calling its \
sethook method and changing its implementation.  All users of the \
function, including those that imported it, will see the change.

Name: python3-module-%oname
Version: 5.0.1
Release: alt2.1

Summary: Hookable object support
Group: Development/Python3

License: ZPL-2.1
Url: http://pypi.python.org/pypi/zope.hookable/
Source: %name-%version.tar
# mapping from PyPI name
# https://www.altlinux.org/Management_of_Python_dependencies_sources#Mapping_project_names_to_distro_names
Provides: python3-module-%{pep503_name %oname} = %EVR

BuildRequires(pre): rpm-build-python3 rpm-macros-sphinx3
BuildRequires: python3-module-sphinx

%py3_requires zope

%description
%descr

%package docs
Summary: Documentation for %oname
Group: Development/Documentation

%description docs
%descr

This package contains documentation for %oname.

%package pickles
Summary: Pickles for zope.hookable
Group: Development/Python

%description pickles
%descr

This package contains pickles for zope.hookable.

%package tests
Summary: Tests for zope.hookable
Group: Development/Python
Requires: %name = %version-%release
%py3_requires zope.testing

%description tests
%descr

This package contains tests for zope.hookable.

%prep
%setup

%prepare_sphinx3 .
ln -s ../objects.inv docs/

%build
%python3_build

export PYTHONPATH=$PWD/src
%make SPHINXBUILD="sphinx-build-3" -C docs pickle
%make SPHINXBUILD="sphinx-build-3" -C docs html

%install
%python3_install

install -d %buildroot%python3_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python3_sitelibdir/%oname/

%files
%doc *.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/*/tests
%exclude %python3_sitelibdir/*/pickle

%files tests
%python3_sitelibdir/*/*/tests

%files docs
%doc docs/_build/html/*

%files pickles
%python3_sitelibdir/*/pickle

%changelog
* Fri Jul 28 2023 Stanislav Levin <slev@altlinux.org> 5.0.1-alt2.1
- NMU: mapped PyPI name to distro's one.

* Mon May 31 2021 Grigory Ustinov <grenka@altlinux.org> 5.0.1-alt2
- Drop specsubst scheme.

* Tue Apr 28 2020 Stanislav Levin <slev@altlinux.org> 5.0.1-alt1
- 5.0.0 -> 5.0.1.

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

