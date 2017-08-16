%define version 0.7.1
%define release alt2
%setup_python_module Epsilon

%def_with python3

%define oname Epsilon
Name: %packagename
Version: %version
Release: %release
BuildArch: noarch

Summary: A set of utility modules used by Divmod projects
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/Epsilon/

Source: http://divmod.org/trac/attachment/wiki/SoftwareReleases/%oname-%version.tar.gz
Patch1: %oname-0.7.0-alt-python3.patch
Patch2: %oname-%version-alt-python3-compat.patch

BuildRequires: python-module-pycrypto python-module-setuptools python-module-wx
BuildRequires: python-modules-json
BuildRequires: python-module-twisted-core-test
%if_with python3
BuildPreReq: rpm-build-python3
BuildRequires: python3-module-cryptography python3-module-zope
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-twisted-core-test
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

%package -n python3-module-%oname
Summary: A set of utility modules used by Divmod projects
Group: Development/Python3

%description -n python3-module-%oname
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
%setup -n %oname-%version

%patch1 -p2
%patch2 -p2

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

%check
py.test ||:

%if_with python3
pushd ../python3
py.test3 ||:
popd
%endif

%files
%python_sitelibdir/Epsilon-*.egg-info
%python_sitelibdir/epsilon
%doc *.txt LICENSE README

%exclude %_bindir/certcreate
%exclude %_bindir/benchmark

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/Epsilon-*.egg-info
%python3_sitelibdir/epsilon
%doc *.txt LICENSE README
%endif

%changelog
* Tue Aug 15 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.7.1-alt2
- Updated build dependencies.
- Enabled tests.

* Thu Jun 02 2016 Yuri N. Sedunov <aris@altlinux.org> 0.7.1-alt1
- 0.7.1

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

