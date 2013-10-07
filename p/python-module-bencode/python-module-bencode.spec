%define modulename bencode

Name: python-module-bencode
Version: 1.0
Release: alt1

Summary: The BitTorrent bencode module as light-weight, standalone package.

Group: Development/Python
License: LGPLv2+
Url: http://pypi.python.org/pypi/%modulename/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pypi.python.org/packages/source/b/%modulename/%modulename-%version.tar

BuildArch: noarch

%setup_python_module %modulename

BuildRequires: python-dev python-module-distribute

%description
This package simply re-packages the existing bencoding and bdecoding
implemention from the 'official' BitTorrent client as a separate,
leight-weight package for re-using them without having the entire
BitTorrent software as a dependency.

%prep
%setup -n %modulename-%version

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/%modulename/
%python_sitelibdir/%modulename-%version-*.egg-info

%changelog
* Mon Oct 07 2013 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt1
- initial build for ALT Linux Sisyphus
