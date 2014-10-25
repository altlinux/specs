%define oname yafowil
Name: python-module-%oname
Version: 2.1.2
Release: alt1.dev1.git20140909
Summary: Yet Another Form WIdget Library
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/yafowil/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/bluedynamics/yafowil.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-interlude
BuildPreReq: python-module-lxml python-module-node python-module-plumber
BuildPreReq: python-modules-json python-module-nose

%py_provides %oname
%py_requires json

%description
YAFOWIL offers html-form creation and modification at runtime. It is
light-weight and provides an extensible, reusable set of blueprints to
build flexible forms.

YAFOWIL is independent from any web-framework, but easy to use in your
web-framework.

It's all just about rendering widgets and extracting the data returned
from the browser per widget. It does not fight with storage.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
YAFOWIL offers html-form creation and modification at runtime. It is
light-weight and provides an extensible, reusable set of blueprints to
build flexible forms.

YAFOWIL is independent from any web-framework, but easy to use in your
web-framework.

It's all just about rendering widgets and extracting the data returned
from the browser per widget. It does not fight with storage.

This package contains tests for %oname

%prep
%setup

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

install -p -m644 src/yafowil/__init__.py \
	%buildroot%python_sitelibdir/yafowil/

%check
nosetests

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests.*

%files tests
%python_sitelibdir/*/tests.*

%changelog
* Sat Oct 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.2-alt1.dev1.git20140909
- Initial build for Sisyphus

