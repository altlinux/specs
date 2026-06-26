%define _unpackaged_files_terminate_build 1
%define pypi_name gaphas
%define module_name gaphas

%def_with check

Name: python3-module-%pypi_name
Version: 5.1.2
Release: alt1
Summary: Diagramming widget library for GTK and Cairo
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/gaphas
Vcs: https://github.com/gaphor/gaphas.git
BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
BuildRequires: libgtk4-gir
BuildRequires: libgraphene-gir
BuildRequires: xvfb-run
%endif

%description
Gaphas is a GTK-based diagramming widget library using Cairo for rendering.
Provides tools, canvas, items, constraint solver, and event handling for
creating diagram-based UI components.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_poetry dev
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
# Disable test_view_registration_2 because destroying the GTK window
# under Xvfb causes a fatal abort in the headless build environment
%pyproject_run -- xvfb-run -s "-screen 0 1600x1200x24 -noreset" \
    pytest -v tests \
    --deselect tests/test_view.py::test_view_registration_2

%files
%doc README.md
%python3_sitelibdir/%module_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Fri Jun 26 2026 Aleksandr A. Voyt <sobue@altlinux.org> 5.1.2-alt1
- 5.1.1 -> 5.1.2

* Thu Nov 06 2025 Aleksandr A. Voyt <sobue@altlinux.org> 5.1.1-alt1
- 5.0.3 -> 5.1.1

* Wed Apr 16 2024 Aleksandr A. Voyt <sobue@altlinux.org> 5.0.3-alt1
- Initial build
