%define sname restkit
Summary: Restkit is an HTTP resource kit for Python
Name: python-module-%sname
Version: 2.3.1
Release: alt1.1
Source0: %name-%version.tar
#Source0: http://pypi.python.org/packages/source/r/%sname/%sname-%version.tar.gz
License: BSD
Group: Development/Python
URL: http://pypi.python.org/pypi/restkit
Packager: Mikhail Pokidko <pma@altlinux.org>
BuildArch: noarch

%add_python_req_skip eventlet

# Automatically added by buildreq on Thu Jul 10 2008
BuildRequires: python-devel
BuildRequires: python-module-setuptools

%description
Restkit is an HTTP resource kit for Python. 
It allows you to easily access to HTTP resource and build objects around it. 
It's the base of couchdbkit a Python CouchDB framework.

%prep
%setup -q

%build
%python_build

%install
%python_install

%files
%doc README.rst THANKS LICENSE NOTICE examples/* doc/*
%_bindir/restcli
%python_sitelibdir/%sname
%python_sitelibdir/%sname-%version-py*.egg-info

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.3.1-alt1.1
- Rebuild with Python-2.7

* Tue Nov 30 2010 Mikhail Pokidko <pma@altlinux.org> 2.3.1-alt1
- v2.3.1

* Mon Sep 20 2010 Mikhail Pokidko <pma@altlinux.org> 2.2.1-alt1
- Version up.

* Wed Aug 04 2010 Mikhail Pokidko <pma@altlinux.org> 2.1.0-alt1
- initial build


