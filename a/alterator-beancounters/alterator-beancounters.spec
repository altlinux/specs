# vim: set ft=spec: -*- rpm-spec -*-

Name: alterator-beancounters
Version: 0.1
Release: alt1

Summary: OpenVZ beancounter observer module
Group: System/Configuration/Other
License: GPL

BuildArch: noarch

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
* Wed Sep 09 2009 Alexey I. Froloff <raorn@altlinux.org> 0.1-alt1
- Initial build
