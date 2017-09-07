Name: pkcs11-profiles
Version: 0.1.0
Release: alt5

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
Requires: librtpkcs11ecp >= 1.5.3.0-alt4

%description rutokenecp
RuToken ECP PAM PKCS11 module configuration

%package p11-kit-proxy
Summary: PKCS#11 Kit Proxy module configuration
License: GPLv3+
Group: System/Configuration/Other
Requires: pam_pkcs11 >= 0.6.9-alt17
Requires: libp11-kit >= 0.23.8-alt2

%description p11-kit-proxy
PKCS#11 Kit Proxy module configuration

%prep
%setup

%install
%makeinstall_std libdir=%_libdir sysconfdir=%_sysconfdir

%files rutokenecp
%_sysconfdir/security/pam_pkcs11/modules.avail/rutokenecp
%_sysconfdir/security/pam_pkcs11/profiles/rutokenecp

%files p11-kit-proxy
%_sysconfdir/security/pam_pkcs11/modules.avail/p11_kit_proxy
%_sysconfdir/security/pam_pkcs11/profiles/p11_kit_proxy

%changelog
* Wed Sep 06 2017 Paul Wolneykien <manowar@altlinux.org> 0.1.0-alt5
- Add 'p11-kit-proxy' subpackage with 'p11_kit_proxy' profile and module.
- Rely on librtpkcs11ecp >= 1.5.3.0-alt4 for pcsc-lite-ccid.
- Fixed the description of the RuTokenECP module.

* Mon Aug 14 2017 Paul Wolneykien <manowar@altlinux.org> 0.1.0-alt4
- Require pcsc-lite-ccid for RuTokenECP.

* Thu Aug 10 2017 Paul Wolneykien <manowar@altlinux.org> 0.1.0-alt3
- Remove the word "profile" from its description.

* Fri Jul 28 2017 Paul Wolneykien <manowar@altlinux.org> 0.1.0-alt2
- Fix: Exclude the mapping settings from the profiles.

* Fri Jun 09 2017 Paul Wolneykien <manowar@altlinux.org> 0.1.0-alt1
- Initial build.
