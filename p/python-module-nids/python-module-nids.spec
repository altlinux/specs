%define packagename python-module-nids

Summary: Python wrapper for libnids (Network Intrusion Detection System)
Name: %packagename
Version: 0.5
Release: alt1.1.1.1
Source0: pynids-%version.tar.gz
Patch: pynids.alt.patch
License: GPL
Group: Development/Python
URL: http://pilcrow.madison.wi.us/pynids/
Packager: Mikhail Pokidko <pma@altlinux.org>
#BuildArch: noarch

Requires: libnids libnet2 libpcap0.8
BuildRequires: libnids-devel python-module-setuptools

%description
pynids is a python wrapper for libnids, a Network Intrusion Detection System
library offering sniffing, IP defragmentation, TCP stream reassembly and TCP
port scan detection. Let your own python routines examine (or kill) network
conversations.

%prep
%setup  -q -n pynids-%version
%patch -p1

%build
%__python setup.py build

%install
%__python setup.py install --root=%buildroot --optimize=2 --record=INSTALLED_FILES

%files -f INSTALLED_FILES

%changelog
* Mon Apr 16 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5-alt1.1.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5-alt1.1.1
- Rebuild with Python-2.7

* Sat Nov 21 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1.1
- Rebuilt with python 2.6

* Sat Apr 05 2008 Mikhail Pokidko <pma@altlinux.org> 0.5-alt1
- Initial ALT build

