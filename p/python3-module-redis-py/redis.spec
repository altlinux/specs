%define _unpackaged_files_terminate_build 1
%define pypi_name redis
%define mod_name %pypi_name

Name: python3-module-redis-py
Version: 4.5.5
Release: alt1.1
Summary: Python client for Redis database and key-value store
License: MIT
Group: Development/Python3
URL: https://pypi.org/project/redis/
Vcs: https://github.com/redis/redis-py
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch:  reimplementation_of_strtobool_function.patch
%pyproject_runtimedeps_metadata
# mapping from PyPI name
Provides: python3-module-%{pep503_name %pypi_name} = %EVR
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%description
%summary.

%prep
%setup
%patch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%files
%doc CHANGES README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
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
