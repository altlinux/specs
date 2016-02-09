%define module_name mongoengine

%def_with python3

Name: python-module-%module_name
Version: 0.10.0
Release: alt2
Summary: A Python Document-Object Mapper for working with MongoDB

License: MIT
Group: Development/Python
Url: http://hmarr.com/mongoengine/

Source: %name-%version.tar
BuildArch: noarch
BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-rednose python-module-colorama
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-rednose python3-module-colorama
%endif

%description
MongoEngine is a Python Object-Document Mapper for working with MongoDB.
MongoEngine is an ORM-like layer on top of PyMongo.

%package -n python3-module-%module_name
Summary: A Python Document-Object Mapper for working with MongoDB
Group: Development/Python3

%description -n python3-module-%module_name
MongoEngine is a Python Object-Document Mapper for working with MongoDB.
MongoEngine is an ORM-like layer on top of PyMongo.

%prep
%setup -q

%if_with python3
cp -fR . ../python3
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
rm -rf %buildroot%python_sitelibdir/tests

%if_with python3
pushd ../python3
%python3_install
rm -rf %buildroot%python3_sitelibdir/tests
popd
%endif

%files
%python_sitelibdir/%module_name
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%module_name
%python3_sitelibdir/%module_name
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Tue Feb 09 2016 Sergey Alembekov <rt@altlinux.ru> 0.10.0-alt2
- add colorama to buildreqs

* Tue Jul 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.0-alt1
- Version 0.10.0

* Sat Jan 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.7-alt2
- Added .egg-info

* Sat Jan 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.7-alt1
- Version 0.8.7

* Sat Jul 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.4-alt1.1
- Added module for Python 3

* Mon Sep 09 2013 Alexey Shabalin <shaba@altlinux.ru> 0.8.4-alt1
- 0.8.4

* Thu Jun 21 2012 Alexey Shabalin <shaba@altlinux.ru> 0.6.2-alt1
- 0.6.2

* Wed Nov 23 2011 Alexey Shabalin <shaba@altlinux.ru> 0.5.2-alt1
- initial build for ALT Linux Sisyphus

