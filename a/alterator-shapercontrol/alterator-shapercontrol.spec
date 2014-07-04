%define _altdata_dir %_datadir/alterator

Name: alterator-shapercontrol
Version: 0.2
Release: alt1
License: %gpl2plus
Group: System/Configuration/Other
Summary: Alterator module for shapercontrol administration
Source: %name-%version.tar

Requires: alterator alterator-sh-functions
Requires: alterator-l10n

BuildPreReq: alterator
BuildPreReq: rpm-build-licenses

BuildArch: noarch

%description
Alterator module for shapercontrol administration.

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
%_libexecdir/%name/

%changelog
* Fri Jul 04 2014 Timur Aitov <timonbl4@altlinux.org> 0.2-alt1
- Fix get interfaces list

* Thu Jul 03 2014 Timur Aitov <timonbl4@altlinux.org> 0.1-alt1
- First build

