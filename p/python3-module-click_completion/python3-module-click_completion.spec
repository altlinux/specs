%define _unpackaged_diles_terminate_build 1
%define pypi_name click_completion

Name: python3-module-%pypi_name
Version: 0.5.2
Release: alt1
Summary: Add or enhance bash, fish, zsh and powershell completion in Click
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/click-completion/
Vcs: https://github.com/click-contrib/click-completion

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3-module-setuptools

%description
%summary.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc LICENSE README.*
%python3_sitelibdir/%pypi_name

%changelog
* Tue Oct 28 2025 Vladislav Eliseev <general@altlinux.org> 0.5.2-alt1
- Initial build for Sisyphus.
