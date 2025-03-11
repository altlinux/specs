%define _unpackaged_files_terminate_build 1
%define pypi_name jiter
%define pypi_nname jiter
%define mod_name jiter

%def_with check

Name: python3-module-%pypi_nname
Version: 0.9.0
Release: alt1

Summary: Fast iterable JSON parser
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/jiter/
Vcs: https://github.com/pydantic/jiter

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar
Source2: %pyproject_deps_config_name
Source3: config.toml
Patch0: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
This is a standalone version of the JSON parser used in pydantic-core.
The recommendation is to only use this package directly if you do not
use pydantic.

%prep
%setup -a1
%autopatch -p1
cd crates/jiter-python
install -vD %SOURCE3 .cargo/config.toml
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile tests/requirements.txt
%endif

%build
cd crates/jiter-python
%pyproject_build

%install
cd crates/jiter-python
%pyproject_install

%check
cd crates/jiter-python
%pyproject_run_pytest -vra -o=addopts=-Wignore

%files
%doc LICENSE README.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Mar 11 2025 Anton Zhukharev <ancieg@altlinux.org> 0.9.0-alt1
- Updated to 0.9.0.

* Tue Mar 04 2025 Anton Zhukharev <ancieg@altlinux.org> 0.8.2-alt1
- Built for ALT Sisyphus.

