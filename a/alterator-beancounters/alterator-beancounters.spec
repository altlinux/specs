# vim: set ft=spec: -*- rpm-spec -*-

Name: alterator-beancounters
Version: 0.1
Release: alt2

Summary: OpenVZ beancounter observer module
Group: System/Configuration/Other
License: GPL

ExclusiveArch: x86_64

Source: %name-%version.tar

Requires: alterator >= 4.6-alt3
Requires: bc
Conflicts: alterator-fbi < 5.7-alt4

BuildPreReq: alterator >= 4.6-alt3

%description
OpenVZ beancounter observer module

%prep
%setup

%build
%make_build

%install
%makeinstall

%files
%_datadir/alterator/applications/*
%_datadir/alterator/ui/*/
%_alterator_backend3dir/*

%changelog
* Mon Nov 05 2018 Alexey Shabalin <shaba@altlinux.org> 0.1-alt2
- build for x86_64 only

* Wed Sep 09 2009 Alexey I. Froloff <raorn@altlinux.org> 0.1-alt1
- Initial build
