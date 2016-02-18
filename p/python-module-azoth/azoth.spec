%define oname azoth

%def_with python3

Name: python-module-%oname
Version: 0.3.0
Release: alt2.git20141205.1
Summary: Sqlalchemy utilities
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/azoth/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/TakesxiSximada/azoth.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-six python-module-transaction
#BuildPreReq: python-module-SQLAlchemy
#BuildPreReq: python-module-nose python-module-mock
#BuildPreReq: python-module-coverage python-module-testfixtures
#BuildPreReq: python-module-virtualenv python-modules-json
#BuildPreReq: python-modules-json python-module-tox
#BuildPreReq: python-module-flake8 python-modules-sqlite3
#BuildPreReq: python-module-zope.interface
#BuildPreReq: python-module-zope.sqlalchemy
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-six python3-module-transaction
#BuildPreReq: python3-module-SQLAlchemy python3-module-tox
#BuildPreReq: python3-module-nose python3-module-mock
#BuildPreReq: python3-module-coverage python3-module-testfixtures
#BuildPreReq: python3-modules-sqlite3 python3-module-flake8
#BuildPreReq: python3-module-zope.interface
#BuildPreReq: python3-module-zope.sqlalchemy
#BuildPreReq: python3-module-virtualenv
#BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
%py_requires zope.interface zope.sqlalchemy

# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: pyflakes python-base python-devel python-module-BTrees python-module-SQLAlchemy python-module-ZODB python-module-mccabe python-module-persistent python-module-pluggy python-module-py python-module-pytest python-module-setuptools python-module-six python-module-transaction python-module-zc.buildout python-module-zc.lockfile python-module-zc.zlibstorage python-module-zdaemon python-module-zope python-module-zope.event python-module-zope.interface python-module-zope.proxy python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-unittest python-tools-2to3 python-tools-pep8 python3 python3-base python3-module-BTrees python3-module-SQLAlchemy python3-module-ZODB python3-module-cffi python3-module-cryptography python3-module-cssselect python3-module-enum34 python3-module-genshi python3-module-mccabe python3-module-ntlm python3-module-persistent python3-module-pip python3-module-pluggy python3-module-py python3-module-pycparser python3-module-pytest python3-module-setuptools python3-module-six python3-module-transaction python3-module-virtualenv python3-module-zc.buildout python3-module-zc.lockfile python3-module-zc.zlibstorage python3-module-zdaemon python3-module-zope python3-module-zope.event python3-module-zope.interface python3-module-zope.proxy python3-pyflakes python3-tools-pep8 xz
BuildRequires: python-module-coverage python-module-flake8 python-module-nose python-module-pbr python-module-setuptools-tests python-module-tox python-module-unittest2 python-module-virtualenv python-module-zc.recipe.egg python-module-zope.sqlalchemy python-modules-sqlite3 python3-module-coverage python3-module-flake8 python3-module-html5lib python3-module-nose python3-module-pbr python3-module-setuptools-tests python3-module-tox python3-module-unittest2 python3-module-zc.recipe.egg python3-module-zope.component python3-module-zope.sqlalchemy python3-modules-sqlite3 rpm-build-python3 time

%description
azoth is sqlalchemy helper library.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
azoth is sqlalchemy helper library.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Sqlalchemy utilities
Group: Development/Python3
%py3_provides %oname
%py3_requires zope.interface zope.sqlalchemy

%description -n python3-module-%oname
azoth is sqlalchemy helper library.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
azoth is sqlalchemy helper library.

This package contains tests for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

sed -i 's|\(nonlocal \)||' azoth/decorators.py

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
rm -fR build
py.test
%if_with python3
pushd ../python3
rm -fR build
py.test-%_python3_version
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/tests
%exclude %python_sitelibdir/*/testutils.*

%files tests
%python_sitelibdir/*/testutils.*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/tests
%exclude %python3_sitelibdir/*/testutils.*
%exclude %python3_sitelibdir/*/*/testutils.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/testutils.*
%python3_sitelibdir/*/*/testutils.*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.3.0-alt2.git20141205.1
- NMU: Use buildreq for BR.

* Thu Jan 01 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt2.git20141205
- Excluded tests

* Wed Dec 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt1.git20141205
- Initial build for Sisyphus

