%define _altdata_dir %_datadir/alterator

Name: alterator-cyrus
Version: 0.02beta
Release: alt1

BuildArch: noarch

Source:%name-%version.tar

Summary: alterator module for system wide cyrus settings
License: GPL
Group: System/Configuration/Other
Requires: alterator >= 4.7-alt4
Requires: alterator-l10n >= 2.0-alt1
Conflicts: alterator-fbi < 5.9-alt2
Conflicts: alterator-lookout < 1.6-alt6

BuildPreReq: alterator >= 4.7-alt4

%description
alterator module for system wide cyrus settings

%prep
%setup -q

%build
%make_build libdir=%_libdir

%install
%makeinstall

%files
%_datadir/alterator/applications/*
%_datadir/alterator/ui/*/
%_alterator_backend3dir/*

%changelog
* Wed Apr 14 2010 Dmitriy L. Kruglikov <dkr@altlinux.org> 0.02beta-alt1
- Initial build.
