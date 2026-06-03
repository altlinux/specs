%define _unpackaged_files_terminate_build 1
%define pypi_name cbor2
%define mod_name %pypi_name

# upstream officially doesn't support tho,
%python3_set_limited_api

%def_with check

Name: python3-module-%pypi_name
Version: 6.1.2
Release: alt1
Summary: Pure Python CBOR (de)serializer with extensive tag support
License: MIT
Group: Development/Python
Url: https://pypi.org/project/cbor2/
Vcs: https://github.com/agronholm/cbor2
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Source2: vendor_rust.tar
Patch0: %name-%version-alt.patch
# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
This library provides encoding and decoding for the Concise Binary Object
Representation (CBOR) (RFC 8949) serialization format. The specification is
fully compatible with the original RFC 7049.

%prep
%setup -a2
%autopatch -p1
mkdir .cargo
cat < vendor_cargoconf.toml >> .cargo/config.toml
%pyproject_scm_init
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_depgroup test
%endif

%build
export RUSTFLAGS="${RUSTFLAGS} -g"
export CARGO_PROFILE_RELEASE_STRIP='none'
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra -o=addopts=''

%files
%_bindir/cbor2
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Jun 03 2026 Stanislav Levin <slev@altlinux.org> 6.1.2-alt1
- 6.1.1 -> 6.1.2

* Fri May 15 2026 Stanislav Levin <slev@altlinux.org> 6.1.1-alt1
- 6.1.0 -> 6.1.1.

* Wed May 13 2026 Stanislav Levin <slev@altlinux.org> 6.1.0-alt1
- 5.9.0 -> 6.1.0.

* Fri Apr 10 2026 Stanislav Levin <slev@altlinux.org> 5.9.0-alt1
- 5.8.0 -> 5.9.0 (fixes: CVE-2026-26209).

* Thu Feb 05 2026 Stanislav Levin <slev@altlinux.org> 5.8.0-alt1
- 5.7.1 -> 5.8.0 (fixes: CVE-2025-68131).

* Mon Oct 27 2025 Stanislav Levin <slev@altlinux.org> 5.7.1-alt1
- 5.7.0 -> 5.7.1.

* Tue Sep 02 2025 Stanislav Levin <slev@altlinux.org> 5.7.0-alt1
- 5.6.5 -> 5.7.0.

* Thu Oct 10 2024 Stanislav Levin <slev@altlinux.org> 5.6.5-alt1
- 5.6.4 -> 5.6.5.

* Wed Oct 09 2024 Stanislav Levin <slev@altlinux.org> 5.6.4-alt1
- 5.4.6 -> 5.6.4.

* Tue Oct 08 2024 Stanislav Levin <slev@altlinux.org> 5.4.6-alt2
- Migrated from removed setuptools' test command (#51666).

* Fri Dec 30 2022 Vitaly Lipatov <lav@altlinux.ru> 5.4.6-alt1
- new version 5.4.6 (with rpmrb script)

* Sun Jul 17 2022 Vitaly Lipatov <lav@altlinux.ru> 5.4.3-alt1
- new version 5.4.3 (with rpmrb script)

* Mon Apr 04 2022 Vitaly Lipatov <lav@altlinux.ru> 5.4.2-alt1
- new version 5.4.2 (with rpmrb script)

* Sun Aug 15 2021 Vitaly Lipatov <lav@altlinux.ru> 5.4.0-alt1
- new version 5.4.0 (with rpmrb script)

* Tue Nov 03 2020 Vitaly Lipatov <lav@altlinux.ru> 5.2.0-alt1
- new version 5.2.0 (with rpmrb script)

* Fri Apr 10 2020 Eugene Omelyanovich <regatio@etersoft.ru> 5.1.0-alt1
- new version (5.1.0) with rpmgs script

