Name: pkcs11-profiles
Version: 0.1.0
Release: alt3

Summary: Set of profiles for PAM PKCS11 configuration
License: GPLv3+
Group: System/Configuration/Other

Source0: %name-%version.tar

%description
%summary

%package rutokenecp
Summary: RuToken ECP PAM PKCS11 module configuration
License: GPLv3+
Group: System/Configuration/Other
Requires: pam_pkcs11 >= 0.6.9-alt9
Requires: librtpkcs11ecp

%description rutokenecp
RuToken ECP PAM PKCS11 module configuration

%prep
%setup

%install

%ifarch x86_64
install -pDm644 modules.avail/rutokenecp-x86_64 %buildroot%_sysconfdir/security/pam_pkcs11/modules.avail/rutokenecp
%else
install -pDm644 modules.avail/rutokenecp %buildroot%_sysconfdir/security/pam_pkcs11/modules.avail/rutokenecp
%endif

install -pDm644 profiles/rutokenecp %buildroot%_sysconfdir/security/pam_pkcs11/profiles/rutokenecp

%files rutokenecp
%_sysconfdir/security/pam_pkcs11/modules.avail/rutokenecp
%_sysconfdir/security/pam_pkcs11/profiles/rutokenecp

%changelog
* Thu Aug 10 2017 Paul Wolneykien <manowar@altlinux.org> 0.1.0-alt3
- Remove the word "profile" from its description.

* Fri Jul 28 2017 Paul Wolneykien <manowar@altlinux.org> 0.1.0-alt2
- Fix: Exclude the mapping settings from the profiles.

* Fri Jun 09 2017 Paul Wolneykien <manowar@altlinux.org> 0.1.0-alt1
- Initial build.
