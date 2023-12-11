Name:    python3-module-ansible-collections
Version: 8.1.0
Release: alt1

Summary: This repository contains the community.general and some other Ansible Collection
License: GPL-3.0+ and Apache-2.0 and BSD-2-Clause and BSD-3-Clause and MIT and MPL-2.0 and PSF-2.0
Group:   Development/Python3
URL:     https://github.com/ansible-collections/community.general

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar
Source1: submodules.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%filter_from_requires /python3(ansible.module_utils.six.moves/d
%filter_from_requires /python-base/d

%description
This repository contains the community.general Ansible Collection. The
collection is a part of the Ansible package and includes many modules and
plugins supported by Ansible community which are not part of more specialized
community collections.

%package -n ansible
Summary: Curated set of Ansible collections included in addition to ansible-core
Group: System/Configuration/Other
License: GPL-3.0+ and Apache-2.0 and BSD-2-Clause and BSD-3-Clause and MIT and MPL-2.0 and PSF-2.0
Requires: ansible-core
Requires: %name = %EVR

%description -n ansible
Ansible is a radically simple model-driven configuration management,
multi-node deployment, and remote task execution system. Ansible works
over SSH and does not require any software or daemons to be installed
on remote nodes. Extension modules can be written in any language and
are transferred to managed machines automatically.

This package provides a curated set of Ansible collections included in addition
to ansible-core

%prep
%setup -n %name-%version
# Use same galaxy.yml as main collection for plugins directory
ln -s ../galaxy.yml plugins/
# Set correct python3 executable in shebang
subst 's|#!.*python$|#!%__python3|' $(grep -Rl '#!.*python$' *)
# Remove tests
rm -rf tests

%install
# Install community.general
mkdir -p %buildroot%python3_sitelibdir/ansible_collections/community/general
cp -a * %buildroot%python3_sitelibdir/ansible_collections/community/general

# Install additional collections
tar xf %SOURCE1 -C %buildroot%python3_sitelibdir/ansible_collections/community --strip-components=2

# Remove tests
find %buildroot%python3_sitelibdir/ansible_collections -name tests | xargs rm -rf

%files
%doc README.md CHANGELOG.rst
%python3_sitelibdir/ansible_collections/*

%files -n ansible

%changelog
* Mon Dec 11 2023 Andrey Cherepanov <cas@altlinux.org> 8.1.0-alt1
- New version (ALT #48437, #48533).

* Tue Nov 14 2023 Andrey Cherepanov <cas@altlinux.org> 8.0.2-alt1
- Initial build for Sisyphus.
