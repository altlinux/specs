%define oname Products.GenericSetup

Name: python-module-%oname
Version: 1.7.4
Release: alt1
Summary: Read Zope configuration state from profile dirs / tarballs
License: ZPL
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.GenericSetup/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-sphinx-devel python-module-Zope2-tests
BuildPreReq: python-module-five.localsitemanager
BuildPreReq: python-module-zope.formlib python-module-zope.datetime
BuildPreReq: python-module-zope.testrunner
BuildPreReq: python-module-zope.component-tests
BuildPreReq: python-module-zope.traversing-tests
BuildPreReq: python-module-zope.security-tests

%py_provides %oname
Requires: python-module-Zope2
%py_requires Products.PluginIndexes Products.ZCTextIndex
%py_requires five.localsitemanager zope.formlib

%description
This product provides a mini-framework for expressing the configured
state of a Zope Site as a set of filesystem artifacts. These artifacts
consist of declarative XML files, which spell out the configuration
settings for each "tool" in the site , and supporting scripts /
templates, in their "canonical" filesystem representations.

%package tests
Summary: Tests for %name
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.testrunner

%description tests
This product provides a mini-framework for expressing the configured
state of a Zope Site as a set of filesystem artifacts. These artifacts
consist of declarative XML files, which spell out the configuration
settings for each "tool" in the site , and supporting scripts /
templates, in their "canonical" filesystem representations.

This package contains tests for %name.

%package docs
Summary: Documentation for %name
Group: Development/Documentation
BuildArch: noarch

%description docs
This product provides a mini-framework for expressing the configured
state of a Zope Site as a set of filesystem artifacts. These artifacts
consist of declarative XML files, which spell out the configuration
settings for each "tool" in the site , and supporting scripts /
templates, in their "canonical" filesystem representations.

This package contains documentation for %name.

%package pickles
Summary: Pickles for %name
Group: Development/Python

%description pickles
This product provides a mini-framework for expressing the configured
state of a Zope Site as a set of filesystem artifacts. These artifacts
consist of declarative XML files, which spell out the configuration
settings for each "tool" in the site , and supporting scripts /
templates, in their "canonical" filesystem representations.

This package contains pickles for %name.

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
%make -C docs pickle
%make -C docs html

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/.build/pickle %buildroot%python_sitelibdir/%oname

%check
export PYTHONPATH=%buildroot%python_sitelibdir
touch %buildroot%python_sitelibdir/Products/__init__.py
python setup.py test
rm -f %buildroot%python_sitelibdir/Products/__init__.py*

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/*/*/test*
%exclude %python_sitelibdir/*/*/*/test*

%files tests
%python_sitelibdir/*/*/test*
%python_sitelibdir/*/*/*/test*

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/.build/html/*

%changelog
* Sat Oct 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.4-alt1
- Initial build for Sisyphus

