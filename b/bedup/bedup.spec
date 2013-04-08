Name: bedup
Version: 0.0.8
Release: alt1

Summary: Deduplication for Btrfs

Packager: Vitaly Lipatov <lav@altlinux.ru>

Url: https://github.com/g2p/bedup
License: GPLv2
Group: File tools

# https://github.com/g2p/bedup.git
Source: %name-%version.tar

BuildRequires: python-dev python-module-cffi python-module-pycparser python-module-distribute

%description
bedup looks for new and changed files, making sure that multiple copies
of identical files share space on disk. It integrates deeply with btrfs
so that scans are incremental and low-impact.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%_bindir/%name
%python_sitelibdir/%name/
%python_sitelibdir/%name-%version-*.egg-info

%changelog
* Mon Apr 08 2013 Vitaly Lipatov <lav@altlinux.ru> 0.0.8-alt1
- initial build for ALT Linux Sisyphus
