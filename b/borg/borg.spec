Name: borg
Version: 1.2.4
Release: alt1

Summary: Deduplicating backup program with compression and authenticated encryption

License: BSD-3-Clause
Group: File tools
Url: https://borgbackup.github.io/borgbackup/

# Source-url: https://github.com/borgbackup/borg/archive/%version.tar.gz
Source: %name-%version.tar
Patch1: borg-unbundle-xxhash-1.1.10.patch

BuildRequires(pre): rpm-build-python3

BuildRequires: gcc-c++
BuildRequires: libacl-devel ipython3 python3-module-Cython libssl-devel python3-dev
BuildRequires: python3-module-setuptools-wheel python3-module-setuptools_scm python3-module-pytest python3-module-msgpack python3-module-pkgconfig
BuildRequires: liblz4-devel libzstd-devel libb2-devel libxxhash-devel

Requires: python3-module-zmq python3-module-msgpack

%description
BorgBackup (short: Borg) is a deduplicating backup program.
Optionally, it supports compression and authenticated encryption.

The main goal of Borg is to provide an efficient and secure way to backup data.
The data deduplication technique used makes Borg suitable for daily backups
since only changes are stored.

The authenticated encryption technique makes it suitable for backups to not
fully trusted targets.

%prep
%setup
#patch1 -p1

#rm -rfv src/borg/algorithms/{lz4,xxh64,zstd,blake2}/
#rm -rfv src/borg/algorithms/{lz4,zstd,blake2}/

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
export BORG_OPENSSL_PREFIX="/usr/include/openssl"
#pyproject_build
%python3_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
export BORG_OPENSSL_PREFIX="/usr/include/openssl"
#pyproject_install
%python3_install

%check
export LANG=en_US.UTF-8
#export PYTHONPATH="$(pwd)/build/lib.linux-$(uname -m)-%__python3_version"
export PYTHONVER="%__python3_version"
export PYTHONPATH="$(pwd)/build/lib.linux-$(uname -m)-cpython-${PYTHONVER//./}"

# copy missing files
cp -a src/borg/testsuite/attic.tar.gz $PYTHONPATH/borg/testsuite/
cp -a src/borg/paperkey.html $PYTHONPATH/borg

