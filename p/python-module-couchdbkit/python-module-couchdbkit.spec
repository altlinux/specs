%define sname couchdbkit

%def_with python3

Summary: A distributed, fault-tolerant and schema-free document-oriented database accessible via a RESTful HTTP/JSON API
Name: python-module-%sname
Version: 0.4.10
Release: alt1.2.1
Source0: %name-%version.tar
#Source0: http://pypi.python.org/packages/source/c/%sname/%sname-%version.tar.gz
License: Apache License v. 2.0
Group: Development/Python
URL: http://couchdbkit.org/
Packager: Mikhail Pokidko <pma@altlinux.org>
BuildArch: noarch

# Automatically added by buildreq on Thu Jul 10 2008
BuildRequires: python-devel
BuildRequires: python-module-setuptools

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%description
Couchdbkit provides you a full featured and easy client to access and manage CouchDB.
It allows you to manage a CouchDB server, databases, doc managements and view access.
All objects mostly reflect python objects for convenience. Server and Databases objects could be used for example as easy as using a dict.

%package -n python3-module-%sname
Summary: A distributed, fault-tolerant and schema-free document-oriented database accessible via a RESTful HTTP/JSON API
Group: Development/Python3

%description -n python3-module-%sname
Couchdbkit provides you a full featured and easy client to access and manage CouchDB.
It allows you to manage a CouchDB server, databases, doc managements and view access.
All objects mostly reflect python objects for convenience. Server and Databases objects could be used for example as easy as using a dict.

%prep
%setup

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
%doc README.rst LICENSE NOTICE doc/*
%python_sitelibdir/%sname
%python_sitelibdir/%sname-%version-py*.egg-info

%if_with python3
%files -n python3-module-%sname
%doc README.rst LICENSE NOTICE doc/*
%python3_sitelibdir/%sname
%python3_sitelibdir/%sname-%version-py*.egg-info
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.10-alt1.2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jul 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.10-alt1.2
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4.10-alt1.1
- Rebuild with Python-2.7

* Tue Aug 03 2010 Mikhail Pokidko <pma@altlinux.org> 0.4.10-alt1
- initial build

