%define mname collective
%define oname %mname.autopermission
Name: python-module-%oname
Version: 1.0
Release: alt1.b3dev.git20130130
Summary: Create permissions in Zope 2 on demand when a <permission /> directive is used
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.autopermission/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.autopermission.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname

%description
This package registers an event handler that initialises permissions on
the fly. To use it, simply include its ZCML:

  <include package="collective.autopermission" />

Then, you can use the <permission /> ZCML statement to define a new type
of permission, without also needing to make the permission "spring into
existence" via ClassSecurityInfo or similar.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

install -p -m644 collective/autopermission/configure.zcml \
	%buildroot%python_sitelibdir/collective/autopermission/

%check
python setup.py test

%files
%doc *.txt docs/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info

%changelog
* Mon Nov 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.b3dev.git20130130
- Initial build for Sisyphus

