Summary: Metapackage to install all software for Rutoken support
Name:    task-rutoken
Version: 1.0
Release: alt1
License: GPL
URL:     https;//www.rutoken.ru
Group:   System/Configuration/Hardware

BuildArch: noarch

Requires: librtpkcs11ecp
Requires: rtadmin
Requires: rutoken-plugin
Requires: openssl-engines-rutoken
Requires: pcsc-lite-rutokens


%description
Metapackage to install all software for Rutoken support

%files

%changelog
* Tue Apr 04 2017 Andrey Cherepanov <cas@altlinux.org> 1.0-alt1
- Initial build in Sisyphus
