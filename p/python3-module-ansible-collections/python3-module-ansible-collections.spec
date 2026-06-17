Name:    python3-module-ansible-collections
Version: 13.1.0
Release: alt1

Summary: This repository contains the community.general and some other Ansible Collection
License: GPL-3.0+ and Apache-2.0 and BSD-2-Clause and BSD-3-Clause and MIT and MPL-2.0 and PSF-2.0
Group:   Development/Python3
URL:     https://github.com/ansible-collections/community.general

Source: %name-%version.tar
Source1: submodules.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%filter_from_requires /python3(ansible.module_utils.six.moves/d
%filter_from_requires /python-base/d
# Using only in tests
%add_python3_req_skip nox

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
tar xf %SOURCE1 -C %buildroot%python3_sitelibdir/ansible_collections --strip-components=1

# Remove tests
find %buildroot%python3_sitelibdir/ansible_collections -name tests | xargs rm -rf
# remove unused scripts
rm -rv %buildroot%python3_sitelibdir/ansible_collections/community/postgresql/.azure-pipelines/

%files
%doc README.md CHANGELOG.rst
%python3_sitelibdir/ansible_collections/

%files -n ansible

%changelog
* Wed Jun 17 2026 Andrey Cherepanov <cas@altlinux.org> 13.1.0-alt1
- New version.

* Thu May 28 2026 Andrey Cherepanov <cas@altlinux.org> 13.0.1-alt2
- community.mysql -> ansible.mysql.

* Tue May 26 2026 Andrey Cherepanov <cas@altlinux.org> 13.0.1-alt1
- New version.

* Tue May 19 2026 Andrey Cherepanov <cas@altlinux.org> 13.0.0-alt1
- New version.

* Mon May 18 2026 Andrey Cherepanov <cas@altlinux.org> 12.6.1-alt1
- New version.

* Tue Apr 21 2026 Andrey Cherepanov <cas@altlinux.org> 12.6.0-alt1
- New version.

* Tue Mar 24 2026 Andrey Cherepanov <cas@altlinux.org> 12.5.0-alt1
- New version.

* Tue Feb 24 2026 Andrey Cherepanov <cas@altlinux.org> 12.4.0-alt1
- New version.

* Tue Jan 27 2026 Andrey Cherepanov <cas@altlinux.org> 12.3.0-alt1
- New version.

* Tue Dec 30 2025 Andrey Cherepanov <cas@altlinux.org> 12.2.0-alt1
- New version.

* Tue Dec 02 2025 Andrey Cherepanov <cas@altlinux.org> 12.1.0-alt1
- New version.

* Tue Nov 11 2025 Andrey Cherepanov <cas@altlinux.org> 12.0.1-alt1
- New version.

* Tue Nov 04 2025 Andrey Cherepanov <cas@altlinux.org> 12.0.0-alt1
- New version.

* Mon Nov 03 2025 Andrey Cherepanov <cas@altlinux.org> 11.4.1-alt1
- New version.

* Fri Oct 10 2025 Andrey Cherepanov <cas@altlinux.org> 11.4.0-alt1
- New version.

* Tue Sep 09 2025 Andrey Cherepanov <cas@altlinux.org> 11.3.0-alt1
- New version.

* Tue Aug 19 2025 Andrey Cherepanov <cas@altlinux.org> 11.2.1-alt1
- New version.

* Thu Aug 14 2025 Andrey Cherepanov <cas@altlinux.org> 11.2.0-alt1
- New version.

* Tue Aug 05 2025 Andrey Cherepanov <cas@altlinux.org> 11.1.2-alt1
- New version.

* Tue Jul 29 2025 Andrey Cherepanov <cas@altlinux.org> 11.1.1-alt1
- New version.

* Tue Jul 15 2025 Andrey Cherepanov <cas@altlinux.org> 11.1.0-alt1
- New version.

* Wed Jun 18 2025 Andrey Cherepanov <cas@altlinux.org> 11.0.0-alt2
- Removed python3(nox) from autoreq because it is used only in tests.

* Tue Jun 17 2025 Andrey Cherepanov <cas@altlinux.org> 11.0.0-alt1
- New version.

* Tue May 20 2025 Andrey Cherepanov <cas@altlinux.org> 10.7.0-alt1
- New version.

* Tue Apr 22 2025 Andrey Cherepanov <cas@altlinux.org> 10.6.0-alt1
- New version.

* Tue Mar 25 2025 Andrey Cherepanov <cas@altlinux.org> 10.5.0-alt1
- New version.

* Tue Feb 25 2025 Andrey Cherepanov <cas@altlinux.org> 10.4.0-alt1
- New version.

* Tue Feb 11 2025 Andrey Cherepanov <cas@altlinux.org> 10.3.1-alt1
- New version.

* Tue Jan 28 2025 Andrey Cherepanov <cas@altlinux.org> 10.3.0-alt1
- New version.

* Wed Jan 01 2025 Andrey Cherepanov <cas@altlinux.org> 10.2.0-alt1
- New version.

* Tue Dec 03 2024 Andrey Cherepanov <cas@altlinux.org> 10.1.0-alt1
- New version.

* Tue Nov 12 2024 Andrey Cherepanov <cas@altlinux.org> 10.0.1-alt1
- New version.

* Tue Nov 05 2024 Andrey Cherepanov <cas@altlinux.org> 10.0.0-alt1
- New version.

* Mon Nov 04 2024 Andrey Cherepanov <cas@altlinux.org> 9.5.1-alt1
- New version.

* Tue Oct 08 2024 Andrey Cherepanov <cas@altlinux.org> 9.5.0-alt1
- New version.

* Tue Sep 10 2024 Andrey Cherepanov <cas@altlinux.org> 9.4.0-alt1
- New version.

* Tue Aug 13 2024 Andrey Cherepanov <cas@altlinux.org> 9.3.0-alt1
- New version.

* Tue Jul 16 2024 Andrey Cherepanov <cas@altlinux.org> 9.2.0-alt1
- New version.

* Tue Jun 18 2024 Andrey Cherepanov <cas@altlinux.org> 9.1.0-alt1
- New version.

* Tue May 28 2024 Andrey Cherepanov <cas@altlinux.org> 9.0.1-alt1
- New version.

* Tue May 21 2024 Andrey Cherepanov <cas@altlinux.org> 9.0.0-alt1
- New version.

* Tue Apr 23 2024 Andrey Cherepanov <cas@altlinux.org> 8.6.0-alt1
- New version.

* Wed Mar 27 2024 Andrey Cherepanov <cas@altlinux.org> 8.5.0-alt1
- New version.

* Sun Mar 03 2024 Vitaly Lipatov <lav@altlinux.ru> 8.4.0-alt2
- remove unused azure scripts
- fix ansible_collections dir packing

* Tue Feb 27 2024 Andrey Cherepanov <cas@altlinux.org> 8.4.0-alt1
- New version.

* Tue Jan 30 2024 Andrey Cherepanov <cas@altlinux.org> 8.3.0-alt1
- New version.

* Wed Jan 03 2024 Andrey Cherepanov <cas@altlinux.org> 8.2.0-alt1
- New version.

* Mon Dec 11 2023 Andrey Cherepanov <cas@altlinux.org> 8.1.0-alt1
- New version (ALT #48437, #48533).

* Tue Nov 14 2023 Andrey Cherepanov <cas@altlinux.org> 8.0.2-alt1
- Initial build for Sisyphus.
