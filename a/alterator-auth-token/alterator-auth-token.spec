Name: alterator-auth-token
Version: 0.1.0
Release: alt2

Source: %name-%version.tar

Packager: Paul Wolneykien <manowar@altlinux.org>

Summary: Alterator module for hardware token authentication setup
License: GPL
Group: System/Configuration/Other

BuildPreReq: alterator >= 5.0

Requires: alterator >= 5.0-alt5
Requires: autologin-sh-functions >= 0.2.1
# Base
Requires: pam_pkcs11 >= 0.6.9-alt9
Requires: card-actions >= 1.8-alt3
Requires: lightdm >= 1.16.7-alt6
Requires: pam_mkuser >= 0.1.0-alt4
# Profiles
Requires: pkcs11-profiles-rutokenecp >= 0.1.0-alt2

Conflicts: alterator-fbi < 5.16-alt1
Conflicts: alterator-lookout < 2.1-alt1

BuildRequires: guile22-devel rpm-build >= 4.0.4-alt103
BuildRequires: alterator >= 5.0
BuildRequires: alterator-fbi >= 5.33-alt1

%description
%summary

%prep
%setup

%build
%make_build

%install
%makeinstall

%files
%_alterator_datadir/applications/*
%_alterator_datadir/ui/*/*.scm
%_alterator_libdir/ui/*/*.go
%_alterator_backend3dir/*

%changelog
* Fri Jul 28 2017 Paul Wolneykien <manowar@altlinux.org> 0.1.0-alt2
- Initial version.
