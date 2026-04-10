%define _unpackaged_files_terminate_build 1

%define pypi_name pysnmp
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 7.1.23
Release: alt1
Summary: Python library for SNMP
License: BSD-2-Clause
Group: Development/Python3
Url: https://pypi.org/project/pysnmp
Vcs: https://github.com/lextudio/pysnmp
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
# renamed from pysnmp4
Provides: python3-module-pysnmp4 = %EVR
Obsoletes: python3-module-pysnmp4 <= 4.4.12-alt1
# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
# not packaged
%add_pyproject_deps_check_filter pep8-naming
%add_pyproject_deps_check_filter pysmi
%add_pyproject_deps_check_filter bump2version
%pyproject_builddeps_metadata_extra dev
%endif

%description
This is a pure-Python, open source and free implementation of v1/v2c/v3 SNMP
engine.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
# skip tests requiring pysmi (not packaged) or internet, sort failures later
%pyproject_run_pytest -vra \
    --ignore tests/smi/manager/test_mib-tree-inspection.py \
    --ignore tests/smi/manager/test_configure-mib-viewer-and-resolve-pdu-varbinds.py \
    --ignore tests/hlapi/v3arch/asyncio/manager/cmdgen/test_v2c_bulkwalk.py \
    --ignore tests/hlapi/v1arch/asyncio/manager/cmdgen/test_v1arch_v1_get.py \
    --ignore tests/hlapi/v1arch/asyncio/manager/cmdgen/test_v1arch_v2c_bulk.py \
    --ignore tests/hlapi/v1arch/asyncio/manager/cmdgen/test_v1arch_v2c_bulkwalk.py \
    --ignore tests/hlapi/v3arch/asyncio/agent/ntforg/test_default-v1-trap.py \
    --ignore tests/hlapi/v3arch/asyncio/manager/cmdgen/test_custom_asn1_mib_search_path.py \
    --ignore tests/hlapi/v3arch/asyncio/manager/cmdgen/test_v1_get.py \
    --ignore tests/hlapi/v3arch/asyncio/agent/ntforg/test_v3-trap.py \
    --ignore tests/smi/manager/test_convert-between-pdu-varbinds-and-mib-objects.py \
    --deselect tests/hlapi/v1arch/asyncio/manager/cmdgen/test_v1arch_v1_set.py::test_v1_set_mac_address \

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Apr 10 2026 Stanislav Levin <slev@altlinux.org> 7.1.23-alt1
- 7.1.22 -> 7.1.23.

* Mon Oct 27 2025 Stanislav Levin <slev@altlinux.org> 7.1.22-alt1
- 7.1.21 -> 7.1.22.

* Thu Jun 19 2025 Stanislav Levin <slev@altlinux.org> 7.1.21-alt1
- 7.1.17 -> 7.1.21.

* Thu Mar 20 2025 Stanislav Levin <slev@altlinux.org> 7.1.17-alt1
- 7.1.16 -> 7.1.17.

* Mon Feb 24 2025 Stanislav Levin <slev@altlinux.org> 7.1.16-alt1
- 4.4.12 -> 7.1.16.

* Thu Jun 02 2022 Grigory Ustinov <grenka@altlinux.org> 4.4.12-alt1
- Build new version.

* Mon Jul 26 2021 Grigory Ustinov <grenka@altlinux.org> 4.4.9-alt2
- Drop python2 support.

* Mon Jun 03 2019 Vitaly Lipatov <lav@altlinux.ru> 4.4.9-alt1
- new version 4.4.9 (with rpmrb script)

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 4.3.1-alt1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.3.1-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Sergey Alembekov <rt@altlinux.ru> 4.3.1-alt1
- Build version 4.3.1

* Fri Mar 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.6-alt1.rc1
- Version 4.2.6rc1

* Mon Aug 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.5-alt1
- Version 4.2.5
- Added module for Python 3

* Mon Sep 09 2013 Alexey Shabalin <shaba@altlinux.ru> 4.2.4-alt1
- 4.2.4

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 4.1.14a-alt3.1
- Rebuild with Python-2.7

* Wed Aug 04 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.14a-alt3
- Added explicit conflict with python-module-pysnmp

* Tue Aug 03 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.14a-alt2
- Added url

* Tue Aug 03 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.14a-alt1
- Version 4.1.14a

* Sat Nov 21 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.8a-alt2
- Rebuilt with python 2.6

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 4.1.8a-alt1.1
- Rebuilt with python-2.5.

* Tue Oct 16 2007 Peter V. Saveliev <peet@altlinux.org> 4.1.8a-alt1
- initial build

