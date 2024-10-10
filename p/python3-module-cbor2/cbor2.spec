%define _unpackaged_files_terminate_build 1
%define pypi_name cbor2
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 5.6.5
Release: alt1
Summary: Pure Python CBOR (de)serializer with extensive tag support
License: MIT
Group: Development/Python
Url: https://pypi.org/project/cbor2/
Vcs: https://github.com/agronholm/cbor2
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra test
%endif

%description
This library provides encoding and decoding for the Concise Binary Object
Representation (CBOR) (RFC 8949) serialization format. The specification is
fully compatible with the original RFC 7049.

%prep
%setup
%pyproject_scm_init
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra -o=addopts=''

%files
%_bindir/cbor2
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/_%mod_name.*.so
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
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

