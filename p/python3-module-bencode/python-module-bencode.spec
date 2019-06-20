%define modulename bencode

Name: python3-module-bencode
Version: 2.1.0
Release: alt1

Summary: The BitTorrent bencode module as light-weight, standalone package

Group: Development/Python
License: LGPLv2+
Url: http://pypi.python.org/pypi/bencode.py

Packager: Vitaly Lipatov <lav@altlinux.ru>

#Source-url: http://pypi.python.org/packages/source/b/bencode.py/bencode.py-%version.tar
# Source-url: https://files.pythonhosted.org/packages/3d/cf/f4c737f89a66c8156e0aec627d82cb25154d5444e4cceee236d33a0c6923/bencode.py-2.1.0.tar.gz
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3 rpm-build-intro
BuildRequires: python3-module-setuptools

%py3_use pbr >= 1.9

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
%python3_sitelibdir/%modulename/
%python3_sitelibdir/%{modulename}*.egg-info

%changelog
* Thu Jun 20 2019 Vitaly Lipatov <lav@altlinux.ru> 2.1.0-alt1
- new version 2.1.0, switch to fork bencode.py
- build python3 only module

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1.qa1
- NMU: applied repocop patch

* Mon Oct 07 2013 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt1
- initial build for ALT Linux Sisyphus
