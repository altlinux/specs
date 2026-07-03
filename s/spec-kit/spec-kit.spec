%define _unpackaged_files_terminate_build 1
%define pypi_name specify-cli
%define mod_name specify_cli
%def_with check

Name: spec-kit
Version: 0.12.4
Release: alt1

Summary: Toolkit to help you get started with Spec-Driven Development
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/specify-cli/
Vcs: https://github.com/github/spec-kit

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

Requires: python3-module-%pypi_name = %EVR

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
BuildRequires: /proc
BuildRequires: git
%pyproject_builddeps_metadata_extra pcsc
%endif

%package -n python3-module-%pypi_name
Summary: Python module for spec-kit
Group: Development/Python3
BuildArch: noarch

%description
An open source toolkit that allows you to focus on product scenarios and
predictable outcomes instead of vibe coding every piece from scratch.

%description -n python3-module-%pypi_name
Python module for spec-kit.

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
%pyproject_run_pytest -vra

%files
%_bindir/specify

%files -n python3-module-%pypi_name
%python3_sitelibdir/%mod_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Jul 03 2026 Artem Krasovskiy <aibure@altlinux.org> 0.12.4-alt1
- Initial build for Sisyphus.
