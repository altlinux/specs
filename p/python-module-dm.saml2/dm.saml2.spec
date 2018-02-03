# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt1.1.1
%define mname dm
%define oname %mname.saml2
Name: python-module-%oname
Version: 3.1.2
#Release: alt1
Summary: SAML2 support based on PyXB
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/dm.saml2/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools
BuildPreReq: python-module-pyxb
BuildPreReq: python-module-dm.xmlsec.binding

%py_provides %oname
%py_requires %mname dm.xmlsec.binding pyxb

%description
This package provides support for SAML2 based on pyxb.

pyxb generates a Python class collection for an XML schema and provides
means to convert between associated Python instances and xml documents.
It is used to generate and parse SAML2 messages.

The package adds support for digital signatures and SAML2 bindings and
metadata management.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%if "%_libexecdir" != "%_libdir"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

install -p -m644 %mname/saml2/*.txt \
	%buildroot%python_sitelibdir/%mname/saml2/

%check
python setup.py test

%files
%doc PKG-INFO
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.1.2-alt1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.1.2-alt1.1
- (AUTO) subst_x86_64.

* Mon Dec 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.2-alt1
- Initial build for Sisyphus

