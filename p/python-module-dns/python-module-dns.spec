%define modulename dns

Name: python-module-%modulename
Version: 1.9.2
Release: alt1.1

Summary: DNS toolkit
License: BSD-like
Group: Development/Python
Url: http://www.dnspython.org
Packager: Python Development Team <python at packages.altlinux.org>

BuildArch: noarch

Source: http://www.dnspython.org/kits/%version/dnspython-%version.tar

%setup_python_module %modulename

%description
dnspython is a DNS toolkit for Python. It supports almost all
record types. It can be used for queries, zone transfers, and dynamic
updates.  It supports TSIG authenticated messages and EDNS0.

dnspython provides both high and low level access to DNS. The high
level classes perform queries for data of a given name, type, and
class, and return an answer set.  The low level classes allow
direct manipulation of DNS zones, messages, names, and records.

%prep
%setup -n dnspython-%version
rm -f examples/._*

%build
%python_build

%install
%python_install

%files
%doc examples ChangeLog LICENSE README TODO
%python_sitelibdir/*

%changelog
* Sun Oct 23 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.9.2-alt1.1
- Rebuild with Python-2.7

* Sat Nov 27 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.2-alt1
- Version 1.9.2

* Mon Feb 08 2010 Vitaly Lipatov <lav@altlinux.ru> 1.8.0-alt1
- cleanup spec
- new version (1.8.0) import in git

* Fri Nov 20 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.4-alt2
- Rebuilt with python 2.6

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 1.3.4-alt1.1
- Rebuilt with python-2.5.

* Mon Oct 03 2005 Andrey Orlov <cray@altlinux.ru> 1.3.4-alt1
- initial release

