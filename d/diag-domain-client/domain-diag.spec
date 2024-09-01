%define _unpackaged_files_terminate_build 1
%define diagnostic_tool domain-client
Name: diag-%diagnostic_tool
Version: 0.2.8
Release: alt1

Summary: Active Directory domain environment diagnostic tool
License: GPLv3
Group: System/Configuration/Other
BuildArch: noarch

Url: https://gitlab.basealt.space/alt/diag-domain-client

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-alterator
BuildRequires: shellcheck

Obsoletes: domain-diag < %EVR

%description
Active Directory domain environment diagnostic tool.

%prep
%setup

%build
sed -i 's/^VERSION=.*/VERSION=%version/' %name
sed -i 's/@VERSION@/%version/g' %name.man

%install
install -p -D -m755 %name %buildroot%_bindir/%name
install -p -D %name.man %buildroot%_mandir/man1/%name.1
install -p -D alterator/%name.backend %buildroot%_alterator_datadir/backends/%name.backend
install -p -D alterator/%diagnostic_tool.diag %buildroot%_alterator_datadir/diagnostictools/%diagnostic_tool.diag
install -p -D %name.svg %buildroot%_iconsdir/hicolor/scalable/apps/%name.svg

%check
shellcheck -e SC1090,SC1091,SC2004,SC2015,SC2034,SC2086,SC2154,SC2001,SC2120,SC2119,SC2317 %name

%files
%_bindir/%name
%_man1dir/%name.*
%_alterator_datadir/backends/%name.backend
%_alterator_datadir/diagnostictools/%diagnostic_tool.diag
%_iconsdir/hicolor/scalable/apps/%name.svg

%changelog
* Mon Sep 02 2024 Evgeny Sinelnikov <sin@altlinux.org> 0.2.8-alt1
- Initial build for Sisyphus

* Tue Jan 30 2024 Andrey Limachko <liannnix@altlinux.org> 0.2.7-alt1
- Fix to work with new alterator version (thx Michael Chernigin)
- Fix description to diagnostic tests in ADT domain-diag (thx Anton Abramov)

* Tue Oct 17 2023 Andrey Limachko <liannnix@altlinux.org> 0.2.6-alt1
- chore: change methods names to alterator-manager interface
  0.1.8-alt1 (thx Aleksey Saprunov)
- chore: add actions_ids (thx Aleksey Saprunov)
- change run method signature (thx Aleksey Saprunov)

* Tue Jun 27 2023 Andrey Limachko <liannnix@altlinux.org> 0.2.5-alt1
- Add ADT backend bindings

* Tue Jun 27 2023 Andrey Limachko <liannnix@altlinux.org> 0.2.4-alt1
- Add license information
- Add man page

* Wed Apr 19 2023 Andrey Limachko <liannnix@altlinux.org> 0.2.3-alt1
- Fixed script return codes
- Fixed nothing to grep bug
- Added resolv.conf search multidomain support
- Fixed script failure when default_realm commented in krb5.conf

* Tue Jan 10 2023 Andrey Limachko <liannnix@altlinux.org> 0.2.2-alt1
- Added kinit from system keytab when run as root
- Fixed ldapsearch timeout limit

* Wed Dec 21 2022 Andrey Limachko <liannnix@altlinux.org> 0.2.1-alt1
- Initial build

