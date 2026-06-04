%define _unpackaged_files_terminate_build 1
%define pypi_name redis
%define mod_name %pypi_name

Name: python3-module-redis-py
Version: 8.0.0
Release: alt1
Summary: Python client for Redis database and key-value store
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/redis/
Vcs: https://github.com/redis/redis-py
BuildArch: noarch
Source: %name-%version.tar
# mapping from PyPI name
Provides: python3-module-%{pep503_name %pypi_name} = %EVR

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hatchling

%add_python3_req_skip pybreaker

%description
%summary.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Jun 02 2026 Egor Ignatov <egori@altlinux.org> 8.0.0-alt1
- New version 8.0.0.

* Sat Mar 28 2026 Grigory Ustinov <grenka@altlinux.org> 7.4.0-alt1.1
- Demodernized packaging.

* Wed Mar 25 2026 Stanislav Levin <slev@altlinux.org> 7.4.0-alt1
- 7.3.0 -> 7.4.0.

* Tue Mar 10 2026 Stanislav Levin <slev@altlinux.org> 7.3.0-alt1
- 7.2.1 -> 7.3.0.

* Tue Mar 03 2026 Stanislav Levin <slev@altlinux.org> 7.2.1-alt1
- 7.2.0 -> 7.2.1.

* Tue Feb 17 2026 Stanislav Levin <slev@altlinux.org> 7.2.0-alt1
- 7.1.1 -> 7.2.0.

* Tue Feb 10 2026 Stanislav Levin <slev@altlinux.org> 7.1.1-alt1
- 7.1.0 -> 7.1.1.

* Thu Nov 27 2025 Stanislav Levin <slev@altlinux.org> 7.1.0-alt1
- 7.0.1 -> 7.1.0.

* Tue Oct 28 2025 Stanislav Levin <slev@altlinux.org> 7.0.1-alt1
- 6.4.0 -> 7.0.1.

* Fri Aug 08 2025 Stanislav Levin <slev@altlinux.org> 6.4.0-alt1
- 6.3.0 -> 6.4.0.

* Wed Aug 06 2025 Stanislav Levin <slev@altlinux.org> 6.3.0-alt1
- 6.2.0 -> 6.3.0.

* Tue Jun 17 2025 Stanislav Levin <slev@altlinux.org> 6.2.0-alt1
- 4.5.5 -> 6.2.0.

* Sat Oct 21 2023 Grigory Ustinov <grenka@altlinux.org> 4.5.5-alt1.1
- Dropped dependency on distutils.

* Wed May 10 2023 Stanislav Levin <slev@altlinux.org> 4.5.5-alt1
- 3.4.1 -> 4.5.5.

* Mon Jul 26 2021 Grigory Ustinov <grenka@altlinux.org> 3.4.1-alt2
- drop python2 support

* Tue Mar 24 2020 Vladimir Didenko <cow@altlinux.org> 3.4.1-alt1
- new version
- fix license name

* Mon Oct 28 2019 Vladimir Didenko <cow@altlinux.org> 3.3.11-alt1
- new version

* Wed Oct 2 2019 Vladimir Didenko <cow@altlinux.org> 3.3.8-alt1
- new version

* Fri Sep 27 2019 Vladimir Didenko <cow@altlinux.org> 3.3.7-alt1
- new version

* Thu Mar 21 2019 Vladimir Didenko <cow@altlinux.org> 3.2.1-alt1
- new version

* Thu Nov 29 2018 Vladimir Didenko <cow@altlinux.org> 3.0.1-alt1
- new version

* Wed Mar 14 2018 Vladimir Didenko <cow@altlinux.org> 2.10.6-alt1
- new version

* Mon Jul 25 2016 Vladimir Didenko <cow@altlinux.org> 2.10.5-alt1
- new version

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.10.3-alt2.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.10.3-alt2.1
- NMU: Use buildreq for BR.

* Tue Feb 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.10.3-alt2
- Don't exclude .egg-info

* Fri Nov 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.10.3-alt1
- Version 2.10.3

* Mon Jun 23 2014 Vladimir Didenko <cow@altlinux.org> 2.10.1-alt1
- new version
- python 3 support

* Tue Aug 14 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 2.6.0-alt1
- new version

* Sat May 19 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 2.4.13-alt1
- build for ALT
