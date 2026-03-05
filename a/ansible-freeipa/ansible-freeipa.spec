%define _unpackaged_files_terminate_build 1

Name: ansible-freeipa
Version: 1.16.0
Release: alt1

Summary: Ansible roles and modules for FreeIPA
License: GPLv3
Group: System/Configuration/Other
Url: https://github.com/freeipa/ansible-freeipa
Vcs: https://github.com/freeipa/ansible-freeipa.git

Source: %name-%version.tar
Patch0: alt-time-servers.patch
Patch1: alt-vars.patch
Patch2: alt-nss-fstore.patch

%add_findreq_skiplist */roles/* */plugins/*

BuildArch: noarch
BuildRequires(pre): rpm-build-python3

Requires: ansible-core

%description
The package contains Ansible roles and playbooks to install and uninstall
FreeIPA servers, replicas and clients. Also modules for group, host, topology
and user management.

%prep
%setup
%autopatch -p1
%python3_fix_shebang .

%build

%install
install -m 755 -d %buildroot%_datadir/ansible/roles/
for mod in ipa{backup,client,server,replica,smartcard_client,smartcard_server}; do
    cp -r roles/$mod %buildroot%_datadir/ansible/roles/
done

install -m 755 -d %buildroot%_datadir/ansible/plugins/
cp -r plugins/* %buildroot%_datadir/ansible/plugins/

%files
%_datadir/ansible/roles/ipaserver/
%_datadir/ansible/roles/ipareplica/
%_datadir/ansible/roles/ipaclient/
%_datadir/ansible/roles/ipabackup/
%_datadir/ansible/roles/ipasmartcard_client/
%_datadir/ansible/roles/ipasmartcard_server/
%_datadir/ansible/plugins/doc_fragments/*
%_datadir/ansible/plugins/module_utils/*
%_datadir/ansible/plugins/modules/*
%_datadir/ansible/plugins/inventory/*
%doc README*.md
%doc playbooks

%changelog
* Fri Feb 27 2026 Aleksandr A. Voyt <sobue@altlinux.org> 1.16.0-alt1
- Update to 1.16.0 (Closes: #49416, #56048)

* Mon Dec 18 2023 Slava Aseev <ptrnine@altlinux.org> 1.12.0-alt1
- Update to new version

* Thu Sep 15 2022 Slava Aseev <ptrnine@altlinux.org> 1.8.4-alt1
- Update to new version

* Tue Dec 07 2021 Slava Aseev <ptrnine@altlinux.org> 1.5.0-alt1
- Update to new version

* Tue Dec 07 2021 Slava Aseev <ptrnine@altlinux.org> 0.4.2-alt2
- Add missing Altlinux.yml for ipareplica
- Remove unnecessary dependencies (and utils directory)

* Tue Oct 26 2021 Slava Aseev <ptrnine@altlinux.org> 0.4.2-alt1
- Initial build for ALT

