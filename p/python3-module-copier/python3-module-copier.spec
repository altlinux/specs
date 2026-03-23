%define _unpackaged_files_terminate_build 1
%define pypi_name copier

# Tests disabled due to failures with prompt_toolkit>=3.0.52
# See: https://github.com/copier-org/copier/discussions/2315
%def_without check

Name: python3-module-%pypi_name
Version: 9.14.0
Release: alt1

Summary: A library for rendering project templates
License: MIT
Group: Development/Python3
Url: https://copier.readthedocs.io/en/stable
Vcs: https://github.com/copier-org/copier

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%add_pyproject_deps_check_filter commitizen
%add_pyproject_deps_check_filter codespell
%add_pyproject_deps_check_filter taplo

%pyproject_builddeps_metadata
BuildRequires: python3-module-coverage
%pyproject_builddeps_check
%endif

%description
Copier is a library for rendering project templates.

It's a modern template engine that supports:
- Jinja2 templating with powerful filters
- YAML configuration for questions
- Multiple template formats
- Version control integration
- Template updates and migrations

%prep
%setup
%pyproject_scm_init
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_depgroup dev
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
# Skip tests that need network access
%pyproject_run_pytest \
  --deselect tests/test_copy.py::test_copy_repo \
  --deselect tests/test_vcs.py::test_clone \
  --deselect tests/test_vcs.py::test_shallow_clone \
  --deselect tests/test_vcs.py::test_local_clone \
  --deselect tests/test_vcs.py::test_removes_temporary_clone \
  --deselect tests/test_vcs.py::test_dont_remove_local_clone \
  --deselect tests/test_vcs.py::test_update_using_local_source_path_with_tilde \
  --deselect tests/test_updatediff.py::test_commit_hooks_respected \
  --deselect tests/test_tools.py::test_types \
  --deselect tests/test_prompt.py::test_path_completion

%files
%doc README.md
%_bindir/%pypi_name
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Mar 23 2026 Denis Rastyogin <gerben@altlinux.org> 9.14.0-alt1
- Updated to 9.14.0.

* Tue Mar 10 2026 Denis Rastyogin <gerben@altlinux.org> 9.13.1-alt1
- Updated to 9.13.1.

* Tue Jan 13 2026 Denis Rastyogin <gerben@altlinux.org> 9.11.1-alt1
- Updated to 9.11.1.

* Tue Oct 07 2025 Denis Sergeev <zeff@altlinux.org> 9.10.2-alt1
- 9.10.1 -> 9.10.2.

* Tue Sep 09 2025 Denis Sergeev <zeff@altlinux.org> 9.10.1-alt1
- 9.9.0 -> 9.10.1.

* Tue Aug 12 2025 Denis Sergeev <zeff@altlinux.org> 9.9.0-alt1
- 9.8.0 -> 9.9.0.

* Fri Aug 01 2025 Denis Sergeev <zeff@altlinux.org> 9.8.0-alt1
- 9.7.1 -> 9.8.0.

* Tue Jul 01 2025 Denis Sergeev <zeff@altlinux.org> 9.7.1-alt1
- Initial build for ALT Sisyphus.
