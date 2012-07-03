Summary: SNMP v1/v2c/v3 engine
Name: python-module-pysnmp4
Version: 4.1.14a
Release: alt3.1
%setup_python_module pysnmp
Url: http://pysnmp.sourceforge.net/
Source0: %modulename-%version.tar.gz
License: BSD
Group: Development/Python
Packager: Python Development Team <python at packages.altlinux.org>
BuildArch: noarch
Conflicts: python-module-pysnmp

%description
This is an alpha-quality revision of pure-Python, open source and free
implementation of v1/v2c/v3 SNMP engine.

%prep
%setup -n %modulename-%version

%build
env CFLAGS="%optflags" python setup.py build

%install
%python_install --optimize=2 --record=INSTALLED_FILES

%files -f INSTALLED_FILES

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 4.1.14a-alt3.1
- Rebuild with Python-2.7

* Wed Aug 04 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.14a-alt3
- Added explicit conflict with python-module-pysnmp

* Tue Aug 03 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.14a-alt2
- Added url

* Tue Aug 03 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.14a-alt1
- Version 4.1.14a

* Sat Nov 21 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.8a-alt2
- Rebuilt with python 2.6

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 4.1.8a-alt1.1
- Rebuilt with python-2.5.

* Tue Oct 16 2007 Peter V. Saveliev <peet@altlinux.org> 4.1.8a-alt1
- initial build

