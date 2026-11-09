Name: task-rutoken
Version: 1.2
Release: alt1

Summary: Metapackage to install all software for Rutoken support
License: GPL
Group: System/Configuration/Hardware

Url: http;//www.rutoken.ru
BuildArch: noarch

Requires: librtpkcs11ecp
%ifarch %ix86 x86_64 aarch64 armh
Requires: openssl-engines-rutoken
%endif
Requires: pcsc-lite-ccid

%description
Metapackage to install all software for Rutoken support

%files
%changelog
* Mon Nov 09 2026 Andrey Cherepanov <cas@altlinux.org> 1.2-alt1
- Removed rtadmin.

* Mon Jan 17 2022 Andrey Cherepanov <cas@altlinux.org> 1.1-alt1
- Fix supported architectures for rtadmin-2.3.

* Thu Jan 21 2021 Andrey Cherepanov <cas@altlinux.org> 1.0-alt5
- Do not require missing rutoken-plugin.

* Wed Oct 16 2019 Michael Shigorin <mike@altlinux.org> 1.0-alt4
- Sync ExclusiveArch: list with librtpkcs11ecp 1.9.12.0-alt1
- Restrict x86-only dependencies yet

* Thu Oct 03 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.0-alt3
- Added ExclusiveArch tag to limit architectures to %%ix86 and x86_64.

* Mon Aug 14 2017 Paul Wolneykien <manowar@altlinux.org> 1.0-alt2
- Fix: Require pcsc-lite-ccid for RuToken.

* Tue Apr 04 2017 Andrey Cherepanov <cas@altlinux.org> 1.0-alt1
- Initial build in Sisyphus
