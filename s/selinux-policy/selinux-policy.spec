%define distro alt
%define polyinstatiate n
%define monolithic n
%if %{?BUILD_TARGETED:0}%{!?BUILD_TARGETED:1}
%define BUILD_TARGETED 1
%endif
%if %{?BUILD_MINIMUM:0}%{!?BUILD_MINIMUM:1}
%define BUILD_MINIMUM 1
%endif
%if %{?BUILD_MLS:0}%{!?BUILD_MLS:1}
%define BUILD_MLS 1
%endif
%define POLICYVER 24
%define libsepol_ver 2.0.41
%define policycoreutils_ver 2.0.79
%define checkpolicy_ver 2.0.21

%define fc_ver .fc3.9.13

Summary: SELinux policy configuration
Name: selinux-policy
Version: 2.20101213
Release: alt1%fc_ver.1
License: %gpl2plus
Group: System/Base
Source: serefpolicy-%version-%release.tar
Source1: modules-targeted.conf
Source2: booleans-targeted.conf
Source3: Makefile.devel
Source4: setrans-targeted.conf
Source5: modules-mls.conf
Source6: booleans-mls.conf
Source8: setrans-mls.conf
Source14: securetty_types-targeted
Source15: securetty_types-mls
Source17: booleans-minimum.conf
Source18: setrans-minimum.conf
Source19: securetty_types-minimum
Source20: customizable_types
Source22: users-mls
Source23: users-targeted
Source25: users-minimum

Url: http://oss.tresys.com/projects/refpolicy
BuildArch: noarch
BuildRequires(pre): rpm-build-licenses
BuildRequires: gawk checkpolicy >= %checkpolicy_ver m4 policycoreutils >= %policycoreutils_ver bzip2
Requires(pre): policycoreutils >= %policycoreutils_ver libsemanage
Requires: checkpolicy >= %checkpolicy_ver m4 

%description 
SELinux Base package

%files 
%_mandir/man*/*
# policycoreutils owns these manpage directories, we only own the files within them
%_mandir/ru/*/*
%dir %_datadir/selinux
%dir %_datadir/selinux/devel
%dir %_datadir/selinux/devel/include
%dir %_datadir/selinux/packages
%dir %_sysconfdir/selinux
%ghost %config(noreplace) %_sysconfdir/selinux/config
%ghost %_sysconfdir/sysconfig/selinux
%_datadir/selinux/devel/include/*
%_datadir/selinux/devel/Makefile
%_datadir/selinux/devel/example.*
%_datadir/selinux/devel/policy.*

%package doc
Summary: SELinux policy documentation
Group: System/Base
Requires(pre): selinux-policy = %version-%release
Requires: xdg-utils

%description doc
SELinux policy documentation package

%files doc
%doc %_datadir/doc/%name-%version
%attr(755,root,root) %_datadir/selinux/devel/policyhelp

%check
if [ -x /usr/sbin/selinuxenabled ] && /usr/sbin/selinuxenabled; then
/usr/bin/sepolgen-ifgen -i %buildroot%_datadir/selinux/devel/include -o /dev/null
fi

%define makeCmds() \
make UNK_PERMS=%5 NAME=%1 TYPE=%2 DISTRO=%distro UBAC=n DIRECT_INITRC=%3 MONOLITHIC=%monolithic POLY=%4 MLS_CATS=1024 MCS_CATS=1024 bare \
make UNK_PERMS=%5 NAME=%1 TYPE=%2 DISTRO=%distro UBAC=n DIRECT_INITRC=%3 MONOLITHIC=%monolithic POLY=%4 MLS_CATS=1024 MCS_CATS=1024  conf \
cp -f selinux_config/modules-%1.conf  ./policy/modules.conf \
cp -f selinux_config/booleans-%1.conf ./policy/booleans.conf \
cp -f selinux_config/users-%1 ./policy/users \

%define installCmds() \
make UNK_PERMS=%5 NAME=%1 TYPE=%2 DISTRO=%distro UBAC=n DIRECT_INITRC=%3 MONOLITHIC=%monolithic POLY=%4 MLS_CATS=1024 MCS_CATS=1024 base.pp \
make validate UNK_PERMS=%5 NAME=%1 TYPE=%2 DISTRO=%distro UBAC=n DIRECT_INITRC=%3 MONOLITHIC=%monolithic POLY=%4 MLS_CATS=1024 MCS_CATS=1024 modules \
make UNK_PERMS=%5 NAME=%1 TYPE=%2 DISTRO=%distro UBAC=n DIRECT_INITRC=%3 MONOLITHIC=%monolithic DESTDIR=%buildroot POLY=%4 MLS_CATS=1024 MCS_CATS=1024 install \
make UNK_PERMS=%5 NAME=%1 TYPE=%2 DISTRO=%distro UBAC=n DIRECT_INITRC=%3 MONOLITHIC=%monolithic DESTDIR=%buildroot POLY=%4 MLS_CATS=1024 MCS_CATS=1024 install-appconfig \
#cp *.pp %buildroot/%_datadir/selinux/%1/ \
mkdir -p %buildroot/%_sysconfdir/selinux/%1/policy \
mkdir -p %buildroot/%_sysconfdir/selinux/%1/modules/active \
mkdir -p %buildroot/%_sysconfdir/selinux/%1/contexts/files \
touch %buildroot/%_sysconfdir/selinux/%1/modules/semanage.read.LOCK \
touch %buildroot/%_sysconfdir/selinux/%1/modules/semanage.trans.LOCK \
rm -rf %buildroot%_sysconfdir/selinux/%1/booleans \
touch %buildroot%_sysconfdir/selinux/%1/seusers \
touch %buildroot%_sysconfdir/selinux/%1/policy/policy.%POLICYVER \
touch %buildroot%_sysconfdir/selinux/%1/contexts/files/file_contexts \
touch %buildroot%_sysconfdir/selinux/%1/contexts/files/file_contexts.homedirs \
install -m0644 selinux_config/securetty_types-%1 %buildroot%_sysconfdir/selinux/%1/contexts/securetty_types \
install -m0644 selinux_config/setrans-%1.conf %buildroot%_sysconfdir/selinux/%1/setrans.conf \
install -m0644 selinux_config/customizable_types %buildroot%_sysconfdir/selinux/%1/contexts/customizable_types \
bzip2 %buildroot/%_datadir/selinux/%1/*.pp \
awk '$1 !~ "/^#/" && $2 == "=" && $3 == "module" { printf "%%s.pp.bz2 ", $1 }' ./policy/modules.conf > %buildroot/%_datadir/selinux/%1/modules.lst
%nil

%define fileList() \
%dir %_datadir/selinux/%1 \
%_datadir/selinux/%1/*.pp.bz2 \
%_datadir/selinux/%1/modules.lst \
%dir %_sysconfdir/selinux/%1 \
%config(noreplace) %_sysconfdir/selinux/%1/setrans.conf \
%ghost %_sysconfdir/selinux/%1/seusers \
%dir %_sysconfdir/selinux/%1/modules \
%verify(not mtime) %_sysconfdir/selinux/%1/modules/semanage.read.LOCK \
%verify(not mtime) %_sysconfdir/selinux/%1/modules/semanage.trans.LOCK \
%attr(700,root,root) %dir %_sysconfdir/selinux/%1/modules/active \
#%verify(not md5 size mtime) %attr(600,root,root) %config(noreplace) %_sysconfdir/selinux/%1/modules/active/seusers \
%dir %_sysconfdir/selinux/%1/policy/ \
%ghost %_sysconfdir/selinux/%1/policy/policy.* \
%dir %_sysconfdir/selinux/%1/contexts \
%config %_sysconfdir/selinux/%1/contexts/customizable_types \
%config(noreplace) %_sysconfdir/selinux/%1/contexts/securetty_types \
%config(noreplace) %_sysconfdir/selinux/%1/contexts/dbus_contexts \
%config %_sysconfdir/selinux/%1/contexts/x_contexts \
%config %_sysconfdir/selinux/%1/contexts/default_contexts \
%config %_sysconfdir/selinux/%1/contexts/virtual_domain_context \
%config %_sysconfdir/selinux/%1/contexts/virtual_image_context \
%config %_sysconfdir/selinux/%1/contexts/sepgsql_contexts \
%config(noreplace) %_sysconfdir/selinux/%1/contexts/default_type \
%config(noreplace) %_sysconfdir/selinux/%1/contexts/failsafe_context \
%config(noreplace) %_sysconfdir/selinux/%1/contexts/initrc_context \
%config(noreplace) %_sysconfdir/selinux/%1/contexts/removable_context \
%config(noreplace) %_sysconfdir/selinux/%1/contexts/userhelper_context \
%dir %_sysconfdir/selinux/%1/contexts/files \
%ghost %_sysconfdir/selinux/%1/contexts/files/file_contexts \
%ghost %_sysconfdir/selinux/%1/contexts/files/file_contexts.homedirs \
%config %_sysconfdir/selinux/%1/contexts/files/media \
%dir %_sysconfdir/selinux/%1/contexts/users \
%config(noreplace) %_sysconfdir/selinux/%1/contexts/users/root \
%config(noreplace) %_sysconfdir/selinux/%1/contexts/users/guest_u \
%config(noreplace) %_sysconfdir/selinux/%1/contexts/users/xguest_u \
%config(noreplace) %_sysconfdir/selinux/%1/contexts/users/user_u \
%config(noreplace) %_sysconfdir/selinux/%1/contexts/users/staff_u 

%define saveFileContext() \
if [ -s /etc/selinux/config ]; then \
     . %_sysconfdir/selinux/config; \
     FILE_CONTEXT=%_sysconfdir/selinux/%1/contexts/files/file_contexts; \
     if [ "${SELINUXTYPE}" = %1 -a -f ${FILE_CONTEXT} ]; then \
        [ -f ${FILE_CONTEXT}.pre ] || cp -f ${FILE_CONTEXT} ${FILE_CONTEXT}.pre; \
     fi \
fi

%define loadpolicy() \
( cd /usr/share/selinux/%1; \
semodule -b base.pp.bz2 -i %2 -s %1; \
); \

%define relabel() \
. %_sysconfdir/selinux/config; \
FILE_CONTEXT=%_sysconfdir/selinux/%1/contexts/files/file_contexts; \
if selinuxenabled && [ "${SELINUXTYPE}" = %1 -a -f ${FILE_CONTEXT}.pre ]; then \
     fixfiles -C ${FILE_CONTEXT}.pre restore; \
     restorecon -R /root /var/log /var/run /var/lib 2> /dev/null; \
     rm -f ${FILE_CONTEXT}.pre; \
fi; 

%description
SELinux Reference Policy - modular.
Based off of reference policy: Checked out revision %version

%build

%prep 
%setup -n serefpolicy-%version-%release


%install
mkdir selinux_config
for i in %SOURCE1 %SOURCE2 %SOURCE3 %SOURCE4 %SOURCE5 %SOURCE6 %SOURCE8 %SOURCE14 %SOURCE15  %SOURCE17 %SOURCE18 %SOURCE19 %SOURCE20 %SOURCE22 %SOURCE23 %SOURCE25;do
 cp $i selinux_config
done
ln -s modules-targeted.conf selinux_config/modules-minimum.conf

# Build targeted policy
mkdir -p %buildroot%_mandir
cp -R  man/* %buildroot%_mandir
mkdir -p %buildroot%_sysconfdir/selinux
mkdir -p %buildroot%_sysconfdir/sysconfig
touch %buildroot%_sysconfdir/selinux/config
touch %buildroot%_sysconfdir/sysconfig/selinux

# Always create policy module package directories
mkdir -p %buildroot%_datadir/selinux/{targeted,mls,minimum,modules}/

# Install devel
make clean
%if %BUILD_TARGETED
# Build targeted policy
# Commented out because only targeted ref policy currently builds
%makeCmds targeted mcs n y allow
%installCmds targeted mcs n y allow
%endif

%if %BUILD_MINIMUM
# Build minimum policy
# Commented out because only minimum ref policy currently builds
%makeCmds minimum mcs n y allow
%installCmds minimum mcs n y allow
%endif

%if %BUILD_MLS
# Build mls policy
%makeCmds mls mls n y deny
%installCmds mls mls n y deny
%endif

make UNK_PERMS=allow NAME=targeted TYPE=mcs DISTRO=%distro UBAC=n DIRECT_INITRC=n MONOLITHIC=%monolithic DESTDIR=%buildroot PKGNAME=%name-%version POLY=y MLS_CATS=1024 MCS_CATS=1024 install-headers install-docs
mkdir %buildroot%_datadir/selinux/devel/
mkdir %buildroot%_datadir/selinux/packages/
mv %buildroot%_datadir/selinux/targeted/include %buildroot%_datadir/selinux/devel/include
install -m 644 selinux_config/Makefile.devel %buildroot%_datadir/selinux/devel/Makefile
install -m 644 doc/example.* %buildroot%_datadir/selinux/devel/
install -m 644 doc/policy.* %buildroot%_datadir/selinux/devel/
echo  "xdg-open file:///usr/share/doc/selinux-policy-%version/html/index.html"> %buildroot%_datadir/selinux/devel/policyhelp
chmod +x %buildroot%_datadir/selinux/devel/policyhelp
rm -rf selinux_config

%post
if [ ! -s /etc/selinux/config ]; then
#
#     New install so we will default to targeted policy
#
echo "
# This file controls the state of SELinux on the system.
# SELINUX= can take one of these three values:
#     enforcing - SELinux security policy is enforced.
#     permissive - SELinux prints warnings instead of enforcing.
#     disabled - No SELinux policy is loaded.
SELINUX=permissive
# SELINUXTYPE= can take one of these two values:
#     targeted - Targeted processes are protected,
#     mls - Multi Level Security protection.
SELINUXTYPE=targeted 

" > /etc/selinux/config

     ln -sf ../selinux/config /etc/sysconfig/selinux 
     restorecon /etc/selinux/config 2> /dev/null || :
     fixfiles onboot ||:
else
     . /etc/selinux/config
     # if first time update booleans.local needs to be copied to sandbox
     [ -f /etc/selinux/${SELINUXTYPE}/booleans.local ] && mv /etc/selinux/${SELINUXTYPE}/booleans.local /etc/selinux/targeted/modules/active/
     [ -f /etc/selinux/${SELINUXTYPE}/seusers ] && cp -f /etc/selinux/${SELINUXTYPE}/seusers /etc/selinux/${SELINUXTYPE}/modules/active/seusers
fi
exit 0

%postun
if [ $1 = 0 ]; then
     setenforce 0 2> /dev/null
     if [ ! -s /etc/selinux/config ]; then
          echo "SELINUX=disabled" > /etc/selinux/config
     else
          sed -i 's/^SELINUX=.*/SELINUX=disabled/g' /etc/selinux/config
     fi
fi
exit 0

%if %BUILD_TARGETED
%package targeted
Summary: SELinux targeted base policy
Group: System/Base
Requires(pre): policycoreutils >= %policycoreutils_ver
Requires(pre): coreutils
Requires(pre): selinux-policy = %version-%release
Requires: selinux-policy = %version-%release

%description targeted
SELinux Reference policy targeted base module.

%pre targeted
%saveFileContext targeted

%post targeted
packages=`cat /usr/share/selinux/targeted/modules.lst`
if [ $1 -eq 1 ]; then
   %loadpolicy targeted $packages
   restorecon -R /root /var/log /var/run /var/lib 2> /dev/null
else
   semodule -n -s targeted -r telepathysofiasip ethereal 2>/dev/null
   %loadpolicy targeted $packages
   %relabel targeted
fi
exit 0

%files targeted
%config(noreplace) %_sysconfdir/selinux/targeted/contexts/users/unconfined_u
%fileList targeted
%endif

%if %BUILD_MINIMUM
%package minimum
Summary: SELinux minimum base policy
Group: System/Base
Requires(post): policycoreutils >= %policycoreutils_ver
Requires(pre): coreutils
Requires(pre): selinux-policy = %version-%release
Requires: selinux-policy = %version-%release

%description minimum
SELinux Reference policy minimum base module.

%pre minimum
%saveFileContext minimum

%post minimum
packages="execmem.pp.bz2 unconfined.pp.bz2 unconfineduser.pp.bz2"
%loadpolicy minimum $packages
if [ $1 -eq 1 ]; then
semanage -S minimum -i - << __eof
login -m  -s unconfined_u -r s0-s0:c0.c1023 __default__
login -m  -s unconfined_u -r s0-s0:c0.c1023 root
__eof
restorecon -R /root /var/log /var/run /var/lib 2> /dev/null
else
%relabel minimum
fi
exit 0

%files minimum
%config(noreplace) %_sysconfdir/selinux/minimum/contexts/users/unconfined_u
%fileList minimum
%endif

%if %BUILD_MLS
%package mls 
Summary: SELinux mls base policy
Group: System/Base
Requires(pre): policycoreutils >= %policycoreutils_ver
Requires(pre): coreutils
Requires(pre): selinux-policy = %version-%release
Requires: selinux-policy = %version-%release

%description mls 
SELinux Reference policy mls base module.

%pre mls 
%saveFileContext mls

%post mls
semodule -n -s mls -r telepathysofiasip ethereal 2>/dev/null
packages=`cat /usr/share/selinux/mls/modules.lst`
%loadpolicy mls $packages

if [ $1 -eq 1 ]; then
   restorecon -R /root /var/log /var/run /var/lib 2> /dev/null
else
%relabel mls
fi
exit 0

%files mls
%config(noreplace) %_sysconfdir/selinux/mls/contexts/users/unconfined_u
%fileList mls

%endif

%changelog
* Wed May 23 2012 Mikhail Efremov <sem@altlinux.org> 2.20101213-alt1.fc3.9.13.1
- Don't generate context for gadgetfs and 9p
- Updated config/ from Fedora.
- logging_read_generic_logs: Allow link files read.
- allow auth_manage_shadow for local_login_t.
- Updated from Fedora git.

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.20100610-alt6.fc3.9.10.1
- Rebuild with Python-2.7

* Mon Dec 27 2010 Mikhail Efremov <sem@altlinux.org> 2.20100610-alt6.fc3.9.10
- allow auth_manage_shadow for local_login_t.

