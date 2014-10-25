%define mname plonetheme
%define oname %mname.classic
Name: python-module-%oname
Version: 1.3.4
Release: alt1.dev0.git20140128
Summary: The classic Plone 3 default theme
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/plonetheme.classic/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plonetheme.classic.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-plone.theme
BuildPreReq: python-module-Products.CMFCore

%py_provides %oname
%py_requires %mname plone.theme Products.CMFCore

%description
This theme implements the look of Plone 3 and earlier in a separate
package, and is supplied for backwards compatibility reasons, and for
people who prefer the old theme over the new standard one in Plone 4.

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
%doc *.txt docs/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info

%changelog
* Sat Oct 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.4-alt1.dev0.git20140128
- Initial build for Sisyphus

