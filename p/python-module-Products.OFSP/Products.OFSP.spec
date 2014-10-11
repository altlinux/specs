%define oname Products.OFSP

%def_disable check

Name: python-module-%oname
Version: 2.13.2
Release: alt1
Summary: General Zope 2 help screens
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.OFSP/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

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
export PYTHONPATH=%buildroot%python_sitelibdir
python setup.py test

%files
%doc *.txt
%python_sitelibdir/Products/*
%python_sitelibdir/*.egg-info

%changelog
* Sat Oct 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.13.2-alt1
- Initial build for Sisyphus

