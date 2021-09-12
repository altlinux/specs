%define oname bencode.py
%define modulename bencodepy

Name: python3-module-bencode
Version: 4.0.0
Release: alt1

Summary: The BitTorrent bencode module as light-weight, standalone package

Group: Development/Python
License: LGPLv2+
Url: http://pypi.python.org/pypi/bencode.py

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-intro >= 2.2.5
BuildRequires(pre): rpm-build-python3

BuildRequires: python3-module-setuptools

%py3_use pbr >= 1.9

Provides: python3-module-%oname = %EVR
Provides: python3-module-%modulename = %EVR

%description
This package simply re-packages the existing bencoding and bdecoding
implemention from the 'official' BitTorrent client as a separate,
leight-weight package for re-using them without having the entire
BitTorrent software as a dependency.

Forked from the bencode package by Thomas Rampelberg.


%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/bencode/
%python3_sitelibdir/%modulename/
%python3_sitelibdir/%{oname}*.egg-info

%changelog
* Sun Sep 12 2021 Vitaly Lipatov <lav@altlinux.ru> 4.0.0-alt1
- new version 4.0.0 (with rpmrb script)
- cleanup spec

* Thu Jun 20 2019 Vitaly Lipatov <lav@altlinux.ru> 2.1.0-alt1
- new version 2.1.0, switch to fork bencode.py
- build python3 only module

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1.qa1
- NMU: applied repocop patch

* Mon Oct 07 2013 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt1
- initial build for ALT Linux Sisyphus
