%define _unpackaged_files_terminate_build 1
%define pypi_name minidb

%def_with check

Name: python3-module-%pypi_name
Version: 2.0.8
Release: alt1

Summary: A simple SQLite3-based store for Python objects
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/minidb/
Vcs: https://github.com/thp/minidb

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-modules-sqlite3
%endif

%description
Store Python objects in SQLite 3. Concise, pythonic API. Fun to use.

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
%pyproject_run_pytest -vra

%files
%doc LICENSE README.md
%python3_sitelibdir/%pypi_name.py
%python3_sitelibdir/__pycache__/%pypi_name.*.pyc
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu May 16 2024 Anton Zhukharev <ancieg@altlinux.org> 2.0.8-alt1
- Updated to 2.0.8.

* Sat Dec 30 2023 Anton Zhukharev <ancieg@altlinux.org> 2.0.7-alt1
- Built for ALT Sisyphus.

