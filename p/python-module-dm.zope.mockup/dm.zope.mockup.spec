%define mname dm.zope
%define oname %mname.mockup
Name: python-module-%oname
Version: 0.1.1.2
Release: alt1
Summary: A (still small) repository of mockup objects for Zope [2] tests
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/dm.zope.mockup/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-ZODB

%py_provides %oname
%py_requires %mname ZODB

%description
This is a (still small) repository with mockup objects to be used in
testsuites for Zope 2 applications and application components.

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
%doc PKG-INFO
%python_sitelibdir/dm/zope/mockup
%python_sitelibdir/*.egg-info

%changelog
* Sat Feb 14 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1.2-alt1
- Initial build for Sisyphus

