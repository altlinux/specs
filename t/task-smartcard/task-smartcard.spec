Name: task-smartcard
Version: 1.0
Release: alt2

Summary: Metapackage to install all software for Smartcard support
License: GPL-3.0-or-later
Group: System/Configuration/Hardware
URL: https://altlinux.org

BuildArch: noarch

Requires: opensc
Requires: pcsc-lite-ccid
Requires: pcsc-lite
Requires: pcsc-lite-acsccid
Requires: pcsc-lite-asedriveiiie-usb
Requires: pcsc-lite-rutokens
Requires: pcsc-tools
Requires: gnutls-utils
Requires: libp11
Requires: libp11-kit
Requires: pam_pkcs11
# rutoken
Requires: librtpkcs11ecp
# JaCarta
Requires: libjcpkcs11
# ESMART
Requires: isbc-pkcs11

%description
%summary.

%files

%changelog
* Tue Jan 27 2026 Anton Midyukov <antohami@altlinux.org> 1.0-alt2
- Add dependencies on librtpkcs11ecp, libjcpkcs11, isbc-pkcs11.

* Sun Jan 25 2026 Anton Midyukov <antohami@altlinux.org> 1.0-alt1
- Initial build.
