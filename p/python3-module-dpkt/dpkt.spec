%define oname dpkt
Name: python3-module-dpkt
Version: 1.9.8
Release: alt1

Summary: Fast, simple packet creation and parsing

License: BSD
Group: Development/Python3
Url: http://monkey.org/~dugsong/dpkt/

# Source-url: https://github.com/kbandla/dpkt/archive/v%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-intro
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pytest python3-module-pytest-cov

%description
Fast, simple packet creation / parsing, with definitions for the basic TCP/IP protocols.

%prep
%setup

%build
%python3_build

#epydoc -o doc -n dpkt -u %url --docformat=plaintext ./dpkt/

%install
%python3_install

%check
%python3_test
py.test3 -vv %oname || py.test3 -p no:warnings -vv %oname

%files
%doc docs AUTHORS LICENSE README* examples
%python3_sitelibdir/*

%changelog
* Sun Mar 12 2023 Vitaly Lipatov <lav@altlinux.ru> 1.9.8-alt1
- new version 1.9.8 (with rpmrb script)

* Mon Apr 04 2022 Vitaly Lipatov <lav@altlinux.ru> 1.9.7.2-alt1
- new version 1.9.7.2 (with rpmrb script)

* Thu Nov 05 2020 Vitaly Lipatov <lav@altlinux.ru> 1.9.4-alt1
- build python3 module separately

* Thu Nov 05 2020 Vitaly Lipatov <lav@altlinux.ru> 1.9.1-alt2
- NMU: fix build (drop pytest-cov requires)

* Tue Feb 20 2018 Fr. Br. George <george@altlinux.ru> 1.9.1-alt1
- Autobuild version bump to 1.9.1
- Build Python3 module

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.8.6-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Mar 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.6-alt1
- Version 1.8.6

* Mon Jun 10 2013 Fr. Br. George <george@altlinux.ru> 1.8-alt1
- Autobuild version bump to 1.8
- Fix docs build

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.7-alt1.1
- Rebuild with Python-2.7

* Thu Jul 28 2011 Fr. Br. George <george@altlinux.ru> 1.7-alt1
- Autobuild version bump to 1.7

* Thu Jul 28 2011 Fr. Br. George <george@altlinux.ru> 1.6-alt3
Clean up spec
New upstream URL

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6-alt2.1
- Rebuilt with python 2.6

* Wed Sep 23 2009 Fr. Br. George <george@altlinux.ru> 1.6-alt2
- Repocop bug fixed

* Sat Jan 10 2009 Fr. Br. George <george@altlinux.ru> 1.6-alt1
- Initial build from OpenSuSE

* Sun Jan 28 2007 - Cristian Rodriguez <judas_iscariote@shorewall.net>
- update to version 1.6
* Wed Sep 06 2006 - James Oakley <jfunk@funktronics.ca> - 1.5-1
- Initial release
