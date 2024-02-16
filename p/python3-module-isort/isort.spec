%define _unpackaged_files_terminate_build 1
%define pypi_name isort

%def_with check

Name: python3-module-%pypi_name
Version: 5.13.2
Release: alt1
Summary: Python utility / library to sort Python imports
Group: Development/Python3
License: MIT
Url: https://pypi.org/project/isort
VCS: https://github.com/PyCQA/isort
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
%add_python3_req_skip pylama.lint
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
BuildRequires: /usr/bin/git
%add_pyproject_deps_check_filter cruft
%add_pyproject_deps_check_filter example-isort-sorting-plugin
%add_pyproject_deps_check_filter example-shared-isort-profile
%add_pyproject_deps_check_filter hypothesmith
%add_pyproject_deps_check_filter pep8-naming
%add_pyproject_deps_check_filter pip-api
%add_pyproject_deps_check_filter pipreqs
%add_pyproject_deps_check_filter portray
%add_pyproject_deps_check_filter requirementslib
%add_pyproject_deps_check_filter safety
%add_pyproject_deps_check_filter smmap2
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
Python utility / library to sort Python imports

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_poetry dev
%endif

# remove bunled(for tests only) plugins/profiles,
# they cannot be loaded within venv and break tests assumptions
rm -r \
    example_shared_isort_profile \
    example_isort_sorting_plugin \
    example_isort_formatting_plugin \
    %nil

# unvendor distributions
rm -r isort/_vendored/*

%build
%pyproject_build

%install
%pyproject_install
mv %buildroot%_bindir/isort{,.py3}

%check
%pyproject_run_pytest -vra tests/unit/

%files
%doc README.md
%_bindir/isort.py3
%_bindir/isort-identify-imports
%python3_sitelibdir/isort/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Feb 15 2024 Stanislav Levin <slev@altlinux.org> 5.13.2-alt1
- 5.12.0 -> 5.13.2.

* Mon Jan 29 2024 Grigory Ustinov <grenka@altlinux.org> 5.12.0-alt1.1
- NMU: Fixed FTBFS.

* Fri Feb 10 2023 Stanislav Levin <slev@altlinux.org> 5.12.0-alt1
- 5.10.1 -> 5.12.0.

* Wed Sep 14 2022 Stanislav Levin <slev@altlinux.org> 5.10.1-alt2
- Modernized packaging (fixes FTBFS due to poetry-core 1.1.0).

* Wed Feb 09 2022 Stanislav Levin <slev@altlinux.org> 5.10.1-alt1
- 4.3.21 -> 5.10.1.

* Tue Oct 05 2021 Ivan A. Melnikov <iv@altlinux.org> 4.3.21-alt2
- Get rid of pylama dependency.

* Thu Oct 17 2019 Stanislav Levin <slev@altlinux.org> 4.3.21-alt1
- 4.2.15 -> 4.3.21.

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 4.2.15-alt3.qa1
- NMU: remove rpm-build-ubt from BR:

* Sat Jun 15 2019 Igor Vlasenko <viy@altlinux.ru> 4.2.15-alt2.qa1
- NMU: remove %%ubt from release

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 4.2.15-alt1.qa1
- NMU: applied repocop patch

* Wed Nov 01 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 4.2.15-alt1
- Initial build for ALT.
