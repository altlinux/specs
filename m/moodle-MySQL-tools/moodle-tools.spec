# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

Name: moodle-MySQL-tools
Version: 0.5
Release: %branch_release alt1

Summary: Moodle MySQL configuration tools
License: %gpl2plus
Group: System/Configuration/Other

Packager: Aleksey Avdeev <solo@altlinux.ru>
BuildArch: noarch

Source10: moodle-tools.alternatives

Source20: mt-MySQL-checkdb.sh
Source21: mt-MySQL-createdb.sh
Source22: mt-MySQL-setdb.sh
Source23: mt-MySQL-setdbuser.sh
Source24: mt-MySQL-newdbname.sh

Requires: MySQL-server-control
Provides: moodle-BD-tools = %version-%release

BuildRequires(pre): rpm-macros-branch
BuildPreReq: rpm-build-licenses
BuildPreReq: rpm-macros-moodle
BuildPreReq: rpm-macros-alternatives

%description
%summary

%install
install -pD -m0644 %SOURCE10 %buildroot%_altdir/%name

install -pD -m0755 %SOURCE20 %buildroot%_sbindir/mt-MySQL-checkdb
install -pD -m0755 %SOURCE21 %buildroot%_sbindir/mt-MySQL-createdb
install -pD -m0755 %SOURCE22 %buildroot%_sbindir/mt-MySQL-setdb
install -pD -m0755 %SOURCE23 %buildroot%_sbindir/mt-MySQL-setdbuser
install -pD -m0755 %SOURCE24 %buildroot%_sbindir/mt-MySQL-newdbname

sed -i '
s|%%_sbindir|%_sbindir|g
' %buildroot%_altdir/%name %buildroot%_sbindir/mt-*

%files
%_sbindir/mt-*
%_altdir/%name

%changelog
* Sat Apr 28 2012 Aleksey Avdeev <solo@altlinux.ru> 0.5-alt1
- Fix handling of empty password in mt-MySQL-setdb

* Fri Apr 20 2012 Aleksey Avdeev <solo@altlinux.ru> 0.4-alt1
- Fix options for:
  + mt-MySQL-checkdb
  + mt-MySQL-createdb
  + mt-MySQL-setdb
  + mt-MySQL-setdbuser
- Add new script mt-MySQL-newdbname
- Add new options for mt-MySQL-setdb:
  + --basedbname
  + --dbmoodleuser
  + --dbrootforce

* Tue Mar 06 2012 Aleksey Avdeev <solo@altlinux.ru> 0.3-alt1
- Fix shell scripts

* Wed Feb 29 2012 Aleksey Avdeev <solo@altlinux.ru> 0.2-alt1
- Fix mt-MySQL-setdb

* Thu Feb 23 2012 Aleksey Avdeev <solo@altlinux.ru> 0.1-alt1
- Initial build for ALT Linux Sisyphus
