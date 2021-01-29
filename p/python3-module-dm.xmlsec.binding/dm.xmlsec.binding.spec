%define mname dm.xmlsec
%define oname %mname.binding

%def_disable check

Name: python3-module-%oname
Version: 2.0
Release: alt2

Summary: Cython/lxml based binding for the XML security library -- for lxml 3.x
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/dm.xmlsec.binding/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: libxml2-devel libxmlsec1-devel libxmlsec1-openssl-devel
BuildRequires: python3-module-Cython python3-module-lxml

Requires: python3-module-%mname = %EVR
%py3_requires lxml

%py3_provides %oname


%description
This package contains a Cython based bindung to Aleksey Sanin's XML
security library to be used together with lxml, the most popular Python
binding to the Gnome XML library libxml2.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
This package contains a Cython based bindung to Aleksey Sanin's XML
security library to be used together with lxml, the most popular Python
binding to the Gnome XML library libxml2.

This package contains tests for %oname.

%package -n python3-module-%mname
Summary: Core files of %mname
Group: Development/Python3
%py3_provides %mname
Requires: python3-module-dm = %EVR

%description -n python3-module-%mname
Core files of %mname.

%package -n python3-module-dm
Summary: Core files of dm
Group: Development/Python3
%py3_provides dm

%description -n python3-module-dm
Core files of dm.

%prep
%setup

sed -i '/transformByHref/s/^/#/' dm/xmlsec/binding/__init__.py

rm -f src/*.c

%build
%python3_build_debug

%install
%python3_install

install -p -m644 dm/__init__.py \
	%buildroot%python3_sitelibdir/dm/
install -p -m644 dm/xmlsec/__init__.py \
	%buildroot%python3_sitelibdir/dm/xmlsec/

%check
%__python3 setup.py test

%files
%doc PKG-INFO
%python3_sitelibdir/dm/xmlsec/*
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/dm/xmlsec/*/tests.*
%exclude %python3_sitelibdir/dm/xmlsec/__init__.py*

%files tests
%python3_sitelibdir/dm/xmlsec/*/tests.*

%files -n python3-module-%mname
%dir %python3_sitelibdir/dm/xmlsec
%python3_sitelibdir/dm/xmlsec/__init__.py*

%files -n python3-module-dm
%dir %python3_sitelibdir/dm
%python3_sitelibdir/dm/__init__.py*


%changelog
* Wed Dec 02 2020 Grigory Ustinov <grenka@altlinux.org> 2.0-alt2
- Fix provides.

* Thu Feb 13 2020 Andrey Bychkov <mrdrew@altlinux.org> 2.0-alt1
- Version updated to 2.0
- porting on python3.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.3.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Dec 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt1
- Initial build for Sisyphus

