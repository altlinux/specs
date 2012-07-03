%define oname cryptacular

%def_with python3

Name: python-module-%oname
Version: 1.4.1
Release: alt1
Summary: A password hashing framework with bcrypt and pbkdf2
License: MIT
Group: Development/Python
Url: http://pypi.python.org/pypi/cryptacular/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute
%endif

%description
cryptacular is a collection of strong password hashing functions that
share a common interface, and a nice way to use bcrypt as a password
hash. It's designed to make it easy for you to migrate away from your
half-assed custom password scheme. Compared with popular choices like
plain text or single rounds of md5 or sha, strong password hashes
greatly increase the computational cost of obtaining users' passwords
from a leaked password database.

cryptacular's interface was inspired by zope.password but cryptacular
does not depend on zope and implements much stronger algorithms.
cryptacular also provides a convenient way to recognize and upgrade
obsolete password hashes on the fly when users log in with their correct
password.

%if_with python3
%package -n python3-module-%oname
Summary: A password hashing framework with bcrypt and pbkdf2 (Python 3)
Group: Development/Python3

%description -n python3-module-%oname
cryptacular is a collection of strong password hashing functions that
share a common interface, and a nice way to use bcrypt as a password
hash. It's designed to make it easy for you to migrate away from your
half-assed custom password scheme. Compared with popular choices like
plain text or single rounds of md5 or sha, strong password hashes
greatly increase the computational cost of obtaining users' passwords
from a leaked password database.

cryptacular's interface was inspired by zope.password but cryptacular
does not depend on zope and implements much stronger algorithms.
cryptacular also provides a convenient way to recognize and upgrade
obsolete password hashes on the fly when users log in with their correct
password.

%package -n python3-module-%oname-tests
Summary: Tests for cryptacular (Python 3)
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires pbkdf2

%description -n python3-module-%oname-tests
cryptacular is a collection of strong password hashing functions that
share a common interface, and a nice way to use bcrypt as a password
hash. It's designed to make it easy for you to migrate away from your
half-assed custom password scheme. Compared with popular choices like
plain text or single rounds of md5 or sha, strong password hashes
greatly increase the computational cost of obtaining users' passwords
from a leaked password database.

cryptacular's interface was inspired by zope.password but cryptacular
does not depend on zope and implements much stronger algorithms.
cryptacular also provides a convenient way to recognize and upgrade
obsolete password hashes on the fly when users log in with their correct
password.

This package contains tests for cryptacular.
%endif

%package tests
Summary: Tests for cryptacular
Group: Development/Python
Requires: %name = %version-%release
%py_requires pbkdf2

%description tests
cryptacular is a collection of strong password hashing functions that
share a common interface, and a nice way to use bcrypt as a password
hash. It's designed to make it easy for you to migrate away from your
half-assed custom password scheme. Compared with popular choices like
plain text or single rounds of md5 or sha, strong password hashes
greatly increase the computational cost of obtaining users' passwords
from a leaked password database.

cryptacular's interface was inspired by zope.password but cryptacular
does not depend on zope and implements much stronger algorithms.
cryptacular also provides a convenient way to recognize and upgrade
obsolete password hashes on the fly when users log in with their correct
password.

This package contains tests for cryptacular.

%prep
%setup
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build
%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install
touch %buildroot%python_sitelibdir/%oname/__init__.py

%if_with python3
pushd ../python3
%python3_install
popd
touch %buildroot%python3_sitelibdir/%oname/__init__.py
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*/*/test*
%exclude %python_sitelibdir/*.pth

%files tests
%python_sitelibdir/*/*/test*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/*/__pycache__/test*
%exclude %python3_sitelibdir/*/*/test*
%exclude %python3_sitelibdir/*.pth

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/__pycache__/test*
%python3_sitelibdir/*/*/test*
%endif

%changelog
* Sun May 20 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.1-alt1
- Version 1.4.1
- Added module for Python 3

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.1-alt1.1
- Rebuild to remove redundant libpython2.7 dependency

* Fri Dec 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.1-alt1
- Version 1.2.1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0-alt2.1
- Rebuild with Python-2.7

* Wed Jun 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt2
- Excluded *.pth

* Sat May 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1
- Initial build for Sisyphus

