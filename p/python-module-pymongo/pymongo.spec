%def_with python3

Name: python-module-pymongo
Version: 2.2
Release: alt1

%setup_python_module pymongo
%setup_python_module gridfs
%setup_python_module bson

Summary: PyMongo is a Python distribution containing tools for working with MongoDB
License: Apache Licence v. 2.0
Group: Development/Python

Url: https://github.com/mongodb/mongo-python-driver

BuildRequires: python-module-distribute

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel
BuildRequires: python3-module-distribute
%endif

Requires: python-module-bson = %version-%release

Source: %name-%version.tar

%description
PyMongo is a Python distribution containing tools for working with
MongoDB, and is the recommended way to work with MongoDB from Python.

%package -n python-module-gridfs
Summary: gridfs package is a gridfs implementation on top of pymongo
Group: Development/Python
Requires: %name = %version-%release

%description -n python-module-gridfs
gridfs package is a gridfs (http://www.mongodb.org/display/DOCS/GridFS+Specification)
implementation on top of pymongo.

%package -n python-module-bson
Summary:  Python bson library
Group: Development/Python
Requires: %name = %version-%release

%description -n python-module-bson
BSON is a binary-encoded serialization of JSON-like documents. BSON is designed
to be lightweight, traversable, and efficient. BSON, like JSON, supports the
embedding of objects and arrays within other objects and arrays.

%if_with python3
%package -n python3-module-pymongo
Group: Development/Python3
Summary: Python3 module for working with MongoDB
%description -n python3-module-pymongo
PyMongo is a Python distribution containing tools for working with
MongoDB, and is the recommended way to work with MongoDB from Python.

%package -n python3-module-gridfs
Summary: gridfs package is a gridfs implementation on top of pymongo
Group: Development/Python3
Requires: python3-module-pymongo = %version-%release

%description -n python3-module-gridfs
gridfs package is a gridfs (http://www.mongodb.org/display/DOCS/GridFS+Specification)
implementation on top of pymongo.

%package -n python3-module-bson
Summary:  Python bson library
Group: Development/Python3
Requires: python3-module-pymongo = %version-%release

%description -n python3-module-bson
BSON is a binary-encoded serialization of JSON-like documents. BSON is designed
to be lightweight, traversable, and efficient. BSON, like JSON, supports the
embedding of objects and arrays within other objects and arrays.
%endif

%prep
%setup
%if_with python3
rm -rf ../python3
cp -a . ../python3
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
%doc README.rst
%python_sitelibdir/pymongo/

%files -n python-module-gridfs
%python_sitelibdir/gridfs/

%files -n python-module-bson
%python_sitelibdir/bson/

%if_with python3
%files -n python3-module-pymongo
%python3_sitelibdir/pymongo/

%files -n python3-module-gridfs
%python3_sitelibdir/gridfs/

%files -n python3-module-bson
%python3_sitelibdir/bson/
%endif

%changelog
* Wed May 02 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 2.2-alt1
- 2.2
- Build with Python3 support

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0.1-alt1.1
- Rebuild with Python-2.7

* Mon Sep 19 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0.1-alt1
- 2.0.1

* Wed Jul 21 2010 Egor Glukhov <kaman@altlinux.org> 1.7-alt1
- Initial build for Sisyphus
