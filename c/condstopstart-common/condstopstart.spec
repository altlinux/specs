# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

Name: condstopstart-common
Version: 0.1
Release: %branch_release alt1

Summary: Common dirs for condstopstart-*
License: %gpl2plus
Group: System/Configuration/Other

Packager: Aleksey Avdeev <solo@altlinux.ru>
BuildArch: noarch

Provides: %condstopstart_subsysdir
Provides: %condstopstart_subsysrundir

BuildRequires(pre): rpm-macros-branch
BuildRequires(pre): rpm-macros-condstopstart
BuildPreReq: rpm-build-licenses

%description
%summary

%install
install -d %buildroot%condstopstart_subsysdir/
install -d %buildroot%condstopstart_subsysrundir/

%files
%attr(755,root,root) %dir %condstopstart_subsysdir/
%attr(755,root,root) %dir %condstopstart_subsysrundir/

%changelog
* Fri Feb 10 2012 Aleksey Avdeev <solo@altlinux.ru> 0.1-alt1
- Initial build for ALT Linux Sisyphus
