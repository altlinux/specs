Summary: Pre-compiled MIB modules for PySNMP
Name: python-module-pysnmp-mibs
Version: 0.0.9a
Release: alt1.1
%setup_python_module pysnmp-mibs
Url: http://pysnmp.sourceforge.net/
Source0: %modulename-%version.tar.gz
License: BSD
Group: Development/Python
Packager: Python Development Team <python at packages.altlinux.org>
BuildArch: noarch

%description
This is a set of pre-compiled MIB files for the PySNMP framework.

%prep
%setup  -q -n %modulename-%version

%build
env CFLAGS="%optflags" python setup.py build

%install
%python_install --optimize=2 --record=INSTALLED_FILES

%files -f INSTALLED_FILES

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.0.9a-alt1.1
- Rebuild with Python-2.7

* Tue Aug 03 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.9a-alt1
- Version 0.0.9a

* Sat Nov 21 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.5a-alt2
- Rebuilt with python 2.6

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 0.0.5a-alt1.1
- Rebuilt with python-2.5.

* Tue Oct 16 2007 Peter V. Saveliev <peet@altlinux.org> 0.0.5a-alt1
- initial build