* Fri Dec 03 2010 Mikhail Efremov <sem@altlinux.org> 2.20100610-alt5.fc3.9.10
- Fix context for /tmp/.private/*.
- procmail_t: allow read symlinks in var_t.
- postfix_local_t: allow read symlinks in var_t.
- Updated from FC git.

* Tue Nov 16 2010 Mikhail Efremov <sem@altlinux.org> 2.20100610-alt4.fc3.9.7
- ALT-specific changes.

* Mon Nov 01 2010 Mikhail Efremov <sem@altlinux.org> 2.20100610-alt3.fc3.9.7
- Temporary allow unconfined_domain for NetworkManager_t.
- ALT-specific changes.
- Updated from FC git.

* Tue Aug 03 2010 Mikhail Efremov <sem@altlinux.org> 2.20100610-alt3.fc3.8.3
- Request relabel on the next reboot if it is first installation.
- Drop setting context for root filesystem /dev/*
    (it is moved to fixfiles(8)).

* Tue Aug 03 2010 Mikhail Efremov <sem@altlinux.org> 2.20100610-alt2.fc3.8.3
- allow module_request for sshd_t
- loadkeys_t: allow read console
- Allow manage tmp dir for local_login_t and sshd_t
- set context for root filesystem /dev/* files

* Mon Jun 28 2010 Mikhail Efremov <sem@altlinux.org> 2.20100610-alt1.fc3.8.3
- ALT-specific fixes
- Update policies from FC

* Thu Mar 04 2010 Mikhail Efremov <sem@altlinux.org> 2.20091117.fc3.7.10-alt1
- initial build for ALT Linux

* Tue Feb 22 2010 Dan Walsh <dwalsh@redhat.com> 3.7.10-3
- Additional policy for rgmanager

* Mon Feb 22 2010 Dan Walsh <dwalsh@redhat.com> 3.7.10-2
- Allow sshd to setattr on pseudo terms

* Mon Feb 22 2010 Dan Walsh <dwalsh@redhat.com> 3.7.10-1
- Update to upstream

* Thu Feb 18 2010 Dan Walsh <dwalsh@redhat.com> 3.7.9-4
- Allow policykit to send itself signals

* Wed Feb 17 2010 Dan Walsh <dwalsh@redhat.com> 3.7.9-3
- Fix duplicate cobbler definition

* Wed Feb 17 2010 Dan Walsh <dwalsh@redhat.com> 3.7.9-2
- Fix file context of /var/lib/avahi-autoipd

* Fri Feb 12 2010 Dan Walsh <dwalsh@redhat.com> 3.7.9-1
- Merge with upstream

* Thu Feb 11 2010 Dan Walsh <dwalsh@redhat.com> 3.7.8-11
- Allow sandbox to work with MLS 

* Tue Feb 9 2010 Dan Walsh <dwalsh@redhat.com> 3.7.8-9
- Make Chrome work with staff user

* Thu Feb 4 2010 Dan Walsh <dwalsh@redhat.com> 3.7.8-8
- Add icecast policy
- Cleanup  spec file

* Wed Feb 3 2010 Dan Walsh <dwalsh@redhat.com> 3.7.8-7
- Add mcelog policy

* Mon Feb 1 2010 Dan Walsh <dwalsh@redhat.com> 3.7.8-6
- Lots of fixes found in F12

* Thu Jan 27 2010 Dan Walsh <dwalsh@redhat.com> 3.7.8-5
- Fix rpm_dontaudit_leaks

* Wed Jan 27 2010 Dan Walsh <dwalsh@redhat.com> 3.7.8-4
- Add getsched to hald_t
- Add file context for Fedora/Redhat Directory Server

* Mon Jan 25 2010 Dan Walsh <dwalsh@redhat.com> 3.7.8-3
- Allow abrt_helper to getattr on all filesystems
- Add label for /opt/real/RealPlayer/plugins/oggfformat\.so     

* Thu Jan 21 2010 Dan Walsh <dwalsh@redhat.com> 3.7.8-2
- Add gstreamer_home_t for ~/.gstreamer

* Mon Jan 18 2010 Dan Walsh <dwalsh@redhat.com> 3.7.8-1
- Update to upstream

* Fri Jan 15 2010 Dan Walsh <dwalsh@redhat.com> 3.7.7-3
- Fix git

* Thu Jan 7 2010 Dan Walsh <dwalsh@redhat.com> 3.7.7-2
- Turn on puppet policy
- Update to dgrift git policy

* Mon Jan 7 2010 Dan Walsh <dwalsh@redhat.com> 3.7.7-1
- Move users file to selection by spec file.
- Allow vncserver to run as unconfined_u:unconfined_r:unconfined_t

* Thu Jan 7 2010 Dan Walsh <dwalsh@redhat.com> 3.7.6-1
- Update to upstream

* Wed Jan 6 2010 Dan Walsh <dwalsh@redhat.com> 3.7.5-8
- Remove most of the permissive domains from F12.

* Tue Jan 5 2010 Dan Walsh <dwalsh@redhat.com> 3.7.5-7
- Add cobbler policy from dgrift

* Mon Jan 4 2010 Dan Walsh <dwalsh@redhat.com> 3.7.5-6
- add usbmon device
- Add allow rulse for devicekit_disk

* Wed Dec 30 2009 Dan Walsh <dwalsh@redhat.com> 3.7.5-5
- Lots of fixes found in F12, fixes from Tom London

* Wed Dec 23 2009 Dan Walsh <dwalsh@redhat.com> 3.7.5-4
- Cleanups from dgrift

* Tue Dec 22 2009 Dan Walsh <dwalsh@redhat.com> 3.7.5-3
- Add back xserver_manage_home_fonts

* Mon Dec 21 2009 Dan Walsh <dwalsh@redhat.com> 3.7.5-2
- Dontaudit sandbox trying to read nscd and sssd

* Fri Dec 18 2009 Dan Walsh <dwalsh@redhat.com> 3.7.5-1
- Update to upstream

* Thu Dec 17 2009 Dan Walsh <dwalsh@redhat.com> 3.7.4-4
- Rename udisks-daemon back to devicekit_disk_t policy

* Wed Dec 16 2009 Dan Walsh <dwalsh@redhat.com> 3.7.4-3
- Fixes for abrt calls

* Fri Dec 11 2009 Dan Walsh <dwalsh@redhat.com> 3.7.4-2
- Add tgtd policy

* Fri Dec 4 2009 Dan Walsh <dwalsh@redhat.com> 3.7.4-1
- Update to upstream release

* Mon Nov 16 2009 Dan Walsh <dwalsh@redhat.com> 3.7.3-1
- Add asterisk policy back in
- Update to upstream release 2.20091117

* Mon Nov 16 2009 Dan Walsh <dwalsh@redhat.com> 3.7.1-1
- Update to upstream release 2.20091117

* Mon Nov 16 2009 Dan Walsh <dwalsh@redhat.com> 3.6.33-2
- Fixup nut policy

* Thu Nov 12 2009 Dan Walsh <dwalsh@redhat.com> 3.6.33-1
- Update to upstream

* Thu Oct 1 2009 Dan Walsh <dwalsh@redhat.com> 3.6.32-17
- Allow vpnc request the kernel to load modules

* Wed Sep 30 2009 Dan Walsh <dwalsh@redhat.com> 3.6.32-16
- Fix minimum policy installs
- Allow udev and rpcbind to request the kernel to load modules

* Wed Sep 30 2009 Dan Walsh <dwalsh@redhat.com> 3.6.32-15
- Add plymouth policy
- Allow local_login to sys_admin

* Tue Sep 29 2009 Dan Walsh <dwalsh@redhat.com> 3.6.32-13
- Allow cupsd_config to read user tmp
- Allow snmpd_t to signal itself
- Allow sysstat_t to makedir in sysstat_log_t

* Fri Sep 25 2009 Dan Walsh <dwalsh@redhat.com> 3.6.32-12
- Update rhcs policy

* Thu Sep 24 2009 Dan Walsh <dwalsh@redhat.com> 3.6.32-11
- Allow users to exec restorecond

* Tue Sep 21 2009 Dan Walsh <dwalsh@redhat.com> 3.6.32-10
- Allow sendmail to request kernel modules load

* Mon Sep 21 2009 Dan Walsh <dwalsh@redhat.com> 3.6.32-9
- Fix all kernel_request_load_module domains

* Mon Sep 21 2009 Dan Walsh <dwalsh@redhat.com> 3.6.32-8
- Fix all kernel_request_load_module domains

* Sun Sep 20 2009 Dan Walsh <dwalsh@redhat.com> 3.6.32-7
- Remove allow_exec* booleans for confined users.  Only available for unconfined_t

* Fri Sep 18 2009 Dan Walsh <dwalsh@redhat.com> 3.6.32-6
- More fixes for sandbox_web_t

* Fri Sep 18 2009 Dan Walsh <dwalsh@redhat.com> 3.6.32-5
- Allow sshd to create .ssh directory and content

* Fri Sep 18 2009 Dan Walsh <dwalsh@redhat.com> 3.6.32-4
- Fix request_module line to module_request

* Fri Sep 18 2009 Dan Walsh <dwalsh@redhat.com> 3.6.32-3
- Fix sandbox policy to allow it to run under firefox.  
- Dont audit leaks.

* Thu Sep 17 2009 Dan Walsh <dwalsh@redhat.com> 3.6.32-2
- Fixes for sandbox

* Wed Sep 17 2009 Dan Walsh <dwalsh@redhat.com> 3.6.32-1
- Update to upstream
- Dontaudit nsplugin search /root
- Dontaudit nsplugin sys_nice

* Mon Sep 15 2009 Dan Walsh <dwalsh@redhat.com> 3.6.31-5
- Fix label on /usr/bin/notepad, /usr/sbin/vboxadd-service
- Remove policycoreutils-python requirement except for minimum

* Mon Sep 14 2009 Dan Walsh <dwalsh@redhat.com> 3.6.31-4
- Fix devicekit_disk_t to getattr on all domains sockets and fifo_files
- Conflicts seedit (You can not use selinux-policy-targeted and seedit at the same time.)


* Thu Sep 10 2009 Dan Walsh <dwalsh@redhat.com> 3.6.31-3
- Add wordpress/wp-content/uploads label
- Fixes for sandbox when run from staff_t

* Thu Sep 10 2009 Dan Walsh <dwalsh@redhat.com> 3.6.31-2
- Update to upstream
- Fixes for devicekit_disk

* Tue Sep 8 2009 Dan Walsh <dwalsh@redhat.com> 3.6.30-6
- More fixes

* Tue Sep 8 2009 Dan Walsh <dwalsh@redhat.com> 3.6.30-5
- Lots of fixes for initrc and other unconfined domains

* Fri Sep 4 2009 Dan Walsh <dwalsh@redhat.com> 3.6.30-4
- Allow xserver to use  netlink_kobject_uevent_socket

* Thu Sep 3 2009 Dan Walsh <dwalsh@redhat.com> 3.6.30-3
- Fixes for sandbox 

* Mon Aug 31 2009 Dan Walsh <dwalsh@redhat.com> 3.6.30-2
- Dontaudit setroubleshootfix looking at /root directory

* Mon Aug 31 2009 Dan Walsh <dwalsh@redhat.com> 3.6.30-1
- Update to upsteam

* Mon Aug 31 2009 Dan Walsh <dwalsh@redhat.com> 3.6.29-2
- Allow gssd to send signals to users
- Fix duplicate label for apache content

* Fri Aug 28 2009 Dan Walsh <dwalsh@redhat.com> 3.6.29-1
- Update to upstream

* Fri Aug 28 2009 Dan Walsh <dwalsh@redhat.com> 3.6.28-9
- Remove polkit_auth on upgrades

* Wed Aug 26 2009 Dan Walsh <dwalsh@redhat.com> 3.6.28-8
- Add back in unconfined.pp and unconfineduser.pp
- Add Sandbox unshare

* Tue Aug 25 2009 Dan Walsh <dwalsh@redhat.com> 3.6.28-7
- Fixes for cdrecord, mdadm, and others

* Sat Aug 22 2009 Dan Walsh <dwalsh@redhat.com> 3.6.28-6
- Add capability setting to dhcpc and gpm

* Sat Aug 22 2009 Dan Walsh <dwalsh@redhat.com> 3.6.28-5
- Allow cronjobs to read exim_spool_t

* Fri Aug 21 2009 Dan Walsh <dwalsh@redhat.com> 3.6.28-4
- Add ABRT policy

* Thu Aug 20 2009 Dan Walsh <dwalsh@redhat.com> 3.6.28-3
- Fix system-config-services policy

* Wed Aug 19 2009 Dan Walsh <dwalsh@redhat.com> 3.6.28-2
- Allow libvirt to change user componant of virt_domain

* Tue Aug 18 2009 Dan Walsh <dwalsh@redhat.com> 3.6.28-1
- Allow cupsd_config_t to be started by dbus
- Add smoltclient policy

* Fri Aug 14 2009 Dan Walsh <dwalsh@redhat.com> 3.6.27-1
- Add policycoreutils-python to pre install

* Thu Aug 13 2009 Dan Walsh <dwalsh@redhat.com> 3.6.26-11
- Make all unconfined_domains permissive so we can see what AVC's happen 

* Mon Aug 10 2009 Dan Walsh <dwalsh@redhat.com> 3.6.26-10
- Add pt_chown policy

* Mon Aug 10 2009 Dan Walsh <dwalsh@redhat.com> 3.6.26-9
- Add kdump policy for Miroslav Grepl
- Turn off execstack boolean

* Fri Aug 7 2009 Bill Nottingham <notting@redhat.com> 3.6.26-8
- Turn on execstack on a temporary basis (#512845)

* Thu Aug 6 2009 Dan Walsh <dwalsh@redhat.com> 3.6.26-7
- Allow nsplugin to connecto the session bus
- Allow samba_net to write to coolkey data

* Wed Aug 5 2009 Dan Walsh <dwalsh@redhat.com> 3.6.26-6
- Allow devicekit_disk to list inotify

* Wed Aug 5 2009 Dan Walsh <dwalsh@redhat.com> 3.6.26-5
- Allow svirt images to create sock_file in svirt_var_run_t

* Tue Aug 4 2009 Dan Walsh <dwalsh@redhat.com> 3.6.26-4
- Allow exim to getattr on mountpoints
- Fixes for pulseaudio

* Fri Jul 31 2009 Dan Walsh <dwalsh@redhat.com> 3.6.26-3
- Allow svirt_t to stream_connect to virtd_t

* Fri Jul 31 2009 Dan Walsh <dwalsh@redhat.com> 3.6.26-2
- Allod hald_dccm_t to create sock_files in /tmp

* Thu Jul 30 2009 Dan Walsh <dwalsh@redhat.com> 3.6.26-1
- More fixes from upstream

* Tue Jul 28 2009 Dan Walsh <dwalsh@redhat.com> 3.6.25-1
- Fix polkit label
- Remove hidebrokensymptoms for nss_ldap fix
- Add modemmanager policy
- Lots of merges from upstream
- Begin removing textrel_shlib_t labels, from fixed libraries

* Tue Jul 28 2009 Dan Walsh <dwalsh@redhat.com> 3.6.24-1
- Update to upstream

* Mon Jul 27 2009 Dan Walsh <dwalsh@redhat.com> 3.6.23-2
- Allow certmaster to override dac permissions

* Thu Jul 22 2009 Dan Walsh <dwalsh@redhat.com> 3.6.23-1
- Update to upstream

* Tue Jul 20 2009 Dan Walsh <dwalsh@redhat.com> 3.6.22-3
- Fix context for VirtualBox

* Tue Jul 14 2009 Dan Walsh <dwalsh@redhat.com> 3.6.22-1
- Update to upstream

* Fri Jul 10 2009 Dan Walsh <dwalsh@redhat.com> 3.6.21-4
- Allow clamscan read amavis spool files

* Wed Jul 8 2009 Dan Walsh <dwalsh@redhat.com> 3.6.21-3
- Fixes for xguest

* Tue Jul  7 2009 Tom "spot" Callaway <tcallawa@redhat.com> 3.6.21-2
- fix multiple directory ownership of mandirs

* Wed Jul 1 2009 Dan Walsh <dwalsh@redhat.com> 3.6.21-1
- Update to upstream

* Tue Jun 30 2009 Dan Walsh <dwalsh@redhat.com> 3.6.20-2
- Add rules for rtkit-daemon

* Thu Jun 25 2009 Dan Walsh <dwalsh@redhat.com> 3.6.20-1
- Update to upstream
- Fix nlscd_stream_connect

* Thu Jun 25 2009 Dan Walsh <dwalsh@redhat.com> 3.6.19-5
- Add rtkit policy

* Wed Jun 24 2009 Dan Walsh <dwalsh@redhat.com> 3.6.19-4
- Allow rpcd_t to stream connect to rpcbind

* Tue Jun 23 2009 Dan Walsh <dwalsh@redhat.com> 3.6.19-3
- Allow kpropd to create tmp files

* Tue Jun 23 2009 Dan Walsh <dwalsh@redhat.com> 3.6.19-2
- Fix last duplicate /var/log/rpmpkgs

* Mon Jun 22 2009 Dan Walsh <dwalsh@redhat.com> 3.6.19-1
- Update to upstream
  * add sssd

* Sat Jun 20 2009 Dan Walsh <dwalsh@redhat.com> 3.6.18-1
- Update to upstream
  * cleanup
* Fri Jun 19 2009 Dan Walsh <dwalsh@redhat.com> 3.6.17-1
- Update to upstream
- Additional mail ports
- Add virt_use_usb boolean for svirt

* Thu Jun 18 2009 Dan Walsh <dwalsh@redhat.com> 3.6.16-4
- Fix mcs rules to include chr_file and blk_file

* Tue Jun 16 2009 Dan Walsh <dwalsh@redhat.com> 3.6.16-3
- Add label for udev-acl

* Mon Jun 15 2009 Dan Walsh <dwalsh@redhat.com> 3.6.16-2
- Additional rules for consolekit/udev, privoxy and various other fixes

* Fri Jun 12 2009 Dan Walsh <dwalsh@redhat.com> 3.6.16-1
- New version for upstream

* Thu Jun 11 2009 Dan Walsh <dwalsh@redhat.com> 3.6.14-3
- Allow NetworkManager to read inotifyfs

* Wed Jun 10 2009 Dan Walsh <dwalsh@redhat.com> 3.6.14-2
- Allow setroubleshoot to run mlocate

* Mon Jun 8 2009 Dan Walsh <dwalsh@redhat.com> 3.6.14-1
- Update to upstream 

* Tue Jun 2 2009 Dan Walsh <dwalsh@redhat.com> 3.6.13-3
- Add fish as a shell
- Allow fprintd to list usbfs_t
- Allow consolekit to search mountpoints
- Add proper labeling for shorewall

* Tue May 26 2009 Dan Walsh <dwalsh@redhat.com> 3.6.13-2
- New log file for vmware
- Allow xdm to setattr on user_tmp_t

* Thu May 21 2009 Dan Walsh <dwalsh@redhat.com> 3.6.13-1
- Upgrade to upstream

* Wed May 20 2009 Dan Walsh <dwalsh@redhat.com> 3.6.12-39
- Allow fprintd to access sys_ptrace
- Add sandbox policy

* Mon May 18 2009 Dan Walsh <dwalsh@redhat.com> 3.6.12-38
- Add varnishd policy

* Thu May 14 2009 Dan Walsh <dwalsh@redhat.com> 3.6.12-37
- Fixes for kpropd

* Tue May 12 2009 Dan Walsh <dwalsh@redhat.com> 3.6.12-36
- Allow brctl to r/w tun_tap_device_t

* Mon May 11 2009 Dan Walsh <dwalsh@redhat.com> 3.6.12-35
- Add /usr/share/selinux/packages

* Mon May 11 2009 Dan Walsh <dwalsh@redhat.com> 3.6.12-34
- Allow rpcd_t to send signals to kernel threads

* Fri May 7 2009 Dan Walsh <dwalsh@redhat.com> 3.6.12-33
- Fix upgrade for F10 to F11

* Thu May 7 2009 Dan Walsh <dwalsh@redhat.com> 3.6.12-31
- Add policy for /var/lib/fprint

* Tue May 5 2009 Dan Walsh <dwalsh@redhat.com> 3.6.12-30
-Remove duplicate line

* Tue May 5 2009 Dan Walsh <dwalsh@redhat.com> 3.6.12-29
- Allow svirt to manage pci and other sysfs device data

* Mon May 4 2009 Dan Walsh <dwalsh@redhat.com> 3.6.12-28
- Fix package selection handling

* Fri May 1 2009 Dan Walsh <dwalsh@redhat.com> 3.6.12-27
- Fix /sbin/ip6tables-save context
- Allod udev to transition to mount
- Fix loading of mls policy file

* Thu Apr 30 2009 Dan Walsh <dwalsh@redhat.com> 3.6.12-26
- Add shorewall policy

* Wed Apr 29 2009 Dan Walsh <dwalsh@redhat.com> 3.6.12-25
- Additional rules for fprintd and sssd

* Tue Apr 28 2009 Dan Walsh <dwalsh@redhat.com> 3.6.12-24
- Allow nsplugin to unix_read unix_write sem for unconfined_java

* Tue Apr 28 2009 Dan Walsh <dwalsh@redhat.com> 3.6.12-23
- Fix uml files to be owned by users

* Tue Apr 28 2009 Dan Walsh <dwalsh@redhat.com> 3.6.12-22
- Fix Upgrade path to install unconfineduser.pp when unocnfined package is 3.0.0 or less

* Mon Apr 27 2009 Dan Walsh <dwalsh@redhat.com> 3.6.12-21
- Allow confined users to manage virt_content_t, since this is home dir content
- Allow all domains to read rpm_script_tmp_t which is what shell creates on redirection

* Mon Apr 27 2009 Dan Walsh <dwalsh@redhat.com> 3.6.12-20
- Fix labeling on /var/lib/misc/prelink*
- Allow xserver to rw_shm_perms with all x_clients
- Allow prelink to execute files in the users home directory

* Fri Apr 24 2009 Dan Walsh <dwalsh@redhat.com> 3.6.12-19
- Allow initrc_t to delete dev_null
- Allow readahead to configure auditing
- Fix milter policy
- Add /var/lib/readahead

* Fri Apr 24 2009 Dan Walsh <dwalsh@redhat.com> 3.6.12-16
- Update to latest milter code from Paul Howarth

* Thu Apr 23 2009 Dan Walsh <dwalsh@redhat.com> 3.6.12-15
- Additional perms for readahead

* Thu Apr 23 2009 Dan Walsh <dwalsh@redhat.com> 3.6.12-14
- Allow pulseaudio to acquire_svc on session bus
- Fix readahead labeling

* Thu Apr 23 2009 Dan Walsh <dwalsh@redhat.com> 3.6.12-13
- Allow sysadm_t to run rpm directly
- libvirt needs fowner

* Wed Apr 22 2009 Dan Walsh <dwalsh@redhat.com> 3.6.12-12
- Allow sshd to read var_lib symlinks for freenx

* Tue Apr 21 2009 Dan Walsh <dwalsh@redhat.com> 3.6.12-11
- Allow nsplugin unix_read and write on users shm and sem
- Allow sysadm_t to execute su

* Tue Apr 21 2009 Dan Walsh <dwalsh@redhat.com> 3.6.12-10
- Dontaudit attempts to getattr user_tmpfs_t by lvm
- Allow nfs to share removable media

* Mon Apr 20 2009 Dan Walsh <dwalsh@redhat.com> 3.6.12-9
- Add ability to run postdrop from confined users

* Sat Apr 18 2009 Dan Walsh <dwalsh@redhat.com> 3.6.12-8
- Fixes for podsleuth

* Fri Apr 17 2009 Dan Walsh <dwalsh@redhat.com> 3.6.12-7
- Turn off nsplugin transition
- Remove Konsole leaked file descriptors for release

* Fri Apr 17 2009 Dan Walsh <dwalsh@redhat.com> 3.6.12-6
- Allow cupsd_t to create link files in print_spool_t
- Fix iscsi_stream_connect typo
- Fix labeling on /etc/acpi/actions
- Don't reinstall unconfine and unconfineuser on upgrade if they are not installed

* Tue Apr 14 2009 Dan Walsh <dwalsh@redhat.com> 3.6.12-5
- Allow audioentroy to read etc files

* Mon Apr 13 2009 Dan Walsh <dwalsh@redhat.com> 3.6.12-4
- Add fail2ban_var_lib_t
- Fixes for devicekit_power_t

* Thu Apr 9 2009 Dan Walsh <dwalsh@redhat.com> 3.6.12-3
- Separate out the ucnonfined user from the unconfined.pp package

* Wed Apr 7 2009 Dan Walsh <dwalsh@redhat.com> 3.6.12-2
- Make sure unconfined_java_t and unconfined_mono_t create user_tmpfs_t.

* Tue Apr 7 2009 Dan Walsh <dwalsh@redhat.com> 3.6.12-1
- Upgrade to latest upstream
- Allow devicekit_disk sys_rawio

* Mon Apr 6 2009 Dan Walsh <dwalsh@redhat.com> 3.6.11-1
- Dontaudit binds to ports < 1024 for named
- Upgrade to latest upstream

* Fri Apr 3 2009 Dan Walsh <dwalsh@redhat.com> 3.6.10-9
- Allow podsleuth to use tmpfs files

* Fri Apr 3 2009 Dan Walsh <dwalsh@redhat.com> 3.6.10-8
- Add customizable_types for svirt

* Fri Apr 3 2009 Dan Walsh <dwalsh@redhat.com> 3.6.10-7
- Allow setroubelshoot exec* privs to prevent crash from bad libraries
- add cpufreqselector

* Thu Apr 2 2009 Dan Walsh <dwalsh@redhat.com> 3.6.10-6
- Dontaudit listing of /root directory for cron system jobs

* Mon Mar 30 2009 Dan Walsh <dwalsh@redhat.com> 3.6.10-5
- Fix missing ld.so.cache label

* Fri Mar 27 2009 Dan Walsh <dwalsh@redhat.com> 3.6.10-4
- Add label for ~/.forward and /root/.forward

* Thu Mar 26 2009 Dan Walsh <dwalsh@redhat.com> 3.6.10-3
- Fixes for svirt

* Thu Mar 19 2009 Dan Walsh <dwalsh@redhat.com> 3.6.10-2
- Fixes to allow svirt read iso files in homedir

* Thu Mar 19 2009 Dan Walsh <dwalsh@redhat.com> 3.6.10-1
- Add xenner and wine fixes from mgrepl

* Wed Mar 18 2009 Dan Walsh <dwalsh@redhat.com> 3.6.9-4
- Allow mdadm to read/write mls override

* Tue Mar 17 2009 Dan Walsh <dwalsh@redhat.com> 3.6.9-3
- Change to svirt to only access svirt_image_t

* Thu Mar 12 2009 Dan Walsh <dwalsh@redhat.com> 3.6.9-2
- Fix libvirt policy

* Thu Mar 12 2009 Dan Walsh <dwalsh@redhat.com> 3.6.9-1
- Upgrade to latest upstream

* Tue Mar 10 2009 Dan Walsh <dwalsh@redhat.com> 3.6.8-4
- Fixes for iscsid and sssd
- More cleanups for upgrade from F10 to Rawhide.

* Mon Mar 9 2009 Dan Walsh <dwalsh@redhat.com> 3.6.8-3
- Add pulseaudio, sssd policy
- Allow networkmanager to exec udevadm

* Sat Mar 7 2009 Dan Walsh <dwalsh@redhat.com> 3.6.8-2
- Add pulseaudio context

* Thu Mar 4 2009 Dan Walsh <dwalsh@redhat.com> 3.6.8-1
- Upgrade to latest patches

* Wed Mar 4 2009 Dan Walsh <dwalsh@redhat.com> 3.6.7-2
- Fixes for libvirt

* Mon Mar 2 2009 Dan Walsh <dwalsh@redhat.com> 3.6.7-1
- Update to Latest upstream

* Sat Feb 28 2009 Dan Walsh <dwalsh@redhat.com> 3.6.6-9
- Fix setrans.conf to show SystemLow for s0

* Fri Feb 27 2009 Dan Walsh <dwalsh@redhat.com> 3.6.6-8
- Further confinement of qemu images via svirt

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 19 2009 Dan Walsh <dwalsh@redhat.com> 3.6.6-6
- Allow NetworkManager to manage /etc/NetworkManager/system-connections

* Wed Feb 18 2009 Dan Walsh <dwalsh@redhat.com> 3.6.6-5
- add virtual_image_context and virtual_domain_context files

* Tue Feb 17 2009 Dan Walsh <dwalsh@redhat.com> 3.6.6-4
- Allow rpcd_t to send signal to mount_t
- Allow libvirtd to run ranged

* Tue Feb 17 2009 Dan Walsh <dwalsh@redhat.com> 3.6.6-3
- Fix sysnet/net_conf_t

* Tue Feb 17 2009 Dan Walsh <dwalsh@redhat.com> 3.6.6-2
- Fix squidGuard labeling

* Wed Feb 11 2009 Dan Walsh <dwalsh@redhat.com> 3.6.6-1
- Re-add corenet_in_generic_if(unlabeled_t)

* Wed Feb 11 2009 Dan Walsh <dwalsh@redhat.com> 3.6.5-3

* Tue Feb 10 2009 Dan Walsh <dwalsh@redhat.com> 3.6.5-2
- Add git web policy

* Mon Feb 9 2009 Dan Walsh <dwalsh@redhat.com> 3.6.5-1
- Add setrans contains from upstream 

* Mon Feb 9 2009 Dan Walsh <dwalsh@redhat.com> 3.6.4-6
- Do transitions outside of the booleans

* Sun Feb 8 2009 Dan Walsh <dwalsh@redhat.com> 3.6.4-5
- Allow xdm to create user_tmp_t sockets for switch user to work

* Thu Feb 5 2009 Dan Walsh <dwalsh@redhat.com> 3.6.4-4
- Fix staff_t domain

* Thu Feb 5 2009 Dan Walsh <dwalsh@redhat.com> 3.6.4-3
- Grab remainder of network_peer_controls patch

* Wed Feb 4 2009 Dan Walsh <dwalsh@redhat.com> 3.6.4-2
- More fixes for devicekit

* Tue Feb 3 2009 Dan Walsh <dwalsh@redhat.com> 3.6.4-1
- Upgrade to latest upstream 

* Mon Feb 2 2009 Dan Walsh <dwalsh@redhat.com> 3.6.3-13
- Add boolean to disallow unconfined_t login

* Fri Jan 30 2009 Dan Walsh <dwalsh@redhat.com> 3.6.3-12
- Add back transition from xguest to mozilla

* Fri Jan 30 2009 Dan Walsh <dwalsh@redhat.com> 3.6.3-11
- Add virt_content_ro_t and labeling for isos directory

* Tue Jan 27 2009 Dan Walsh <dwalsh@redhat.com> 3.6.3-10
- Fixes for wicd daemon

* Mon Jan 26 2009 Dan Walsh <dwalsh@redhat.com> 3.6.3-9
- More mls/rpm fixes 

* Fri Jan 23 2009 Dan Walsh <dwalsh@redhat.com> 3.6.3-8
- Add policy to make dbus/nm-applet work

* Thu Jan 22 2009 Dan Walsh <dwalsh@redhat.com> 3.6.3-7
- Remove polgen-ifgen from post and add trigger to policycoreutils-python

* Wed Jan 21 2009 Dan Walsh <dwalsh@redhat.com> 3.6.3-6
- Add wm policy
- Make mls work in graphics mode

* Tue Jan 20 2009 Dan Walsh <dwalsh@redhat.com> 3.6.3-3
- Fixed for DeviceKit

* Mon Jan 19 2009 Dan Walsh <dwalsh@redhat.com> 3.6.3-2
- Add devicekit policy

* Mon Jan 19 2009 Dan Walsh <dwalsh@redhat.com> 3.6.3-1
- Update to upstream

* Thu Jan 15 2009 Dan Walsh <dwalsh@redhat.com> 3.6.2-5
- Define openoffice as an x_domain

* Mon Jan 12 2009 Dan Walsh <dwalsh@redhat.com> 3.6.2-4
- Fixes for reading xserver_tmp_t

* Thu Jan 8 2009 Dan Walsh <dwalsh@redhat.com> 3.6.2-3
- Allow cups_pdf_t write to nfs_t

* Tue Jan 6 2009 Dan Walsh <dwalsh@redhat.com> 3.6.2-2
- Remove audio_entropy policy

* Mon Jan 5 2009 Dan Walsh <dwalsh@redhat.com> 3.6.2-1
- Update to upstream

* Sun Jan 4 2009 Dan Walsh <dwalsh@redhat.com> 3.6.1-15
- Allow hal_acl_t to getattr/setattr fixed_disk

* Sat Dec 27 2008 Dan Walsh <dwalsh@redhat.com> 3.6.1-14
- Change userdom_read_all_users_state to include reading symbolic links in /proc

* Mon Dec 22 2008 Dan Walsh <dwalsh@redhat.com> 3.6.1-13
- Fix dbus reading /proc information

* Thu Dec 18 2008 Dan Walsh <dwalsh@redhat.com> 3.6.1-12
- Add missing alias for home directory content

* Wed Dec 17 2008 Dan Walsh <dwalsh@redhat.com> 3.6.1-11
- Fixes for IBM java location

* Thu Dec 11 2008 Dan Walsh <dwalsh@redhat.com> 3.6.1-10
- Allow unconfined_r unconfined_java_t

* Tue Dec 9 2008 Dan Walsh <dwalsh@redhat.com> 3.6.1-9
- Add cron_role back to user domains

* Mon Dec 8 2008 Dan Walsh <dwalsh@redhat.com> 3.6.1-8
- Fix sudo setting of user keys

* Thu Dec 4 2008 Dan Walsh <dwalsh@redhat.com> 3.6.1-7
- Allow iptables to talk to terminals
- Fixes for policy kit
- lots of fixes for booting. 

* Wed Dec 3 2008 Dan Walsh <dwalsh@redhat.com> 3.6.1-4
- Cleanup policy

* Mon Dec 01 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 3.6.1-2
- Rebuild for Python 2.6

* Fri Nov 5 2008 Dan Walsh <dwalsh@redhat.com> 3.5.13-19
- Fix labeling on /var/spool/rsyslog

* Thu Nov 5 2008 Dan Walsh <dwalsh@redhat.com> 3.5.13-18
- Allow postgresl to bind to udp nodes

* Wed Nov 5 2008 Dan Walsh <dwalsh@redhat.com> 3.5.13-17
- Allow lvm to dbus chat with hal
- Allow rlogind to read nfs_t 

* Wed Nov 5 2008 Dan Walsh <dwalsh@redhat.com> 3.5.13-16
- Fix cyphesis file context

* Tue Nov 3 2008 Dan Walsh <dwalsh@redhat.com> 3.5.13-15
- Allow hal/pm-utils to look at /var/run/video.rom
- Add ulogd policy

* Tue Nov 3 2008 Dan Walsh <dwalsh@redhat.com> 3.5.13-14
- Additional fixes for cyphesis
- Fix certmaster file context
- Add policy for system-config-samba
- Allow hal to read /var/run/video.rom

* Mon Nov 3 2008 Dan Walsh <dwalsh@redhat.com> 3.5.13-13
- Allow dhcpc to restart ypbind
- Fixup labeling in /var/run

* Thu Oct 30 2008 Dan Walsh <dwalsh@redhat.com> 3.5.13-12
- Add certmaster policy

* Wed Oct 29 2008 Dan Walsh <dwalsh@redhat.com> 3.5.13-11
- Fix confined users 
- Allow xguest to read/write xguest_dbusd_t

* Mon Oct 27 2008 Dan Walsh <dwalsh@redhat.com> 3.5.13-9
- Allow openoffice execstack/execmem privs

* Fri Oct 24 2008 Dan Walsh <dwalsh@redhat.com> 3.5.13-8
- Allow mozilla to run with unconfined_execmem_t

* Thu Oct 23 2008 Dan Walsh <dwalsh@redhat.com> 3.5.13-7
- Dontaudit domains trying to write to .xsession-errors

* Thu Oct 23 2008 Dan Walsh <dwalsh@redhat.com> 3.5.13-6
- Allow nsplugin to look at autofs_t directory

* Wed Oct 22 2008 Dan Walsh <dwalsh@redhat.com> 3.5.13-5
- Allow kerneloops to create tmp files

* Wed Oct 22 2008 Dan Walsh <dwalsh@redhat.com> 3.5.13-4
- More alias for fastcgi

* Tue Oct 21 2008 Dan Walsh <dwalsh@redhat.com> 3.5.13-3
- Remove mod_fcgid-selinux package

* Mon Oct 20 2008 Dan Walsh <dwalsh@redhat.com> 3.5.13-2
- Fix dovecot access

* Fri Oct 17 2008 Dan Walsh <dwalsh@redhat.com> 3.5.13-1
- Policy cleanup 

* Thu Oct 16 2008 Dan Walsh <dwalsh@redhat.com> 3.5.12-3
- Remove Multiple spec
- Add include
- Fix makefile to not call per_role_expansion

* Wed Oct 15 2008 Dan Walsh <dwalsh@redhat.com> 3.5.12-2
- Fix labeling of libGL

* Fri Oct 10 2008 Dan Walsh <dwalsh@redhat.com> 3.5.12-1
- Update to upstream

* Wed Oct 8 2008 Dan Walsh <dwalsh@redhat.com> 3.5.11-1
- Update to upstream policy

* Mon Oct 6 2008 Dan Walsh <dwalsh@redhat.com> 3.5.10-3
- Fixes for confined xwindows and xdm_t 

* Fri Oct 3 2008 Dan Walsh <dwalsh@redhat.com> 3.5.10-2
- Allow confined users and xdm to exec wm
- Allow nsplugin to talk to fifo files on nfs

* Fri Oct 3 2008 Dan Walsh <dwalsh@redhat.com> 3.5.10-1
- Allow NetworkManager to transition to avahi and iptables
- Allow domains to search other domains keys, coverup kernel bug

* Wed Oct 1 2008 Dan Walsh <dwalsh@redhat.com> 3.5.9-4
- Fix labeling for oracle 

* Wed Oct 1 2008 Dan Walsh <dwalsh@redhat.com> 3.5.9-3
- Allow nsplugin to comminicate with xdm_tmp_t sock_file

* Mon Sep 29 2008 Dan Walsh <dwalsh@redhat.com> 3.5.9-2
- Change all user tmpfs_t files to be labeled user_tmpfs_t
- Allow radiusd to create sock_files

* Wed Sep 24 2008 Dan Walsh <dwalsh@redhat.com> 3.5.9-1
- Upgrade to upstream

* Tue Sep 23 2008 Dan Walsh <dwalsh@redhat.com> 3.5.8-7
- Allow confined users to login with dbus

* Mon Sep 22 2008 Dan Walsh <dwalsh@redhat.com> 3.5.8-6
- Fix transition to nsplugin

* Mon Sep 22 2008 Dan Walsh <dwalsh@redhat.com> 3.5.8-5
- Add file context for /dev/mspblk.*

* Sun Sep 21 2008 Dan Walsh <dwalsh@redhat.com> 3.5.8-4
- Fix transition to nsplugin
'
* Thu Sep 18 2008 Dan Walsh <dwalsh@redhat.com> 3.5.8-3
- Fix labeling on new pm*log
- Allow ssh to bind to all nodes

* Thu Sep 11 2008 Dan Walsh <dwalsh@redhat.com> 3.5.8-1
- Merge upstream changes
- Add Xavier Toth patches

* Wed Sep 10 2008 Dan Walsh <dwalsh@redhat.com> 3.5.7-2
- Add qemu_cache_t for /var/cache/libvirt

* Fri Sep 5 2008 Dan Walsh <dwalsh@redhat.com> 3.5.7-1
- Remove gamin policy

* Thu Sep 4 2008 Dan Walsh <dwalsh@redhat.com> 3.5.6-2
- Add tinyxs-max file system support

* Wed Sep 3 2008 Dan Walsh <dwalsh@redhat.com> 3.5.6-1
- Update to upstream
-       New handling of init scripts

* Fri Aug 29 2008 Dan Walsh <dwalsh@redhat.com> 3.5.5-4
- Allow pcsd to dbus
- Add memcache policy

* Fri Aug 29 2008 Dan Walsh <dwalsh@redhat.com> 3.5.5-3
- Allow audit dispatcher to kill his children

* Tue Aug 26 2008 Dan Walsh <dwalsh@redhat.com> 3.5.5-2
- Update to upstream
- Fix crontab use by unconfined user

* Tue Aug 12 2008 Dan Walsh <dwalsh@redhat.com> 3.5.4-2
- Allow ifconfig_t to read dhcpc_state_t

* Mon Aug 11 2008 Dan Walsh <dwalsh@redhat.com> 3.5.4-1
- Update to upstream

* Thu Aug 7 2008 Dan Walsh <dwalsh@redhat.com> 3.5.3-1
- Update to upstream 

* Wed Aug 2 2008 Dan Walsh <dwalsh@redhat.com> 3.5.2-2
- Allow system-config-selinux to work with policykit

* Fri Jul 25 2008 Dan Walsh <dwalsh@redhat.com> 3.5.1-5
- Fix novel labeling

* Fri Jul 25 2008 Dan Walsh <dwalsh@redhat.com> 3.5.1-4
- Consolodate pyzor,spamassassin, razor into one security domain
- Fix xdm requiring additional perms.

* Fri Jul 25 2008 Dan Walsh <dwalsh@redhat.com> 3.5.1-3
- Fixes for logrotate, alsa

* Thu Jul 25 2008 Dan Walsh <dwalsh@redhat.com> 3.5.1-2
- Eliminate vbetool duplicate entry

* Wed Jul 16 2008 Dan Walsh <dwalsh@redhat.com> 3.5.1-1
- Fix xguest -> xguest_mozilla_t -> xguest_openiffice_t
- Change dhclient to be able to red networkmanager_var_run

* Tue Jul 15 2008 Dan Walsh <dwalsh@redhat.com> 3.5.0-1
- Update to latest refpolicy
- Fix libsemanage initial install bug

* Wed Jul 9 2008 Dan Walsh <dwalsh@redhat.com> 3.4.2-14
- Add inotify support to nscd

* Tue Jul 8 2008 Dan Walsh <dwalsh@redhat.com> 3.4.2-13
- Allow unconfined_t to setfcap

* Mon Jul 7 2008 Dan Walsh <dwalsh@redhat.com> 3.4.2-12
- Allow amanda to read tape
- Allow prewikka cgi to use syslog, allow audisp_t to signal cgi
- Add support for netware file systems

* Thu Jul 3 2008 Dan Walsh <dwalsh@redhat.com> 3.4.2-11
- Allow ypbind apps to net_bind_service

* Wed Jul 2 2008 Dan Walsh <dwalsh@redhat.com> 3.4.2-10
- Allow all system domains and application domains to append to any log file

* Sun Jun 29 2008 Dan Walsh <dwalsh@redhat.com> 3.4.2-9
- Allow gdm to read rpm database
- Allow nsplugin to read mplayer config files

* Thu Jun 26 2008 Dan Walsh <dwalsh@redhat.com> 3.4.2-8
- Allow vpnc to run ifconfig

* Tue Jun 24 2008 Dan Walsh <dwalsh@redhat.com> 3.4.2-7
- Allow confined users to use postgres
- Allow system_mail_t to exec other mail clients
- Label mogrel_rails as an apache server

* Mon Jun 23 2008 Dan Walsh <dwalsh@redhat.com> 3.4.2-6
- Apply unconfined_execmem_exec_t to haskell programs

* Sun Jun 22 2008 Dan Walsh <dwalsh@redhat.com> 3.4.2-5
- Fix prelude file context

* Fri Jun 12 2008 Dan Walsh <dwalsh@redhat.com> 3.4.2-4
- allow hplip to talk dbus
- Fix context on ~/.local dir

* Thu Jun 12 2008 Dan Walsh <dwalsh@redhat.com> 3.4.2-3
- Prevent applications from reading x_device

* Thu Jun 12 2008 Dan Walsh <dwalsh@redhat.com> 3.4.2-2
- Add /var/lib/selinux context

* Wed Jun 11 2008 Dan Walsh <dwalsh@redhat.com> 3.4.2-1
- Update to upstream 

* Wed Jun 4 2008 Dan Walsh <dwalsh@redhat.com> 3.4.1-5
- Add livecd policy

* Wed Jun 4 2008 Dan Walsh <dwalsh@redhat.com> 3.4.1-3
- Dontaudit search of admin_home for init_system_domain
- Rewrite of xace interfaces
- Lots of new fs_list_inotify
- Allow livecd to transition to setfiles_mac

* Fri May 9 2008 Dan Walsh <dwalsh@redhat.com> 3.4.1-2
- Begin XAce integration

* Fri May 9 2008 Dan Walsh <dwalsh@redhat.com> 3.4.1-1
- Merge Upstream

* Wed May 7 2008 Dan Walsh <dwalsh@redhat.com> 3.3.1-48
- Allow amanada to create data files

* Wed May 7 2008 Dan Walsh <dwalsh@redhat.com> 3.3.1-47
- Fix initial install, semanage setup

* Tue May 6 2008 Dan Walsh <dwalsh@redhat.com> 3.3.1-46
- Allow system_r for httpd_unconfined_script_t

* Wed Apr 30 2008 Dan Walsh <dwalsh@redhat.com> 3.3.1-45
- Remove dmesg boolean
- Allow user domains to read/write game data

* Mon Apr 28 2008 Dan Walsh <dwalsh@redhat.com> 3.3.1-44
- Change unconfined_t to transition to unconfined_mono_t when running mono
- Change XXX_mono_t to transition to XXX_t when executing bin_t files, so gnome-do will work

* Mon Apr 28 2008 Dan Walsh <dwalsh@redhat.com> 3.3.1-43
- Remove old booleans from targeted-booleans.conf file

* Fri Apr 25 2008 Dan Walsh <dwalsh@redhat.com> 3.3.1-42
- Add boolean to mmap_zero
- allow tor setgid
- Allow gnomeclock to set clock

* Thu Apr 24 2008 Dan Walsh <dwalsh@redhat.com> 3.3.1-41
- Don't run crontab from unconfined_t

* Wed Apr 23 2008 Dan Walsh <dwalsh@redhat.com> 3.3.1-39
- Change etc files to config files to allow users to read them

* Fri Apr 14 2008 Dan Walsh <dwalsh@redhat.com> 3.3.1-37
- Lots of fixes for confined domains on NFS_t homedir

* Mon Apr 14 2008 Dan Walsh <dwalsh@redhat.com> 3.3.1-36
- dontaudit mrtg reading /proc
- Allow iscsi to signal itself
- Allow gnomeclock sys_ptrace

* Thu Apr 10 2008 Dan Walsh <dwalsh@redhat.com> 3.3.1-33
- Allow dhcpd to read kernel network state

* Thu Apr 10 2008 Dan Walsh <dwalsh@redhat.com> 3.3.1-32
- Label /var/run/gdm correctly
- Fix unconfined_u user creation

* Tue Apr 8 2008 Dan Walsh <dwalsh@redhat.com> 3.3.1-31
- Allow transition from initrc_t to getty_t

* Tue Apr 8 2008 Dan Walsh <dwalsh@redhat.com> 3.3.1-30
- Allow passwd to communicate with user sockets to change gnome-keyring

* Sat Apr 5 2008 Dan Walsh <dwalsh@redhat.com> 3.3.1-29
- Fix initial install

* Fri Apr 4 2008 Dan Walsh <dwalsh@redhat.com> 3.3.1-28
- Allow radvd to use fifo_file
- dontaudit setfiles reading links
- allow semanage sys_resource
- add allow_httpd_mod_auth_ntlm_winbind boolean
- Allow privhome apps including dovecot read on nfs and cifs home 
dirs if the boolean is set


* Tue Apr 1 2008 Dan Walsh <dwalsh@redhat.com> 3.3.1-27
- Allow nsplugin to read /etc/mozpluggerrc, user_fonts
- Allow syslog to manage innd logs.
- Allow procmail to ioctl spamd_exec_t

* Sat Mar 28 2008 Dan Walsh <dwalsh@redhat.com> 3.3.1-26
- Allow initrc_t to dbus chat with consolekit.

* Thu Mar 27 2008 Dan Walsh <dwalsh@redhat.com> 3.3.1-25
- Additional access for nsplugin
- Allow xdm setcap/getcap until pulseaudio is fixed

* Tue Mar 25 2008 Dan Walsh <dwalsh@redhat.com> 3.3.1-24
- Allow mount to mkdir on tmpfs
- Allow ifconfig to search debugfs

* Fri Mar 18 2008 Dan Walsh <dwalsh@redhat.com> 3.3.1-23
- Fix file context for MATLAB
- Fixes for xace

* Tue Mar 18 2008 Dan Walsh <dwalsh@redhat.com> 3.3.1-22
- Allow stunnel to transition to inetd children domains
- Make unconfined_dbusd_t an unconfined domain 

* Mon Mar 17 2008 Dan Walsh <dwalsh@redhat.com> 3.3.1-21
- Fixes for qemu/virtd

* Fri Mar 14 2008 Dan Walsh <dwalsh@redhat.com> 3.3.1-20
- Fix bug in mozilla policy to allow xguest transition
- This will fix the 

libsemanage.dbase_llist_query: could not find record value
libsemanage.dbase_llist_query: could not query record value (No such file or
directory)
 bug in xguest

* Fri Mar 14 2008 Dan Walsh <dwalsh@redhat.com> 3.3.1-19
- Allow nsplugin to run acroread

* Thu Mar 13 2008 Dan Walsh <dwalsh@redhat.com> 3.3.1-18
- Add cups_pdf policy
- Add openoffice policy to run in xguest

* Thu Mar 13 2008 Dan Walsh <dwalsh@redhat.com> 3.3.1-17
- prewika needs to contact mysql
- Allow syslog to read system_map files

* Wed Mar 12 2008 Dan Walsh <dwalsh@redhat.com> 3.3.1-16
- Change init_t to an unconfined_domain

* Tue Mar 11 2008 Dan Walsh <dwalsh@redhat.com> 3.3.1-15
- Allow init to transition to initrc_t on shell exec.
- Fix init to be able to sendto init_t.
- Allow syslog to connect to mysql
- Allow lvm to manage its own fifo_files
- Allow bugzilla to use ldap
- More mls fixes 

* Tue Mar 11 2008 Bill Nottingham <notting@redhat.com> 3.3.1-14
- fixes for init policy (#436988)
- fix build

* Mon Mar 10 2008 Dan Walsh <dwalsh@redhat.com> 3.3.1-13
- Additional changes for MLS policy

* Thu Mar 6 2008 Dan Walsh <dwalsh@redhat.com> 3.3.1-12
- Fix initrc_context generation for MLS

* Mon Mar 3 2008 Dan Walsh <dwalsh@redhat.com> 3.3.1-11
- Fixes for libvirt

* Mon Mar 3 2008 Dan Walsh <dwalsh@redhat.com> 3.3.1-10
- Allow bitlebee to read locale_t

* Fri Feb 29 2008 Dan Walsh <dwalsh@redhat.com> 3.3.1-9
- More xselinux rules

* Thu Feb 28 2008 Dan Walsh <dwalsh@redhat.com> 3.3.1-8
- Change httpd_$1_script_r*_t to httpd_$1_content_r*_t

* Wed Feb 27 2008 Dan Walsh <dwalsh@redhat.com> 3.3.1-6
- Prepare policy for beta release
- Change some of the system domains back to unconfined
- Turn on some of the booleans

* Tue Feb 26 2008 Dan Walsh <dwalsh@redhat.com> 3.3.1-5
- Allow nsplugin_config execstack/execmem
- Allow nsplugin_t to read alsa config
- Change apache to use user content 

* Tue Feb 26 2008 Dan Walsh <dwalsh@redhat.com> 3.3.1-4
- Add cyphesis policy

* Tue Feb 26 2008 Dan Walsh <dwalsh@redhat.com> 3.3.1-2
- Fix Makefile.devel to build mls modules
- Fix qemu to be more specific on labeling

* Tue Feb 26 2008 Dan Walsh <dwalsh@redhat.com> 3.3.1-1
- Update to upstream fixes

* Fri Feb 22 2008 Dan Walsh <dwalsh@redhat.com> 3.3.0-2
- Allow staff to mounton user_home_t

* Fri Feb 22 2008 Dan Walsh <dwalsh@redhat.com> 3.3.0-1
- Add xace support

* Thu Feb 21 2008 Dan Walsh <dwalsh@redhat.com> 3.2.9-2
- Add fusectl file system

* Wed Feb 20 2008 Dan Walsh <dwalsh@redhat.com> 3.2.9-1
- Fixes from yum-cron
- Update to latest upstream


* Tue Feb 19 2008 Dan Walsh <dwalsh@redhat.com> 3.2.8-2
- Fix userdom_list_user_files


* Fri Feb 15 2008 Dan Walsh <dwalsh@redhat.com> 3.2.8-1
- Merge with upstream

* Thu Feb 5 2008 Dan Walsh <dwalsh@redhat.com> 3.2.7-6
- Allow udev to send audit messages

* Thu Feb 5 2008 Dan Walsh <dwalsh@redhat.com> 3.2.7-5
- Add additional login users interfaces
  -     userdom_admin_login_user_template(staff)

* Thu Feb 5 2008 Dan Walsh <dwalsh@redhat.com> 3.2.7-3
- More fixes for polkit

* Thu Feb 5 2008 Dan Walsh <dwalsh@redhat.com> 3.2.7-2
- Eliminate transition from unconfined_t to qemu by default
- Fixes for gpg

* Tue Feb 5 2008 Dan Walsh <dwalsh@redhat.com> 3.2.7-1
- Update to upstream

* Tue Feb 5 2008 Dan Walsh <dwalsh@redhat.com> 3.2.6-7
- Fixes for staff_t

* Tue Feb 5 2008 Dan Walsh <dwalsh@redhat.com> 3.2.6-6
- Add policy for kerneloops
- Add policy for gnomeclock

* Mon Feb 4 2008 Dan Walsh <dwalsh@redhat.com> 3.2.6-5
- Fixes for libvirt

* Sun Feb 3 2008 Dan Walsh <dwalsh@redhat.com> 3.2.6-4
- Fixes for nsplugin

* Sat Feb 2 2008 Dan Walsh <dwalsh@redhat.com> 3.2.6-3
- More fixes for qemu

* Sat Feb 2 2008 Dan Walsh <dwalsh@redhat.com> 3.2.6-2
- Additional ports for vnc and allow qemu and libvirt to search all directories

* Fri Feb 1 2008 Dan Walsh <dwalsh@redhat.com> 3.2.6-1
- Update to upstream
- Add libvirt policy
- add qemu policy

* Fri Feb 1 2008 Dan Walsh <dwalsh@redhat.com> 3.2.5-25
- Allow fail2ban to create a socket in /var/run

* Wed Jan 30 2008 Dan Walsh <dwalsh@redhat.com> 3.2.5-24
- Allow allow_httpd_mod_auth_pam to work

* Wed Jan 30 2008 Dan Walsh <dwalsh@redhat.com> 3.2.5-22
- Add audisp policy and prelude

* Mon Jan 28 2008 Dan Walsh <dwalsh@redhat.com> 3.2.5-21
- Allow all user roles to executae samba net command

* Fri Jan 25 2008 Dan Walsh <dwalsh@redhat.com> 3.2.5-20
- Allow usertypes to read/write noxattr file systems

* Thu Jan 24 2008 Dan Walsh <dwalsh@redhat.com> 3.2.5-19
- Fix nsplugin to allow flashplugin to work in enforcing mode

* Wed Jan 23 2008 Dan Walsh <dwalsh@redhat.com> 3.2.5-18
- Allow pam_selinux_permit to kill all processes

* Mon Jan 21 2008 Dan Walsh <dwalsh@redhat.com> 3.2.5-17
- Allow ptrace or user processes by users of same type
- Add boolean for transition to nsplugin

* Mon Jan 21 2008 Dan Walsh <dwalsh@redhat.com> 3.2.5-16
- Allow nsplugin sys_nice, getsched, setsched

* Mon Jan 21 2008 Dan Walsh <dwalsh@redhat.com> 3.2.5-15
- Allow login programs to talk dbus to oddjob

* Thu Jan 17 2008 Dan Walsh <dwalsh@redhat.com> 3.2.5-14
- Add procmail_log support
- Lots of fixes for munin

* Tue Jan 15 2008 Dan Walsh <dwalsh@redhat.com> 3.2.5-13
- Allow setroubleshoot to read policy config and send audit messages

* Mon Jan 14 2008 Dan Walsh <dwalsh@redhat.com> 3.2.5-12
- Allow users to execute all files in homedir, if boolean set
- Allow mount to read samba config

* Sun Jan 13 2008 Dan Walsh <dwalsh@redhat.com> 3.2.5-11
- Fixes for xguest to run java plugin

* Mon Jan 7 2008 Dan Walsh <dwalsh@redhat.com> 3.2.5-10
- dontaudit pam_t and dbusd writing to user_home_t

* Mon Jan 7 2008 Dan Walsh <dwalsh@redhat.com> 3.2.5-9
- Update gpg to allow reading of inotify

* Wed Jan 2 2008 Dan Walsh <dwalsh@redhat.com> 3.2.5-8
- Change user and staff roles to work correctly with varied perms

* Mon Dec 31 2007 Dan Walsh <dwalsh@redhat.com> 3.2.5-7
- Fix munin log,
- Eliminate duplicate mozilla file context
- fix wpa_supplicant spec

* Mon Dec 24 2007 Dan Walsh <dwalsh@redhat.com> 3.2.5-6
- Fix role transition from unconfined_r to system_r when running rpm
- Allow unconfined_domains to communicate with user dbus instances

* Sat Dec 21 2007 Dan Walsh <dwalsh@redhat.com> 3.2.5-5
- Fixes for xguest

* Thu Dec 20 2007 Dan Walsh <dwalsh@redhat.com> 3.2.5-4
- Let all uncofined domains communicate with dbus unconfined

* Thu Dec 20 2007 Dan Walsh <dwalsh@redhat.com> 3.2.5-3
- Run rpm in system_r

* Wed Dec 19 2007 Dan Walsh <dwalsh@redhat.com> 3.2.5-2
- Zero out customizable types

* Wed Dec 19 2007 Dan Walsh <dwalsh@redhat.com> 3.2.5-1
- Fix definiton of admin_home_t

* Wed Dec 19 2007 Dan Walsh <dwalsh@redhat.com> 3.2.4-5
- Fix munin file context

* Tue Dec 18 2007 Dan Walsh <dwalsh@redhat.com> 3.2.4-4
- Allow cron to run unconfined apps

* Mon Dec 17 2007 Dan Walsh <dwalsh@redhat.com> 3.2.4-3
- Modify default login to unconfined_u

* Thu Dec 13 2007 Dan Walsh <dwalsh@redhat.com> 3.2.4-1
- Dontaudit dbus user client search of /root

* Wed Dec 12 2007 Dan Walsh <dwalsh@redhat.com> 3.2.4-1
- Update to upstream

* Tue Dec 11 2007 Dan Walsh <dwalsh@redhat.com> 3.2.3-2
- Fixes for polkit
- Allow xserver to ptrace

* Tue Dec 11 2007 Dan Walsh <dwalsh@redhat.com> 3.2.3-1
- Add polkit policy
- Symplify userdom context, remove automatic per_role changes

* Tue Dec 4 2007 Dan Walsh <dwalsh@redhat.com> 3.2.2-1
- Update to upstream
- Allow httpd_sys_script_t to search users homedirs

* Mon Dec 3 2007 Dan Walsh <dwalsh@redhat.com> 3.2.1-3
- Allow rpm_script to transition to unconfined_execmem_t

* Fri Nov 30 2007 Dan Walsh <dwalsh@redhat.com> 3.2.1-1
- Remove user based home directory separation

* Wed Nov 28 2007 Dan Walsh <dwalsh@redhat.com> 3.1.2-2
- Remove user specific crond_t

* Mon Nov 19 2007 Dan Walsh <dwalhh@redhat.com> 3.1.2-1
- Merge with upstream
- Allow xsever to read hwdata_t
- Allow login programs to setkeycreate

* Sat Nov 10 2007 Dan Walsh <dwalsh@redhat.com> 3.1.1-1
- Update to upstream

* Mon Oct 22 2007 Dan Walsh <dwalsh@redhat.com> 3.1.0-1
- Update to upstream

* Mon Oct 22 2007 Dan Walsh <dwalsh@redhat.com> 3.0.8-30
- Allow XServer to read /proc/self/cmdline
- Fix unconfined cron jobs
- Allow fetchmail to transition to procmail
- Fixes for hald_mac
- Allow system_mail to transition to exim
- Allow tftpd to upload files
- Allow xdm to manage unconfined_tmp
- Allow udef to read alsa config
- Fix xguest to be able to connect to sound port

* Fri Oct 17 2007 Dan Walsh <dwalsh@redhat.com> 3.0.8-28
- Fixes for hald_mac 
- Treat unconfined_home_dir_t as a home dir
- dontaudit rhgb writes to fonts and root

* Fri Oct 17 2007 Dan Walsh <dwalsh@redhat.com> 3.0.8-27
- Fix dnsmasq
- Allow rshd full login privs

* Thu Oct 16 2007 Dan Walsh <dwalsh@redhat.com> 3.0.8-26
- Allow rshd to connect to ports > 1023

* Thu Oct 16 2007 Dan Walsh <dwalsh@redhat.com> 3.0.8-25
- Fix vpn to bind to port 4500
- Allow ssh to create shm
- Add Kismet policy

* Tue Oct 16 2007 Dan Walsh <dwalsh@redhat.com> 3.0.8-24
- Allow rpm to chat with networkmanager

* Mon Oct 15 2007 Dan Walsh <dwalsh@redhat.com> 3.0.8-23
- Fixes for ipsec and exim mail
- Change default to unconfined user

* Fri Oct 12 2007 Dan Walsh <dwalsh@redhat.com> 3.0.8-22
- Pass the UNK_PERMS param to makefile
- Fix gdm location

* Wed Oct 10 2007 Dan Walsh <dwalsh@redhat.com> 3.0.8-21
- Make alsa work

* Tue Oct 9 2007 Dan Walsh <dwalsh@redhat.com> 3.0.8-20
- Fixes for consolekit and startx sessions

* Mon Oct 8 2007 Dan Walsh <dwalsh@redhat.com> 3.0.8-19
- Dontaudit consoletype talking to unconfined_t

* Thu Oct 4 2007 Dan Walsh <dwalsh@redhat.com> 3.0.8-18
- Remove homedir_template

* Tue Oct 2 2007 Dan Walsh <dwalsh@redhat.com> 3.0.8-17
- Check asound.state

* Mon Oct 1 2007 Dan Walsh <dwalsh@redhat.com> 3.0.8-16
- Fix exim policy

* Thu Sep 24 2007 Dan Walsh <dwalsh@redhat.com> 3.0.8-15
- Allow tmpreadper to read man_t
- Allow racoon to bind to all nodes
- Fixes for finger print reader

* Tue Sep 24 2007 Dan Walsh <dwalsh@redhat.com> 3.0.8-14
- Allow xdm to talk to input device (fingerprint reader)
- Allow octave to run as java

* Tue Sep 24 2007 Dan Walsh <dwalsh@redhat.com> 3.0.8-13
- Allow login programs to set ioctl on /proc

* Mon Sep 24 2007 Dan Walsh <dwalsh@redhat.com> 3.0.8-12
- Allow nsswitch apps to read samba_var_t

* Mon Sep 24 2007 Dan Walsh <dwalsh@redhat.com> 3.0.8-11
- Fix maxima

* Mon Sep 24 2007 Dan Walsh <dwalsh@redhat.com> 3.0.8-10
- Eliminate rpm_t:fifo_file avcs
- Fix dbus path for helper app

* Sat Sep 22 2007 Dan Walsh <dwalsh@redhat.com> 3.0.8-9
- Fix service start stop terminal avc's

* Fri Sep 21 2007 Dan Walsh <dwalsh@redhat.com> 3.0.8-8
- Allow also to search var_lib
- New context for dbus launcher 

* Fri Sep 21 2007 Dan Walsh <dwalsh@redhat.com> 3.0.8-7
- Allow cupsd_config_t to read/write usb_device_t
- Support for finger print reader,
- Many fixes for clvmd
- dbus starting networkmanager

* Thu Sep 20 2007 Dan Walsh <dwalsh@redhat.com> 3.0.8-5
- Fix java and mono to run in xguest account

* Wed Sep 19 2007 Dan Walsh <dwalsh@redhat.com> 3.0.8-4
- Fix to add xguest account when inititial install
- Allow mono, java, wine to run in userdomains

* Wed Sep 19 2007 Dan Walsh <dwalsh@redhat.com> 3.0.8-3
- Allow xserver to search devpts_t
- Dontaudit ldconfig output to homedir

* Tue Sep 18 2007 Dan Walsh <dwalsh@redhat.com> 3.0.8-2
- Remove hplip_etc_t change back to etc_t.


* Mon Sep 17 2007 Dan Walsh <dwalsh@redhat.com> 3.0.8-1
- Allow cron to search nfs and samba homedirs

* Tue Sep 11 2007 Dan Walsh <dwalsh@redhat.com> 3.0.7-10
- Allow NetworkManager to dbus chat with yum-updated

* Tue Sep 11 2007 Dan Walsh <dwalsh@redhat.com> 3.0.7-9
- Allow xfs to bind to port 7100

* Mon Sep 10 2007 Dan Walsh <dwalsh@redhat.com> 3.0.7-8
- Allow newalias/sendmail dac_override
- Allow bind to bind to all udp ports

* Fri Sep 7 2007 Dan Walsh <dwalsh@redhat.com> 3.0.7-7
- Turn off direct transition

* Fri Sep 7 2007 Dan Walsh <dwalsh@redhat.com> 3.0.7-6
- Allow wine to run in system role

* Thu Sep 6 2007 Dan Walsh <dwalsh@redhat.com> 3.0.7-5
- Fix java labeling 

* Thu Sep 6 2007 Dan Walsh <dwalsh@redhat.com> 3.0.7-4
- Define user_home_type as home_type

* Tue Aug 28 2007 Dan Walsh <dwalsh@redhat.com> 3.0.7-3
- Allow sendmail to create etc_aliases_t

* Tue Aug 28 2007 Dan Walsh <dwalsh@redhat.com> 3.0.7-2
- Allow login programs to read symlinks on homedirs

* Mon Aug 27 2007 Dan Walsh <dwalsh@redhat.com> 3.0.7-1
- Update an readd modules

* Fri Aug 24 2007 Dan Walsh <dwalsh@redhat.com> 3.0.6-3
- Cleanup  spec file

* Fri Aug 24 2007 Dan Walsh <dwalsh@redhat.com> 3.0.6-2
- Allow xserver to be started by unconfined process and talk to tty

* Wed Aug 22 2007 Dan Walsh <dwalsh@redhat.com> 3.0.6-1
- Upgrade to upstream to grab postgressql changes

* Tue Aug 21 2007 Dan Walsh <dwalsh@redhat.com> 3.0.5-11
- Add setransd for mls policy

* Mon Aug 20 2007 Dan Walsh <dwalsh@redhat.com> 3.0.5-10
- Add ldconfig_cache_t

* Sat Aug 18 2007 Dan Walsh <dwalsh@redhat.com> 3.0.5-9
- Allow sshd to write to proc_t for afs login

* Sat Aug 18 2007 Dan Walsh <dwalsh@redhat.com> 3.0.5-8
- Allow xserver access to urand

* Tue Aug 14 2007 Dan Walsh <dwalsh@redhat.com> 3.0.5-7
- allow dovecot to search mountpoints

* Sat Aug 11 2007 Dan Walsh <dwalsh@redhat.com> 3.0.5-6
- Fix Makefile for building policy modules

* Fri Aug 10 2007 Dan Walsh <dwalsh@redhat.com> 3.0.5-5
- Fix dhcpc startup of service 

* Fri Aug 10 2007 Dan Walsh <dwalsh@redhat.com> 3.0.5-4
- Fix dbus chat to not happen for xguest and guest users

* Mon Aug 6 2007 Dan Walsh <dwalsh@redhat.com> 3.0.5-3
- Fix nagios cgi
- allow squid to communicate with winbind

* Mon Aug 6 2007 Dan Walsh <dwalsh@redhat.com> 3.0.5-2
- Fixes for ldconfig

* Thu Aug 2 2007 Dan Walsh <dwalsh@redhat.com> 3.0.5-1
- Update from upstream

* Wed Aug 1 2007 Dan Walsh <dwalsh@redhat.com> 3.0.4-6
- Add nasd support

* Wed Aug 1 2007 Dan Walsh <dwalsh@redhat.com> 3.0.4-5
- Fix new usb devices and dmfm

* Mon Jul 30 2007 Dan Walsh <dwalsh@redhat.com> 3.0.4-4
- Eliminate mount_ntfs_t policy, merge into mount_t

* Mon Jul 30 2007 Dan Walsh <dwalsh@redhat.com> 3.0.4-3
- Allow xserver to write to ramfs mounted by rhgb

* Tue Jul 23 2007 Dan Walsh <dwalsh@redhat.com> 3.0.4-2
- Add context for dbus machine id

* Tue Jul 23 2007 Dan Walsh <dwalsh@redhat.com> 3.0.4-1
- Update with latest changes from upstream

* Tue Jul 23 2007 Dan Walsh <dwalsh@redhat.com> 3.0.3-6
- Fix prelink to handle execmod

* Mon Jul 23 2007 Dan Walsh <dwalsh@redhat.com> 3.0.3-5
- Add ntpd_key_t to handle secret data

* Fri Jul 20 2007 Dan Walsh <dwalsh@redhat.com> 3.0.3-4
- Add anon_inodefs
- Allow unpriv user exec pam_exec_t
- Fix trigger

* Fri Jul 20 2007 Dan Walsh <dwalsh@redhat.com> 3.0.3-3
- Allow cups to use generic usb
- fix inetd to be able to run random apps (git)

* Thu Jul 19 2007 Dan Walsh <dwalsh@redhat.com> 3.0.3-2
- Add proper contexts for rsyslogd

* Thu Jul 19 2007 Dan Walsh <dwalsh@redhat.com> 3.0.3-1
- Fixes for xguest policy

* Tue Jul 17 2007 Dan Walsh <dwalsh@redhat.com> 3.0.2-9
- Allow execution of gconf

* Sat Jul 14 2007 Dan Walsh <dwalsh@redhat.com> 3.0.2-8
- Fix moilscanner update problem

* Thu Jul 12 2007 Dan Walsh <dwalsh@redhat.com> 3.0.2-7
- Begin adding policy to separate setsebool from semanage
- Fix xserver.if definition to not break sepolgen.if

* Wed Jul 11 2007 Dan Walsh <dwalsh@redhat.com> 3.0.2-5
- Add new devices

* Tue Jul 10 2007 Dan Walsh <dwalsh@redhat.com> 3.0.2-4
- Add brctl policy

* Fri Jul 6 2007 Dan Walsh <dwalsh@redhat.com> 3.0.2-3
- Fix root login to include system_r

* Fri Jul 6 2007 Dan Walsh <dwalsh@redhat.com> 3.0.2-2
- Allow prelink to read kernel sysctls

* Mon Jul 2 2007 Dan Walsh <dwalsh@redhat.com> 3.0.1-5
- Default to user_u:system_r:unconfined_t 

* Sun Jul 1 2007 Dan Walsh <dwalsh@redhat.com> 3.0.1-4
- fix squid
- Fix rpm running as uid

* Wed Jun 26 2007 Dan Walsh <dwalsh@redhat.com> 3.0.1-3
- Fix syslog declaration

* Wed Jun 26 2007 Dan Walsh <dwalsh@redhat.com> 3.0.1-2
- Allow avahi to access inotify
- Remove a lot of bogus security_t:filesystem avcs

* Fri May 25 2007 Dan Walsh <dwalsh@redhat.com> 3.0.1-1
- Remove ifdef strict policy from upstream

* Fri May 18 2007 Dan Walsh <dwalsh@redhat.com> 2.6.5-3
- Remove ifdef strict to allow user_u to login 

* Fri May 18 2007 Dan Walsh <dwalsh@redhat.com> 2.6.5-2
- Fix for amands
- Allow semanage to read pp files
- Allow rhgb to read xdm_xserver_tmp

* Fri May 18 2007 Dan Walsh <dwalsh@redhat.com> 2.6.4-7
- Allow kerberos servers to use ldap for backing store

* Thu May 17 2007 Dan Walsh <dwalsh@redhat.com> 2.6.4-6
- allow alsactl to read kernel state

* Wed May 16 2007 Dan Walsh <dwalsh@redhat.com> 2.6.4-5
- More fixes for alsactl
- Transition from hal and modutils
- Fixes for suspend resume.  
     - insmod domtrans to alsactl
     - insmod writes to hal log

* Wed May 16 2007 Dan Walsh <dwalsh@redhat.com> 2.6.4-2
- Allow unconfined_t to transition to NetworkManager_t
- Fix netlabel policy

* Mon May 14 2007 Dan Walsh <dwalsh@redhat.com> 2.6.4-1
- Update to latest from upstream

* Fri May 4 2007 Dan Walsh <dwalsh@redhat.com> 2.6.3-1
- Update to latest from upstream

* Mon Apr 30 2007 Dan Walsh <dwalsh@redhat.com> 2.6.2-1
- Update to latest from upstream

* Fri Apr 27 2007 Dan Walsh <dwalsh@redhat.com> 2.6.1-4
- Allow pcscd_t to send itself signals

* Fri Apr 27 2007 Dan Walsh <dwalsh@redhat.com> 2.6.1-3
- 

* Wed Apr 25 2007 Dan Walsh <dwalsh@redhat.com> 2.6.1-2
- Fixes for unix_update
- Fix logwatch to be able to search all dirs

* Mon Apr 23 2007 Dan Walsh <dwalsh@redhat.com> 2.6.1-1
- Upstream bumped the version

* Thu Apr 19 2007 Dan Walsh <dwalsh@redhat.com> 2.5.12-12
- Allow consolekit to syslog
- Allow ntfs to work with hal

* Thu Apr 19 2007 Dan Walsh <dwalsh@redhat.com> 2.5.12-11
- Allow iptables to read etc_runtime_t

* Thu Apr 19 2007 Dan Walsh <dwalsh@redhat.com> 2.5.12-10
- MLS Fixes

* Wed Apr 18 2007 Dan Walsh <dwalsh@redhat.com> 2.5.12-8
- Fix path of /etc/lvm/cache directory
- Fixes for alsactl and pppd_t
- Fixes for consolekit

* Tue Apr 17 2007 Dan Walsh <dwalsh@redhat.com> 2.5.12-5
- Allow insmod_t to mount kvmfs_t filesystems

* Tue Apr 17 2007 Dan Walsh <dwalsh@redhat.com> 2.5.12-4
- Rwho policy
- Fixes for consolekit

* Fri Apr 12 2007 Dan Walsh <dwalsh@redhat.com> 2.5.12-3
- fixes for fusefs

* Thu Apr 12 2007 Dan Walsh <dwalsh@redhat.com> 2.5.12-2
- Fix samba_net to allow it to view samba_var_t

* Tue Apr 10 2007 Dan Walsh <dwalsh@redhat.com> 2.5.12-1
- Update to upstream

* Tue Apr 10 2007 Dan Walsh <dwalsh@redhat.com> 2.5.11-8
- Fix Sonypic backlight
- Allow snmp to look at squid_conf_t

* Mon Apr 9 2007 Dan Walsh <dwalsh@redhat.com> 2.5.11-7
- Fixes for pyzor, cyrus, consoletype on everything installs

* Mon Apr 9 2007 Dan Walsh <dwalsh@redhat.com> 2.5.11-6
- Fix hald_acl_t to be able to getattr/setattr on usb devices
- Dontaudit write to unconfined_pipes for load_policy

* Thu Apr 5 2007 Dan Walsh <dwalsh@redhat.com> 2.5.11-5
- Allow bluetooth to read inotifyfs

* Wed Apr 4 2007 Dan Walsh <dwalsh@redhat.com> 2.5.11-4
- Fixes for samba domain controller.
- Allow ConsoleKit to look at ttys

* Tue Apr 3 2007 Dan Walsh <dwalsh@redhat.com> 2.5.11-3
- Fix interface call

* Tue Apr 3 2007 Dan Walsh <dwalsh@redhat.com> 2.5.11-2
- Allow syslog-ng to read /var
- Allow locate to getattr on all filesystems
- nscd needs setcap

* Mon Mar 26 2007 Dan Walsh <dwalsh@redhat.com> 2.5.11-1
- Update to upstream

* Fri Mar 23 2007 Dan Walsh <dwalsh@redhat.com> 2.5.10-2
- Allow samba to run groupadd

* Thu Mar 22 2007 Dan Walsh <dwalsh@redhat.com> 2.5.10-1
- Update to upstream

* Thu Mar 22 2007 Dan Walsh <dwalsh@redhat.com> 2.5.9-6
- Allow mdadm to access generic scsi devices

* Wed Mar 21 2007 Dan Walsh <dwalsh@redhat.com> 2.5.9-5
- Fix labeling on udev.tbl dirs

* Tue Mar 20 2007 Dan Walsh <dwalsh@redhat.com> 2.5.9-4
- Fixes for logwatch

* Tue Mar 20 2007 Dan Walsh <dwalsh@redhat.com> 2.5.9-3
- Add fusermount and mount_ntfs policy

* Tue Mar 20 2007 Dan Walsh <dwalsh@redhat.com> 2.5.9-2
- Update to upstream
- Allow saslauthd to use kerberos keytabs

* Mon Mar 19 2007 Dan Walsh <dwalsh@redhat.com> 2.5.8-8
- Fixes for samba_var_t

* Mon Mar 19 2007 Dan Walsh <dwalsh@redhat.com> 2.5.8-7
- Allow networkmanager to setpgid
- Fixes for hal_acl_t

* Mon Mar 19 2007 Dan Walsh <dwalsh@redhat.com> 2.5.8-6
- Remove disable_trans booleans
- hald_acl_t needs to talk to nscd

* Thu Mar 15 2007 Dan Walsh <dwalsh@redhat.com> 2.5.8-5
- Fix prelink to be able to manage usr dirs.

* Tue Mar 13 2007 Dan Walsh <dwalsh@redhat.com> 2.5.8-4
- Allow insmod to launch init scripts

* Tue Mar 13 2007 Dan Walsh <dwalsh@redhat.com> 2.5.8-3
- Remove setsebool policy

* Mon Mar 12 2007 Dan Walsh <dwalsh@redhat.com> 2.5.8-2
- Fix handling of unlabled_t packets

* Thu Mar 8 2007 Dan Walsh <dwalsh@redhat.com> 2.5.8-1
- More of my patches from upstream

* Thu Mar 1 2007 Dan Walsh <dwalsh@redhat.com> 2.5.7-1
- Update to latest from upstream
- Add fail2ban policy

* Wed Feb 28 2007 Dan Walsh <dwalsh@redhat.com> 2.5.6-1
- Update to remove security_t:filesystem getattr problems

* Fri Feb 23 2007 Dan Walsh <dwalsh@redhat.com> 2.5.5-2
- Policy for consolekit

* Fri Feb 23 2007 Dan Walsh <dwalsh@redhat.com> 2.5.5-1
- Update to latest from upstream

* Wed Feb 21 2007 Dan Walsh <dwalsh@redhat.com> 2.5.4-2
- Revert Nemiver change
- Set sudo as a corecmd so prelink will work,  remove sudoedit mapping, since this will not work, it does not transition.
- Allow samba to execute useradd

* Tue Feb 20 2007 Dan Walsh <dwalsh@redhat.com> 2.5.4-1
- Upgrade to the latest from upstream

* Thu Feb 15 2007 Dan Walsh <dwalsh@redhat.com> 2.5.3-3
- Add sepolgen support
- Add bugzilla policy

* Wed Feb 14 2007 Dan Walsh <dwalsh@redhat.com> 2.5.3-2
- Fix file context for nemiver

* Sun Feb 11 2007 Dan Walsh <dwalsh@redhat.com> 2.5.3-1
- Remove include sym link

* Mon Feb 5 2007 Dan Walsh <dwalsh@redhat.com> 2.5.2-6
- Allow mozilla, evolution and thunderbird to read dev_random.
Resolves: #227002
- Allow spamd to connect to smtp port
Resolves: #227184
- Fixes to make ypxfr work
Resolves: #227237

* Sun Feb 4 2007 Dan Walsh <dwalsh@redhat.com> 2.5.2-5
- Fix ssh_agent to be marked as an executable
- Allow Hal to rw sound device 

* Thu Feb 1 2007 Dan Walsh <dwalsh@redhat.com> 2.5.2-4
- Fix spamassisin so crond can update spam files
- Fixes to allow kpasswd to work
- Fixes for bluetooth

* Fri Jan 25 2007 Dan Walsh <dwalsh@redhat.com> 2.5.2-3
- Remove some targeted diffs in file context file

* Thu Jan 25 2007 Dan Walsh <dwalsh@redhat.com> 2.5.2-2
- Fix squid cachemgr labeling

* Thu Jan 25 2007 Dan Walsh <dwalsh@redhat.com> 2.5.2-1
- Add ability to generate webadm_t policy
- Lots of new interfaces for httpd
- Allow sshd to login as unconfined_t

* Mon Jan 22 2007 Dan Walsh <dwalsh@redhat.com> 2.5.1-5
- Continue fixing, additional user domains

* Wed Jan 10 2007 Dan Walsh <dwalsh@redhat.com> 2.5.1-4
- Begin adding user confinement to targeted policy 

* Wed Jan 10 2007 Dan Walsh <dwalsh@redhat.com> 2.5.1-2
- Fixes for prelink, ktalkd, netlabel

* Mon Jan 8 2007 Dan Walsh <dwalsh@redhat.com> 2.5.1-1
- Allow prelink when run from rpm to create tmp files
Resolves: #221865
- Remove file_context for exportfs
Resolves: #221181
- Allow spamassassin to create ~/.spamassissin
Resolves: #203290
- Allow ssh access to the krb tickets
- Allow sshd to change passwd
- Stop newrole -l from working on non securetty
Resolves: #200110
- Fixes to run prelink in MLS machine
Resolves: #221233
- Allow spamassassin to read var_lib_t dir
Resolves: #219234

* Fri Dec 29 2006 Dan Walsh <dwalsh@redhat.com> 2.4.6-20
- fix mplayer to work under strict policy
- Allow iptables to use nscd
Resolves: #220794

* Thu Dec 28 2006 Dan Walsh <dwalsh@redhat.com> 2.4.6-19
- Add gconf policy and make it work with strict

* Sat Dec 23 2006 Dan Walsh <dwalsh@redhat.com> 2.4.6-18
- Many fixes for strict policy and by extension mls.

* Fri Dec 22 2006 Dan Walsh <dwalsh@redhat.com> 2.4.6-17
- Fix to allow ftp to bind to ports > 1024
Resolves: #219349

* Tue Dec 19 2006 Dan Walsh <dwalsh@redhat.com> 2.4.6-16
- Allow semanage to exec it self.  Label genhomedircon as semanage_exec_t
Resolves: #219421
- Allow sysadm_lpr_t to manage other print spool jobs
Resolves: #220080

* Mon Dec 18 2006 Dan Walsh <dwalsh@redhat.com> 2.4.6-15
- allow automount to setgid
Resolves: #219999

* Thu Dec 14 2006 Dan Walsh <dwalsh@redhat.com> 2.4.6-14
- Allow cron to polyinstatiate 
- Fix creation of boot flags
Resolves: #207433

* Thu Dec 14 2006 Dan Walsh <dwalsh@redhat.com> 2.4.6-13
- Fixes for irqbalance
Resolves: #219606

* Thu Dec 14 2006 Dan Walsh <dwalsh@redhat.com> 2.4.6-12
- Fix vixie-cron to work on mls
Resolves: #207433

* Wed Dec 13 2006 Dan Walsh <dwalsh@redhat.com> 2.4.6-11
Resolves: #218978

* Tue Dec 12 2006 Dan Walsh <dwalsh@redhat.com> 2.4.6-10
- Allow initrc to create files in /var directories
Resolves: #219227

* Fri Dec 8 2006 Dan Walsh <dwalsh@redhat.com> 2.4.6-9
- More fixes for MLS
Resolves: #181566

* Wed Dec 6 2006 Dan Walsh <dwalsh@redhat.com> 2.4.6-8
- More Fixes polyinstatiation
Resolves: #216184

* Wed Dec 6 2006 Dan Walsh <dwalsh@redhat.com> 2.4.6-7
- More Fixes polyinstatiation
- Fix handling of keyrings
Resolves: #216184

* Mon Dec 4 2006 Dan Walsh <dwalsh@redhat.com> 2.4.6-6
- Fix polyinstatiation
- Fix pcscd handling of terminal
Resolves: #218149
Resolves: #218350

* Fri Dec 1 2006 Dan Walsh <dwalsh@redhat.com> 2.4.6-5
- More fixes for quota
Resolves: #212957

* Fri Dec 1 2006 Dan Walsh <dwalsh@redhat.com> 2.4.6-4
- ncsd needs to use avahi sockets
Resolves: #217640
Resolves: #218014

* Thu Nov 28 2006 Dan Walsh <dwalsh@redhat.com> 2.4.6-3
- Allow login programs to polyinstatiate homedirs
Resolves: #216184
- Allow quotacheck to create database files
Resolves: #212957

* Tue Nov 28 2006 Dan Walsh <dwalsh@redhat.com> 2.4.6-1
- Dontaudit appending hal_var_lib files 
Resolves: #217452
Resolves: #217571
Resolves: #217611
Resolves: #217640
Resolves: #217725

* Mon Nov 21 2006 Dan Walsh <dwalsh@redhat.com> 2.4.5-4
- Fix context for helix players file_context #216942

* Mon Nov 20 2006 Dan Walsh <dwalsh@redhat.com> 2.4.5-3
- Fix load_policy to be able to mls_write_down so it can talk to the terminal

* Mon Nov 20 2006 Dan Walsh <dwalsh@redhat.com> 2.4.5-2
- Fixes for hwclock, clamav, ftp

* Wed Nov 15 2006 Dan Walsh <dwalsh@redhat.com> 2.4.5-1
- Move to upstream version which accepted my patches

* Wed Nov 15 2006 Dan Walsh <dwalsh@redhat.com> 2.4.4-2
- Fixes for nvidia driver

* Tue Nov 14 2006 Dan Walsh <dwalsh@redhat.com> 2.4.4-2
- Allow semanage to signal mcstrans

* Tue Nov 14 2006 Dan Walsh <dwalsh@redhat.com> 2.4.4-1
- Update to upstream

* Mon Nov 13 2006 Dan Walsh <dwalsh@redhat.com> 2.4.3-13
- Allow modstorage to edit /etc/fstab file

* Mon Nov 13 2006 Dan Walsh <dwalsh@redhat.com> 2.4.3-12
- Fix for qemu, /dev/

* Mon Nov 13 2006 Dan Walsh <dwalsh@redhat.com> 2.4.3-11
- Fix path to realplayer.bin

* Fri Nov 10 2006 Dan Walsh <dwalsh@redhat.com> 2.4.3-10
- Allow xen to connect to xen port

* Fri Nov 10 2006 Dan Walsh <dwalsh@redhat.com> 2.4.3-9
- Allow cups to search samba_etc_t directory
- Allow xend_t to list auto_mountpoints

* Thu Nov 9 2006 Dan Walsh <dwalsh@redhat.com> 2.4.3-8
- Allow xen to search automount

* Thu Nov 9 2006 Dan Walsh <dwalsh@redhat.com> 2.4.3-7
- Fix spec of jre files 

* Wed Nov 8 2006 Dan Walsh <dwalsh@redhat.com> 2.4.3-6
- Fix unconfined access to shadow file

* Wed Nov 8 2006 Dan Walsh <dwalsh@redhat.com> 2.4.3-5
- Allow xend to create files in xen_image_t directories

* Wed Nov 8 2006 Dan Walsh <dwalsh@redhat.com> 2.4.3-4
- Fixes for /var/lib/hal

* Tue Nov 7 2006 Dan Walsh <dwalsh@redhat.com> 2.4.3-3
- Remove ability for sysadm_t to look at audit.log

* Tue Nov 7 2006 Dan Walsh <dwalsh@redhat.com> 2.4.3-2
- Fix rpc_port_types
- Add aide policy for mls

* Mon Nov 6 2006 Dan Walsh <dwalsh@redhat.com> 2.4.3-1
- Merge with upstream

* Fri Nov 3 2006 Dan Walsh <dwalsh@redhat.com> 2.4.2-8
- Lots of fixes for ricci

* Fri Nov 3 2006 Dan Walsh <dwalsh@redhat.com> 2.4.2-7
- Allow xen to read/write fixed devices with a boolean
- Allow apache to search /var/log

* Thu Nov 2 2006 James Antill <james.antill@redhat.com> 2.4.2-6
- Fix policygentool specfile problem.
- Allow apache to send signals to it's logging helpers.
- Resolves: rhbz#212731

* Wed Nov 1 2006 Dan Walsh <dwalsh@redhat.com> 2.4.2-5
- Add perms for swat

* Tue Oct 31 2006 Dan Walsh <dwalsh@redhat.com> 2.4.2-4
- Add perms for swat

* Mon Oct 30 2006 Dan Walsh <dwalsh@redhat.com> 2.4.2-3
- Allow daemons to dump core files to /

* Fri Oct 27 2006 Dan Walsh <dwalsh@redhat.com> 2.4.2-2
- Fixes for ricci

* Fri Oct 27 2006 Dan Walsh <dwalsh@redhat.com> 2.4.2-1
- Allow mount.nfs to work

* Fri Oct 27 2006 Dan Walsh <dwalsh@redhat.com> 2.4.1-5
- Allow ricci-modstorage to look at lvm_etc_t

* Mon Oct 23 2006 Dan Walsh <dwalsh@redhat.com> 2.4.1-4
- Fixes for ricci using saslauthd

* Mon Oct 23 2006 Dan Walsh <dwalsh@redhat.com> 2.4.1-3
- Allow mountpoint on home_dir_t and home_t

* Mon Oct 23 2006 Dan Walsh <dwalsh@redhat.com> 2.4.1-2
- Update xen to read nfs files

* Mon Oct 23 2006 Dan Walsh <dwalsh@redhat.com> 2.4-4
- Allow noxattrfs to associate with other noxattrfs 

* Mon Oct 23 2006 Dan Walsh <dwalsh@redhat.com> 2.4-3
- Allow hal to use power_device_t

* Fri Oct 20 2006 Dan Walsh <dwalsh@redhat.com> 2.4-2
- Allow procemail to look at autofs_t
- Allow xen_image_t to work as a fixed device

* Thu Oct 19 2006 Dan Walsh <dwalsh@redhat.com> 2.4-1
- Refupdate from upstream

* Thu Oct 19 2006 Dan Walsh <dwalsh@redhat.com> 2.3.19-4
- Add lots of fixes for mls cups

* Wed Oct 18 2006 Dan Walsh <dwalsh@redhat.com> 2.3.19-3
- Lots of fixes for ricci


* Mon Oct 16 2006 Dan Walsh <dwalsh@redhat.com> 2.3.19-2
- Fix number of cats

* Mon Oct 16 2006 Dan Walsh <dwalsh@redhat.com> 2.3.19-1
- Update to upstream

* Thu Oct 12 2006 James Antill <jantill@redhat.com> 2.3.18-10
- More iSCSI changes for #209854

* Tue Oct 10 2006 James Antill <jantill@redhat.com> 2.3.18-9
- Test ISCSI fixes for #209854

* Sun Oct 8 2006 Dan Walsh <dwalsh@redhat.com> 2.3.18-8
- allow semodule to rmdir selinux_config_t dir

* Fri Oct 6 2006 Dan Walsh <dwalsh@redhat.com> 2.3.18-7
- Fix boot_runtime_t problem on ppc.  Should not be creating these files.

* Thu Oct 5 2006 Dan Walsh <dwalsh@redhat.com> 2.3.18-6
- Fix context mounts on reboot
- Fix ccs creation of directory in /var/log

* Thu Oct 5 2006 Dan Walsh <dwalsh@redhat.com> 2.3.18-5
- Update for tallylog

* Thu Oct 5 2006 Dan Walsh <dwalsh@redhat.com> 2.3.18-4
- Allow xend to rewrite dhcp conf files
- Allow mgetty sys_admin capability

* Wed Oct 4 2006 Dan Walsh <dwalsh@redhat.com> 2.3.18-3
- Make xentapctrl work

* Tue Oct 3 2006 Dan Walsh <dwalsh@redhat.com> 2.3.18-2
- Don't transition unconfined_t to bootloader_t
- Fix label in /dev/xen/blktap

* Tue Oct 3 2006 Dan Walsh <dwalsh@redhat.com> 2.3.18-1
- Patch for labeled networking

* Mon Oct 2 2006 Dan Walsh <dwalsh@redhat.com> 2.3.17-2
- Fix crond handling for mls

* Fri Sep 28 2006 Dan Walsh <dwalsh@redhat.com> 2.3.17-1
- Update to upstream

* Fri Sep 28 2006 Dan Walsh <dwalsh@redhat.com> 2.3.16-9
- Remove bluetooth-helper transition
- Add selinux_validate for semanage
- Require new version of libsemanage

* Fri Sep 28 2006 Dan Walsh <dwalsh@redhat.com> 2.3.16-8
- Fix prelink

* Fri Sep 28 2006 Dan Walsh <dwalsh@redhat.com> 2.3.16-7
- Fix rhgb

* Thu Sep 27 2006 Dan Walsh <dwalsh@redhat.com> 2.3.16-6
- Fix setrans handling on MLS and useradd

* Wed Sep 27 2006 Dan Walsh <dwalsh@redhat.com> 2.3.16-5
- Support for fuse
- fix vigr

* Wed Sep 27 2006 Dan Walsh <dwalsh@redhat.com> 2.3.16-4
- Fix dovecot, amanda
- Fix mls

* Mon Sep 25 2006 Dan Walsh <dwalsh@redhat.com> 2.3.16-2
- Allow java execheap for itanium

* Mon Sep 25 2006 Dan Walsh <dwalsh@redhat.com> 2.3.16-1
- Update with upstream

* Mon Sep 25 2006 Dan Walsh <dwalsh@redhat.com> 2.3.15-2
- mls fixes 

* Fri Sep 22 2006 Dan Walsh <dwalsh@redhat.com> 2.3.15-1
- Update from upstream 

* Fri Sep 22 2006 Dan Walsh <dwalsh@redhat.com> 2.3.14-8
- More fixes for mls
- Revert change on automount transition to mount

* Wed Sep 20 2006 Dan Walsh <dwalsh@redhat.com> 2.3.14-7
- Fix cron jobs to run under the correct context

* Tue Sep 19 2006 Dan Walsh <dwalsh@redhat.com> 2.3.14-6
- Fixes to make pppd work

* Mon Sep 18 2006 Dan Walsh <dwalsh@redhat.com> 2.3.14-4
- Multiple policy fixes
- Change max categories to 1023

* Sat Sep 16 2006 Dan Walsh <dwalsh@redhat.com> 2.3.14-3
- Fix transition on mcstransd

* Fri Sep 15 2006 Dan Walsh <dwalsh@redhat.com> 2.3.14-2
- Add /dev/em8300 defs

* Fri Sep 15 2006 Dan Walsh <dwalsh@redhat.com> 2.3.14-1
- Upgrade to upstream

* Thu Sep 14 2006 Dan Walsh <dwalsh@redhat.com> 2.3.13-6
- Fix ppp connections from network manager

* Wed Sep 13 2006 Dan Walsh <dwalsh@redhat.com> 2.3.13-5
- Add tty access to all domains boolean
- Fix gnome-pty-helper context for ia64

* Mon Sep 11 2006 Dan Walsh <dwalsh@redhat.com> 2.3.13-4
- Fixed typealias of firstboot_rw_t

* Thu Sep 7 2006 Dan Walsh <dwalsh@redhat.com> 2.3.13-3
- Fix location of xel log files
- Fix handling of sysadm_r -> rpm_exec_t 

* Thu Sep 7 2006 Dan Walsh <dwalsh@redhat.com> 2.3.13-2
- Fixes for autofs, lp

* Wed Sep 6 2006 Dan Walsh <dwalsh@redhat.com> 2.3.13-1
- Update from upstream

* Tue Sep 5 2006 Dan Walsh <dwalsh@redhat.com> 2.3.12-2
- Fixup for test6

* Tue Sep 5 2006 Dan Walsh <dwalsh@redhat.com> 2.3.12-1
- Update to upstream

* Fri Sep 1 2006 Dan Walsh <dwalsh@redhat.com> 2.3.11-1
- Update to upstream

* Fri Sep 1 2006 Dan Walsh <dwalsh@redhat.com> 2.3.10-7
- Fix suspend to disk problems

* Thu Aug 31 2006 Dan Walsh <dwalsh@redhat.com> 2.3.10-6
- Lots of fixes for restarting daemons at the console.

* Wed Aug 30 2006 Dan Walsh <dwalsh@redhat.com> 2.3.10-3
- Fix audit line
- Fix requires line

* Tue Aug 29 2006 Dan Walsh <dwalsh@redhat.com> 2.3.10-1
- Upgrade to upstream

* Mon Aug 28 2006 Dan Walsh <dwalsh@redhat.com> 2.3.9-6
- Fix install problems

* Fri Aug 25 2006 Dan Walsh <dwalsh@redhat.com> 2.3.9-5
- Allow setroubleshoot to getattr on all dirs to gather RPM data

* Thu Aug 24 2006 Dan Walsh <dwalsh@redhat.com> 2.3.9-4
- Set /usr/lib/ia32el/ia32x_loader to unconfined_execmem_exec_t for ia32 platform
- Fix spec for /dev/adsp

* Thu Aug 24 2006 Dan Walsh <dwalsh@redhat.com> 2.3.9-3
- Fix xen tty devices

* Thu Aug 24 2006 Dan Walsh <dwalsh@redhat.com> 2.3.9-2
- Fixes for setroubleshoot

* Wed Aug 23 2006 Dan Walsh <dwalsh@redhat.com> 2.3.9-1
- Update to upstream

* Sun Aug 20 2006 Dan Walsh <dwalsh@redhat.com> 2.3.8-2
- Fixes for stunnel and postgresql
- Update from upstream

* Sat Aug 10 2006 Dan Walsh <dwalsh@redhat.com> 2.3.7-1
- Update from upstream
- More java fixes

* Fri Aug 10 2006 Dan Walsh <dwalsh@redhat.com> 2.3.6-4
- Change allow_execstack to default to on, for RHEL5 Beta.  
  This is required because of a Java compiler problem.
  Hope to turn off for next beta

* Thu Aug 10 2006 Dan Walsh <dwalsh@redhat.com> 2.3.6-3
- Misc fixes

* Wed Aug 9 2006 Dan Walsh <dwalsh@redhat.com> 2.3.6-2
- More fixes for strict policy

* Tue Aug 8 2006 Dan Walsh <dwalsh@redhat.com> 2.3.6-1
- Quiet down anaconda audit messages

* Mon Aug 7 2006 Dan Walsh <dwalsh@redhat.com> 2.3.5-1
- Fix setroubleshootd

* Thu Aug 3 2006 Dan Walsh <dwalsh@redhat.com> 2.3.4-1
- Update to the latest from upstream

* Thu Aug 3 2006 Dan Walsh <dwalsh@redhat.com> 2.3.3-20
- More fixes for xen

* Thu Aug 3 2006 Dan Walsh <dwalsh@redhat.com> 2.3.3-19
- Fix anaconda transitions

* Wed Aug 2 2006 Dan Walsh <dwalsh@redhat.com> 2.3.3-18
- yet more xen rules
 
* Tue Aug 1 2006 Dan Walsh <dwalsh@redhat.com> 2.3.3-17
- more xen rules

* Mon Jul 31 2006 Dan Walsh <dwalsh@redhat.com> 2.3.3-16
- Fixes for Samba

* Sat Jul 29 2006 Dan Walsh <dwalsh@redhat.com> 2.3.3-15
- Fixes for xen

* Fri Jul 28 2006 Dan Walsh <dwalsh@redhat.com> 2.3.3-14
- Allow setroubleshootd to send mail

* Wed Jul 26 2006 Dan Walsh <dwalsh@redhat.com> 2.3.3-13
- Add nagios policy

* Wed Jul 26 2006 Dan Walsh <dwalsh@redhat.com> 2.3.3-12
-  fixes for setroubleshoot

* Wed Jul 26 2006 Dan Walsh <dwalsh@redhat.com> 2.3.3-11
- Added Paul Howarth patch to only load policy packages shipped 
  with this package
- Allow pidof from initrc to ptrace higher level domains
- Allow firstboot to communicate with hal via dbus

* Mon Jul 24 2006 Dan Walsh <dwalsh@redhat.com> 2.3.3-10
- Add policy for /var/run/ldapi

* Sat Jul 22 2006 Dan Walsh <dwalsh@redhat.com> 2.3.3-9
- Fix setroubleshoot policy

* Fri Jul 21 2006 Dan Walsh <dwalsh@redhat.com> 2.3.3-8
- Fixes for mls use of ssh
- named  has a new conf file

* Fri Jul 21 2006 Dan Walsh <dwalsh@redhat.com> 2.3.3-7
- Fixes to make setroubleshoot work

* Wed Jul 19 2006 Dan Walsh <dwalsh@redhat.com> 2.3.3-6
- Cups needs to be able to read domain state off of printer client

* Wed Jul 19 2006 Dan Walsh <dwalsh@redhat.com> 2.3.3-5
- add boolean to allow zebra to write config files

* Tue Jul 18 2006 Dan Walsh <dwalsh@redhat.com> 2.3.3-4
- setroubleshootd fixes

* Mon Jul 17 2006 Dan Walsh <dwalsh@redhat.com> 2.3.3-3
- Allow prelink to read bin_t symlink
- allow xfs to read random devices
- Change gfs to support xattr


* Mon Jul 17 2006 Dan Walsh <dwalsh@redhat.com> 2.3.3-2
- Remove spamassassin_can_network boolean

* Fri Jul 14 2006 Dan Walsh <dwalsh@redhat.com> 2.3.3-1
- Update to upstream
- Fix lpr domain for mls

* Fri Jul 14 2006 Dan Walsh <dwalsh@redhat.com> 2.3.2-4
- Add setroubleshoot policy

* Fri Jul 7 2006 Dan Walsh <dwalsh@redhat.com> 2.3.2-3
- Turn off auditallow on setting booleans

* Fri Jul 7 2006 Dan Walsh <dwalsh@redhat.com> 2.3.2-2
- Multiple fixes

* Fri Jul 7 2006 Dan Walsh <dwalsh@redhat.com> 2.3.2-1
- Update to upstream

* Thu Jun 22 2006 Dan Walsh <dwalsh@redhat.com> 2.3.1-1
- Update to upstream
- Add new class for kernel key ring

* Wed Jun 21 2006 Dan Walsh <dwalsh@redhat.com> 2.2.49-1
- Update to upstream

* Tue Jun 20 2006 Dan Walsh <dwalsh@redhat.com> 2.2.48-1
- Update to upstream

* Tue Jun 20 2006 Dan Walsh <dwalsh@redhat.com> 2.2.47-5
- Break out selinux-devel package

* Fri Jun 16 2006 Dan Walsh <dwalsh@redhat.com> 2.2.47-4
- Add ibmasmfs

* Thu Jun 15 2006 Dan Walsh <dwalsh@redhat.com> 2.2.47-3
- Fix policygentool gen_requires

* Tue Jun 13 2006 Dan Walsh <dwalsh@redhat.com> 2.2.47-1
- Update from Upstream

* Tue Jun 13 2006 Dan Walsh <dwalsh@redhat.com> 2.2.46-2
- Fix spec of realplay

* Tue Jun 13 2006 Dan Walsh <dwalsh@redhat.com> 2.2.46-1
- Update to upstream

* Mon Jun 12 2006 Dan Walsh <dwalsh@redhat.com> 2.2.45-3
- Fix semanage

* Mon Jun 12 2006 Dan Walsh <dwalsh@redhat.com> 2.2.45-2
- Allow useradd to create_home_dir in MLS environment

* Thu Jun 8 2006 Dan Walsh <dwalsh@redhat.com> 2.2.45-1
- Update from upstream

* Tue Jun 6 2006 Dan Walsh <dwalsh@redhat.com> 2.2.44-1
- Update from upstream

* Tue Jun 6 2006 Dan Walsh <dwalsh@redhat.com> 2.2.43-4
- Add oprofilefs

* Sun May 28 2006 Dan Walsh <dwalsh@redhat.com> 2.2.43-3
- Fix for hplip and Picasus

* Sat May 27 2006 Dan Walsh <dwalsh@redhat.com> 2.2.43-2
- Update to upstream

* Fri May 26 2006 Dan Walsh <dwalsh@redhat.com> 2.2.43-1
- Update to upstream

* Fri May 26 2006 Dan Walsh <dwalsh@redhat.com> 2.2.42-4
- fixes for spamd

* Wed May 24 2006 Dan Walsh <dwalsh@redhat.com> 2.2.42-3
- fixes for java, openldap and webalizer

* Mon May 22 2006 Dan Walsh <dwalsh@redhat.com> 2.2.42-2
- Xen fixes

* Thu May 18 2006 Dan Walsh <dwalsh@redhat.com> 2.2.42-1
- Upgrade to upstream

* Thu May 18 2006 Dan Walsh <dwalsh@redhat.com> 2.2.41-1
- allow hal to read boot_t files
- Upgrade to upstream

* Wed May 17 2006 Dan Walsh <dwalsh@redhat.com> 2.2.40-2
- allow hal to read boot_t files

* Tue May 16 2006 Dan Walsh <dwalsh@redhat.com> 2.2.40-1
- Update from upstream

* Mon May 15 2006 Dan Walsh <dwalsh@redhat.com> 2.2.39-2
- Fixes for amavis

* Mon May 15 2006 Dan Walsh <dwalsh@redhat.com> 2.2.39-1
- Update from upstream

* Fri May 12 2006 Dan Walsh <dwalsh@redhat.com> 2.2.38-6
- Allow auditctl to search all directories

* Thu May 11 2006 Dan Walsh <dwalsh@redhat.com> 2.2.38-5
- Add acquire service for mono.

* Thu May 11 2006 Dan Walsh <dwalsh@redhat.com> 2.2.38-4
- Turn off allow_execmem boolean
- Allow ftp dac_override when allowed to access users homedirs

* Wed May 10 2006 Dan Walsh <dwalsh@redhat.com> 2.2.38-3
- Clean up spec file
- Transition from unconfined_t to prelink_t

* Mon May 8 2006 Dan Walsh <dwalsh@redhat.com> 2.2.38-2
- Allow execution of cvs command

* Fri May 5 2006 Dan Walsh <dwalsh@redhat.com> 2.2.38-1
- Update to upstream

* Wed May 3 2006 Dan Walsh <dwalsh@redhat.com> 2.2.37-1
- Update to upstream

* Mon May 1 2006 Dan Walsh <dwalsh@redhat.com> 2.2.36-2
- Fix libjvm spec

* Tue Apr 25 2006 Dan Walsh <dwalsh@redhat.com> 2.2.36-1
- Update to upstream

* Tue Apr 25 2006 James Antill <jantill@redhat.com> 2.2.35-2
- Add xm policy
- Fix policygentool

* Mon Apr 24 2006 Dan Walsh <dwalsh@redhat.com> 2.2.35-1
- Update to upstream
- Fix postun to only disable selinux on full removal of the packages

* Fri Apr 21 2006 Dan Walsh <dwalsh@redhat.com> 2.2.34-3
- Allow mono to chat with unconfined

* Thu Apr 20 2006 Dan Walsh <dwalsh@redhat.com> 2.2.34-2
- Allow procmail to sendmail
- Allow nfs to share dosfs

* Thu Apr 20 2006 Dan Walsh <dwalsh@redhat.com> 2.2.34-1
- Update to latest from upstream
- Allow selinux-policy to be removed and kernel not to crash

* Tue Apr 18 2006 Dan Walsh <dwalsh@redhat.com> 2.2.33-1
- Update to latest from upstream
- Add James Antill patch for xen
- Many fixes for pegasus

* Sat Apr 15 2006 Dan Walsh <dwalsh@redhat.com> 2.2.32-2
- Add unconfined_mount_t
- Allow privoxy to connect to httpd_cache
- fix cups labeleing on /var/cache/cups

* Fri Apr 14 2006 Dan Walsh <dwalsh@redhat.com> 2.2.32-1
- Update to latest from upstream

* Fri Apr 14 2006 Dan Walsh <dwalsh@redhat.com> 2.2.31-1
- Update to latest from upstream
- Allow mono and unconfined to talk to initrc_t dbus objects

* Tue Apr 11 2006 Dan Walsh <dwalsh@redhat.com> 2.2.30-2
- Change libraries.fc to stop shlib_t form overriding texrel_shlib_t

* Tue Apr 11 2006 Dan Walsh <dwalsh@redhat.com> 2.2.30-1
- Fix samba creating dirs in homedir
- Fix NFS so its booleans would work

* Mon Apr 10 2006 Dan Walsh <dwalsh@redhat.com> 2.2.29-6
- Allow secadm_t ability to relabel all files
- Allow ftp to search xferlog_t directories
- Allow mysql to communicate with ldap
- Allow rsync to bind to rsync_port_t

* Mon Apr 10 2006 Russell Coker <rcoker@redhat.com> 2.2.29-5
- Fixed mailman with Postfix #183928
- Allowed semanage to create file_context files.
- Allowed amanda_t to access inetd_t TCP sockets and allowed amanda_recover_t
  to bind to reserved ports.  #149030
- Don't allow devpts_t to be associated with tmp_t.
- Allow hald_t to stat all mountpoints.
- Added boolean samba_share_nfs to allow smbd_t full access to NFS mounts.
  #169947
- Make mount run in mount_t domain from unconfined_t to prevent mislabeling of
  /etc/mtab.
- Changed the file_contexts to not have a regex before the first ^/[a-z]/
  whenever possible, makes restorecon slightly faster.
- Correct the label of /etc/named.caching-nameserver.conf
- Now label /usr/src/kernels/.+/lib(/.*)? as usr_t instead of
  /usr/src(/.*)?/lib(/.*)? - I don't think we need anything else under /usr/src
  hit by this.
- Granted xen access to /boot, allowed mounting on xend_var_lib_t, and allowed
  xenstored_t rw access to the xen device node.

* Tue Apr 4 2006 Dan Walsh <dwalsh@redhat.com> 2.2.29-4
- More textrel_shlib_t file path fixes
- Add ada support

* Mon Apr 3 2006 Dan Walsh <dwalsh@redhat.com> 2.2.29-3
- Get auditctl working in MLS policy

* Mon Apr 3 2006 Dan Walsh <dwalsh@redhat.com> 2.2.29-2
- Add mono dbus support
- Lots of file_context fixes for textrel_shlib_t in FC5
- Turn off execmem auditallow since they are filling log files

* Fri Mar 30 2006 Dan Walsh <dwalsh@redhat.com> 2.2.29-1
- Update to upstream

* Thu Mar 30 2006 Dan Walsh <dwalsh@redhat.com> 2.2.28-3
- Allow automount and dbus to read cert files

* Thu Mar 30 2006 Dan Walsh <dwalsh@redhat.com> 2.2.28-2
- Fix ftp policy
- Fix secadm running of auditctl

* Mon Mar 27 2006 Dan Walsh <dwalsh@redhat.com> 2.2.28-1
- Update to upstream

* Wed Mar 22 2006 Dan Walsh <dwalsh@redhat.com> 2.2.27-1
- Update to upstream

* Wed Mar 22 2006 Dan Walsh <dwalsh@redhat.com> 2.2.25-3
- Fix policyhelp

* Wed Mar 22 2006 Dan Walsh <dwalsh@redhat.com> 2.2.25-2
- Fix pam_console handling of usb_device
- dontaudit logwatch reading /mnt dir

* Fri Mar 17 2006 Dan Walsh <dwalsh@redhat.com> 2.2.24-1
- Update to upstream

* Wed Mar 15 2006 Dan Walsh <dwalsh@redhat.com> 2.2.23-19
- Get transition rules to create policy.20 at SystemHigh

* Tue Mar 14 2006 Dan Walsh <dwalsh@redhat.com> 2.2.23-18
- Allow secadmin to shutdown system
- Allow sendmail to exec newalias

* Tue Mar 14 2006 Dan Walsh <dwalsh@redhat.com> 2.2.23-17
- MLS Fixes
     dmidecode needs mls_file_read_up
- add ypxfr_t
- run init needs access to nscd
- udev needs setuid
- another xen log file
- Dontaudit mount getattr proc_kcore_t

* Tue Mar 14 2006 Karsten Hopp <karsten@redhat.de> 2.2.23-16
- fix buildroot usage (#185391)

* Thu Mar 9 2006 Dan Walsh <dwalsh@redhat.com> 2.2.23-15
- Get rid of mount/fsdisk scan of /dev messages
- Additional fixes for suspend/resume

* Thu Mar 9 2006 Dan Walsh <dwalsh@redhat.com> 2.2.23-14
- Fake make to rebuild enableaudit.pp

* Thu Mar 9 2006 Dan Walsh <dwalsh@redhat.com> 2.2.23-13
- Get xen networking running.

* Thu Mar 9 2006 Dan Walsh <dwalsh@redhat.com> 2.2.23-12
- Fixes for Xen
- enableaudit should not be the same as base.pp
- Allow ps to work for all process

* Thu Mar  9 2006 Jeremy Katz <katzj@redhat.com> - 2.2.23-11
- more xen policy fixups

* Wed Mar  8 2006 Jeremy Katz <katzj@redhat.com> - 2.2.23-10
- more xen fixage (#184393)

* Wed Mar 8 2006 Dan Walsh <dwalsh@redhat.com> 2.2.23-9
- Fix blkid specification
- Allow postfix to execute mailman_que

* Wed Mar 8 2006 Dan Walsh <dwalsh@redhat.com> 2.2.23-8
- Blkid changes
- Allow udev access to usb_device_t
- Fix post script to create targeted policy config file

* Wed Mar 8 2006 Dan Walsh <dwalsh@redhat.com> 2.2.23-7
- Allow lvm tools to create drevice dir

* Tue Mar 7 2006 Dan Walsh <dwalsh@redhat.com> 2.2.23-5
- Add Xen support

* Mon Mar 6 2006 Dan Walsh <dwalsh@redhat.com> 2.2.23-4
- Fixes for cups
- Make cryptosetup work with hal

* Sun Mar 5 2006 Dan Walsh <dwalsh@redhat.com> 2.2.23-3
- Load Policy needs translock

* Sat Mar 4 2006 Dan Walsh <dwalsh@redhat.com> 2.2.23-2
- Fix cups html interface

* Sat Mar 4 2006 Dan Walsh <dwalsh@redhat.com> 2.2.23-1
- Add hal changes suggested by Jeremy
- add policyhelp to point at policy html pages

* Mon Feb 27 2006 Dan Walsh <dwalsh@redhat.com> 2.2.22-2
- Additional fixes for nvidia and cups

* Mon Feb 27 2006 Dan Walsh <dwalsh@redhat.com> 2.2.22-1
- Update to upstream
- Merged my latest fixes
- Fix cups policy to handle unix domain sockets

* Sat Feb 25 2006 Dan Walsh <dwalsh@redhat.com> 2.2.21-9
- NSCD socket is in nscd_var_run_t needs to be able to search dir

* Fri Feb 24 2006 Dan Walsh <dwalsh@redhat.com> 2.2.21-8
- Fixes Apache interface file

* Fri Feb 24 2006 Dan Walsh <dwalsh@redhat.com> 2.2.21-7
- Fixes for new version of cups

* Fri Feb 24 2006 Dan Walsh <dwalsh@redhat.com> 2.2.21-6
- Turn off polyinstatiate util after FC5

* Fri Feb 24 2006 Dan Walsh <dwalsh@redhat.com> 2.2.21-5
- Fix problem with privoxy talking to Tor

* Thu Feb 22 2006 Dan Walsh <dwalsh@redhat.com> 2.2.21-4
- Turn on polyinstatiation

* Thu Feb 22 2006 Dan Walsh <dwalsh@redhat.com> 2.2.21-3
- Don't transition from unconfined_t to fsadm_t

* Thu Feb 22 2006 Dan Walsh <dwalsh@redhat.com> 2.2.21-2
- Fix policy update model.

* Thu Feb 22 2006 Dan Walsh <dwalsh@redhat.com> 2.2.21-1
- Update to upstream

* Wed Feb 22 2006 Dan Walsh <dwalsh@redhat.com> 2.2.20-1
- Fix load_policy to work on MLS
- Fix cron_rw_system_pipes for postfix_postdrop_t
- Allow audotmount to run showmount

* Tue Feb 21 2006 Dan Walsh <dwalsh@redhat.com> 2.2.19-2
- Fix swapon
- allow httpd_sys_script_t to be entered via a shell
- Allow httpd_sys_script_t to read eventpolfs

* Tue Feb 21 2006 Dan Walsh <dwalsh@redhat.com> 2.2.19-1
- Update from upstream

* Tue Feb 21 2006 Dan Walsh <dwalsh@redhat.com> 2.2.18-2
- allow cron to read apache files

* Tue Feb 21 2006 Dan Walsh <dwalsh@redhat.com> 2.2.18-1
- Fix vpnc policy to work from NetworkManager

* Mon Feb 20 2006 Dan Walsh <dwalsh@redhat.com> 2.2.17-2
- Update to upstream
- Fix semoudle polcy

* Thu Feb 16 2006 Dan Walsh <dwalsh@redhat.com> 2.2.16-1
- Update to upstream 
- fix sysconfig/selinux link

* Wed Feb 15 2006 Dan Walsh <dwalsh@redhat.com> 2.2.15-4
- Add router port for zebra
- Add imaze port for spamd
- Fixes for amanda and java

* Tue Feb 14 2006 Dan Walsh <dwalsh@redhat.com> 2.2.15-3
- Fix bluetooth handling of usb devices
- Fix spamd reading of ~/
- fix nvidia spec

* Tue Feb 14 2006 Dan Walsh <dwalsh@redhat.com> 2.2.15-1
- Update to upsteam

* Mon Feb 13 2006 Dan Walsh <dwalsh@redhat.com> 2.2.14-2
- Add users_extra files

* Fri Feb 10 2006 Dan Walsh <dwalsh@redhat.com> 2.2.14-1
- Update to upstream

* Fri Feb 10 2006 Dan Walsh <dwalsh@redhat.com> 2.2.13-1
- Add semodule policy

* Tue Feb 7 2006 Dan Walsh <dwalsh@redhat.com> 2.2.12-1
- Update from upstream


* Mon Feb 6 2006 Dan Walsh <dwalsh@redhat.com> 2.2.11-2
- Fix for spamd to use razor port

* Fri Feb 3 2006 Dan Walsh <dwalsh@redhat.com> 2.2.11-1
- Fixes for mcs
- Turn on mount and fsadm for unconfined_t

* Wed Feb 1 2006 Dan Walsh <dwalsh@redhat.com> 2.2.10-1
- Fixes for the -devel package

* Wed Feb 1 2006 Dan Walsh <dwalsh@redhat.com> 2.2.9-2
- Fix for spamd to use ldap

* Fri Jan 27 2006 Dan Walsh <dwalsh@redhat.com> 2.2.9-1
- Update to upstream

* Fri Jan 27 2006 Dan Walsh <dwalsh@redhat.com> 2.2.8-2
- Update to upstream
- Fix rhgb, and other Xorg startups

* Thu Jan 26 2006 Dan Walsh <dwalsh@redhat.com> 2.2.7-1
- Update to upstream

* Thu Jan 26 2006 Dan Walsh <dwalsh@redhat.com> 2.2.6-3
- Separate out role of secadm for mls

* Thu Jan 26 2006 Dan Walsh <dwalsh@redhat.com> 2.2.6-2
- Add inotifyfs handling

* Thu Jan 26 2006 Dan Walsh <dwalsh@redhat.com> 2.2.6-1
- Update to upstream
- Put back in changes for pup/zen

* Tue Jan 24 2006 Dan Walsh <dwalsh@redhat.com> 2.2.5-1
- Many changes for MLS 
- Turn on strict policy

* Mon Jan 23 2006 Dan Walsh <dwalsh@redhat.com> 2.2.4-1
- Update to upstream

* Wed Jan 18 2006 Dan Walsh <dwalsh@redhat.com> 2.2.3-1
- Update to upstream
- Fixes for booting and logging in on MLS machine

* Wed Jan 18 2006 Dan Walsh <dwalsh@redhat.com> 2.2.2-1
- Update to upstream
- Turn off execheap execstack for unconfined users
- Add mono/wine policy to allow execheap and execstack for them
- Add execheap for Xdm policy

* Wed Jan 18 2006 Dan Walsh <dwalsh@redhat.com> 2.2.1-1
- Update to upstream
- Fixes to fetchmail,

* Tue Jan 17 2006 Dan Walsh <dwalsh@redhat.com> 2.1.13-1
- Update to upstream

* Tue Jan 17 2006 Dan Walsh <dwalsh@redhat.com> 2.1.12-3
- Fix for procmail/spamassasin
- Update to upstream
- Add rules to allow rpcd to work with unlabeled_networks.

* Sat Jan 14 2006 Dan Walsh <dwalsh@redhat.com> 2.1.11-1
- Update to upstream
- Fix ftp Man page

* Fri Jan 13 2006 Dan Walsh <dwalsh@redhat.com> 2.1.10-1
- Update to upstream

* Wed Jan 11 2006 Jeremy Katz <katzj@redhat.com> - 2.1.9-2
- fix pup transitions (#177262)
- fix xen disks (#177599)

* Tue Jan 10 2006 Dan Walsh <dwalsh@redhat.com> 2.1.9-1
- Update to upstream

* Tue Jan 10 2006 Dan Walsh <dwalsh@redhat.com> 2.1.8-3
- More Fixes for hal and readahead

* Mon Jan 9 2006 Dan Walsh <dwalsh@redhat.com> 2.1.8-2
- Fixes for hal and readahead

* Mon Jan 9 2006 Dan Walsh <dwalsh@redhat.com> 2.1.8-1
- Update to upstream
- Apply 
* Fri Jan 7 2006 Dan Walsh <dwalsh@redhat.com> 2.1.7-4
- Add wine and fix hal problems

* Thu Jan 6 2006 Dan Walsh <dwalsh@redhat.com> 2.1.7-3
- Handle new location of hal scripts

* Thu Jan 5 2006 Dan Walsh <dwalsh@redhat.com> 2.1.7-2
- Allow su to read /etc/mtab

* Wed Jan 4 2006 Dan Walsh <dwalsh@redhat.com> 2.1.7-1
- Update to upstream

* Tue Jan 3 2006 Dan Walsh <dwalsh@redhat.com> 2.1.6-24
- Fix  "libsemanage.parse_module_headers: Data did not represent a module." problem

* Tue Jan 3 2006 Dan Walsh <dwalsh@redhat.com> 2.1.6-23
- Allow load_policy to read /etc/mtab

* Mon Jan 2 2006 Dan Walsh <dwalsh@redhat.com> 2.1.6-22
- Fix dovecot to allow dovecot_auth to look at /tmp

* Mon Jan 2 2006 Dan Walsh <dwalsh@redhat.com> 2.1.6-21
- Allow restorecon to read unlabeled_t directories in order to fix labeling.

* Fri Dec 30 2005 Dan Walsh <dwalsh@redhat.com> 2.1.6-20
- Add Logwatch policy

* Wed Dec 28 2005 Dan Walsh <dwalsh@redhat.com> 2.1.6-18
- Fix /dev/ub[a-z] file context

* Tue Dec 27 2005 Dan Walsh <dwalsh@redhat.com> 2.1.6-17
- Fix library specification
- Give kudzu execmem privs

* Thu Dec 22 2005 Dan Walsh <dwalsh@redhat.com> 2.1.6-16
- Fix hostname in targeted policy

* Wed Dec 21 2005 Dan Walsh <dwalsh@redhat.com> 2.1.6-15
- Fix passwd command on mls

* Wed Dec 21 2005 Dan Walsh <dwalsh@redhat.com> 2.1.6-14
- Lots of fixes to make mls policy work

* Tue Dec 20 2005 Dan Walsh <dwalsh@redhat.com> 2.1.6-13
- Add dri libs to textrel_shlib_t
- Add system_r role for java
- Add unconfined_exec_t for vncserver
- Allow slapd to use kerberos

* Mon Dec 19 2005 Dan Walsh <dwalsh@redhat.com> 2.1.6-11
- Add man pages

* Fri Dec 16 2005 Dan Walsh <dwalsh@redhat.com> 2.1.6-10
- Add enableaudit.pp

* Fri Dec 16 2005 Dan Walsh <dwalsh@redhat.com> 2.1.6-9
- Fix mls policy

* Fri Dec 16 2005 Dan Walsh <dwalsh@redhat.com> 2.1.6-8
- Update mls file from old version

* Thu Dec 15 2005 Dan Walsh <dwalsh@redhat.com> 2.1.6-5
- Add sids back in
- Rebuild with update checkpolicy

* Thu Dec 15 2005 Dan Walsh <dwalsh@redhat.com> 2.1.6-4
- Fixes to allow automount to use portmap
- Fixes to start kernel in s0-s15:c0.c255

* Wed Dec 14 2005 Dan Walsh <dwalsh@redhat.com> 2.1.6-3
- Add java unconfined/execmem policy 

* Wed Dec 14 2005 Dan Walsh <dwalsh@redhat.com> 2.1.6-2
- Add file context for /var/cvs
- Dontaudit webalizer search of homedir

* Tue Dec 13 2005 Dan Walsh <dwalsh@redhat.com> 2.1.6-1
- Update from upstream

* Tue Dec 13 2005 Dan Walsh <dwalsh@redhat.com> 2.1.4-2
- Clean up spec
- range_transition crond to SystemHigh

* Mon Dec 12 2005 Dan Walsh <dwalsh@redhat.com> 2.1.4-1
- Fixes for hal
- Update to upstream

* Mon Dec 12 2005 Dan Walsh <dwalsh@redhat.com> 2.1.3-1
- Turn back on execmem since we need it for java, firefox, ooffice
- Allow gpm to stream socket to itself

* Mon Dec 12 2005 Jeremy Katz <katzj@redhat.com> - 2.1.2-3
- fix requirements to be on the actual packages so that policy can get
  created properly at install time

* Sun Dec  10 2005 Dan Walsh <dwalsh@redhat.com> 2.1.2-2
- Allow unconfined_t to execmod texrel_shlib_t

* Sat Dec  9 2005 Dan Walsh <dwalsh@redhat.com> 2.1.2-1
- Update to upstream 
- Turn off allow_execmem and allow_execmod booleans
- Add tcpd and automount policies

* Fri Dec  8 2005 Dan Walsh <dwalsh@redhat.com> 2.1.1-3
- Add two new httpd booleans, turned off by default
     * httpd_can_network_relay
     * httpd_can_network_connect_db

* Fri Dec  8 2005 Dan Walsh <dwalsh@redhat.com> 2.1.1-2
- Add ghost for policy.20

* Thu Dec  8 2005 Dan Walsh <dwalsh@redhat.com> 2.1.1-1
- Update to upstream
- Turn off boolean allow_execstack

* Thu Dec  8 2005 Dan Walsh <dwalsh@redhat.com> 2.1.0-3
- Change setrans-mls to use new libsetrans
- Add default_context rule for xdm

* Thu Dec  8 2005 Dan Walsh <dwalsh@redhat.com> 2.1.0-2.
- Change Requires to PreReg for requiring of policycoreutils on install

* Wed Dec  7 2005 Dan Walsh <dwalsh@redhat.com> 2.1.0-1.
- New upstream release

* Wed Dec  7 2005 Dan Walsh <dwalsh@redhat.com> 2.0.11-2.
Add xdm policy

* Tue Dec  6 2005 Dan Walsh <dwalsh@redhat.com> 2.0.11-1.
Update from upstream

* Fri Dec  2 2005 Dan Walsh <dwalsh@redhat.com> 2.0.9-1.
Update from upstream

* Fri Dec  2 2005 Dan Walsh <dwalsh@redhat.com> 2.0.8-1.
Update from upstream

* Fri Dec  2 2005 Dan Walsh <dwalsh@redhat.com> 2.0.7-3
- Also trigger to rebuild policy for versions up to 2.0.7.

* Tue Nov 29 2005 Dan Walsh <dwalsh@redhat.com> 2.0.7-2
- No longer installing policy.20 file, anaconda handles the building of the app.

* Tue Nov 29 2005 Dan Walsh <dwalsh@redhat.com> 2.0.6-2
- Fixes for dovecot and saslauthd

* Wed Nov 23 2005 Dan Walsh <dwalsh@redhat.com> 2.0.5-4
- Cleanup pegasus and named 
- Fix spec file
- Fix up passwd changing applications

* Tue Nov 21 2005 Dan Walsh <dwalsh@redhat.com> 2.0.5-1
-Update to latest from upstream

* Tue Nov 21 2005 Dan Walsh <dwalsh@redhat.com> 2.0.4-1
- Add rules for pegasus and avahi

* Mon Nov 21 2005 Dan Walsh <dwalsh@redhat.com> 2.0.2-2
- Start building MLS Policy

* Fri Nov 18 2005 Dan Walsh <dwalsh@redhat.com> 2.0.2-1
- Update to upstream

* Wed Nov 9 2005 Dan Walsh <dwalsh@redhat.com> 2.0.1-2
- Turn on bash

* Wed Nov 9 2005 Dan Walsh <dwalsh@redhat.com> 2.0.1-1
- Initial version
