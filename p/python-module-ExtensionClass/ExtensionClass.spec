%define oname ExtensionClass
Name: python-module-%oname
Version: 4.3.0
Release: alt1
Summary: Metaclass for subclassable extension types
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/ExtensionClass/

# https://github.com/zopefoundation/ExtensionClass.git
Source: %name-%version.tar

BuildRequires: python-module-setuptools-tests
BuildRequires: python-module-nose

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
Group: Development/Python
Requires: %name = %version-%release

%description tests
Tests for ExtensionClass, ComputedAttribute and MethodObject.

%prep
%setup

%build
%add_optflags -fno-strict-aliasing
%python_build

%install
%python_install

%check
python setup.py test
nosetests

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests.*

%files tests
%python_sitelibdir/*/tests.*

%changelog
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

