# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

Name: moodle-install-tools
Version: 0.10
Release: %branch_release alt1

Summary: Moodle install tools
License: %gpl2plus
Group: System/Configuration/Other

Packager: Aleksey Avdeev <solo@altlinux.ru>
BuildArch: noarch

Source1: mt-install.conf
Source10: mt-install-wwwrootnew.sh
Source11: mt-install-lsdbtypes.sh
Source12: mt-install-defaultdbtype.sh
Source13: mt-install-getdbtype.sh
Source14: mt-install-rundbscript.sh
Source15: mt-install-scriptnametodbtype.sh
Source16: mt-install-lslangs.sh
Source17: mt-install.sh
Source18: mt-install-configfiletosymlink.sh
Source19: mt-install-lsdefaults.sh
Source20: mt-install-lsconfigs.sh
Source21: mt-install-setconfig.sh
Source22: mt-install-getactiveconfig.sh
Source23: mt-install-wwwroot-getproto.sh
Source24: mt-install-wwwroot-getsitename.sh
Source25: mt-install-wwwroot-getport.sh
Source26: mt-install-wwwroot-getpath.sh
Source27: mt-install-wwwroot.sh
Source28: mt-install-setpassword.sh
Source29: mt-install-auto.sh

Requires: moodle-BD-tools >= 0.4
Requires: moodle-tools >= 0.7
Requires: %_sbindir/mt-getthislanguage
Requires: %_sbindir/mt-getuserpasswordhash
Requires: %_sbindir/mt-setuserpasswordhash
Requires: %_sbindir/mt-plugins-setauth
Requires: %_sbindir/mt-plugins-setparams
Conflicts: alterator-moodle-install < 1.8
Obsoletes: moodle-domain-tools < 0.3

BuildRequires(pre): rpm-macros-branch
BuildPreReq: rpm-build-licenses
BuildPreReq: rpm-macros-moodle
BuildPreReq: rpm-macros-alternatives

%description
%summary

%install
install -pD -m0755 %SOURCE1 %buildroot%_sysconfdir/sysconfig/mt-install
install -pD -m0755 %SOURCE10 %buildroot%_sbindir/mt-install-wwwrootnew
install -pD -m0755 %SOURCE11 %buildroot%_sbindir/mt-install-lsdbtypes
install -pD -m0755 %SOURCE12 %buildroot%_sbindir/mt-install-defaultdbtype
install -pD -m0755 %SOURCE13 %buildroot%_sbindir/mt-install-getdbtype
install -pD -m0755 %SOURCE14 %buildroot%_sbindir/mt-install-rundbscript
install -pD -m0755 %SOURCE15 %buildroot%_sbindir/mt-install-scriptnametodbtype
install -pD -m0755 %SOURCE16 %buildroot%_sbindir/mt-install-lslangs
install -pD -m0755 %SOURCE17 %buildroot%_sbindir/mt-install
install -pD -m0755 %SOURCE18 %buildroot%_sbindir/mt-install-configfiletosymlink
install -pD -m0755 %SOURCE19 %buildroot%_sbindir/mt-install-lsdefaults
install -pD -m0755 %SOURCE20 %buildroot%_sbindir/mt-install-lsconfigs
install -pD -m0755 %SOURCE21 %buildroot%_sbindir/mt-install-setconfig
install -pD -m0755 %SOURCE22 %buildroot%_sbindir/mt-install-getactiveconfig
install -pD -m0755 %SOURCE23 %buildroot%_sbindir/mt-install-wwwroot-getproto
install -pD -m0755 %SOURCE24 %buildroot%_sbindir/mt-install-wwwroot-getsitename
install -pD -m0755 %SOURCE25 %buildroot%_sbindir/mt-install-wwwroot-getport
install -pD -m0755 %SOURCE26 %buildroot%_sbindir/mt-install-wwwroot-getpath
install -pD -m0755 %SOURCE27 %buildroot%_sbindir/mt-install-wwwroot
install -pD -m0755 %SOURCE28 %buildroot%_sbindir/mt-install-setpassword
install -pD -m0755 %SOURCE29 %buildroot%_sbindir/mt-install-auto

