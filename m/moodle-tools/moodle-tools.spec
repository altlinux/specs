# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

Name: moodle-tools
Version: 0.10
Release: %branch_release alt1

Summary: Moodle configuration tools
License: %gpl2plus
Group: System/Configuration/Other

Packager: Aleksey Avdeev <solo@altlinux.ru>
BuildArch: noarch

Source10: mt-getCFG.php
Source11: mt-setCFG.sh
Source12: mt-newdataroot.sh
Source13: mt-getdef.php
Source14: mt-setdef.sh
Source15: mt-getconfigsuffix.sh
Source16: mt-getthislanguage.php
Source17: mt-createpasswordhash.php
Source18: mt-getuserpasswordhash.php
Source19: mt-setuserpasswordhash.php

BuildRequires(pre): rpm-macros-branch
BuildPreReq: rpm-build-licenses
BuildPreReq: rpm-macros-moodle

%description
%summary

%install
install -pD -m0755 %SOURCE10 %buildroot%_sbindir/mt-getCFG
install -pD -m0755 %SOURCE11 %buildroot%_sbindir/mt-setCFG
install -pD -m0755 %SOURCE12 %buildroot%_sbindir/mt-newdataroot
install -pD -m0755 %SOURCE13 %buildroot%_sbindir/mt-getdef
install -pD -m0755 %SOURCE14 %buildroot%_sbindir/mt-setdef
install -pD -m0755 %SOURCE15 %buildroot%_sbindir/mt-getconfigsuffix
install -pD -m0755 %SOURCE16 %buildroot%_sbindir/mt-getthislanguage
install -pD -m0755 %SOURCE17 %buildroot%_sbindir/mt-createpasswordhash
install -pD -m0755 %SOURCE18 %buildroot%_sbindir/mt-getuserpasswordhash
install -pD -m0755 %SOURCE19 %buildroot%_sbindir/mt-setuserpasswordhash

sed -i '
s|%%_sbindir|%_sbindir|g
s|%%webserver_group|%webserver_group|g
s|%%moodle_datadir|%moodle_datadir|g
s|%%moodle_dir|%moodle_dir|g
s|%%moodle_domainsdir|%moodle_domainsdir|g
' %buildroot%_sbindir/mt-*

# Create symlinks
ln -s mt-newdataroot %buildroot%_sbindir/mt-newdatadir

%files
%_sbindir/mt-*

%changelog
* Sun May 06 2012 Aleksey Avdeev <solo@altlinux.ru> 0.10-alt1
- Fix var quite in mt-setCFG
- Fix options use:
  + mt-getCFG
  + mt-getdef
  + mt-getthislanguage
  + mt-createpasswordhash
  + mt-getuserpasswordhash
  + mt-setuserpasswordhash

* Wed Apr 25 2012 Aleksey Avdeev <solo@altlinux.ru> 0.9-alt1
- Add new script:
  + mt-createpasswordhash
  + mt-getuserpasswordhash
  + mt-setuserpasswordhash

* Sat Mar 17 2012 Aleksey Avdeev <solo@altlinux.ru> 0.8-alt1
- Add mt-getthislanguage

* Tue Mar 13 2012 Aleksey Avdeev <solo@altlinux.ru> 0.7-alt1
- Add new options for mt-getconfigsuffix:
  + --delimiter
  + --full-path

* Wed Mar 07 2012 Aleksey Avdeev <solo@altlinux.ru> 0.6-alt1
- Fix shell scripts
- Add new script mt-getconfigsuffix
- Add new options for mt-get{CFG,def}:
  + --array
  + --bool
- Add new options for mt-newdataroot:
  + --config
  + --distrolib
  + --no-config-update
  + --no-distrolib-update

* Fri Mar 02 2012 Aleksey Avdeev <solo@altlinux.ru> 0.5-alt1
- Rename mt-newdatadir to mt-newdataroot
- Fix mt-getCFG and mt-getdef

* Wed Feb 29 2012 Aleksey Avdeev <solo@altlinux.ru> 0.4-alt1
- Fix mt-newdatadir

* Fri Feb 24 2012 Aleksey Avdeev <solo@altlinux.ru> 0.3-alt1
- Fix mt-newdatadir

* Tue Feb 21 2012 Aleksey Avdeev <solo@altlinux.ru> 0.2-alt1
- Fix mt-setCFG
- Add new script:
  + mt-getdef
  + mt-setdef

* Fri Feb 17 2012 Aleksey Avdeev <solo@altlinux.ru> 0.1-alt1
- Initial build for ALT Linux Sisyphus
