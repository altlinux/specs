%define oname couchquery

Summary: Python library for simple and dynamic access to CouchDB
Name: python-module-couchquery
Version: 0.9
Release: alt1.1
Source0: %name-%version-%release.tar
License: GPL
Group: Development/Python
URL: http://github.com/mikeal/couchquery
Packager: Mikhail Pokidko <pma@altlinux.org>
BuildArch: noarch

# Automatically added by buildreq on Thu Jul 10 2008
BuildRequires: python-devel
BuildRequires: python-module-setuptools

%description
This module is an attempt to combine the best features of httplib with
the scalability of asynchat.

I have pasted as much code as I could from httplib (Python 2.0) because it
is a well written and widely used interface. This may be a mistake,
because the behavior of AsynchHTTPConnection os quite different from that of
httplib.HTTPConnection


%prep
%setup -q

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/%oname
%python_sitelibdir/%oname-*.egg-info

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9-alt1.1
- Rebuild with Python-2.7

* Mon Dec 21 2009 Mikhail Pokidko <pma@altlinux.org> 0.9-alt1
- release 0.9

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.3-alt1.1
- Rebuilt with python 2.6

* Thu Oct 15 2009 Mikhail Pokidko <pma@altlinux.org> 0.8.3-alt1
- Initial build



