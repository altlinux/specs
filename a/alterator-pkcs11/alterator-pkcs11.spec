# vim: set ft=spec: -*- rpm-spec -*-

Name: alterator-pkcs11
Version: 0.1
Release: alt2

Summary: PKCS#11 user certificate manager
Group: System/Configuration/Other
License: GPL

BuildArch: noarch

Source: %name-%version.tar

Requires: alterator >= 4.6-alt3
Requires: alterator-l10n >= 2.7-alt11
Conflicts: alterator-fbi < 5.7-alt4

BuildPreReq: alterator >= 4.6-alt3

%description
PKCS#11 user certificate management module.

%prep
%setup

%build
%make_build

%install
%makeinstall

%files
%_datadir/alterator/applications/*
%_datadir/alterator/ui/*
%_alterator_backend3dir/*

%changelog
* Tue Sep 29 2009 Alexey I. Froloff <raorn@altlinux.org> 0.1-alt2
- Fixed description (closes: #21771)
- Added translations via alterator-l10n

* Sun Sep 27 2009 Alexey I. Froloff <raorn@altlinux.org> 0.1-alt1
- Initial build
