%define oname Products.PythonScripts

#def_disable check

Name: python-module-%oname
Version: 2.14.0
Release: alt2.dev0.git20150618
Summary: Provides support for restricted execution of Python scripts in Zope 2
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.PythonScripts/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/zopefoundation/Products.PythonScripts.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-AccessControl python-module-Acquisition
BuildPreReq: python-module-DateTime python-module-DocumentTemplate
BuildPreReq: python-module-RestrictedPython-tests python-module-zExceptions
BuildPreReq: python-module-nose

%py_provides %oname
Requires: python-module-Zope2

%description
The Python Scripts product provides support for restricted execution of
Python scripts, exposing them as callable objects within the Zope
environment.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires RestrictedPython.tests

%description tests
The Python Scripts product provides support for restricted execution of
Python scripts, exposing them as callable objects within the Zope
environment.

This package contains tests for %oname.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
export PYTHONPATH=$PWD/src
python setup.py test
nosetests -vv %oname

%files
%doc *.txt
%python_sitelibdir/Products/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/*/tests

%changelog
* Sun Aug 30 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.14.0-alt2.dev0.git20150618
- Enabled check

* Sun Aug 30 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.14.0-alt1.dev0.git20150618
- Version 2.14.0.dev0
- Disabled testing for bootstrap

* Thu Oct 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.13.3-alt1.dev.git20130313
- Version 2.13.3dev
- Enabled testing

* Sat Oct 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.13.2-alt1
- Initial build for Sisyphus

