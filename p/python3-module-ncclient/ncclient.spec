%define _unpackaged_files_terminate_build 1
%define pypi_name ncclient
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 0.6.16
Release: alt1
Summary: Python library for NETCONF clients
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/ncclient/
VCS: https://github.com/ncclient/ncclient
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch
# https://github.com/ncclient/ncclient/issues/598
%add_pyproject_deps_runtime_filter setuptools
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
BuildRequires: python3-module-pytest
%endif

%description
ncclient is a Python library that facilitates client-side scripting
and application development around the NETCONF protocol. ncclient
was developed by Shikar Bhushan. It is now maintained by Leonidas
Poulopoulos (@leopoul)

%prep
%setup
%autopatch -p1
# workaround for versioneer
grep -qsF ' export-subst' .gitattributes || exit 1
vers_f="$(sed -n 's/ export-subst//p' .gitattributes)"
grep -qs '^[ ]*git_refnames[ ]*=[ ]*".*"[ ]*$' "$vers_f" || exit 1
sed -i 's/^\([ ]*\)git_refnames[ ]*=[ ]*".*"[ ]*$/\1git_refnames = " (tag: v%version, upstream\/master)"/' "$vers_f"
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra test/

%files
%doc README.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Oct 10 2024 Stanislav Levin <slev@altlinux.org> 0.6.16-alt1
- 0.6.13 -> 0.6.16.

* Thu Jan 25 2024 Grigory Ustinov <grenka@altlinux.org> 0.6.13-alt2
- Fixed FTBFS.

* Tue Feb 07 2023 Stanislav Levin <slev@altlinux.org> 0.6.13-alt1
- 0.6.12 -> 0.6.13.

* Fri Jul 23 2021 Stanislav Levin <slev@altlinux.org> 0.6.12-alt1
- 0.6.3 -> 0.6.12.
- Enabled testing.

* Thu Jan 10 2019 Alexey Shabalin <shaba@altlinux.org> 0.6.3-alt1
- 0.6.3
- build python3 package

* Wed Nov 30 2016 Valentin Rosavitskiy <valintinr@altlinux.org> 0.5.2-alt1
- New version

* Fri Jun 10 2016 Valentin Rosavitskiy <valintinr@altlinux.org> 0.4.7-alt1
- New version

* Tue Apr 28 2015 Valentin Rosavitskiy <valintinr@altlinux.org> 0.4.3-alt1
- New version

* Thu Oct 30 2014 Valentin Rosavitskiy <valintinr@altlinux.org> 0.4.2-alt1
- Initla build for ALT

