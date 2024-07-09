%define pypi_name jsonschema

%def_with check

Name: python3-module-%pypi_name
Version: 4.23.0
Release: alt1

Summary: An implementation of JSON Schema validation for Python

License: MIT
Group: Development/Python3
URL: https://pypi.org/project/jsonschema
VCS: https://github.com/python-jsonschema/jsonschema
BuildArch: noarch
Source0: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hatchling
BuildRequires: python3-module-hatch-fancy-pypi-readme
BuildRequires: python3-module-hatch-vcs
%if_with check
BuildRequires: python3-module-attrs
BuildRequires: python3-module-jsonschema-specifications
BuildRequires: python3-module-referencing
BuildRequires: python3-module-rpds-py
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pip
%endif

# https://bugzilla.altlinux.org/38673
Conflicts: python-module-jsonschema < 2.6.0-alt3

%description
jsonschema is an implementation of the JSON Schema specification for Python.

%prep
%setup

%build
if [ ! -d .git ]; then
    git init
    git config user.email Julian@GrayVines.com
    git config user.name Julian Berman
    git add .
    git commit -m 'release'
    git tag '%version'
fi
%pyproject_build

%install
%pyproject_install
rm -rfv %buildroot%python3_sitelibdir/%pypi_name/benchmarks/
rm -rfv %buildroot%python3_sitelibdir/%pypi_name/tests/

%check
export JSON_SCHEMA_TEST_SUITE=$PWD/json
%pyproject_run_pytest -v jsonschema

%files
%doc *.rst COPYING
%_bindir/%pypi_name
%python3_sitelibdir/%pypi_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Jul 09 2024 Anton Vyatkin <toni@altlinux.org> 4.23.0-alt1
- New version 4.23.0.

* Thu May 16 2024 Anton Vyatkin <toni@altlinux.org> 4.22.0-alt1
- New version 4.22.0.

* Sun Jan 21 2024 Anton Vyatkin <toni@altlinux.org> 4.21.1-alt1
- New version 4.21.1.

* Tue Oct 31 2023 Anton Vyatkin <toni@altlinux.org> 4.19.2-alt1
- New version 4.19.2.

* Thu Sep 21 2023 Anton Vyatkin <toni@altlinux.org> 4.19.1-alt1
- New version 4.19.1.

* Tue Aug 08 2023 Anton Vyatkin <toni@altlinux.org> 4.19.0-alt1
- New version 4.19.0.

* Thu Aug 03 2023 Anton Vyatkin <toni@altlinux.org> 4.18.6-alt1
- new version 4.18.6

* Tue Jul 18 2023 Anton Vyatkin <toni@altlinux.org> 4.18.4-alt1
- new version 4.18.4

* Sat Jul 15 2023 Anton Vyatkin <toni@altlinux.org> 4.18.3-alt1
- new version 4.18.3

* Mon Jan 23 2023 Stanislav Levin <slev@altlinux.org> 4.17.3-alt2
- Shipped required core files (closes: #45008).

* Tue Jan 10 2023 Vladimir Didenko <cow@altlinux.org> 4.17.3-alt1
- New version

* Tue Nov 29 2022 Vladimir Didenko <cow@altlinux.org> 4.17.1-alt1
- New version

* Fri Oct 07 2022 Vladimir Didenko <cow@altlinux.org> 4.16.0-alt1
- New version

* Mon Sep 05 2022 Vladimir Didenko <cow@altlinux.org> 4.15.0-alt1
- New version

* Fri May 06 2022 Vladimir Didenko <cow@altlinux.org> 4.5.1-alt1
- Updated to upstream release 4.5.1
- Disable tests run (running tests using nose is broken)

* Mon Aug 23 2021 Vitaly Lipatov <lav@altlinux.ru> 3.2.0-alt4
- add Conflicts to old python-module-jsonschema (ALT bug 38673)

* Thu Nov 12 2020 Vitaly Lipatov <lav@altlinux.ru> 3.2.0-alt3
- use python3-module-twisted-core-tests for tests
- cleanup spec: add URL for tarball, don't pack sources to gz
- disable tests packing

* Fri Oct 30 2020 Vitaly Lipatov <lav@altlinux.ru> 3.2.0-alt2
- NMU: drop benchmarks packing

* Fri Jul 03 2020 Vladimir Didenko <cow@altlinux.org> 3.2.0-alt1
- Updated to upstream release 3.2.0
- Build python3 version as separate package

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.6.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Aug 01 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.6.0-alt1
- Updated to upstream release 2.6.0.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.5.1-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jul 29 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.1-alt1
- Version 2.5.1

* Fri Oct 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.0-alt1
- Version 2.4.0
- Added module for Python 3

* Thu Sep 13 2012 Pavel Shilovsky <piastry@altlinux.org> 0.2-alt1
- Initial release for Sisyphus (based on Fedora)
