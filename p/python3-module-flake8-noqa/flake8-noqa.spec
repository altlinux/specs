%define _unpackaged_files_terminate_build 1
%define pypi_name flake8-noqa
%define mod_name flake8_noqa

%def_with check

Name: python3-module-%pypi_name
Version: 1.5.0
Release: alt1

Summary: Check code for one-element tuple

License: LGPL-3.0
Group: Development/Python3
Url: https://pypi.org/project/flake8-noqa/
Vcs: https://github.com/plinss/flake8-noqa

BuildArch: noarch
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
%if_with check
BuildRequires: python3-module-pydocstyle
BuildRequires: python3-module-flake8-docstrings
BuildRequires: python3-module-typing_extensions
BuildRequires: python3-module-flake8
BuildRequires: python3-module-pytest
%endif

%description
%summary.

%prep
%setup
sed -i '/^\[project\]/a version = "%version"' pyproject.toml
sed -i '/^dynamic = .*/d' pyproject.toml

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest test.py

%files
%doc LICENSE README.md
%python3_sitelibdir_noarch/%mod_name/
%python3_sitelibdir_noarch/%{pyproject_distinfo %mod_name}/

%changelog
* Wed Feb 18 2026 Timofei Fedotov <sovtouch@altlinux.org> 1.5.0-alt1
- Updated to 1.5.0.

* Tue Sep 2 2025 Timofei Fedotov <sovtouch@altlinux.org> 1.4.0-alt1
- Initial build for ALT Sisyphus.
