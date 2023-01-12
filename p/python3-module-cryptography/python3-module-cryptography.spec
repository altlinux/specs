%define oname cryptography

%def_disable test

Name: python3-module-%oname
Version: 39.0.0
Release: alt1

Summary: Cryptographic recipes and primitives to Python developers

License: Apache-2.0
Group: Development/Python3
Url: https://pypi.python.org/pypi/cryptography/

Packager: Vladimir Didenko <cow@altlinux.org>

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

# see gear/predownloaded-preinstall-hook
Source1: %name-development-%version.tar

BuildRequires(pre): rpm-build-intro >= 2.2.4
BuildRequires(pre): rpm-build-python3

BuildRequires: python3-devel python3-module-cffi python3-module-setuptools
BuildRequires: libssl-devel
BuildRequires: /proc
BuildRequires: rust rust-cargo python3-module-setuptools_rust
BuildRequires: python3-module-toml python3-module-semantic_version
BuildRequires: python3-module-asn1crypto >= 0.21.0
%if_enabled test
BuildRequires: python3-module-cryptography-vectors
BuildRequires: python3-module-pretend python3-module-iso8601 python3-module-pytz
BuildRequires: python3-module-pytest >= 3.9.3
BuildRequires: python3-module-hypothesis
%endif

%py3_requires cffi

%description
cryptography is a package which provides cryptographic recipes and primitives to Python developers.
Our goal is for it to be your "cryptographic standard library". cryptography includes both high level
recipes, and low level interfaces to common cryptographic algorithms such as symmetric ciphers, message
digests and key derivation functions.


%prep
%setup -a1

mkdir -p .cargo
cat >> .cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "src/rust/vendor"
EOF

%build
export CARGO_NET_OFFLINE=true
%python3_build

%install
%python3_install

%filter_from_requires /python3[(]cryptography.hazmat.bindings._commoncrypto[)]/d
%filter_from_requires /python3[(]cryptography.hazmat.bindings._constant_time[)]/d
%filter_from_requires /python3[(]cryptography.hazmat.bindings._openssl[)]/d
%filter_from_requires /python3[(]cryptography.hazmat.bindings._padding[)]/d
%filter_from_requires /python3[(]cryptography.hazmat.bindings._rust[)]/d

%if_enabled test
%check
py.test3
%endif


