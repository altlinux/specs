# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

Name: moodle-domain-tools
Version: 0.2
Release: %branch_release alt1

Summary: Moodle domain configuration tools
License: %gpl2plus
Group: System/Configuration/Other

Packager: Aleksey Avdeev <solo@altlinux.ru>
BuildArch: noarch

Source10: mt-domain-create.sh

Requires: %_sbindir/mt-newdataroot
Requires: %_sbindir/mt-getdef
Requires: %_sbindir/mt-setdef
Requires: %_sbindir/mt-getCFG
Requires: %_sbindir/mt-setCFG

BuildRequires(pre): rpm-macros-branch
BuildPreReq: rpm-build-licenses
BuildPreReq: rpm-macros-moodle

%description
%summary

%install
install -pD -m0755 %SOURCE10 %buildroot%_sbindir/mt-domain-create

sed -i '
s|%%_sbindir|%_sbindir|g
s|%%webserver_group|%webserver_group|g
s|%%moodle_datadir|%moodle_datadir|g
s|%%moodle_dir|%moodle_dir|g
' %buildroot%_sbindir/mt-*

%files
%_sbindir/mt-*

%changelog
* Fri Mar 02 2012 Aleksey Avdeev <solo@altlinux.ru> 0.2-alt1
- Add option --dataroot to mt-domain-create

* Thu Mar 01 2012 Aleksey Avdeev <solo@altlinux.ru> 0.1-alt1
- Initial build for ALT Linux Sisyphus
