Name: bedup
Version: 0.10.1
Release: alt1.1

Summary: Deduplication for Btrfs

Packager: Vitaly Lipatov <lav@altlinux.ru>

Url: https://github.com/g2p/bedup
License: GPLv2
Group: File tools

# Source-git: https://github.com/g2p/bedup.git
Source: %name-%version.tar

BuildPreReq: rpm-build-python3

BuildRequires: python3-dev python3-module-pycparser python3-module-distribute
BuildRequires: python3-module-cffi >= 0.4.2

Requires: python3-module-pycparser python3-module-markupsafe python3-modules-sqlite3

# pkg_resources.DistributionNotFound: The 'python-editor>=0.3' distribution was not found and is required by alembic
Requires: python3-module-editor

%description
bedup looks for new and changed files, making sure that multiple copies
of identical files share space on disk. It integrates deeply with btrfs
so that scans are incremental and low-impact.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%_bindir/%name
%python3_sitelibdir/%name/
%python3_sitelibdir/%name-%version-*.egg-info

%changelog
* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.10.1-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Tue Aug 09 2016 Vitaly Lipatov <lav@altlinux.ru> 0.10.1-alt1
- build new bugfix version

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.10.0-alt1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Oct 29 2015 Vitaly Lipatov <lav@altlinux.ru> 0.10.0-alt1
- new version, use python3
- fix requires (ALT bug #31380)

* Mon Apr 29 2013 Vitaly Lipatov <lav@altlinux.ru> 0.9.0-alt1
- new version
- fix requires

* Mon Apr 08 2013 Vitaly Lipatov <lav@altlinux.ru> 0.0.8-alt1
- initial build for ALT Linux Sisyphus
