%define module_name mongoengine

Name: python3-module-%module_name
Version: 0.28.2
Release: alt1

Summary: A Python Document-Object Mapper for working with MongoDB
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/mongoengine
Vcs: https://github.com/MongoEngine/mongoengine

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%description
MongoEngine is a Python Object-Document Mapper for working with MongoDB.
MongoEngine is an ORM-like layer on top of PyMongo.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/%module_name
%python3_sitelibdir/%module_name-%version.dist-info

%changelog
* Mon Jul 22 2024 Anton Vyatkin <toni@altlinux.org> 0.28.2-alt1
- New version 0.28.2.
- Return to Sisyphus.

* Tue May 25 2021 Grigory Ustinov <grenka@altlinux.org> 0.10.0-alt3
- Drop python2 support.

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.10.0-alt2.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.10.0-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

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

