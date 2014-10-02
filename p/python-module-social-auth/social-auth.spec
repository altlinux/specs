%define oname social-auth

%def_with python3

Name: python-module-%oname
Version: 0.2.2
Release: alt2.git20140930
Summary: Python social authentication made simple
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/python-social-auth/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/omab/python-social-auth.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_provides social

%description
Python Social Auth is an easy-to-setup social
authentication/registration mechanism with support for several
frameworks and auth providers.

Crafted using base code from django-social-auth, it implements a common
interface to define new authentication providers from third parties, and
to bring support for more frameworks and ORMs.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Python Social Auth is an easy-to-setup social
authentication/registration mechanism with support for several
frameworks and auth providers.

Crafted using base code from django-social-auth, it implements a common
interface to define new authentication providers from third parties, and
to bring support for more frameworks and ORMs.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Python social authentication made simple
Group: Development/Python3
%add_python3_req_skip web
%py3_provides social

%description -n python3-module-%oname
Python Social Auth is an easy-to-setup social
authentication/registration mechanism with support for several
frameworks and auth providers.

Crafted using base code from django-social-auth, it implements a common
interface to define new authentication providers from third parties, and
to bring support for more frameworks and ORMs.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR
%add_python3_req_skip sure

%description -n python3-module-%oname-tests
Python Social Auth is an easy-to-setup social
authentication/registration mechanism with support for several
frameworks and auth providers.

Crafted using base code from django-social-auth, it implements a common
interface to define new authentication providers from third parties, and
to bring support for more frameworks and ORMs.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Python Social Auth is an easy-to-setup social
authentication/registration mechanism with support for several
frameworks and auth providers.

Crafted using base code from django-social-auth, it implements a common
interface to define new authentication providers from third parties, and
to bring support for more frameworks and ORMs.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Python Social Auth is an easy-to-setup social
authentication/registration mechanism with support for several
frameworks and auth providers.

Crafted using base code from django-social-auth, it implements a common
interface to define new authentication providers from third parties, and
to bring support for more frameworks and ORMs.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

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

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C docs pickle
%make -C docs html

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%files
%doc Changelog *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/*/tests
%exclude %python_sitelibdir/*/*/*/tests.*
%exclude %python_sitelibdir/*/*/*/*/tests.*

%files tests
%python_sitelibdir/*/tests
%python_sitelibdir/*/*/*/tests.*
%python_sitelibdir/*/*/*/*/tests.*

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html examples

%if_with python3
%files -n python3-module-%oname
%doc Changelog *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests
%exclude %python3_sitelibdir/*/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%python3_sitelibdir/*/*/*/tests.*
%python3_sitelibdir/*/*/*/*/tests.*
%python3_sitelibdir/*/*/*/*/*/tests.*
%endif

%changelog
* Thu Oct 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.2-alt2.git20140930
- Fixed requirement
- Added necessary provides

* Thu Oct 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.2-alt1.git20140930
- Initial build for Sisyphus

