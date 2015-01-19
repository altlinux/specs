%define _altdata_dir %_datadir/alterator

Name: alterator-ddos
Version: 0.2.0
Release: alt1
License: %gpl2plus
Group: System/Configuration/Other
Summary: Alterator module for ddos-deflate administration
Source: %name-%version.tar

Requires: alterator alterator-sh-functions
Requires: alterator-l10n
Requires: ddos-deflate

BuildPreReq: alterator
BuildPreReq: rpm-build-licenses

BuildArch: noarch

%description
Alterator module for ddos-deflate administration.

%prep
%setup -q

%build
%make_build

%install
%makeinstall

%files
%_altdata_dir/applications/*
%_altdata_dir/ui/*/
%_alterator_backend3dir/*

%changelog
* Mon Jan 19 2015 Mikhail Efremov <sem@altlinux.org> 0.2.0-alt1
- Add IP whitelist.

* Wed Sep 17 2014 Mikhail Efremov <sem@altlinux.org> 0.1.1-alt1
- Add Russian name for module.

* Mon Jul 07 2014 Timur Aitov <timonbl4@altlinux.org> 0.1-alt1
- First build

