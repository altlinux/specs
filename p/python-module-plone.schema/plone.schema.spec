%define oname plone.schema

%def_disable check

Name: python-module-%oname
Version: 1.0
Release: alt1.a2.dev0.git20140417
Summary: Plone specific extensions and fields for zope schematas
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.schema/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.schema.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-plone.app.dexterity
BuildPreReq: python-module-plone.app.z3cform
BuildPreReq: python-module-plone.app.testing
#BuildPreReq: python-module-Products.CMFPlone

%py_provides %oname
%py_requires plone plone.app.dexterity plone.app.z3cform

%description
Plone specific extensions and fields for zope schematas.

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
python setup.py test

%files
%doc *.rst
%python_sitelibdir/*

%changelog
* Wed Oct 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.a2.dev0.git20140417
- Initial build for Sisyphus

