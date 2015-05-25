Name: ansible-lint
Version: 2.1.0
Release: alt1
Summary: Best practices checker for Ansible

Group: System/Libraries
License: MIT
Url: https://github.com/willthames/ansible-lint

Source: %name-%version.tar
Packager: Evgenii Terechkov <evg@altlinux.org>

BuildArch: noarch
BuildRequires: python-module-setuptools

%description
ansible-lint checks playbooks for practices and behaviour that could potentially be improved

%prep
%setup

%build
%python_build

%install
%python_install --record=INSTALLED_FILES

%files -f INSTALLED_FILES
%doc CONTRIBUTING.md README.md examples

%changelog
* Mon May 25 2015 Terechkov Evgenii <evg@altlinux.org> 2.1.0-alt1
- Initial build for ALT Linux Sisyphus
