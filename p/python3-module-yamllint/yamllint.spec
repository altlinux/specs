%define _unpackaged_files_terminate_build 1
%define pypi_name yamllint

%def_with check

Name: python3-module-%pypi_name
Version: 1.33.0
Release: alt1
Summary: A linter for YAML files
License: GPLv3
Group: Development/Python
Url: https://pypi.org/project/yamllint/
Vcs: https://github.com/adrienverge/yamllint
BuildArch: noarch
Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Provides: yamllint = %EVR
Obsoletes: yamllint <= 1.24.2-alt1

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
BuildRequires: /dev/pts
%pyproject_builddeps_metadata
%endif

BuildRequires: python3-module-sphinx-sphinx-build-symlink

%description
A linter for YAML files.

yamllint does not only check for syntax validity, but for weirdnesses like key
repetition and cosmetic problems such as lines length, trailing spaces,
indentation, etc.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

# man page
pushd docs
make man
popd

%install
%pyproject_install

# man page
install -D -m0644 docs/_build/man/yamllint.1 %buildroot/%_man1dir/yamllint.1

%check
%pyproject_run_unittest discover

%files
%doc README.rst CHANGELOG.rst
%_man1dir/yamllint.1.*

%_bindir/yamllint
%python3_sitelibdir/yamllint/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Nov 14 2023 Stanislav Levin <slev@altlinux.org> 1.33.0-alt1
- 1.32.0 -> 1.33.0.

* Tue May 23 2023 Stanislav Levin <slev@altlinux.org> 1.32.0-alt1
- 1.31.0 -> 1.32.0.

* Tue Apr 25 2023 Stanislav Levin <slev@altlinux.org> 1.31.0-alt1
- 1.28.0 -> 1.31.0.

* Mon Sep 12 2022 Stanislav Levin <slev@altlinux.org> 1.28.0-alt1
- 1.24.2 -> 1.28.0.

* Mon Sep 14 2020 Stanislav Levin <slev@altlinux.org> 1.24.2-alt1
- 1.17.0 -> 1.24.2.

* Fri Sep 20 2019 Terechkov Evgenii <evg@altlinux.org> 1.17.0-alt1
- Initial build for ALT Linux Sisyphus
