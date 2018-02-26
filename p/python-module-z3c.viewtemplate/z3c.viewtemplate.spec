%define oname z3c.viewtemplate
Name: python-module-%oname
Version: 0.4.1
Release: alt2.1
Summary: View Templates
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.viewtemplate/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.app.pagetemplate zope.component zope.configuration
%py_requires zope.contentprovider zope.i18nmessageid zope.pagetemplate
%py_requires zope.publisher zope.tal

%description
This package allows us to separate the registration of the view code and
the view templates.

Why is this a good thing?

While developing customizable applications that require us to develop
multiple customer UIs for one particular application, we noticed there
is a fine but clear distinction between skins and layers. Layers contain
the logic to prepare data for presentation output, namely the view
classes. Skins, on the other hand contain the resources to generate the
UI, for example templates, images and CSS files.

The problem of the existing infrastructure is that code, template and
layer are all hardlinked in one zcml configuration directive of the view
component -- page, content provider, viewlet. This package separates
this triplet -- code, template, layer -- into two pairs, code/layer and
template/skin. No additional components are introduced, since skins and
layers are physically the same components.

%package tests
Summary: Tests for View Templates
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.testing zope.testing

%description tests
This package allows us to separate the registration of the view code and
the view templates.

This package contains tests for View Templates.

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
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4.1-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt2
- Added necessary requirements
- Excluded *.pth

* Thu Jun 02 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt1
- Initial build for Sisyphus