%files
%python3_sitelibdir/%oname/
%python3_sitelibdir/*.egg-*

%changelog
* Thu Jan 12 2023 Vladimir Didenko <cow@altlinux.ru> 39.0.0-alt1
- new version (39.0.0)

* Fri Sep 9 2022 Vladimir Didenko <cow@altlinux.ru> 38.0.1-alt1
- new version (38.0.1)

* Wed May 4 2022 Vladimir Didenko <cow@altlinux.ru> 37.0.2-alt1
- new version (37.0.2)

* Thu Dec 2 2021 Vladimir Didenko <cow@altlinux.ru> 36.0.0-alt1
- new version (36.0.0)

* Wed Oct 20 2021 Stanislav Levin <slev@altlinux.org> 35.0.0-alt2
- Backported fix for legacy PEM headers (#6340).

* Thu Sep 30 2021 Vladimir Didenko <cow@altlinux.ru> 35.0.0-alt1
- new version (35.0.0)

* Sun Apr 25 2021 Vitaly Lipatov <lav@altlinux.ru> 3.4.7-alt1
- new version (3.4.7) with rpmgs script (ALT bug 39889)
- update src/rust/vendor separately

* Thu Mar 4 2021 Vladimir Didenko <cow@altlinux.ru> 3.4.6-alt1
- new version (3.4.6)

* Tue Feb 9 2021 Vladimir Didenko <cow@altlinux.ru> 3.4.3-alt3
- use upstream fix for cyclic import error

* Tue Feb 9 2021 Vladimir Didenko <cow@altlinux.ru> 3.4.3-alt2
- fix cyclic import error

* Tue Feb 9 2021 Vladimir Didenko <cow@altlinux.ru> 3.4.3-alt1
- new version (closes: #39662)

* Mon Feb 8 2021 Vladimir Didenko <cow@altlinux.ru> 3.4.1-alt1
- new version (3.4.1)

* Wed Dec 9 2020 Vladimir Didenko <cow@altlinux.ru> 3.3.0-alt1
- new version (3.3.0)

* Mon Oct 28 2020 Vladimir Didenko <cow@altlinux.ru> 3.2.1-alt1
- new version (3.2.1)

* Mon Oct 26 2020 Vladimir Didenko <cow@altlinux.ru> 3.2-alt1
- new version (3.2)

* Wed Sep 9 2020 Vladimir Didenko <cow@altlinux.ru> 3.1-alt1
- new version (3.1)

* Mon Aug 03 2020 Stanislav Levin <slev@altlinux.org> 3.0-alt2
- Added missing runtime dependency on cffi.

* Tue Jul 21 2020 Vladimir Didenko <cow@altlinux.ru> 3.0-alt1
- new version (3.0)
- build Python 3 version as separate package

* Fri Apr 3 2020 Vladimir Didenko <cow@altlinux.ru> 2.9-alt1
- new version (2.9)
- re-enable tests

* Thu Jan 16 2020 Grigory Ustinov <grenka@altlinux.org> 2.8-alt2
- Bootstrap for python3.8.

* Thu Oct 17 2019 Vladimir Didenko <cow@altlinux.ru> 2.8-alt1
- new version (2.8)

* Tue Jun 04 2019 Vitaly Lipatov <lav@altlinux.ru> 2.7-alt1
- new version (2.7) with rpmgs script (ALT bug 36848)
- switch to build from tarball
- enable test

* Wed Mar 13 2019 Vladimir Didenko <cow@altlinux.ru> 2.6.1-alt1
- 2.6.1

* Fri Feb 15 2019 Vladimir Didenko <cow@altlinux.ru> 2.5.0-alt1
- 2.5.0

* Fri Nov 23 2018 Vladimir Didenko <cow@altlinux.ru> 2.4.2-alt1
- 2.4.2

* Wed Aug 29 2018 Grigory Ustinov <grenka@altlinux.org> 2.3.0-alt1.1
- NMU: Rebuild with new openssl 1.1.0.

* Wed Jul 18 2018 Vladimir Didenko <cow@altlinux.ru> 2.3.0-alt1
- 2.3.0

* Thu May 24 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.2.2-alt2
- NMU: fixed buildtime and runtime dependencies.

* Fri Apr 06 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.2.2-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Thu Apr 5 2018 Vladimir Didenko <cow@altlinux.ru> 2.2.2-alt1
- 2.2.2

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.1.4-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Dec 15 2017 Vladimir Didenko <cow@altlinux.ru> 2.1.4-alt1
- 2.1.4

* Wed Oct 18 2017 Vladimir Didenko <cow@altlinux.ru> 2.1.1-alt1
- 2.1.1

* Wed Jul 19 2017 Vladimir Didenko <cow@altlinux.ru> 2.0.0-alt1
- 2.0.0

* Thu Jun 8 2017 Vladimir Didenko <cow@altlinux.ru> 1.9.0-alt1
- 1.9.0

* Mon Mar 13 2017 Vladimir Didenko <cow@altlinux.ru> 1.8.1-alt1
- 1.8.1

* Fri Dec 16 2016 Vladimir Didenko <cow@altlinux.ru> 1.7.1-alt1
- 1.7.1

* Tue Nov 22 2016 Vladimir Didenko <cow@altlinux.ru> 1.6.0-alt1
- 1.6.0

* Tue Oct 18 2016 Vladimir Didenko <cow@altlinux.ru> 1.5.2-alt1
- 1.5.2

* Tue Aug 30 2016 Vladimir Didenko <cow@altlinux.ru> 1.5.0-alt1
- 1.5.0

* Thu Jun 9 2016 Vladimir Didenko <cow@altlinux.ru> 1.4.0-alt1
- 1.4.0

* Wed Mar 23 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3.1-alt1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Tue Mar 22 2016 Vladimir Didenko <cow@altlinux.ru> 1.3.1-alt1
- 1.3.1

* Mon Mar 21 2016 Vladimir Didenko <cow@altlinux.ru> 1.3.0-alt1
- 1.3.0

* Mon Mar 07 2016 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.2.3-alt1
- NMU: 1.2.1 -> 1.2.3 (fixes FTBFS).

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 1.2.1-alt1.1
- NMU: Use buildreq for BR.

* Sun Jan 10 2016 Vladimir Didenko <cow@altlinux.ru> 1.2.1-alt1
- 1.2.1

* Fri Oct 30 2015 Vladimir Didenko <cow@altlinux.ru> 1.1.0-alt1
- 1.1.0

* Sun Sep 27 2015 Vladimir Didenko <cow@altlinux.ru> 1.0.2-alt1
- 1.0.2

* Fri Sep 18 2015 Vladimir Didenko <cow@altlinux.ru> 1.0.1-alt2
- Add cffi to requirements (closes: #31280)

* Mon Sep 7 2015 Vladimir Didenko <cow@altlinux.ru> 1.0.1-alt1
- 1.0.1

* Wed Aug 12 2015 Vladimir Didenko <cow@altlinux.ru> 1.0.0-alt1
- 1.0.0

* Sun Jun 7 2015 Vladimir Didenko <cow@altlinux.ru> 0.9.1-alt1
- 0.9.1

* Sat Apr 11 2015 Vladimir Didenko <cow@altlinux.ru> 0.8.2-alt1
- 0.8.2

* Fri Mar 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0-alt2
- Added *.egg-info

* Tue Mar 10 2015 Vladimir Didenko <cow@altlinux.ru> 0.8.0-alt1
- 0.8.0

* Fri Jan 16 2015 Vladimir Didenko <cow@altlinux.ru> 0.7.2-alt1
- 0.7.2

* Mon Dec 29 2014 Vladimir Didenko <cow@altlinux.ru> 0.7.1-alt1
- 0.7.1

* Thu Dec 18 2014 Vladimir Didenko <cow@altlinux.ru> 0.7.0-alt1
- 0.7.0

* Thu Oct 16 2014 Vladimir Didenko <cow@altlinux.ru> 0.6.1-alt1
- 0.6.1

* Mon Oct 13 2014 Vladimir Didenko <cow@altlinux.ru> 0.6.0-alt1
- 0.6.0

* Thu Aug 21 2014 Vladimir Didenko <cow@altlinux.ru> 0.5.4-alt1
- 0.5.4

* Tue Jul 29 2014 Vladimir Didenko <cow@altlinux.ru> 0.5.2-alt1
- initial build for Sisyphus
