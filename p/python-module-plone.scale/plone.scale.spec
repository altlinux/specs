%define oname plone.scale

Name: python-module-%oname
Version: 1.3.5
Release: alt1.dev0.git20140907
Summary: Image scaling
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.scale/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-Zope2-tests
BuildPreReq: python-module-sphinx-devel python-module-persistent
BuildPreReq: python-module-repoze.sphinx.autointerface
BuildPreReq: python-module-zope.annotation python-module-Pillow

%py_provides %oname
%py_requires plone zope.interface zope.annotation PIL zope.component

%description
This package contains image scaling logic for use in Zope environments.
It supports Zope 2, grok and other systems build on using the Zope
ToolKit (ZTK).

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package contains image scaling logic for use in Zope environments.
It supports Zope 2, grok and other systems build on using the Zope
ToolKit (ZTK).

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
This package contains image scaling logic for use in Zope environments.
It supports Zope 2, grok and other systems build on using the Zope
ToolKit (ZTK).

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
This package contains image scaling logic for use in Zope environments.
It supports Zope 2, grok and other systems build on using the Zope
ToolKit (ZTK).

This package contains documentation for %oname.

%prep
%setup

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

export PYTHONPATH=%buildroot%python_sitelibdir
touch %buildroot%python_sitelibdir/plone/__init__.py
%make -C docs pickle
%make -C docs html
rm -f %buildroot%python_sitelibdir/plone/__init__.py*

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/.build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/*/tests
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/.build/html/*

%files tests
%python_sitelibdir/*/*/tests

%changelog
* Wed Oct 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.5-alt1.dev0.git20140907
- Version 1.3.5.dev0
- Enabled testing

* Thu Oct 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.4-alt1
- Initial build for Sisyphus

