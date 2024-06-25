%define _unpackaged_files_terminate_build 1
%define pypi_name s3transfer
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 0.10.2
Release: alt1

Summary: An Amazon S3 Transfer Manager

License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/s3transfer/
Vcs: https://github.com/boto/s3transfer
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
# awscrt is extra stuff required by `s3transfer[crt]` => `botocore[crt]`
# awscrt is not packaged yet
%filter_from_requires /python3(awscrt\(\..*\)\?)/d
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
%pypi_name is a Python library for managing Amazon S3 transfers.

Note.
This project is not currently GA. If you are planning to use this code in
production, make sure to lock to a minor version as interfaces may break from
minor version to minor version.  For a basic, stable interface of %pypi_name,
try the interfaces exposed in boto3.

%prep
%setup
%autopatch1 -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile requirements-dev.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run -- python scripts/ci/run-tests

%files
%doc README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Jun 25 2024 Stanislav Levin <slev@altlinux.org> 0.10.2-alt1
- 0.10.1 -> 0.10.2.

* Mon Mar 18 2024 Stanislav Levin <slev@altlinux.org> 0.10.1-alt1
- 0.10.0 -> 0.10.1.

* Mon Feb 26 2024 Stanislav Levin <slev@altlinux.org> 0.10.0-alt1
- 0.6.1 -> 0.10.0.

* Mon May 29 2023 Stanislav Levin <slev@altlinux.org> 0.6.1-alt1
- 0.6.0 -> 0.6.1.

* Mon Jul 18 2022 Vitaly Lipatov <lav@altlinux.ru> 0.6.0-alt1
- new version 0.6.0

* Wed Mar 09 2022 Stanislav Levin <slev@altlinux.org> 0.5.2-alt1
- 0.3.3 -> 0.5.2.

* Thu Jun 17 2021 Vitaly Lipatov <lav@altlinux.ru> 0.3.3-alt2
- build python3 module separately

* Tue Sep 08 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 0.3.3-alt1
- Updated to upstream version 0.3.3.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.10-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Aug 25 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.10-alt1
- Initial build for ALT.
