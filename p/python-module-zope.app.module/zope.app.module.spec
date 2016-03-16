%define oname zope.app.module

%def_with python3

Name: python-module-%oname
Version: 3.5.0
Release: alt3.1
Summary: Zope 3 persistent code/module support
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.app.module/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires zope.app zope.interface zope.component zope.container
%py_requires zope.schema zope.filerepresentation ZODB3 zodbcode

%description
Persistent Python modules allow us to develop and store Python modules
in the ZODB in contrast to storing them on the filesystem. You might
want to look at the zodbcode package for the details of the
implementation. In Zope 3 we implemented persistent modules as
utilities. These utilities are known as module managers that manage the
source code, compiled module and name of the module. We then provide a
special module registry that looks up the utilities to find modules.

%package -n python3-module-%oname
Summary: Zope 3 persistent code/module support
Group: Development/Python3
%py3_requires zope.app zope.interface zope.component zope.container
%py3_requires zope.schema zope.filerepresentation ZODB3 zodbcode

%description -n python3-module-%oname
Persistent Python modules allow us to develop and store Python modules
in the ZODB in contrast to storing them on the filesystem. You might
want to look at the zodbcode package for the details of the
implementation. In Zope 3 we implemented persistent modules as
utilities. These utilities are known as module managers that manage the
source code, compiled module and name of the module. We then provide a
special module registry that looks up the utilities to find modules.

%package -n python3-module-%oname-tests
Summary: Tests for zope.app.module
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.app.testing

%description -n python3-module-%oname-tests
Persistent Python modules allow us to develop and store Python modules
in the ZODB in contrast to storing them on the filesystem. You might
want to look at the zodbcode package for the details of the
implementation. In Zope 3 we implemented persistent modules as
utilities. These utilities are known as module managers that manage the
source code, compiled module and name of the module. We then provide a
special module registry that looks up the utilities to find modules.

This package contains tests for zope.app.module.

%package tests
Summary: Tests for zope.app.module
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.testing

%description tests
Persistent Python modules allow us to develop and store Python modules
in the ZODB in contrast to storing them on the filesystem. You might
want to look at the zodbcode package for the details of the
implementation. In Zope 3 we implemented persistent modules as
utilities. These utilities are known as module managers that manage the
source code, compiled module and name of the module. We then provide a
special module registry that looks up the utilities to find modules.

This package contains tests for zope.app.module.

%prep
%setup

%if_with python3
cp -fR . ../python3
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
%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%ifarch x86_64
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/*/tests.*

%files tests
%python_sitelibdir/*/*/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/*/tests.*
%python3_sitelibdir/*/*/*/*/tests.*
%endif

%changelog
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.5.0-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Jul 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.0-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5.0-alt2.1
- Rebuild with Python-2.7

* Mon Jun 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.0-alt2
- Added necessary requirements
- Excluded *.pth

* Tue May 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.0-alt1
- Initial build for Sisyphus

