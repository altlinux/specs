%setup_python_module pysnmp
Summary: Python SNMP Toolkit
Name: %packagename
Version: 4.3.2
Release: alt1
URL: http://sourceforge.net/projects/pysnmp/
Source: https://pypi.python.org/packages/9e/77/795fcc9d9a01adcb6175a3bf6532132addb8904922afd7877a9930d89f2f/pysnmp-%{version}.tar.gz
License: BSD
Group: Development/Python
Packager: Python Development Team <python at packages.altlinux.org>
BuildArch: noarch

%description
This is a Python implementation of SNMP v.1/v.2c engine. Its general
functionality is to assemble/disassemble SNMP messages from/into
given SNMP Object IDs along with associated values. PySNMP also provides
a few transport methods specific to TCP/IP networking.

PySNMP is written entirely in Python and is self-sufficient in terms
that it does not rely on any third party tool (it is not a wrapper!).

%prep
%setup -q -n %modulename-%version

%build
env CFLAGS="%optflags" python setup.py build

%install
%python_install \
        --optimize=2 \
        --record=INSTALLED_FILES
	
%clean

%files -f INSTALLED_FILES
%defattr(-,root,root)
%doc CHANGES* LICENSE* README* TODO*
%doc docs examples

%changelog
* Sat Dec 31 2016 Igor Vlasenko <viy@altlinux.ru> 4.3.2-alt1
- automated PyPI update

* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.4.3-alt2.1
- Rebuild with Python-2.7

* Sat Nov 21 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.3-alt2
- Rebuilt with python 2.6

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 3.4.3-alt1.1
- Rebuilt with python-2.5.

* Fri May  6 2005 Konstantin Klimchev <koka@altlinux.ru> 3.4.3-alt1
- new 3.4.3
- python2.4

* Mon Aug 23 2004 Konstantin Klimchev <koka@altlinux.ru> 3.4.2-alt1
- initial build for Sisyphus
