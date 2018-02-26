%define oname z3c.hashedresource
Name: python-module-%oname
Version: 1.1.3
Release: alt1
Summary: Provides URLs for resources that change whenever their content changes
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.hashedresource/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

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

%build
%python_build

%install
%python_install

%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/test*

%files tests
%python_sitelibdir/*/*/test*

%changelog
* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.3-alt1
- Version 1.1.3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.2-alt2.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.2-alt2
- Added necessary requirements
- Excluded *.pth

* Mon Jun 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.2-alt1
- Initial build for Sisyphus