sed -i '
s|%%_altdir|%_altdir|g
s|%%_sysconfdir|%_sysconfdir|g
s|%%_sbindir|%_sbindir|g
s|%%webserver_group|%webserver_group|g
s|%%moodle_datadir|%moodle_datadir|g
s|%%moodle_domainsdir|%moodle_domainsdir|g
s|%%moodle_dir|%moodle_dir|g
' %buildroot%_sbindir/mt-* %buildroot%_sysconfdir/sysconfig/*

%files
%config(noreplace) %_sysconfdir/sysconfig/*
%_sbindir/mt-*

%changelog
* Thu May 10 2012 Aleksey Avdeev <solo@altlinux.ru> 0.10-alt1
- Add new options for mt-install-auto:
  + --authinstalladd
  + --authinstallinsert
  + --authinstallset
  + --authinstallrm

* Sun May 06 2012 Aleksey Avdeev <solo@altlinux.ru> 0.9-alt1
- Update --dbsocket option for:
  + mt-install
  + mt-install-auto
- Update in mt-install-lsdefaults dbsocket out
- Add new options for mt-install and mt-install-auto:
  + --authadd
  + --authinsert
  + --authset
  + --authrm
  + --ldaphosturl
  + --ldapcontexts
- Add new options for mt-install-auto:
  + --plugins-setparams

* Sat Apr 28 2012 Aleksey Avdeev <solo@altlinux.ru> 0.8-alt1
- Fix getting adminuser and lang in mt-install-lsdefaults
- Fix create symlink for configfile in mt-install
- Fix option for mt-install:
  + --wwwrootpath
  + --datarootauto
- Add in mt-install-lsdefaults out:
  + adminpasshash
  + passwordsaltmain
- Add new options for mt-install:
  + --adminpasshash
  + --passwordsaltmain
  + --msg
- Add new scripts:
  + mt-install-setpassword
  + mt-install-auto

* Fri Apr 20 2012 Aleksey Avdeev <solo@altlinux.ru> 0.7-alt1
- Fix options for mt-install
- Add %%_sysconfdir/sysconfig/mt-install
- Add new options for mt-install:
  + --basedbname
  + --dbmoodleuser
  + --dbrootforce
  + --datarootauto
  + --wwwrootproto
  + --wwwrootsitename
  + --wwwrootport
  + --wwwrootpath
- Add new scripts:
  + mt-install-wwwroot
  + mt-install-wwwroot-getproto
  + mt-install-wwwroot-getsitename
  + mt-install-wwwroot-getport
  + mt-install-wwwroot-getpath
- Add in mt-install-lsdefaults out:
  + adminuser
  + basedbname
  + fullname
  + shortname
  + wwwrootproto
  + wwwrootsitename
  + wwwrootport
  + wwwrootpath

* Sat Mar 17 2012 Aleksey Avdeev <solo@altlinux.ru> 0.6-alt1
- Update mt-install-lslangs:
  + determination of available locales on
    a %%moodle_dir/lang/<lang>/langconfig.php files
  + out strings: <lang>\t<langname>
  + add option --moodledir

* Thu Mar 15 2012 Aleksey Avdeev <solo@altlinux.ru> 0.5-alt1
- Add mt-install-getactiveconfig

* Tue Mar 13 2012 Aleksey Avdeev <solo@altlinux.ru> 0.4-alt1
- Add new scripts:
  + mt-install-lsconfigs
  + mt-install-setconfig

* Wed Mar 07 2012 Aleksey Avdeev <solo@altlinux.ru> 0.3-alt1
- Rename package to moodle-install-tools
- Fix shell scripts
- Rename mt-domain-create to mt-install-wwwrootnew
- Add new scripts:
  + mt-install
  + mt-install-configfiletosymlink
  + mt-install-defaultdbtype
  + mt-install-lsdbtypes
  + mt-install-lsdefaults
  + mt-install-lslangs
  + mt-install-getdbtype
  + mt-install-rundbscript
  + mt-install-scriptnametodbtype

* Fri Mar 02 2012 Aleksey Avdeev <solo@altlinux.ru> 0.2-alt1
- Add option --dataroot to mt-domain-create

* Thu Mar 01 2012 Aleksey Avdeev <solo@altlinux.ru> 0.1-alt1
- Initial build for ALT Linux Sisyphus
