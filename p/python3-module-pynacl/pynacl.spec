%define _unpackaged_files_terminate_build 1

%define pypi_name pynacl
%define mod_name nacl

# .github/workflows/wheel-builder.yml
%python3_set_limited_api 3.8

%def_with check

Name: python3-module-%pypi_name
Version: 1.6.1
Release: alt1
Summary: Python binding to the Networking and Cryptography (NaCl) library
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/PyNaCl/
Vcs: https://github.com/pyca/pynacl/
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
BuildRequires: libsodium-devel >= 1.0.16
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra tests
%endif

%description
PyNaCl is a Python binding to the Networking and Cryptography library,
a crypto library with the stated goal of improving usability, security
and speed.

%prep
%setup
# Remove bundled libsodium, to be sure
rm -r src/libsodium/
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
export SODIUM_INSTALL=system
%pyproject_build

%check
%pyproject_run_pytest -ra

%install
%pyproject_install

%files
%doc README.rst
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Dec 16 2025 Stanislav Levin <slev@altlinux.org> 1.6.1-alt1
- 1.5.0 -> 1.6.1.

* Wed Apr 02 2025 Stanislav Levin <slev@altlinux.org> 1.5.0-alt2.1
- NMU: fixed FTBFS (setuptools 75.8.1)

* Tue Jun 04 2024 Stanislav Levin <slev@altlinux.org> 1.5.0-alt2
- Added missing runtime dependency on cffi.

* Tue May 17 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.5.0-alt1
- 1.5.0 released

* Fri Aug 06 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.0-alt1
- 1.4.0 released

* Wed Jul 28 2021 Grigory Ustinov <grenka@altlinux.org> 1.3.0-alt2
- Drop python2 support.

* Tue Jan 22 2019 Vitaly Lipatov <lav@altlinux.ru> 1.3.0-alt1
- new version 1.3.0 (with rpmrb script)

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 1.1.2-alt1.1.1.qa1
- NMU: applied repocop patch

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.2-alt1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Mon Feb 12 2018 Vitaly Lipatov <lav@altlinux.ru> 1.1.2-alt1.1
- NMU: autorebuild with libsodium-1.0.16

* Wed Jun 14 2017 Vitaly Lipatov <lav@altlinux.ru> 1.1.2-alt1
- initial build for ALT Sisyphus

