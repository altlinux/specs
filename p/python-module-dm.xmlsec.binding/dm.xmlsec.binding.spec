%define mname dm.xmlsec
%define oname %mname.binding

%def_disable check

Name: python-module-%oname
Version: 1.3.1
Release: alt1.1
Summary: Cython/lxml based binding for the XML security library -- for lxml 3.x
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/dm.xmlsec.binding/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: libxml2-devel libxmlsec1-devel libxmlsec1-openssl-devel
BuildPreReq: python-module-setuptools python-module-Cython
BuildPreReq: python-module-lxml

%py_provides %oname
Requires: python-module-%mname = %EVR
%py_requires lxml

%description
This package contains a Cython based bindung to Aleksey Sanin's XML
security library to be used together with lxml, the most popular Python
binding to the Gnome XML library libxml2.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package contains a Cython based bindung to Aleksey Sanin's XML
security library to be used together with lxml, the most popular Python
binding to the Gnome XML library libxml2.

This package contains tests for %oname.

%package -n python-module-%mname
Summary: Core files of %mname
Group: Development/Python
%py_provides %mname
Requires: python-module-dm = %EVR

%description -n python-module-%mname
Core files of %mname.

%package -n python-module-dm
Summary: Core files of dm
Group: Development/Python
%py_provides dm

%description -n python-module-dm
Core files of dm.

%prep
%setup

rm -f src/*.c

%build
%python_build_debug

%install
%python_install

install -p -m644 dm/__init__.py \
	%buildroot%python_sitelibdir/dm/
install -p -m644 dm/xmlsec/__init__.py \
	%buildroot%python_sitelibdir/dm/xmlsec/

%check
python setup.py test

%files
%doc PKG-INFO
%python_sitelibdir/dm/xmlsec/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/dm/xmlsec/*/tests.*
%exclude %python_sitelibdir/dm/xmlsec/__init__.py*

%files tests
%python_sitelibdir/dm/xmlsec/*/tests.*

%files -n python-module-%mname
%dir %python_sitelibdir/dm/xmlsec
%python_sitelibdir/dm/xmlsec/__init__.py*

%files -n python-module-dm
%dir %python_sitelibdir/dm
%python_sitelibdir/dm/__init__.py*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.3.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Dec 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt1
- Initial build for Sisyphus

