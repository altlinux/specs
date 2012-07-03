%define oname z3c.persistentfactory
Name: python-module-%oname
Version: 0.3
Release: alt2.1
Summary: Wrap instance methods in persistent factory wrappers for using instance methods as ZCA factories
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.persistentfactory/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.interface zope.component ZODB3

%description
The ZCA and the ZODB are a good combination where components require
persistent state. ZCA factories or handlers typically retrieve any
persistent state required from the persistent objects being adapted. If
the persistent state required is not specific to the objects being
adapted, a common solution is to register a persistent utility which is
then looked up in the factory or handler. The persistent utility
approach requires, however, that the one appropriate utility is looked
up which requires support in the ZCA registrations either in the
interface provided or the utility name.

In some cases, however, it is more consistent with the object oriented
semantics of Python and the ZCA to think of the factory or handler as an
instance method of a persistent object. With this approach the
non-context specific persistent state can be accessed on self.

%package tests
Summary: Tests for z3c.persistentfactory
Group: Development/Python
Requires: %name = %version-%release

%description tests
The ZCA and the ZODB are a good combination where components require
persistent state. ZCA factories or handlers typically retrieve any
persistent state required from the persistent objects being adapted. If
the persistent state required is not specific to the objects being
adapted, a common solution is to register a persistent utility which is
then looked up in the factory or handler. The persistent utility
approach requires, however, that the one appropriate utility is looked
up which requires support in the ZCA registrations either in the
interface provided or the utility name.

In some cases, however, it is more consistent with the object oriented
semantics of Python and the ZCA to think of the factory or handler as an
instance method of a persistent object. With this approach the
non-context specific persistent state can be accessed on self.

This package contains tests for z3c.persistentfactory.

%prep
%setup

%build
%python_build

%install
%python_install

%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%files
%doc *.txt docs/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/test*

%files tests
%python_sitelibdir/*/*/test*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3-alt2.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt2
- Added necessary requirements
- Excluded *.pth

* Mon Jun 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1
- Initial build for Sisyphus

