Name: pam_p11
Version: 0.1.5
Release: alt4

Summary: Simple RSA authentication with PKCS#11 modules
License: LGPLv2.1+
Group: System/Base

Url: https://github.com/OpenSC/pam_p11
Source: %name-%version.tar.bz2
Packager: Michael Shigorin <mike@altlinux.org>

BuildRequires: libp11-devel libssl-devel libpam-devel zlib-devel

%description
pam_p11 is a pluggable authentication module (PAM) package for
using cryptographic PKCS#11 tokens such as smart cards and USB
crypto tokens for local authentication.

pam_p11 uses libp11 to access any PKCS#11 module but it is
primarily developed for and tested with OpenSC PKCS#11.

pam_p11 implements two authentication modules:
* pam_p11_openssh authenticates the user against public keys
  found in OpenSSH ~/.ssh/authorized_keys file.
* pam_p11_opensc authenticates the user against certificates
  found in ~/.eid/authorized_certificates_. It is compatible with
  the older opensc "pamopensc" authentication module (eid mode).

pam_p11 is very simple, it has no config file, no options other
than the PKCS#11 module file, does not know about certificate
chains, certificate authorities, revocation lists or OCSP.
Perfect for the small installation with no frills.

pam_p11 was written by an international team and is licensed as
Open Source software under the LGPL license.

%prep
%setup

%build
# NB: fails during install as of 0.1.5
#autoreconf
%configure --libdir=/%_lib
%make_build

%install
%makeinstall_std

%files
%doc NEWS doc/README doc/ChangeLog doc/*.html doc/*.css
/%_lib/security/*.so

%changelog
* Mon Sep 21 2015 Michael Shigorin <mike@altlinux.org> 0.1.5-alt4
- built for ALT Linux again (bits based on openSUSE spec)

* Mon May 25 2009 Lebedev Sergey <barabashka@altlinux.org> 0.1.5-alt3
- fixed build with new automake-1.11

* Wed Dec 03 2008 Lebedev Sergey <barabashka@altlinux.org> 0.1.5-alt2
- fixed configure libdir options

* Tue Dec 02 2008 Lebedev Sergey <barabashka@altlinux.org> 0.1.5-alt1
- initial build
