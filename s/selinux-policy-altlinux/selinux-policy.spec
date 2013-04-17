%define policy_name altlinux
%define date 20130417

Summary: SELinux %policy_name policy
Name: selinux-policy-altlinux
Version: 0.0.1
Release: alt1
License: %distributable
Group: System/Base
Source: %name-%date.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-licenses
Requires(pre): libsemanage
Requires(pre): policycoreutils
Requires(pre): policycoreutils-newrole

Requires: policycoreutils-newrole
Requires: checkpolicy
Requires: policycoreutils-mcstransd
Requires: policycoreutils-restorecond

%define policy_conf %_sysconfdir/selinux/%policy_name
%define policy_data %_datadir/selinux/%policy_name

%description
SELinux %policy_name policy

%prep 
%setup -n %name

%install
mkdir %buildroot
cp -a * %buildroot

%post
%{echo:Install new SeLinux base module to %policy_conf}
semodule -n -s %policy_name -b %policy_data/base.pp
touch /.autorelabel

%files 
%dir %policy_conf
%dir %policy_conf/contexts
%dir %policy_conf/contexts/users
%dir %policy_conf/contexts/files
%dir %policy_conf/modules
%dir %policy_conf/modules/active
%dir %policy_conf/modules/active/modules
%dir %policy_conf/policy
%dir %policy_data
%dir %_sysconfdir/secutiry/alt.newrole

%policy_conf/contexts/dbus_contexts
%policy_conf/contexts/default_contexts
%policy_conf/contexts/default_type
%policy_conf/contexts/x_contexts
%policy_conf/contexts/netfilter_contexts
%policy_conf/contexts/securetty_types

%policy_data/*.pp

%_sysconfdir/secutiry/alt.newrole/helper
%_sysconfdir/secutiry/alt.newrole/mktmpdir
%_sysconfdir/secutiry/alt.newrole/mkworkdir

/lib/systemd/selinux-autorelabel
/lib/systemd/system/selinux-autorelabel-mark.service
/lib/systemd/system/selinux-autorelabel.service

%doc /usr/share/doc/selinux-policy-altlinux/README

%changelog
* Wed Apr 17 2013 Andriy Stepanov <stanv@altlinux.ru> 0.0.1-alt1
- Initial. Build version from: 20130417
