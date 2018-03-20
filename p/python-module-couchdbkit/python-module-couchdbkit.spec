%define modname couchdbkit

Name: python-module-%modname
Version: 0.6.5
Release: alt1

Summary: Couchdbkit provides you a full featured and easy client to access and manage CouchDB.
License: Apache License v. 2.0
Group: Development/Python

URL: http://couchdbkit.org/
# https://github.com/benoitc/couchdbkit
Packager: Andrey Bychkov <mrdrew@altlinux.org>
BuildArch: noarch

Source: couchdbkit-%version.tar

# Automatically added by buildreq on Thu Jul 10 2008
BuildRequires: python-module-setuptools
BuildRequires: python-devel

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel
BuildPreReq: python3-module-setuptools
BuildPreReq: python-tools-2to3


%description
Couchdbkit provides you a full featured and easy client to access and manage CouchDB. It allows you to manage a CouchDBserver, databases, doc managements and view access. All objects mostly reflect python objects for convenience. Server and Databases objects could be used for example as easy as using a dict.

%package -n python3-module-%modname
Summary: Couchdbkit provides you a full featured and easy client to access and manage CouchDB.
Group: Development/Python3
%add_python3_req_skip django.test.simple

%description -n python3-module-%modname
Couchdbkit provides you a full featured and easy client to access and manage CouchDB. It allows you to manage a CouchDBserver, databases, doc managements and view access. All objects mostly reflect python objects for convenience. Server and Databases objects could be used for example as easy as using a dict.

%prep
%setup -n couchdbkit-%version

cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python_build

pushd ../python3
%python3_build
popd

%install
%python_install

pushd ../python3
%python3_install
popd

%files
%doc README.rst LICENSE NOTICE doc/*
%python_sitelibdir/%modname
%python_sitelibdir/%modname-%version-py*.egg-info

%files -n python3-module-%modname
%doc README.rst LICENSE NOTICE doc/*
%python3_sitelibdir/%modname
%python3_sitelibdir/%modname-%version-py*.egg-info


%changelog
* Tue Mar 20 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.6.5-alt1
- Version 0.6.5

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.10-alt1.2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jul 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.10-alt1.2
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4.10-alt1.1
- Rebuild with Python-2.7

* Tue Aug 03 2010 Mikhail Pokidko <pma@altlinux.org> 0.4.10-alt1
- initial build
