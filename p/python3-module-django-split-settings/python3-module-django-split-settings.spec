%define pypi_name django-split-settings

%def_with check

Name: python3-module-%pypi_name
Version: 1.3.2
Release: alt1

Summary: Organize Django settings into multiple files and directories
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/django-split-settings
Vcs: https://github.com/wemake-services/django-split-settings

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-poetry
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-django
%endif

%description
Organize Django settings into multiple files and directories.
Easily override and modify settings. Use wildcards and optional settings files.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
sed -i '/--cov*/d' setup.cfg
%pyproject_run_pytest -v

%files
%doc README.*
%python3_sitelibdir/split_settings
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Sun Jul 21 2024 Anton Vyatkin <toni@altlinux.org> 1.3.2-alt1
- Initial build for Sisyphus.
