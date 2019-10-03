Summary: Metapackage to install all software for Rutoken support
Name:    task-rutoken
Version: 1.0
Release: alt3
License: GPL
URL:     https;//www.rutoken.ru
Group:   System/Configuration/Hardware

ExclusiveArch: %ix86 x86_64

Requires: librtpkcs11ecp
Requires: rtadmin
Requires: rutoken-plugin
Requires: openssl-engines-rutoken
Requires: pcsc-lite-ccid


%description
Metapackage to install all software for Rutoken support

%files

%changelog
* Thu Oct 03 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.0-alt3
- Added ExclusiveArch tag to limit architectures to %%ix86 and x86_64.

* Mon Aug 14 2017 Paul Wolneykien <manowar@altlinux.org> 1.0-alt2
- Fix: Require pcsc-lite-ccid for RuToken.

* Tue Apr 04 2017 Andrey Cherepanov <cas@altlinux.org> 1.0-alt1
- Initial build in Sisyphus
