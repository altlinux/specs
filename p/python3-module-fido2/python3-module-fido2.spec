%define _unpackaged_files_terminate_build 1
%define pypi_name fido2

%def_with check

Name: python3-module-%pypi_name
Version: 1.1.2
Release: alt1

Summary: Provides library functionality for communicating with a FIDO device over USB as well as verifying attestation and assertion signatures
License: BSD-2-Clause and Apache-2.0 and MPL-2.0
Group: Development/Python3
Url: https://pypi.org/project/fido2/
Vcs: https://github.com/Yubico/python-fido2

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
Provides library functionality for communicating with a FIDO device over USB
as well as verifying attestation and assertion signatures.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%if_with check
%pyproject_deps_resync_check_poetry dev
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc README.adoc COPYING COPYING.APLv2 COPYING.MPLv2 NEWS examples
%python3_sitelibdir/%pypi_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Thu Jul 20 2023 Anton Zhukharev <ancieg@altlinux.org> 1.1.2-alt1
- Updated to 1.1.2.

* Sun Apr 09 2023 Anton Zhukharev <ancieg@altlinux.org> 1.1.1-alt1
- New version.

* Thu Mar 30 2023 Anton Zhukharev <ancieg@altlinux.org> 1.1.0-alt1
- New version.
- Clean up spec.

* Wed Sep 14 2022 Stanislav Levin <slev@altlinux.org> 1.0.0-alt2
- NMU: Fixed FTBFS (poetry-core 1.1.0).

* Sat Jul 23 2022 Anton Zhukharev <ancieg@altlinux.org> 1.0.0-alt1
- initial build for Sisyphus

