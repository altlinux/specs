%define oname pcap

Name: python3-module-%oname
Epoch: 1
Version: 1.3.0
Release: alt1

Summary: Simplified object-oriented Python extension module for libpcap
License: BSD
Group: Development/Python3
Url: https://github.com/hellais/pypcap

# https://github.com/hellais/pypcap.git
Source: %name-%version.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: libpcap-devel


%description
PyPcap is simplified object-oriented Python extension module for libpcap
- the current tcpdump.org version, the legacy version shipping with some
of the BSD operating systems

%prep
%setup

%build
%__python3 setup.py config
%python3_build
%__python3 setup.py build

%install
%python3_install

%files
%doc Changelog.md LICENSE README.rst
%python3_sitelibdir/*


%changelog
* Thu Dec 15 2022 Grigory Ustinov <grenka@altlinux.org> 1:1.3.0-alt1
- Automatically updated to 1.3.0.

* Mon Jan 25 2021 Grigory Ustinov <grenka@altlinux.org> 1:1.2.3-alt1
- Automatically updated to 1.2.3.

* Mon Feb 10 2020 Andrey Bychkov <mrdrew@altlinux.org> 1:1.2.2-alt2
- Build for python2 disabled.

* Thu Apr 11 2019 Grigory Ustinov <grenka@altlinux.org> 1:1.2.2-alt1
- Build new version for python3.7.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1:1.1.6-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Wed Aug 23 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1:1.1.6-alt1
- Updated to upstream version 1.1.6.
- Enabled python3 build.

* Tue Mar 24 2015 Fr. Br. George <george@altlinux.ru> 1.1.1-alt1
- Autobuild version bump to 1.1.1
- Fix build
- Rename module as it provides python2.7(pcap), not pypcap

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1-alt2.1
- Rebuild with Python-2.7

* Thu Aug 26 2010 Fr. Br. George <george@altlinux.ru> 1.1-alt2
- Fix build

* Sat Nov 21 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1.1
- Rebuilt with python 2.6

* Sat Jan 10 2009 Fr. Br. George <george@altlinux.ru> 1.1-alt1
- Initial build from scratch

