# needs dnspython
%def_without check

Name:           python3-module-pymongo
Version:        4.3.3
Release:        alt1

Summary:        Python driver for MongoDB

Group:          Development/Python3
# All code is ASL 2.0 except bson/time64*.{c,h} which is MIT
License:        Apache-2.0 and MIT
URL:            http://api.mongodb.org/python
Source0:        http://pypi.python.org/packages/source/p/pymongo/pymongo-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

Requires:       python3-module-bson = %EVR

%description
The Python driver for MongoDB.

%package -n python3-module-gridfs
Summary:        Python GridFS driver for MongoDB
Group:          Development/Python3
Requires:       python3-module-pymongo = %EVR

%description -n python3-module-gridfs
GridFS is a storage specification for large objects in MongoDB.  This package
contains the python3 version of this module.

%package -n python3-module-bson
Summary:        Python bson library
Group:          Development/Python3

%description -n python3-module-bson
BSON is a binary-encoded serialization of JSON-like documents. BSON is designed
to be lightweight, traversable, and efficient. BSON, like JSON, supports the
embedding of objects and arrays within other objects and arrays.  This package
contains the python3 version of this module.

%prep
%setup -n pymongo-%{version}

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_create_default_config
%tox_check_pyproject

%files
%doc LICENSE README.rst doc
%python3_sitelibdir/pymongo
%python3_sitelibdir/%{pyproject_distinfo pymongo}

%files -n python3-module-gridfs
%doc LICENSE README.rst doc
%python3_sitelibdir/gridfs

%files -n python3-module-bson
%doc LICENSE README.rst doc
%python3_sitelibdir/bson

%changelog
* Tue Jan 31 2023 Grigory Ustinov <grenka@altlinux.org> 4.3.3-alt1
- Build new version.

* Wed Jul 28 2021 Grigory Ustinov <grenka@altlinux.org> 3.8.0-alt2
- Drop python2 support.

* Sat Jun 01 2019 Vitaly Lipatov <lav@altlinux.ru> 3.8.0-alt1
- NMU: new version 3.8.0 (with rpmrb script)

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 3.6.0-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Wed Dec 20 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 3.6.0-alt1
- Updated to upstream version 3.6.0.

* Mon Dec 19 2016 Vladimir Didenko <cow@altlinux.org> 3.4.0-alt1
- Version 3.4.0

* Wed Oct 26 2016 Vladimir Didenko <cow@altlinux.org> 3.3.0-alt1
- Version 3.3.0
- Build python 3 version

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.0.3-alt1.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 3.0.3-alt1.1
- NMU: Use buildreq for BR.

* Fri Jul 31 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.3-alt1
- Version 3.0.3

* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7.2-alt1
- Version 2.7.2

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 2.5.2-alt1_6
- update to new release by fcimport

* Tue Jul 08 2014 Igor Vlasenko <viy@altlinux.ru> 2.5.2-alt1_5
- update to new release by fcimport

* Tue Jun 03 2014 Igor Vlasenko <viy@altlinux.ru> 2.5.2-alt1_4
- update to new release by fcimport

* Mon Sep 09 2013 Igor Vlasenko <viy@altlinux.ru> 2.5.2-alt1_3
- new version

* Sat Mar 23 2013 Aleksey Avdeev <solo@altlinux.ru> 2.3-alt2.1
- Rebuild with Python-3.3

* Wed Jan 09 2013 Igor Vlasenko <viy@altlinux.ru> 2.3-alt2
- 2.3

* Sun Jan 06 2013 Igor Vlasenko <viy@altlinux.ru> 2.3-alt1_5
- fc import

* Wed May 02 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 2.2-alt1
- 2.2
- Build with Python3 support

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0.1-alt1.1
- Rebuild with Python-2.7

* Mon Sep 19 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0.1-alt1
- 2.0.1

* Wed Jul 21 2010 Egor Glukhov <kaman@altlinux.org> 1.7-alt1
- Initial build for Sisyphus
