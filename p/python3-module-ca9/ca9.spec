%define _unpackaged_files_terminate_build 1
%define pypi_name ca9
%define mod_name ca9

%def_with check

Name: python3-module-%pypi_name
Version: 0.9.0
Release: alt1

Summary: CA9 is a local evidence engine for Python AppSec triage
License: MPL-2.0
Group: Development/Python3
Url: https://duriantaco.github.io/ca9
VCS: https://github.com/duriantaco/ca9

BuildArch: noarch

Source0: %name-%version.tar
Source1: pyproject_deps.json
Patch: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
%pyproject_runtimedeps_metadata_extra cli
%pyproject_runtimedeps_metadata_extra mcp
Requires: python3-module-yaml
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_metadata_extra cli
%pyproject_builddeps_metadata_extra mcp
BuildRequires: python3-module-yaml
%endif

%description
ca9 tells you whether your dependency supply chain is safe enough
to ship, and helps stop unsafe packages before they run.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
# drop website-only scaffolding and the branding assets before %doc
rm -rf docs/robots.txt docs/assets

%build
%pyproject_build

%install
%pyproject_install
ln -sf %_licensedir/MPL-2.0 LICENSE

%check
# test_npm_gateway_config_files_are_accepted_by_npm is skipped: npm is not
# pulled into the build just for this single config-compatibility check
%pyproject_run_pytest -vra

%files
%doc README.md docs
%doc --no-dereference LICENSE
%_bindir/%pypi_name
%_bindir/%pypi_name-mcp
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{mod_name}_mcp/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Nov 12 2026 Dmitry Mihalchenko <tascad@altlinux.org> 0.9.0-alt1
- Initial build for ALT Sisyphus.
