%define module_name jabberpy
Name: python-module-%module_name
Version: 0.5.0
Release: alt6.1

Summary: Python module for Jabber
Group: Development/Python
License: LGPL
URL: http://jabberpy.sourceforge.net
Packager: Denis Klimov <zver@altlinux.org>

BuildArch: noarch
Requires: python >= 2.0

Source: %name-%version.tar

BuildRequires: python-devel >= 2.0

%description
jabber.py is a Python module for the Jabber instant messaging
protocol. jabber.py deals with the xml parsing and socket code,
leaving the programmer to concentrate on developing quality Jabber
based applications with Python.

#%package examples
#Summary: Examples for jabberpy python module
#Group: Development/Python
#%description examples
#Examples for jabberpy python module

%prep
%setup
#%__perl -pi -e 's|^#!.*python2|#!%__python|' examples/*.py

%build
%python_build

%install
#mkdir -p %buildroot%_datadir/%module_name
#cp -r examples %buildroot%_datadir/%module_name
%python_install

%files
%doc README
%python_sitelibdir/jabber*

#%files examples
#%_datadir/%module_name

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.0-alt6.1
- Rebuild with Python-2.7

* Sat Dec 26 2009 Denis Klimov <zver@altlinux.org> 0.5.0-alt6
- comment perl command on examples

* Sat Dec 26 2009 Denis Klimov <zver@altlinux.org> 0.5.0-alt5
- fix DeprecationWarning for sha

* Sat Nov 21 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt4.1
- Rebuilt with python 2.6

* Sat Nov 21 2009 Denis Klimov <zver@altlinux.org> 0.5.0-alt4
- add missing jabber/__init__.py
- fix version in setup.py

* Sat Nov 21 2009 Denis Klimov <zver@altlinux.org> 0.5.0-alt3
- comment examples subpackage. It have unmet dependcies.

* Sat Nov 21 2009 Denis Klimov <zver@altlinux.org> 0.5.0-alt2
- add examples subpackage

* Fri Nov 20 2009 Denis Klimov <zver@altlinux.org> 0.5.0-alt1
- new version
- remove needless -q and -n params from setup macro
- use python macros

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 0.4-alt3.1
- Rebuilt with python-2.5.

* Mon Oct 06 2003 Mikhail Zabaluev <mhz@altlinux.ru> 0.4-alt3
- Replaced python to python-devel in BuildRequires

* Thu Mar 13 2003 Mikhail Zabaluev <mhz@altlinux.ru> 0.4-alt2
- Patch0: graceful disconnect

* Thu Feb 27 2003 Mikhail Zabaluev <mhz@altlinux.ru> 0.4-alt1
- 0.4
- Patches have gone upstream

* Sat Aug 24 2002 Mikhail Zabaluev <mhz@altlinux.ru> 0.3-alt5
- Enhanced auth patch

* Fri Aug 23 2002 Mikhail Zabaluev <mhz@altlinux.ru> 0.3-alt4
- Replace references to python2 binary in Python scripts

* Fri Aug 23 2002 Mikhail Zabaluev <mhz@altlinux.ru> 0.3-alt3
- Eliminated sleep(1) on disconnect

* Thu Aug 15 2002 Mikhail Zabaluev <mhz@altlinux.ru> 0.3-alt2
- Patched the faulty auth method
- Make the log method flush

* Wed May 29 2002 Mikhail Zabaluev <mhz@altlinux.ru> 0.3-alt1
- Initial release
