%define oname zc.displayname

%def_with python3

Name: python-module-%oname
Version: 1.1
Release: alt3.1
Summary: A Zope 3 extension for pluggable display names
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zc.displayname/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires zope.app.container zope.app.pagetemplate zope.component
%py_requires zope.dublincore zope.i18n zope.i18nmessageid zope.interface
%py_requires zope.location zope.proxy zope.publisher zope.security
%py_requires zope.testing zope.traversing

%description
The default display name generator simply takes a Dublin Core title or a
__name__ and returns it, truncated if desired. It uses a helper function
intended to make writing other display name generators easier,
convertName.

No help is offered yet for using HTML with the
IBrowserDisplayNameGenerator interface.

Given an ILocation that can be adapted to
zope.dublincore.interfaces.IDCDescriptiveProperties, and that actually
has a value for it, it returns the DC title; otherwise, it uses
__name__.

%package -n python3-module-%oname
Summary: A Zope 3 extension for pluggable display names
Group: Development/Python3
%py3_requires zope.app.container zope.app.pagetemplate zope.component
%py3_requires zope.dublincore zope.i18n zope.i18nmessageid zope.interface
%py3_requires zope.location zope.proxy zope.publisher zope.security
%py3_requires zope.testing zope.traversing

%description -n python3-module-%oname
The default display name generator simply takes a Dublin Core title or a
__name__ and returns it, truncated if desired. It uses a helper function
intended to make writing other display name generators easier,
convertName.

No help is offered yet for using HTML with the
IBrowserDisplayNameGenerator interface.

Given an ILocation that can be adapted to
zope.dublincore.interfaces.IDCDescriptiveProperties, and that actually
has a value for it, it returns the DC title; otherwise, it uses
__name__.

%package -n python3-module-%oname-tests
Summary: Tests for zc.displayname
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
The default display name generator simply takes a Dublin Core title or a
__name__ and returns it, truncated if desired. It uses a helper function
intended to make writing other display name generators easier,
convertName.

No help is offered yet for using HTML with the
IBrowserDisplayNameGenerator interface.

Given an ILocation that can be adapted to
zope.dublincore.interfaces.IDCDescriptiveProperties, and that actually
has a value for it, it returns the DC title; otherwise, it uses
__name__.

This package contains tests for zc.displayname.

%package tests
Summary: Tests for zc.displayname
Group: Development/Python
Requires: %name = %version-%release

%description tests
The default display name generator simply takes a Dublin Core title or a
__name__ and returns it, truncated if desired. It uses a helper function
intended to make writing other display name generators easier,
convertName.

No help is offered yet for using HTML with the
IBrowserDisplayNameGenerator interface.

Given an ILocation that can be adapted to
zope.dublincore.interfaces.IDCDescriptiveProperties, and that actually
has a value for it, it returns the DC title; otherwise, it uses
__name__.

This package contains tests for zc.displayname.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jul 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt2
- Added necessary requirements
- Excluded *.pth

* Mon May 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1
- Initial build for Sisyphus

