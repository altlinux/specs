%define sname couchapp
Summary: Utilities to make standalone CouchDB application development simple
Name: python-module-%sname
Version: 0.7.2
Release: alt1.1
Source0: %name-%version.tar
License: Apache 2.0
Group: Development/Python
URL: http://code.google.com/p/couchdb-python/
Packager: Mikhail Pokidko <pma@altlinux.org>
BuildArch: noarch

BuildRequires: python-module-setuptools

%description
CouchApp is designed to structure standalone CouchDB application development for maximum application portability.
CouchApp is a set of scripts and a jQuery plugin designed to bring clarity and order to the freedom of CouchDB's document-based approach.

%prep
%setup -q

%build
%python_build

%install
%python_install

%files
%doc couchapp.txt THANKS.txt README.md NOTICE LICENSE
%_bindir/couch*
%python_sitelibdir/%sname
%python_sitelibdir/Couchapp-%version-py*.egg-info/

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.7.2-alt1.1
- Rebuild with Python-2.7

* Fri Nov 26 2010 Mikhail Pokidko <pma@altlinux.org> 0.7.2-alt1
- 0.7.2

* Mon Sep 20 2010 Mikhail Pokidko <pma@altlinux.org> 0.7.1-alt1
- Version up.

* Wed Sep 01 2010 Mikhail Pokidko <pma@altlinux.org> 0.7.0-alt2
- Various fixes. Mustache and evently improvements.

* Fri Aug 13 2010 Mikhail Pokidko <pma@altlinux.org> 0.7.0-alt1
- initial build



