Name: task-smartcard
Version: 1.0
Release: alt1

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

%description
%summary.

%files


%changelog
* Sun Jan 25 2026 Anton Midyukov <antohami@altlinux.org> 1.0-alt1
- Initial build.
