%define _unpackaged_files_terminate_build 1
%define pypi_name fastspec
%define mod_name fastspec

# no tests
%def_without check

Name: python3-module-%pypi_name
Version: 0.2.3
Release: alt1

Summary: Dynamic OpenAPI, Discovery, and GraphQL spec client for Python
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/fastspec/
Vcs: https://github.com/AnswerDotAI/fastspec

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
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
Dynamic OpenAPI, Discovery, and GraphQL spec client for Python - turn
any API spec into a fully-typed async client with attribute chaining,
streaming, and file uploads

%prep
%setup
%autopatch -p1
%pyproject_scm_init
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Aug 26 2026 Anton Zhukharev <ancieg@altlinux.org> 0.2.3-alt1
- Packaged for ALT Sisyphus.
