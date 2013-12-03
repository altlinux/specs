%define modulename dns

# Testing requires network access
%def_without check

Name: python-module-%modulename
Version: 1.11.1
Release: alt1.git20130921

Summary: DNS toolkit
License: BSD-like
Group: Development/Python
Url: http://www.dnspython.org
Packager: Python Development Team <python at packages.altlinux.org>

BuildArch: noarch

# http://www.dnspython.org/kits/%version/dnspython-%version.tar
# git://github.com/rthalley/dnspython.git
Source: %name-%version.tar

Provides: python-module-dnspython = %EVR
Obsoletes: python-module-dnspython <= 1.10.0-alt1

%setup_python_module %modulename

BuildPreReq: python-module-epydoc

%description
dnspython is a DNS toolkit for Python. It supports almost all
record types. It can be used for queries, zone transfers, and dynamic
updates.  It supports TSIG authenticated messages and EDNS0.

dnspython provides both high and low level access to DNS. The high
level classes perform queries for data of a given name, type, and
class, and return an answer set.  The low level classes allow
direct manipulation of DNS zones, messages, names, and records.

%prep
%setup
rm -f examples/._*

%build
%python_build
%make_build doc

%install
%python_install

%if_with check
%check
pushd tests
%make PYTHONPATH="../:$PYTHONPATH" check
popd
%endif

%files
%doc examples/ html/ ChangeLog LICENSE
%python_sitelibdir/*

%changelog
* Tue Dec 03 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.11.1-alt1.git20130921
- Version 1.11.1

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 1.10.0-alt2
- Version 1.10.0
- Obsoletes python-module-dnspython (ALT #28727)

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

