%define pypi_name ansible-sign

%def_without check

Name:    python3-module-%pypi_name
Version: 0.1.1
Release: alt1

Summary: The `ansible-sign` utility for signing and verifying Ansible project directory contents.
License: MIT
Group:   Development/Python3
URL:     https://github.com/ansible/ansible-sign

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools python3-module-wheel

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
%summary

%prep
%setup -n %pypi_name-%version
subst '/^name/a version = %version' setup.cfg

%build
%pyproject_build

%install
%pyproject_install

%check
#%%tox_create_default_config
%tox_check_pyproject

%files
%doc *.md
%_bindir/%pypi_name
%python3_sitelibdir/ansible_sign
%python3_sitelibdir/%{pyproject_distinfo ansible_sign}

%changelog
* Mon Jul 22 2024 Andrey Cherepanov <cas@altlinux.org> 0.1.1-alt1
- Initial build for Sisyphus.
