%define _unpackaged_files_terminate_build 1

Name: ansible-freeipa
Version: 0.4.2
Release: alt2

Summary: Ansible roles and modules for FreeIPA
License: GPLv3
Group: System/Configuration/Other
Url: https://github.com/freeipa/ansible-freeipa

# https://github.com/freeipa/ansible-freeipa.git
Source: %name-%version.tar
Patch: %name-%version-alt.patch

%add_findreq_skiplist */roles/* */plugins/*

BuildArch: noarch
BuildRequires(pre): rpm-build-python3

%description
The package contains Ansible roles and playbooks to install and uninstall
FreeIPA servers, replicas and clients. Also modules for group, host, topology
and user management.

%package tests
Summary: ansible-freeipa tests
Group: Development/Python3
Requires: %name = %EVR

%description tests
Tests for FreeIPA Ansible roles and modules

%prep
%setup
%patch -p1

# Fix shebangs
grep -rlE '#!/usr/bin/(env )?python' | xargs subst 's|^#!/usr/bin/\(env \)\?python|#!/usr/bin/python3|'

%build

%install
install -m 755 -d %buildroot%_datadir/ansible/roles/
for mod in ipa{backup,client,server,replica}; do
    cp -r roles/$mod %buildroot%_datadir/ansible/roles/
    cp -r roles/$mod/README.md README-server.md
done

install -m 755 -d %buildroot%_datadir/ansible/plugins/
cp -r plugins/* %buildroot%_datadir/ansible/plugins/

install -m 755 -d %buildroot%_datadir/%name
cp requirements{,-dev}.txt %buildroot%_datadir/%name/

# Install tests
cp requirements-tests.txt %buildroot%_datadir/%name/
install -m 755 -d %buildroot%_datadir/%name/tests
cp -r tests %buildroot%_datadir/%name/

%files
%_datadir/ansible/roles/ipaserver
%_datadir/ansible/roles/ipareplica
%_datadir/ansible/roles/ipaclient
%_datadir/ansible/roles/ipabackup
%_datadir/ansible/plugins/doc_fragments/*
%_datadir/ansible/plugins/module_utils/*
%_datadir/ansible/plugins/modules/*
%doc README*.md
%doc playbooks
%_datadir/%name
%exclude %_datadir/%name/requirements-tests.txt
%exclude %_datadir/%name/tests

%files tests
%_datadir/%name/requirements-tests.txt
%_datadir/%name/tests

%changelog
* Tue Dec 07 2021 Slava Aseev <ptrnine@altlinux.org> 0.4.2-alt2
- Add missing Altlinux.yml for ipareplica
- Remove unnecessary dependencies (and utils directory)

* Tue Oct 26 2021 Slava Aseev <ptrnine@altlinux.org> 0.4.2-alt1
- Initial build for ALT

