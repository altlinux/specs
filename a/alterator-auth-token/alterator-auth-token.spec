Name: alterator-auth-token
Version: 0.1.0
Release: alt5

Source: %name-%version.tar
Source1: openssl-gost.control

Packager: Paul Wolneykien <manowar@altlinux.org>

Summary: Alterator module for hardware token authentication setup
License: GPL
Group: System/Configuration/Other

BuildPreReq: alterator >= 5.0

Requires: alterator >= 5.1-alt1
Requires: alterator-lookout >= 2.6-alt1
Requires: alterator-sh-functions >= 0.11-alt2
# Base
Requires: pam_pkcs11 >= 0.6.9-alt9
Requires: card-actions >= 1.8-alt3
Requires: lightdm >= 1.16.7-alt6
Requires: pam_mkuser >= 0.1.0-alt4
Requires: ca-gost-certificates
Requires: openssl-engines
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

# Install the control scripts
install -D -p -m0755 %_sourcedir/openssl-gost.control \
        %buildroot%_controldir/openssl-gost

%files
%_alterator_datadir/applications/*
%_alterator_datadir/ui/*/*.scm
%_alterator_libdir/ui/*/*.go
%_alterator_backend3dir/*
# TO BE MOVED TO openssl-engines
%_controldir/openssl-gost

%changelog
* Wed Aug 09 2017 Paul Wolneykien <manowar@altlinux.org> 0.1.0-alt5
- Fix: Require "openssl-engines" (need libgost.so).
- Fix/improve: Check for OpenSSL errors while processing GOST
  certificates.
- Fix: Display the backend error messages.
  
* Wed Aug 09 2017 Paul Wolneykien <manowar@altlinux.org> 0.1.0-alt4
- Add 'openssl-gost.control' (to be moved to openssl-engines).

* Fri Aug 04 2017 Paul Wolneykien <manowar@altlinux.org> 0.1.0-alt3
- Fill the values from URI preset.
- Fix: Don\'t require autologin-sh-functions..
- Write settings once on Apply. Use groupbox with a tumbler.
- Fix the certificate rehashing. Convert to PEM on the fly (slow).
- Require openssl-engines >= 1.0.2k-alt2 (control openssl-gost).
- Fix: Require ca-gost-certificates unversioned.
- Control GOST config and CAs.
- Add GOST tumbler.

* Fri Jul 28 2017 Paul Wolneykien <manowar@altlinux.org> 0.1.0-alt2
- Initial version.
