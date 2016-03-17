%define oname zc.copy

%def_with python3

Name: python-module-%oname
Version: 1.2
Release: alt3.1
Summary: Pluggable object copying (deprecated in favor of zope.copy)
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zc.copy/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires zope.copy zope.copypastemove zope.location

%description
This package used to provide a pluggable replacement of ObjectCopier
class and locationCopy function from zope.copypastemove and
zope.location respectively. Currently, all its functionality is merged
to those packages and the new zope.copy package is provided that
contains the actual pluggable copying mechanism used to be in this
package with no dependencies except zope.interface.

This package now only provides backward-compatibility imports and should
not be used for new developments.

%package -n python3-module-%oname
Summary: Pluggable object copying (deprecated in favor of zope.copy)
Group: Development/Python3
%py3_requires zope.copy zope.copypastemove zope.location

%description -n python3-module-%oname
This package used to provide a pluggable replacement of ObjectCopier
class and locationCopy function from zope.copypastemove and
zope.location respectively. Currently, all its functionality is merged
to those packages and the new zope.copy package is provided that
contains the actual pluggable copying mechanism used to be in this
package with no dependencies except zope.interface.

This package now only provides backward-compatibility imports and should
not be used for new developments.

%package -n python3-module-%oname-tests
Summary: Tests for zc.copy
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
This package used to provide a pluggable replacement of ObjectCopier
class and locationCopy function from zope.copypastemove and
zope.location respectively. Currently, all its functionality is merged
to those packages and the new zope.copy package is provided that
contains the actual pluggable copying mechanism used to be in this
package with no dependencies except zope.interface.

This package now only provides backward-compatibility imports and should
not be used for new developments.

This package contains tests for zc.copy.

%package tests
Summary: Tests for zc.copy
Group: Development/Python
Requires: %name = %version-%release

%description tests
This package used to provide a pluggable replacement of ObjectCopier
class and locationCopy function from zope.copypastemove and
zope.location respectively. Currently, all its functionality is merged
to those packages and the new zope.copy package is provided that
contains the actual pluggable copying mechanism used to be in this
package with no dependencies except zope.interface.

This package now only provides backward-compatibility imports and should
not be used for new developments.

This package contains tests for zc.copy.

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
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/*/tests.*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.2-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jul 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt2
- Added necessary requirements
- Excluded *.pth

* Mon May 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1
- Initial build for Sisyphus

