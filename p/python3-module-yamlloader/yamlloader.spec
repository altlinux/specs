%define _unpackaged_files_terminate_build 1
%define pypi_name yamlloader

%def_with check

Name: python3-module-%pypi_name
Version: 1.3.2
Release: alt1
Summary: Ordered YAML loader and dumper for PyYAML
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/yamlloader
VCS: https://github.com/Phynix/yamlloader.git
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
BuildRequires: python3-module-hypothesis
%endif

%description
This module provides loaders and dumpers for PyYAML. Currently, an OrderedDict
loader/dumper is implemented, allowing to keep items order when loading resp.
dumping a file from/to an OrderedDict (Python 3.7+: Also regular dicts are
supported and are the default items to be loaded to. As of Python 3.7
preservation of insertion order is a language feature of regular dicts.).

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
%pyproject_run_unittest discover

%files
%doc README.rst
%python3_sitelibdir/yamlloader/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Aug 03 2023 Stanislav Levin <slev@altlinux.org> 1.3.2-alt1
- 1.2.2 -> 1.3.2.

* Mon Dec 05 2022 Stanislav Levin <slev@altlinux.org> 1.2.2-alt1
- 1.1.0 -> 1.2.2.

* Fri Jul 23 2021 Stanislav Levin <slev@altlinux.org> 1.1.0-alt1
- Initial build for Sisyphus.
