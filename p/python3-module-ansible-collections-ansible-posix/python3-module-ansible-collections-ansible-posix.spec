Name: python3-module-ansible-collections-ansible-posix
Version: 2.1.0
Release: alt1

Summary: Ansible Collection for Posix
License: GPL-3.0+
Group:   Development/Python3
URL:     https://galaxy.ansible.com/ui/repo/published/ansible/posix
VCS:     https://github.com/ansible-collections/ansible.posix

Source: %name-%version.tar
Patch0: 0001-Replace-ansible.module_utils.six-with-python-six.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: ansible-core

%description
An Ansible Collection of modules and plugins that target POSIX
UNIX/Linux and derivative Operating Systems.

%prep
%setup
%autopatch -p1

%install
# Install ansible.posix
mkdir -p %buildroot%python3_sitelibdir/ansible_collections/ansible/posix
cp -a * %buildroot%python3_sitelibdir/ansible_collections/ansible/posix

# Remove tests
find %buildroot%python3_sitelibdir/ansible_collections -name tests | xargs rm -rf

%files
%doc *.md
%python3_sitelibdir/ansible_collections/ansible/posix/*

%changelog
* Wed Jan 14 2026 Roman Efimenkov <trogjan@altlinux.org> 2.1.0-alt1
- Initial build for Sisyphus.