TEST_SELECTOR="not test_fuse and not test_readonly_mount and not benchmark"
py.test-3 -x -vk "$TEST_SELECTOR" $PYTHONPATH/borg/testsuite/*.py

%files
%doc LICENSE AUTHORS CHANGES.rst README.rst
%_bindir/borg
%_bindir/borgfs
%python3_sitelibdir/borg/
%python3_sitelibdir/borgbackup-*.egg-info/


%changelog
* Sat Apr 01 2023 Dmitriy D. Shadrinov <shadrinov@altlinux.org> 1.2.4-alt1
- 1.2.4 release

* Mon Aug 22 2022 Dmitry D. Shadrinov <shadrinov@altlinux.org> 1.2.2-alt1
- 1.2.2 release

* Tue Aug 02 2022 Dmitriy D. Shadrinov <shadrinov@altlinux.org> 1.2.1-alt1
- 1.2.1 release

* Fri May 13 2022 Dmitriy D. Shadrinov <shadrinov@altlinux.org> 1.2.0-alt3
- python3-module-msgpack requires added

* Mon Apr 25 2022 Dmitriy D. Shadrinov <shadrinov@altlinux.org> 1.2.0-alt2
- rebuild with system liblz4, libzstd, libxxhash

* Fri Apr 08 2022 Dmitriy D. Shadrinov <shadrinov@altlinux.org> 1.2.0-alt1
- 1.2.0 release

* Wed Dec 01 2021 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.1.17-alt3
- enabled tests

* Wed Sep 15 2021 Dmitriy D. Shadrinov <shadrinov@altlinux.org> 1.1.17-alt2
- build with bundled xxhash

* Sat Jul 17 2021 Dmitriy D. Shadrinov <shadrinov@altlinux.org> 1.1.17-alt1
- 1.1.17 release

* Fri Dec 25 2020 Dmitriy D. Shadrinov <shadrinov@altlinux.org> 1.1.15-alt1
- 1.1.15 release

* Fri Dec 04 2020 Dmitriy D. Shadrinov <shadrinov@altlinux.org> 1.1.14-alt3
- restored selftest.py and testsuite module

* Thu Dec 03 2020 Dmitriy D. Shadrinov <shadrinov@altlinux.org> 1.1.14-alt2
- removed unittest selftest.py

* Sun Nov 01 2020 Dmitriy D. Shadrinov <shadrinov@altlinux.org> 1.1.14-alt1
- 1.1.14 release

* Fri Oct 30 2020 Vitaly Lipatov <lav@altlinux.ru> 1.1.13-alt2
- NMU: don't pack testsuite

* Thu Jun 11 2020 Dmitriy D. Shadrinov <shadrinov@altlinux.org> 1.1.13-alt1
- 1.1.13 release

* Fri Mar 27 2020 Dmitriy D. Shadrinov <shadrinov@altlinux.org> 1.1.11-alt1
- update version to 1.1.11

* Sun Oct 20 2019 Vitaly Lipatov <lav@altlinux.ru> 1.1.10-alt2
- remove source code of the bundled libraries
- build with external blake2
- build with external xxhash (ALT bug 36408)

* Wed Jun 05 2019 Vitaly Lipatov <lav@altlinux.ru> 1.1.10-alt1
- borgbackup 1.1.10 bug fix release (now bundling msgpack)
- gcc-c++ used

* Sun Mar 31 2019 Dmitriy D. Shadrinov <shadrinov@altlinux.org> 1.1.9-alt2
- rebuilder with external libzstd

* Sun Feb 24 2019 Dmitriy D. Shadrinov <shadrinov@altlinux.org> 1.1.9-alt1
- update version to 1.1.9

* Tue Dec 25 2018 Dmitriy D. Shadrinov <shadrinov@altlinux.org> 1.1.8-alt1
- update version to 1.1.8

* Wed Aug 29 2018 Grigory Ustinov <grenka@altlinux.org> 1.1.7-alt1.1
- NMU: Rebuild with new openssl 1.1.0.

* Tue Aug 14 2018 Dmitriy D. Shadrinov <shadrinov@altlinux.org> 1.1.7-alt1
- update version to 1.1.7

* Thu Jun 14 2018 Dmitriy D. Shadrinov <shadrinov@altlinux.org> 1.1.6-alt1
- update version to 1.1.6

* Mon May 21 2018 Dmitriy D. Shadrinov <shadrinov@altlinux.org> 1.1.5-alt1
- update version to 1.1.5

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.4-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Fri Jan 12 2018 Dmitriy D. Shadrinov <shadrinov@altlinux.org> 1.1.4-alt1
- update version to 1.1.4

* Thu Dec 07 2017 Dmitriy D. Shadrinov <shadrinov@altlinux.org> 1.1.3-alt1
- update version to 1.1.3

* Fri Nov 17 2017 Dmitriy D. Shadrinov <shadrinov@altlinux.org> 1.1.2-alt1
- update version to 1.1.2

* Mon Oct 30 2017 Dmitriy D. Shadrinov <shadrinov@altlinux.org> 1.1.1-alt1
- update version to 1.1.1

* Sat Oct 14 2017 Dmitriy D. Shadrinov <shadrinov@altlinux.org> 1.1.0-alt2
- update version to 1.1.0

* Tue Oct 03 2017 Dmitriy D. Shadrinov <shadrinov@altlinux.org> 1.1.0-alt1.rc4
- update version to 1.1.0rc4

* Tue Sep 19 2017 Dmitriy D. Shadrinov <shadrinov@altlinux.org> 1.1.0-alt1.rc3
- update version to 1.1.0rc3

* Mon Aug 28 2017 Dmitriy D. Shadrinov <shadrinov@altlinux.org> 1.1.0-alt1.rc2
- update version to 1.1.0rc2

* Tue Aug 15 2017 Dmitriy D. Shadrinov <shadrinov@altlinux.org> 1.1.0-alt1.rc1
- update version to 1.1.0rc1

* Fri Aug 05 2016 Vitaly Lipatov <lav@altlinux.ru> 1.0.6-alt1
- new version 1.0.6 (with rpmrb script)

* Tue Jul 26 2016 Vitaly Lipatov <lav@altlinux.ru> 1.0.5-alt1
- new version 1.0.5 (with rpmrb script)

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.24.0-alt1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Fri Aug 14 2015 Vitaly Lipatov <lav@altlinux.ru> 0.24.0-alt1
- initial build for ALT Linux Sisyphus
