%define oname z3c.hashedresource

%def_with python3

Name: python-module-%oname
Version: 1.1.3
Release: alt2.1
Summary: Provides URLs for resources that change whenever their content changes
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.hashedresource/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires z3c.noop zope.app.publisher zope.component zope.interface
%py_requires zope.publisher

%description
While we want browsers to cache static resources such as CSS-stylesheets
and JavaScript files, we also want them not to use the cached version if
the files on the server have been updated. (And we don't want to make
end-users have to empty their browser cache to get the latest version.
Nor explain how to do that over the phone every time.)

To make browsers update their caches of resources immediately when the
resource changes, the absolute URLs of resources can now be made to
contain a hash of the resource's contents, so it will look like
/++noop++12345/@@/myresource instead of /@@/myresource.

In developer mode the hash is recomputed each time the resource is asked
for its URL, while in production mode the hash is computed only once, so
remember to restart the server after changing resource files (else
browsers will still see the old URL unchanged and use their outdated
cached versions of the files).

To use this package, include its configure.zcml and use
z3c.hashedresource.interfaces.IHashedResourceSkin or a skin that
inherits from it.

%package -n python3-module-%oname
Summary: Provides URLs for resources that change whenever their content changes
Group: Development/Python3
%py3_requires z3c.noop zope.app.publisher zope.component zope.interface
%py3_requires zope.publisher

%description -n python3-module-%oname
While we want browsers to cache static resources such as CSS-stylesheets
and JavaScript files, we also want them not to use the cached version if
the files on the server have been updated. (And we don't want to make
end-users have to empty their browser cache to get the latest version.
Nor explain how to do that over the phone every time.)

To make browsers update their caches of resources immediately when the
resource changes, the absolute URLs of resources can now be made to
contain a hash of the resource's contents, so it will look like
/++noop++12345/@@/myresource instead of /@@/myresource.

In developer mode the hash is recomputed each time the resource is asked
for its URL, while in production mode the hash is computed only once, so
remember to restart the server after changing resource files (else
browsers will still see the old URL unchanged and use their outdated
cached versions of the files).

To use this package, include its configure.zcml and use
z3c.hashedresource.interfaces.IHashedResourceSkin or a skin that
inherits from it.

%package -n python3-module-%oname-tests
Summary: Tests for z3c.hashedresource
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.app.testing zope.app.zcmlfiles zope.security
%py3_requires zope.site zope.testbrowser

%description -n python3-module-%oname-tests
While we want browsers to cache static resources such as CSS-stylesheets
and JavaScript files, we also want them not to use the cached version if
the files on the server have been updated. (And we don't want to make
end-users have to empty their browser cache to get the latest version.
Nor explain how to do that over the phone every time.)

To make browsers update their caches of resources immediately when the
resource changes, the absolute URLs of resources can now be made to
contain a hash of the resource's contents, so it will look like
/++noop++12345/@@/myresource instead of /@@/myresource.

In developer mode the hash is recomputed each time the resource is asked
for its URL, while in production mode the hash is computed only once, so
remember to restart the server after changing resource files (else
browsers will still see the old URL unchanged and use their outdated
cached versions of the files).

To use this package, include its configure.zcml and use
z3c.hashedresource.interfaces.IHashedResourceSkin or a skin that
inherits from it.

This package contains tests for z3c.hashedresource.

%package tests
Summary: Tests for z3c.hashedresource
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.testing zope.app.zcmlfiles zope.security
%py_requires zope.site zope.testbrowser

%description tests
While we want browsers to cache static resources such as CSS-stylesheets
and JavaScript files, we also want them not to use the cached version if
the files on the server have been updated. (And we don't want to make
end-users have to empty their browser cache to get the latest version.
Nor explain how to do that over the phone every time.)

To make browsers update their caches of resources immediately when the
resource changes, the absolute URLs of resources can now be made to
contain a hash of the resource's contents, so it will look like
/++noop++12345/@@/myresource instead of /@@/myresource.

In developer mode the hash is recomputed each time the resource is asked
for its URL, while in production mode the hash is computed only once, so
remember to restart the server after changing resource files (else
browsers will still see the old URL unchanged and use their outdated
cached versions of the files).

To use this package, include its configure.zcml and use
z3c.hashedresource.interfaces.IHashedResourceSkin or a skin that
inherits from it.

This package contains tests for z3c.hashedresource.

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
%exclude %python_sitelibdir/*/*/test*

%files tests
%python_sitelibdir/*/*/test*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/test*
%exclude %python3_sitelibdir/*/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/test*
%python3_sitelibdir/*/*/*/test*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1.3-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Jul 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.3-alt2
- Added module for Python 3

* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.3-alt1
- Version 1.1.3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.2-alt2.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.2-alt2
- Added necessary requirements
- Excluded *.pth

* Mon Jun 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.2-alt1
- Initial build for Sisyphus

