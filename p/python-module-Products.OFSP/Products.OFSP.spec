%define oname Products.OFSP

Name: python-module-%oname
Version: 2.13.3
Release: alt1.dev.git20130313
Summary: General Zope 2 help screens
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.OFSP/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/zopefoundation/Products.OFSP.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests

%py_provides %oname
Requires: python-module-Zope2

%description
OFSP provides the general Zope 2 help.

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

%files
%doc *.txt
%python_sitelibdir/Products/*
%python_sitelibdir/*.egg-info

%changelog
* Wed Oct 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.13.3-alt1.dev.git20130313
- Version 2.13.3dev
- Enabled testing

* Sat Oct 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.13.2-alt1
- Initial build for Sisyphus

