%define _unpackaged_files_terminate_build 1
%define pypi_name jinja2-humanize-extension
%define mod_name jinja2_humanize_extension

%def_with check

Name: python3-module-%pypi_name
Version: 0.4.0
Release: alt1+23.g4143025

Summary: a jinja2 extension to use humanize library inside jinja2 templates
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/jinja2-humanize-extension/
Vcs: https://github.com/metwork-framework/jinja2_humanize_extension

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
%summary.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile dev-requirements.txt
%endif

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
* Wed Aug 19 2026 Anton Zhukharev <ancieg@altlinux.org> 0.4.0-alt1+23.g4143025
- Packaged for ALT Sisyphus.
