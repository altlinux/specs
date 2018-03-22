%define oname pcap
%def_with python3

Name: python-module-%oname
Epoch: 1
Version: 1.1.6
Release: alt1.1
Summary: Simplified object-oriented Python extension module for libpcap
Url: https://github.com/hellais/pypcap
License: BSD
Group: Development/Python

# https://github.com/hellais/pypcap.git
Source: %name-%version.tar.gz

BuildRequires: libpcap-devel
BuildRequires: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
%endif

Provides: python-module-pypcap = %EVR
Conflicts: python-module-pypcap < %EVR
Obsoletes: python-module-pypcap
Provides: python-module-kbandla-pypcap = %EVR
Obsoletes: python-module-kbandla-pypcap

%description
PyPcap is simplified object-oriented Python extension module for libpcap
- the current tcpdump.org version, the legacy version shipping with some
of the BSD operating systems

%if_with python3
%package -n python3-module-%oname
Group: Development/Python3
Summary:        Simplified object-oriented Python extension module for libpcap

%description -n python3-module-%oname
PyPcap is simplified object-oriented Python extension module for libpcap
- the current tcpdump.org version, the legacy version shipping with some
of the BSD operating systems
%endif

%prep
%setup

%if_with python3
cp -a . ../python3
%endif

%build
python setup.py config
%python_build
python setup.py build

%if_with python3
pushd ../python3
python3 setup.py config
%python3_build
python3 setup.py build
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc Changelog.md LICENSE README.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc Changelog.md LICENSE README.rst
%python3_sitelibdir/*
%endif

%changelog
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

