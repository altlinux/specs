%define module_name scapy
Name:		scapy
Summary:	Scapy is a powerful interactive packet manipulation program written in Python
Version:	2.1.0
Release:	alt1.1
Group:		Networking/Other
License:	GPL3
URL:		http://www.secdev.org/projects/scapy/	
Source:		%name-%version.tar.gz
BuildArch: 	noarch
Requires:	python >= 2.5

# Automatically added by buildreq on Thu Oct 16 2008 (-bi)
BuildRequires: python-devel python-module-setuptools

%description
Scapy is a powerful interactive packet manipulation program.
It is able to forge or decode packets of a wide number of protocols,
send them on the wire, capture them, match requests and replies, and
much more.
It can easily handle most classical tasks like scanning, tracerouting,
probing, unit tests, attacks or network discovery.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%_bindir/*scapy
%_man1dir/*
%python_sitelibdir/%name
%exclude %python_sitelibdir/%name/arch/windows

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.1.0-alt1.1
- Rebuild with Python-2.7

* Tue Aug 30 2011 Denis Klimov <zver@altlinux.org> 2.1.0-alt1
- new version
- using python macros in build and install sections
- format description

* Thu Dec 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0.10-alt1.1
- Rebuilt with python 2.6

* Thu Oct 16 2008 Mikhail Pokidko <pma@altlinux.org> 2.0.0.10-alt1
- Migrating to version 2.0.0.10

* Fri Apr 25 2008 Mikhail Pokidko <pma@altlinux.org> 1.1.1-alt1
- Initial ALT build

