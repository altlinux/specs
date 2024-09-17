%define oname ExtensionClass

%def_with check

Name: python3-module-%oname
Version: 6.0
Release: alt1

Summary: Metaclass for subclassable extension types
License: ZPL-2.1
Group: Development/Python3
Url: https://pypi.org/project/ExtensionClass/
Vcs: https://github.com/zopefoundation/ExtensionClass.git

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-zope.testrunner
%endif

%description
ExtensionClass:
This package provides a metaclass that allows classes implemented in
extension modules to be subclassed in Python. Unless you need
ExtensionClasses for legacy applications (e.g. Zope 2), you probably
want to use Python's new-style classes (available since Python 2.2).

ComputedAttribute:
This package provides a way to attach attributes to an ExtensionClass or
instance that are computed by calling a callable. This works very much
like property known from new-style classes, except that a
ComputedAttribute can also be attached to an instance and that it
honours ExtensionClass semantics (which is useful for retaining
Acquisition wrappers, for example).

MethodObject:
This package lets you attach additional "methods" to ExtensionClasses.
These "methods" are actually implemented by subclassing the
MethodObject.Method class and implementing the __call__ method there.
Instances of those classes will be bound to the instances they're
attached to and will receive that instance object as a first parameter
(after self).

%package tests
Summary: Tests for ExtensionClass, ComputedAttribute and MethodObject
Group: Development/Python3
Requires: %name = %EVR

%description tests
Tests for ExtensionClass, ComputedAttribute and MethodObject.

%prep
%setup

%build
%add_optflags -fno-strict-aliasing
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run -- zope-testrunner --test-path=src -vc

%files
%doc *.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests.*

%files tests
%python3_sitelibdir/*/tests.*


%changelog
* Tue Sep 17 2024 Anton Vyatkin <toni@altlinux.org> 6.0-alt1
- New version 6.0.

* Thu Oct 05 2023 Anton Vyatkin <toni@altlinux.org> 5.1-alt1
- New version 5.1.

* Wed Mar 29 2023 Anton Vyatkin <toni@altlinux.org> 5.0-alt1
- New version 5.0.

* Wed Jan 15 2020 Andrey Bychkov <mrdrew@altlinux.org> 4.3.0-alt2
- porting on python3

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 4.3.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Nov 30 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 4.3.0-alt1
- Updated to upstream version 4.3.0.

* Tue Feb 02 2016 Sergey Alembekov <rt@altlinux.ru> 4.1.3-alt2.dev0.git20150522
- clean buildreq

* Wed Aug 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.3-alt1.dev0.git20150522
- Version 4.1.3.dev0

* Fri Dec 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1-alt1.git20141218
- Version 4.1

* Thu Nov 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1-alt1.b1.git20141112
- Version 4.1b1

* Wed Oct 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1-alt1.a1.git20130504
- Snapshot from git
- Enabled testing

* Mon Sep 16 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1-alt1.a1
- Version 4.1a1

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 4.0a1-alt1.1
- Rebuild to remove redundant libpython2.7 dependency

* Fri Dec 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0a1-alt1
- Version 4.0a1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.13.2-alt1.1
- Rebuild with Python-2.7

* Mon May 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.13.2-alt1
- Initial build for Sisyphus

