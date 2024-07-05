Name: ansible-lint
Version: 24.6.1
Release: alt1

Summary: Best practices checker for Ansible

Group: System/Libraries
License: GPLv3+
Url: https://github.com/ansible/ansible-lint
Source: %name-%version.tar

BuildArch: noarch
BuildRequires(pre): rpm-macros-python3
BuildRequires: python3-devel >= 3.10
BuildRequires: rpm-build-python3 %pyproject_buildrequires
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-tox python3-module-pip python3-module-wheel
BuildRequires: python3-module-setuptools >= 65.3.0
BuildRequires: python3-module-setuptools_scm >= 7.0.5
BuildRequires: python3-module-rich >= 12.0.0
BuildRequires: python3-module-ruamel-yaml >= 0.18.5
BuildRequires: python3-module-yamllint >= 1.30.0
BuildRequires: ansible-core >= 2.12.0 python3-module-ansible-compat >= 4.1.11

# for tests
#BuildRequires: python3-module-yaml >= 5.4.1
#BuildRequires: python3-module-pytest >= 7.2.2 python3-module-pytest-xdist >= 2.1.0
#BuildRequires: python3-module-pylint python3-module-mypy python3-module-black
#BuildRequires: python3-module-wcmatch

Requires: ansible-core >= 2.13.0
Requires: ansible-compat >= 24.5.0
Requires: python3-module-yamllint

%description
ansible-lint checks playbooks for practices and behavior that could
potentially be improved.

%prep
%setup
echo "ref-names: tag: v%version" > .git_archival.txt

%build
%pyproject_build

%install
%pyproject_install

#%%check
#%%pyproject_run_pytest

%files
%doc README.md examples
%_bindir/%name
%python3_sitelibdir/*

%changelog
* Fri Jul 05 2024 Alexey Shabalin <shaba@altlinux.org> 24.6.1-alt1
- New version 24.6.1.

* Sun May 19 2024 Alexey Shabalin <shaba@altlinux.org> 24.5.0-alt1
- New version 24.5.0.

* Tue Jan 30 2024 Alexey Shabalin <shaba@altlinux.org> 6.22.2-alt1
- new version 6.22.2

* Sat Jan 27 2024 Grigory Ustinov <grenka@altlinux.org> 4.3.7-alt1.2
- Fixed FTBFS.

* Sat Aug 06 2022 Grigory Ustinov <grenka@altlinux.org> 4.3.7-alt1.1
- Fixed build requires.

* Tue Nov 24 2020 Alexey Shabalin <shaba@altlinux.org> 4.3.7-alt1
- new version 4.3.7

* Sun Sep 06 2020 Alexey Shabalin <shaba@altlinux.org> 4.3.4-alt1
- 4.3.4

* Thu Mar 12 2020 Alexey Shabalin <shaba@altlinux.org> 4.2.0-alt1
- 4.2.0

* Thu Sep 12 2019 Grigory Ustinov <grenka@altlinux.org> 4.1.0-alt1
- Build new version with python3.

* Mon May 25 2015 Terechkov Evgenii <evg@altlinux.org> 2.1.0-alt1
- Initial build for ALT Linux Sisyphus
