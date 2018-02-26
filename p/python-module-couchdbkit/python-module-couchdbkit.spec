%define sname couchdbkit
Summary: A distributed, fault-tolerant and schema-free document-oriented database accessible via a RESTful HTTP/JSON API
Name: python-module-%sname
Version: 0.4.10
Release: alt1.1
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

%description
Couchdbkit provides you a full featured and easy client to access and manage CouchDB.
It allows you to manage a CouchDB server, databases, doc managements and view access.
All objects mostly reflect python objects for convenience. Server and Databases objects could be used for example as easy as using a dict.

%prep
%setup -q

%build
%python_build

%install
%python_install

%files
%doc README.rst LICENSE NOTICE doc/*
%python_sitelibdir/%sname
%python_sitelibdir/%sname-%version-py*.egg-info

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4.10-alt1.1
- Rebuild with Python-2.7

* Tue Aug 03 2010 Mikhail Pokidko <pma@altlinux.org> 0.4.10-alt1
- initial build

