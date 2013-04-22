%define policy_name altlinux
%define date 20130422
%define seconf %_sysconfdir/selinux/config
%define default_mode permissive

Summary: SELinux %policy_name policy
Name: selinux-policy-altlinux
Version: 0.0.1
Release: alt2
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
Requires: libshell

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
# Always install new policy
semodule -n -s %policy_name -b %policy_data/base.pp

# Install
if [ $1 -eq 1 ]; then
    echo "Warning:"
    echo -e "\tUpdate SeLinux config: %seconf"
    ( . shell-config; shell_config_set "%seconf" "SELINUX" "%default_mode" )
    ( . shell-config; shell_config_set "%seconf" "SELINUXTYPE" "%policy_name" )

    # Relabel all FileSystem
    echo -e "\tSeLinux Policy installed for the first time."
    echo -e "\tMake sure to:"
    echo -e "\t\t * enable SeLinux in kernel."
    echo -e "\t\t * configure PAM for SeLinux."
    echo -e "\tIt is necessary to relabel FS. Please do a reboot."
    echo -e "\tDefault mode is: %default_mode."
    echo -e "\tFor more information visit: http://www.altlinux.org/sl"
    # XXX: suppose there are no other working policy.
    touch /.autorelabel
fi

# Upgrade
if [ $1 -eq 2 ]; then
:
fi


%postun
# XXX: Actual policy still remains installed in /etc/selinux/

# Uninstall RPM package
if [ $1 = 0 ]; then
    echo "Warning:"
    echo -e "\tSet SeLinux enforcing mode to permissive."
    selinuxenabled && setenforce 0
    echo -e "\tDisable SeLinux in config: %seconf"
    ( . shell-config; shell_config_set "%seconf" "SELINUX" "disabled" )
fi


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

%attr(0755,root,root) %_sysconfdir/secutiry/alt.newrole/helper
%attr(0755,root,root) %_sysconfdir/secutiry/alt.newrole/mktmpdir
%attr(0755,root,root) %_sysconfdir/secutiry/alt.newrole/mkworkdir
%config(noreplace) %_sysconfdir/secutiry/alt.newrole/config

/lib/systemd/selinux-autorelabel
%_unitdir/selinux-autorelabel-mark.service
%_unitdir/selinux-autorelabel.service
%_unitdir/sysinit.target.wants/selinux-autorelabel.service

%doc /usr/share/doc/selinux-policy-altlinux/README

%changelog
* Fri Apr 19 2013 Andriy Stepanov <stanv@altlinux.ru> 0.0.1-alt2
- Build: 20130422

* Wed Apr 17 2013 Andriy Stepanov <stanv@altlinux.ru> 0.0.1-alt1
- Initial. Build version from: 20130417
