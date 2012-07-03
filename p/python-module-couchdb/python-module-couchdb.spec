%define sname couchdb
Summary: Python library for working with CouchDB. 
Name: python-module-%sname
Version: 0.8
Release: alt1.1
Source0: %name-%version.tar
#Source0: http://pypi.python.org/packages/source/C/CouchDB/CouchDB-%{version}.tar.gz
License: BSD
Group: Development/Python
URL: http://code.google.com/p/couchdb-python/
Packager: Mikhail Pokidko <pma@altlinux.org>
BuildArch: noarch

# Automatically added by buildreq on Thu Jul 10 2008
BuildRequires: python-devel
BuildRequires: python-module-setuptools

%description
A Python library for CouchDB. It provides a convenient high level interface for the CouchDB server.

%prep
%setup -q

%build
%python_build

%install
%python_install

%files
%doc README.txt ChangeLog.txt COPYING doc/*
%_bindir/couch*
%python_sitelibdir/%sname
%python_sitelibdir/CouchDB-%version-py*.egg-info

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.8-alt1.1
- Rebuild with Python-2.7

* Wed Dec 01 2010 Mikhail Pokidko <pma@altlinux.org> 0.8-alt1
- v0.8

* Fri Jul 16 2010 Mikhail Pokidko <pma@altlinux.org> 0.7-alt1
- v0.7

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6-alt1.1
- Rebuilt with python 2.6

* Mon Oct 12 2009 Mikhail Pokidko <pma@altlinux.org> 0.6-alt1
- Initial ALT build



