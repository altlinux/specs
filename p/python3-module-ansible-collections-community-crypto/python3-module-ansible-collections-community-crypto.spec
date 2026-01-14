Name: python3-module-ansible-collections-community-crypto
Version: 3.0.5
Release: alt1

Summary: The community.crypto collection for Ansible
License: GPL-3.0+ and Apache-2.0 and BSD 3-Clause
Group:   Development/Python3
URL:     https://galaxy.ansible.com/ui/repo/published/community/crypto
VCS:     https://github.com/ansible-collections/community.crypto

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: ansible-core

%description
Provides modules and plugins for many cryptographic operations.

%prep
%setup

%install
# Install community.crypto
mkdir -p %buildroot%python3_sitelibdir/ansible_collections/community/crypto
cp -a * %buildroot%python3_sitelibdir/ansible_collections/community/crypto

# Remove tests
find %buildroot%python3_sitelibdir/ansible_collections -name tests | xargs rm -rf

%files
%doc *.md
%python3_sitelibdir/ansible_collections/community/crypto/*

%changelog
* Wed Jan 14 2026 Roman Efimenkov <trogjan@altlinux.org> 3.0.5-alt1
- Initial build for Sisyphus.
