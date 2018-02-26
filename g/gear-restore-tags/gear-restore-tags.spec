# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

Name: gear-restore-tags
Version: 0.0.2
Release: %branch_release alt1

Summary: Manage restored tags in the package repository
License: %gpl2plus
Group: Development/Other

Packager: Aleksey Avdeev <solo@altlinux.ru>
BuildArch: noarch

Source0: %name

Requires: gear >= 1.3.0

BuildRequires(pre): rpm-macros-branch
BuildPreReq: rpm-build-licenses

%description
%summary

%install
install -pD -m755 %SOURCE0 %buildroot%_bindir/%name

# Set @VERSION@
sed -i 's/@VERSION@/%version/g' %buildroot%_bindir/%name

%files
%_bindir/*

%changelog
* Wed Jan 11 2012 Aleksey Avdeev <solo@altlinux.ru> 0.0.2-alt1
- Fix tags restoring

* Thu Dec 29 2011 Aleksey Avdeev <solo@altlinux.ru> 0.0.1-alt1
- Initial build for ALT Linux Sisyphus
