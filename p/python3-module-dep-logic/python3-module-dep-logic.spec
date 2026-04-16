%define pypi_name dep-logic
%define mod_name dep_logic

%def_with check

Name:    python3-module-%pypi_name
Version: 0.5.2
Release: alt1

Summary: Python dependency specifications supporting logical operations
License: Apache-2.0
Group:   Development/Python3
URL:     https://github.com/pdm-project/dep-logic

Source: %pypi_name-%version.tar

Patch1: support-packaging-26.0.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools_scm python3-module-wheel
BuildRequires: python3-module-pdm
BuildRequires: python3-module-pdm-backend

%if_with check
BuildRequires: python3-module-pytest
%endif

BuildArch: noarch

%description
%summary.

%prep
%setup -n %pypi_name-%version
%patch1 -p1

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
%pyproject_run_pytest

%files
%doc *.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Apr 14 2026 Alexander Burmatov <thatman@altlinux.org> 0.5.2-alt1
- New 0.5.2 version.

* Mon Jan 27 2025 Ivan A. Melnikov <iv@altlinux.org> 0.4.10-alt1.1
- NMU: basic loongarch64 support

* Thu Dec 19 2024 Alexander Burmatov <thatman@altlinux.org> 0.4.10-alt1
- New 0.4.10 version.

* Tue Jan 09 2024 Alexander Burmatov <thatman@altlinux.org> 0.0.4-alt1
- Initial build for Sisyphus.
