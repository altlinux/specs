%define modulename xmpp

Name: python-module-%modulename
Version: 0.5.0
Release: alt3.1

%setup_python_module %modulename

Summary: XMPP-IM-compliant library for jabber instant messenging
License: GPL
Group: Development/Python

Url: http://xmpppy.sourceforge.net/
BuildArch: noarch

Source: %name-%version.tar

BuildPreReq: %py_dependencies setuptools
Provides: python-module-xmpppy

%description
This library provides functionality for writing xmpp-compliant
clients, servers and/or components/transports.

It was initially designed as a "rework" of the jabberpy library but
has become a separate product.

Unlike jabberpy it is distributed under the terms of GPL.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%doc README doc
%python_sitelibdir/%modulename/*
%python_sitelibdir/*.egg-info

%changelog
* Sun Oct 23 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.0-alt3.1
- Rebuild with Python-2.7

* Mon Apr 19 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 0.5.0-alt3
- Merge python-module-xmpppy and python-module-xmpp into one package.
- Provide "python-module-xmpppy".

* Wed Dec 16 2009 Igor Vlasenko <viy@altlinux.ru> 0.4.0-alt3.qa1
- NMU (by repocop): the following fixes applied:
  * vendor-tag for python-module-xmpp
  * postclean-05-filetriggers for spec file

* Mon Nov 23 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt3
- Rebuilt with python 2.6

* Tue Jan 29 2008 Grigory Batalov <bga@altlinux.ru> 0.4.0-alt2.1
- Rebuilt with python-2.5.

* Tue Jan 22 2008 Grigory Batalov <bga@altlinux.ru> 0.4.0-alt2
- Use python_sitelibdir macro while packaging.

* Fri Feb 02 2007 Mikhail Pokidko <pma@altlinux.ru> 0.4.0-alt1
- NMU. Version 0.4.0.

* Mon Mar 07 2005 Andrey Orlov <cray@altlinux.ru> 0.2-alt3.pre2
- xsend installed in tooldir as jabber_send

* Sun Mar 06 2005 Andrey Orlov <cray@altlinux.ru> 0.2-alt2.pre2
- initial release

