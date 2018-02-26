# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

%define macrosname condstopstart

Name: rpm-macros-%macrosname
Version: 0.1
Release: %branch_release alt1

Summary: Rpm macros for condstopstart
License: %gpl2plus
Group: Development/Other

Packager: Aleksey Avdeev <solo@altlinux.ru>
BuildArch: noarch

Source1: %macrosname.rpm-macros

BuildRequires(pre): rpm-macros-branch
BuildPreReq: rpm-build-licenses

%description
%summary

%install
install -pD -m644 %SOURCE1 %buildroot%_rpmmacrosdir/%macrosname

%files
%_rpmmacrosdir/%macrosname

%changelog
* Wed Feb 08 2012 Aleksey Avdeev <solo@altlinux.ru> 0.1-alt1
- Initial build for ALT Linux Sisyphus
