%define pypi_name pdm

%def_with check

Name:    python3-module-%pypi_name
Version: 2.26.7
Release: alt1

Summary: A modern Python package and dependency manager supporting the latest PEP standards
License: MIT
Group:   Development/Python3
URL:     https://github.com/pdm-project/pdm

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools_scm python3-module-wheel
BuildRequires: python3-module-pdm-backend
BuildRequires: python3-module-dep-logic

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-unearth
BuildRequires: python3-module-pytest-mock
BuildRequires: python3-module-resolvelib
BuildRequires: python3-module-tomlkit
BuildRequires: python3-module-pyproject_hooks
BuildRequires: python3-module-installer
BuildRequires: python3-module-blinker
BuildRequires: python3-module-pytest-httpserver
BuildRequires: python3-module-findpython
BuildRequires: python3-module-virtualenv
BuildRequires: python3-module-python-dotenv
BuildRequires: python3-module-pbs-installer
BuildRequires: python3-module-hishel
BuildRequires: python3-module-id
BuildRequires: python3-module-pytest-httpx
%endif

Requires: python3-module-pdm-alt-namespace

%filter_from_provides /^python3(%pypi_name)/d

BuildArch: noarch

Source: %pypi_name-%version.tar
Patch: support-installer-1.0.patch

%description
%summary.

%prep
%setup -n %pypi_name-%version
%patch -p1

# setuptools_scm implements a file_finders entry point which returns all files
# tracked by SCM.
if [ ! -d .git ]; then
    git init
    git config user.email author@example.com
    git config user.name author
    git add .
    git commit -m 'release'
    git tag '%version'
fi

%build
%pyproject_build

%install
%pyproject_install

%check
# Requires network
donttest="network"
donttest="$donttest or test_build_with_no_isolation"
# Different requires python
donttest="$donttest or test_use_remember_last_selection"
# Old pbs installer version
donttest="$donttest or test_project_best_match_max"
donttest="$donttest or test_project_best_match_min"
# Broken with installer v1
donttest="$donttest or test_uninstall_with_console_scripts"
donttest="$donttest or test_install_wheel_with_cache"
donttest="$donttest or test_can_install_wheel_with_cache_in_multiple_projects"
donttest="$donttest or test_url_requirement_is_not_cached"
donttest="$donttest or test_install_wheel_with_data_scripts"
%pyproject_run_pytest -k "not ($donttest)"

%files
%doc *.md
%_bindir/%pypi_name
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Apr 15 2026 Alexander Burmatov <thatman@altlinux.org> 2.26.7-alt1
- New 2.26.7 version.

* Thu Dec 19 2024 Alexander Burmatov <thatman@altlinux.org> 2.22.0-alt1
- New 2.22.0 version.

* Tue Jan 09 2024 Alexander Burmatov <thatman@altlinux.org> 2.11.2-alt1
- New 2.11.2 version.

* Thu Oct 26 2023 Alexander Burmatov <thatman@altlinux.org> 2.10.0-alt1
- Initial build for Sisyphus.
