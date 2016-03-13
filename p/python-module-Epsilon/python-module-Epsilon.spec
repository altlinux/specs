%define version 0.7.0
%define release alt1
%setup_python_module Epsilon

%def_with python3

Name: %packagename
Version:%version
Release: alt1.1.1
BuildArch: noarch

Summary: A set of utility modules used by Divmod projects
License: MIT
Group: Development/Python
Packager: Alexey Shabalin <shaba@altlinux.ru>
Url: http://divmod.org/trac/wiki/DivmodEpsilon

Source: http://divmod.org/trac/attachment/wiki/SoftwareReleases/%modulename-%version.tar.gz
Patch: Epsilon-0.7.0-alt-python3.patch

#BuildPreReq: rpm-build-python
# Automatically added by buildreq on Mon Feb 01 2016 (-bi)
# optimized out: python-base python-devel python-module-numpy python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-logging python-modules-unittest python-tools-2to3 python3 python3-base python3-module-cffi python3-module-enum34 python3-module-pycparser python3-module-setuptools python3-module-zope.interface
BuildRequires: python-module-pycrypto python-module-setuptools python-module-wx python3-module-cryptography python3-module-zope rpm-build-python3 time

#BuildRequires: python-devel python-module-setuptools
#BuildPreReq: python-module-twisted python-module-OpenSSL
#BuildPreReq: python-modules-email
#BuildPreReq: python-module-zope.interface
%if_with python3
#BuildPreReq: rpm-build-python3
#BuildRequires: python3-devel python3-module-setuptools
#BuildPreReq: python3-module-OpenSSL
#BuildPreReq: python3-module-zope.interface python-tools-2to3
%endif

%description
A small utility package that depends on tools too recent for Twisted
(like datetime in python2.4) but performs generic enough functions that
it can be used in projects that don't want to share Divmod's other
projects' large footprint.

Currently included:

    * A powerful date/time formatting and import/export class
    (ExtimeDotTime), for exchanging date and time information between
    all Python's various ways to interpret objects as times or time
    deltas.
    * Tools for managing concurrent asynchronous processes within Twisted.
    * A metaclass which helps you define classes with explicit states.
    * A featureful Version class.
    * A formal system for application of monkey-patches. 

%package -n python3-module-%modulename
Summary: A set of utility modules used by Divmod projects
Group: Development/Python3

%description -n python3-module-%modulename
A small utility package that depends on tools too recent for Twisted
(like datetime in python2.4) but performs generic enough functions that
it can be used in projects that don't want to share Divmod's other
projects' large footprint.

Currently included:

    * A powerful date/time formatting and import/export class
    (ExtimeDotTime), for exchanging date and time information between
    all Python's various ways to interpret objects as times or time
    deltas.
    * Tools for managing concurrent asynchronous processes within Twisted.
    * A metaclass which helps you define classes with explicit states.
    * A featureful Version class.
    * A formal system for application of monkey-patches. 

%prep
%setup -n %modulename-%version

%patch -p2

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%python_sitelibdir/Epsilon-*.egg-info
%python_sitelibdir/epsilon
%doc *.txt LICENSE README

%exclude %_bindir/benchmark

%if_with python3
%files -n python3-module-%modulename
%python3_sitelibdir/Epsilon-*.egg-info
%python3_sitelibdir/epsilon
%doc *.txt LICENSE README
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.7.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt1.1
- NMU: Use buildreq for BR.

* Wed Aug 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.0-alt1
- Version 0.7.0
- Added module for Python 3

* Fri Oct 28 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.0-alt1.1
- Rebuild with Python-2.7

* Tue Mar 16 2010 Alexey Shabalin <shaba@altlinux.ru> 0.6.0-alt1
- 0.6.0

* Tue Nov 17 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.12-alt1.1
- Rebuilt with python 2.6

* Sun Apr 19 2009 Alexey Shabalin <shaba@altlinux.ru> 0.5.12-alt1
- 0.5.12
- build as noarch

* Mon Nov 03 2008 Alexey Shabalin <shaba@altlinux.ru> 0.5.9-alt1
- first build for Sisyphus
- thx to aris@ for spec 

