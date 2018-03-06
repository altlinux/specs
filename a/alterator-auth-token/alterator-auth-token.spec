Name: alterator-auth-token
Version: 0.1.2
Release: alt1

Source: %name-%version.tar

Packager: Paul Wolneykien <manowar@altlinux.org>

Summary: Alterator module for hardware token authentication setup
License: GPL
Group: System/Configuration/Other

BuildPreReq: alterator >= 5.0

Requires: alterator >= 5.1-alt1
Requires: alterator-lookout >= 2.6-alt1
Requires: alterator-sh-functions >= 0.11-alt2
Requires: alterator-service-functions >= 3.0.0-alt2
# PKCS#11
Requires: pam_pkcs11 >= 0.6.9-alt15
Requires: card-actions >= 1.8-alt3
Requires: pam_mkuser >= 0.1.0-alt4
# GOST CAs are now optional
#Requires: ca-gost-certificates
Requires: openssl-engines

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
* Tue Mar 06 2018 Paul Wolneykien <manowar@altlinux.org> 0.1.2-alt1
- SDDM-ready version (closes: #34334).

* Fri Sep 01 2017 Paul Wolneykien <manowar@altlinux.org> 0.1.1-alt1
- Control GOST authentication support leaving system-wide OpenSSL
  configuration untouched.

* Tue Aug 15 2017 Paul Wolneykien <manowar@altlinux.org> 0.1.0-alt8
- Fixed service start/stop control: make additional check for the
  chroot environment (requires alterator-service-functions >=
  3.0.0-alt2).

* Mon Aug 14 2017 Paul Wolneykien <manowar@altlinux.org> 0.1.0-alt7
- Fix: Keep owner and mode of /etc/openssl/openssl.cnf unmodified.
- Do not ecplicitly require the RuTokenECP profile.
- Require alterator-service-functions >= 3.0.0.

* Thu Aug 10 2017 Paul Wolneykien <manowar@altlinux.org> 0.1.0-alt6
- Check that the pkcs11-evenmgr service is running when not in
  installer mode.
- Fix: Support the installer (chroot) mode when installing GOST CAs.
- Expect pre-c_rehash\'ed GOST CAs.

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
