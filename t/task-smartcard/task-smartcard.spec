Name: task-smartcard
Version: 1.0
Release: alt4

Summary: Metapackage to install all software for Smartcard support
License: GPL-3.0-or-later
Group: System/Configuration/Hardware
URL: https://altlinux.org

Requires: opensc
Requires: pcsc-lite-ccid
Requires: pcsc-lite
Requires: pcsc-lite-acsccid
Requires: pcsc-lite-rutokens
Requires: pcsc-tools
Requires: gnutls-utils
Requires: libp11
Requires: libp11-kit
Requires: pam_pkcs11

%ifnarch %ix86 riscv64 loongarch64
# rutoken
Requires: librtpkcs11ecp
# JaCarta
Requires: libjcpkcs11
# ESMART
Requires: isbc-pkcs11
%endif

%description
%summary.

%files

%changelog
* Tue Mar 10 2026 Anton Midyukov <antohami@altlinux.org> 1.0-alt4
- Remove dependency on pcsc-lite-asedriveiiie-usb.

* Fri Mar 06 2026 Anton Midyukov <antohami@altlinux.org> 1.0-alt3
- Fix dependencies for riscv64, loongarch64.

* Tue Jan 27 2026 Anton Midyukov <antohami@altlinux.org> 1.0-alt2
- Add dependencies on librtpkcs11ecp, libjcpkcs11, isbc-pkcs11.

* Sun Jan 25 2026 Anton Midyukov <antohami@altlinux.org> 1.0-alt1
- Initial build.
