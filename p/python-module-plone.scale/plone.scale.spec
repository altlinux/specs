%define oname plone.scale

%def_without python3

Name: python-module-%oname
Version: 1.3.4
Release: alt1
Summary: Image scaling
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.scale/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-sphinx-devel python-module-persistent
BuildPreReq: python-module-repoze.sphinx.autointerface
BuildPreReq: python-module-zope.annotation python-module-Pillow
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
%py_requires plone zope.interface zope.annotation PIL

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

%package -n python3-module-%oname
Summary: Image scaling
Group: Development/Python3
%py3_provides %oname
%py3_requires plone zope.interface zope.annotation PIL

%description -n python3-module-%oname
This package contains image scaling logic for use in Zope environments.
It supports Zope 2, grok and other systems build on using the Zope
ToolKit (ZTK).

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
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

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
touch %buildroot%python_sitelibdir/plone/__init__.py
%make -C docs pickle
%make -C docs html
rm -f %buildroot%python_sitelibdir/plone/__init__.py*

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/.build/pickle %buildroot%python_sitelibdir/%oname/

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

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests
%endif

%changelog
* Thu Oct 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.4-alt1
- Initial build for Sisyphus

