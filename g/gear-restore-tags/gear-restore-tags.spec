# vim: set ft=spec: -*- rpm-spec -*-
Name: gear-restore-tags
Version: 0.0.3
Release: alt1
Summary: Manage restored tags in the gear package repository
License: %gpl2plus
Group: Development/Other
BuildArch: noarch

Source0: %name

Requires: gear >= 1.3.0
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
* Sat Dec 17 2022 Anton Farygin <rider@altlinux.ru> 0.0.3-alt1
- removed rpm-macros-branch build dependency (not needed anymore)
- fixed year in source code copyright notice

* Wed Jan 11 2012 Aleksey Avdeev <solo@altlinux.ru> 0.0.2-alt1
- Fix tags restoring

* Thu Dec 29 2011 Aleksey Avdeev <solo@altlinux.ru> 0.0.1-alt1
- Initial build for ALT Linux Sisyphus
