%define mname eea
%define oname %mname.jquery
Name: python-module-%oname
Version: 8.2
Release: alt1.dev.git20141203
Summary: jQuery library and plugins for Plone
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/eea.jquery/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/eea/eea.jquery.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-collective.js.jqueryui
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-zope.configuration

%py_provides %oname
Requires: python-module-%mname = %EVR
%py_requires collective.js.jqueryui

%description
EEA jQuery provides jQuery 1.3.2 and 1.4.2 JS libraries as zope3
resources and some jQuery plugins like: annotator, bbq, browser, cookie,
fancybox, galleryview, jqzoom, qtip, splitter, tagcloud, flashembed and
more.

Each plugin comes with its own GenericSetup profile in order to easily
use it within your Plone sites.

%package tests
Summary: Tests for %oname
Group:Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing zope.configuration

%description tests
EEA jQuery provides jQuery 1.3.2 and 1.4.2 JS libraries as zope3
resources and some jQuery plugins like: annotator, bbq, browser, cookie,
fancybox, galleryview, jqzoom, qtip, splitter, tagcloud, flashembed and
more.

Each plugin comes with its own GenericSetup profile in order to easily
use it within your Plone sites.

This package contains tests for %oname.

%package -n python-module-%mname
Summary: Core files of %mname
Group: Development/Python
%py_provides %mname

%description -n python-module-%mname
Core files of %mname.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

install -p -m644 %mname/__init__.py \
	%buildroot%python_sitelibdir/%mname/
pushd %mname/jquery
cp -fR *.txt *.zcml documentation profiles profiles-bbb utils \
	%buildroot%python_sitelibdir/%mname/jquery/
for i in browser jquery plugins upgrades; do
	cp -fR $i/* \
		%buildroot%python_sitelibdir/%mname/jquery/$i/
done
popd

%check
python setup.py test
rm -fR build
py.test

%files
%doc *.md *.txt docs/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/test*
%exclude %python_sitelibdir/%mname/*/*/test*
%exclude %python_sitelibdir/%mname/__init__.py*

%files tests
%python_sitelibdir/%mname/*/test*
%python_sitelibdir/%mname/*/*/test*

%files -n python-module-%mname
%dir %python_sitelibdir/%mname
%python_sitelibdir/%mname/__init__.py*

%changelog
* Mon Dec 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 8.2-alt1.dev.git20141203
- Initial build for Sisyphus

