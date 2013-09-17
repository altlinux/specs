%define policy_name altlinux
%define date 20130917
%define seconf %_sysconfdir/selinux/config
%define default_mode permissive

Summary: SELinux %policy_name policy
Name: selinux-policy-altlinux
Version: 0.0.2
Release: alt6
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
Requires: policycoreutils-gui
Requires: policycoreutils-restorecond
Requires: libshell
Requires: m4
Requires: netlabel_tools
Requires: setools-console

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

# XXX
mkdir -p /etc/selinux/altlinux/contexts/files
touch /etc/selinux/altlinux/contexts/files/file_contexts.local
# XXX

# Always install all modules
for i in %policy_data/modules/*.pp; do
echo -e "\t\t* Install module $(basename "$i")" 
semodule -n -s %policy_name -i "$i"
done

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
%dir %policy_data/support
%dir %policy_data/modules
%dir %_sysconfdir/security/alt.newrole

%policy_conf/contexts/dbus_contexts
%policy_conf/contexts/default_contexts
%policy_conf/contexts/default_type
%policy_conf/contexts/x_contexts
%policy_conf/contexts/netfilter_contexts
%policy_conf/contexts/securetty_types

%policy_data/*.pp
%policy_data/modules/*.pp
%policy_data/*.if

%policy_data/support/*.spt
%policy_data/Makefile

%attr(0755,root,root) %_sysconfdir/security/alt.newrole/helper
%attr(0755,root,root) %_sysconfdir/security/alt.newrole/mkdirs
%config(noreplace) %_sysconfdir/security/alt.newrole/dirs
%config(noreplace) %_sysconfdir/security/alt.newrole/config

%_bindir/kde4sl

/lib/systemd/selinux-autorelabel
%_unitdir/selinux-autorelabel-mark.service
%_unitdir/selinux-autorelabel.service
%_unitdir/sysinit.target.wants/selinux-autorelabel.service

%doc /usr/share/doc/selinux-policy-altlinux/README

%changelog
* Tue Sep 17 2013 Andriy Stepanov <stanv@altlinux.ru> 0.0.2-alt6
- Build: 20130917

* Thu Sep 12 2013 Andriy Stepanov <stanv@altlinux.ru> 0.0.2-alt5
- Build: 20130912

* Thu Sep 05 2013 Andriy Stepanov <stanv@altlinux.ru> 0.0.2-alt4
- Build: 20130905

* Thu Jul 25 2013 Andriy Stepanov <stanv@altlinux.ru> 0.0.2-alt3
- Build: 20130725

* Wed Jun 19 2013 Andriy Stepanov <stanv@altlinux.ru> 0.0.2-alt2
- Post script for modules

* Wed Jun 19 2013 Andriy Stepanov <stanv@altlinux.ru> 0.0.2-alt1
- Build: 20130619

* Mon May 20 2013 Andriy Stepanov <stanv@altlinux.ru> 0.0.1-alt4
- Build: 20130520

* Wed Apr 24 2013 Andriy Stepanov <stanv@altlinux.ru> 0.0.1-alt3
- Build: 20130425

* Fri Apr 19 2013 Andriy Stepanov <stanv@altlinux.ru> 0.0.1-alt2
- Build: 20130422

* Wed Apr 17 2013 Andriy Stepanov <stanv@altlinux.ru> 0.0.1-alt1
- Initial. Build version from: 20130417
