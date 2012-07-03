%define version 0.6.0
%define release alt1
%setup_python_module Epsilon

Name: %packagename
Version:%version
Release: %release.1
BuildArch: noarch

Summary: A set of utility modules used by Divmod projects
License: MIT
Group: Development/Python
Packager: Alexey Shabalin <shaba@altlinux.ru>
Url: http://divmod.org/trac/wiki/DivmodEpsilon

Source: http://divmod.org/trac/attachment/wiki/SoftwareReleases/%modulename-%version.tar.gz

BuildPreReq: rpm-build-python
BuildRequires: python-devel python-module-setuptools python-module-twisted python-module-OpenSSL python-modules-email
BuildPreReq: python-module-zope.interface

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


%prep
%setup -n %modulename-%version

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/Epsilon-*.egg-info
%python_sitelibdir/epsilon
%doc *.txt LICENSE README

%exclude %_bindir/benchmark

# remove dependencies on combinator
%exclude %python_sitelibdir/epsilon/release.*
%exclude %python_sitelibdir/epsilon/test/test_release.*

%changelog
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

