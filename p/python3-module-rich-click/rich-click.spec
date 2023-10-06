%define _unpackaged_files_terminate_build 1
%define pypi_name rich-click
%define mod_name rich_click

%def_with check

Name: python3-module-%pypi_name
Version: 1.6.1
Release: alt1
Summary: Format click help output nicely with rich
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/rich-click
Vcs: https://github.com/ewels/rich-click
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%endif

%description
The intention of rich-click is to provide attractive help output from click,
formatted with rich, with minimal customisation required.

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
# .github/workflows/test-examples.yml
%pyproject_run -- bash -s <<-'ENDTEST'
set -eu

for f in examples/*py
do
    echo -e "\n\n$f"
    python $f --help || exit 1;
done
ENDTEST

%files
%doc README.*
%_bindir/rich-click
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Oct 04 2023 Stanislav Levin <slev@altlinux.org> 1.6.1-alt1
- Initial build for Sisyphus.
