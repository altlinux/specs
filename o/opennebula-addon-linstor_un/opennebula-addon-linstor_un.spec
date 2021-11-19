%define _groupname	oneadmin
%define _username	oneadmin
%define _destination	%_localstatedir/one/remotes

Summary: Community driven full-feature Linstor storage driver for OpenNebula
Name: opennebula-addon-linstor_un
Version: 1.8.2
Release: alt1
License: Apache-2.0
Group: System/Servers
Url: https://github.com/OpenNebula/addon-linstor_un
# git-vcs: https://github.com/OpenNebula/addon-linstor_un.git
Source: %name-%version.tar
Patch: %name-%version.patch
Packager: Andrew A. Vasilyev <andy@altlinux.org>
BuildArch: noarch

Requires: jq linstor-satellite opennebula-server >= 5.8

%description
Community driven full-feature Linstor storage driver for OpenNebula.

%prep
%setup
%patch -p1

%install
install -d -m755 %buildroot%_destination/vmm/kvm
install -d -m755 %buildroot%_destination/datastore/linstor_un
install -d -m755 %buildroot%_destination/tm/linstor_un
install -d -m755 %buildroot%_destination/etc/datastore/linstor_un
install -m755 vmm/kvm/* %buildroot%_destination/vmm/kvm
install -m755 datastore/linstor_un/* %buildroot%_destination/datastore/linstor_un
install -m755 tm/linstor_un/* %buildroot%_destination/tm/linstor_un
install -m755 datastore/linstor_un/linstor_un.conf %buildroot%_destination/etc/datastore/linstor_un

%pre

%post
if [ "$1" -eq 1 ]; then
# In install, not update
# Update oned.conf

sed -i -e 's/ 0 kvm/ 0 kvm -l save=save_linstor_un,restore=restore_linstor_un/' /etc/one/oned.conf
sed -i -E 's/( -d dummy.*) -s (.*)$/\1,linstor_un -s \2/' /etc/one/oned.conf
sed -i -E 's/( -d dummy.*)"$/\1,linstor_un"/' /etc/one/oned.conf

cat >> /etc/one/oned.conf <<EOF

TM_MAD_CONF = [
    NAME = "linstor_un", LN_TARGET = "NONE", CLONE_TARGET = "SYSTEM", SHARED = "yes",
    DS_MIGRATE = "YES", DRIVER = "raw", ALLOW_ORPHANS="yes"
]

DS_MAD_CONF = [
    NAME = "linstor_un", PERSISTENT_ONLY = "NO",
    MARKETPLACE_ACTIONS = "export"
]

EOF

fi

%files
%doc README.md LICENSE
%_destination/vmm/kvm/*
%_destination/datastore/linstor_un
%_destination/tm/linstor_un
%dir %_destination/etc/datastore/linstor_un
%config(noreplace) %_destination/etc/datastore/linstor_un/linstor_un.conf

%changelog
* Fri Nov 19 2021 Andrew A. Vasilyev <andy@altlinux.org> 1.8.2-alt1
- 1.8.2

* Wed Jan 20 2021 Andrew A. Vasilyev <andy@altlinux.org> 1.7.4-alt1
- 1.7.4

* Thu Jan 14 2021 Andrew A. Vasilyev <andy@altlinux.org> 1.7.3-alt1
- 1.7.3

* Thu Nov 26 2020 Andrew A. Vasilyev <andy@altlinux.org> 1.7.2-alt1
- 1.7.2

* Tue Aug 25 2020 Andrew A. Vasilyev <andy@altlinux.org> 1.7.1-alt1
- 1.7.1

* Sat Jul 18 2020 Andrew A. Vasilyev <andy@altlinux.org> 1.7.0-alt1
- 1.7.0
- set LEGACY_MONITORING by default for OpenNebula 5.10- support

* Mon Jun 29 2020 Andrew A. Vasilyev <andy@altlinux.org> 1.6.3-alt1
- 1.6.3

* Wed Jun 24 2020 Andrew A. Vasilyev <andy@altlinux.org> 1.6.2-alt1
- 1.6.2
- revert build for arm arch

* Thu Jun 18 2020 Alexey Shabalin <shaba@altlinux.org> 1.6.1-alt2
- exclude build for arm arch

* Wed Jun 03 2020 Andrew A. Vasilyev <andy@altlinux.org> 1.6.1-alt1
- 1.6.1

* Wed May 20 2020 Andrew A. Vasilyev <andy@altlinux.org> 1.6.0-alt1
- 1.6.0

* Fri May 15 2020 Andrew A. Vasilyev <andy@altlinux.org> 1.5.3-alt1
- 1.5.3

* Wed Apr 29 2020 Andrew A. Vasilyev <andy@altlinux.org> 1.5.1-alt1
- 1.5.1

* Fri Apr 24 2020 Andrew A. Vasilyev <andy@altlinux.org> 1.5.0-alt1
- 1.5.0

* Thu Apr 23 2020 Andrew A. Vasilyev <andy@altlinux.org> 1.4.1-alt1
- 1.4.1

* Thu Apr 23 2020 Andrew A. Vasilyev <andy@altlinux.org> 1.4.0-alt1
- 1.4.0

* Thu Apr 02 2020 Andrew A. Vasilyev <andy@altlinux.org> 1.3.0-alt1
- initial build for ALT

