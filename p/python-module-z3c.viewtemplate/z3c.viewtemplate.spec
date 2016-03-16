%define oname z3c.viewtemplate

%def_with python3

Name: python-module-%oname
Version: 0.4.1
Release: alt3.1
Summary: View Templates
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.viewtemplate/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

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

%package -n python3-module-%oname
Summary: View Templates
Group: Development/Python3
%py3_requires zope.app.pagetemplate zope.component zope.configuration
%py3_requires zope.contentprovider zope.i18nmessageid zope.pagetemplate
%py3_requires zope.publisher zope.tal

%description -n python3-module-%oname
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

%package -n python3-module-%oname-tests
Summary: Tests for View Templates
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.app.testing zope.testing

%description -n python3-module-%oname-tests
This package allows us to separate the registration of the view code and
the view templates.

This package contains tests for View Templates.

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

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
find -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.1-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jul 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4.1-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt2
- Added necessary requirements
- Excluded *.pth

* Thu Jun 02 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt1
- Initial build for Sisyphus

