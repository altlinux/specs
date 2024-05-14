%define _unpackaged_files_terminate_build 1

%define oname mdit-plugins
%define mname mdit_py_plugins
%define pypi_name mdit-py-plugins

%def_with check

Name: python3-module-%oname
Version: 0.4.1
Release: alt1
Summary: Collection of core plugins for markdown-it-py 
License: MIT
Group: Development/Python3
URL: https://pypi.org/project/mdit-py-plugins
VCS: https://github.com/executablebooks/mdit-py-plugins

BuildArch: noarch

Source: %name-%version.tar
Source1: %pyproject_deps_config_name

Provides: python3-module-%pypi_name

BuildRequires(pre): rpm-build-pyproject

%pyproject_runtimedeps_metadata
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_metadata_extra testing
%pyproject_builddeps_metadata_extra linkify
%endif

%description
Collection of core plugins for markdown-it-py.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject
%pyproject_run_pytest -ra tests

%files
%doc LICENSE README.md
%python3_sitelibdir/%mname/
%python3_sitelibdir/%{pyproject_distinfo %mname}

%changelog
* Tue May 14 2024 Grigory Ustinov <grenka@altlinux.org> 0.4.1-alt1
- Automatically updated to 0.4.1.

* Tue Jul 11 2023 Andrey Limachko <liannnix@altlinux.org> 0.4.0-alt1
- 0.3.5 -> 0.4.0

* Fri Mar 03 2023 Grigory Ustinov <grenka@altlinux.org> 0.3.5-alt1
- Automatically updated to 0.3.5.

* Sat Feb 18 2023 Grigory Ustinov <grenka@altlinux.org> 0.3.4-alt1
- Automatically updated to 0.3.4.

* Fri Dec 09 2022 Grigory Ustinov <grenka@altlinux.org> 0.3.3-alt1
- Automatically updated to 0.3.3.

* Wed Oct 19 2022 Grigory Ustinov <grenka@altlinux.org> 0.3.1-alt1
- Automatically updated to 0.3.1.

* Tue Sep 13 2022 Grigory Ustinov <grenka@altlinux.org> 0.3.0-alt1
- Automatically updated to 0.3.0.

* Thu Oct 07 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 0.2.8-alt1
- Initial build for ALT.
