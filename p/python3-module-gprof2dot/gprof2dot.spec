%define _unpackaged_files_terminate_build 1
%define pypi_name gprof2dot
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 2024.6.6
Release: alt1
Summary: Generate a dot graph from the output of several profilers
License: LGPL-3
Group: Development/Python3
Url: https://pypi.org/project/gprof2dot
Vcs: https://github.com/jrfonseca/gprof2dot
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
BuildRequires: /usr/bin/dot
# dot's output is polluted with
# Fontconfig error: Cannot load default config file: No such file: (null)
# if /etc/fonts/fonts.conf is missing
BuildRequires: fontconfig
%endif

%description
This is a Python script to convert the output from many profilers into a dot
graph.

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
# per the comment in .github/workflows/testOnly.yml
%pyproject_run -- python tests/test.py --max-acceptable=0

%files
%doc README.*
%_bindir/gprof2dot
%python3_sitelibdir/%mod_name.py
%python3_sitelibdir/__pycache__/%mod_name.*
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Thu Jun 06 2024 Stanislav Levin <slev@altlinux.org> 2024.6.6-alt1
- 2022.7.29 -> 2024.6.6.

* Mon Jul 24 2023 Stanislav Levin <slev@altlinux.org> 2022.7.29-alt1
- Initial build for Sisyphus.
