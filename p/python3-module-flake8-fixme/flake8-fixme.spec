%define _unpackaged_files_terminate_build 1
%define pypi_name flake8-fixme
%define mod_name flake8_fixme

%def_with check

Name: python3-module-%pypi_name
Version: 1.1.1
Release: alt1

Summary: Check for FIXME, TODO and other temporary developer notes
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/flake8-fixme/
Vcs: https://github.com/tommilligan/flake8-fixme

BuildArch: noarch
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-python3
BuildRequires: python3-module-flake8
BuildRequires: python3-module-setuptools
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-black
%endif

%description
%summary.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest %_builddir/%name-%version/integrate/test

%files
%doc LICENSE README.md
%python3_sitelibdir_noarch/%mod_name
%python3_sitelibdir_noarch/%{pyproject_distinfo %mod_name}

%changelog
* Tue Sep 2 2025 Timofei Fedotov <sovtouch@altlinux.org> 1.1.1-alt1
- Initial build for ALT Sisyphus.
