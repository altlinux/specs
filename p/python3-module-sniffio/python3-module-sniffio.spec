%define _unpackaged_files_terminate_build 1
%define pypi_name sniffio
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 1.3.0
Release: alt1

Summary: Sniff out which async library your code is running under
License: MIT or Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/sniffio/
Vcs: https://github.com/python-trio/sniffio
BuildArch: noarch
Source: %pypi_name-%version.tar
Source1: %pyproject_deps_config_name
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
This is a tiny package whose only purpose is to let you detect which async
library (like Trio, and asyncio, and ...) your code is running under.

%prep
%setup -n %pypi_name-%version
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile test-requirements.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run -- bash -s <<-'ENDUNITTEST'
set -eu
mkdir empty
cd empty
python -m pytest --pyargs %mod_name -ra
ENDUNITTEST

%files
%doc README.*
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/
%exclude %python3_sitelibdir/%pypi_name/_tests

%changelog
* Tue Nov 07 2023 Stanislav Levin <slev@altlinux.org> 1.3.0-alt1
- 1.2.0 -> 1.3.0.

* Wed Feb 09 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2.0-alt1
- 1.2.0

* Fri Nov 06 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.0-alt2
- exclude tests from package due to excessive reqs

* Tue Jan 15 2019 Evgeny Sinelnikov <sin@altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus
