%define _unpackaged_files_terminate_build 1
%define diagnostic_tool domain-client

Name: diag-%diagnostic_tool
Version: 0.5.1
Release: alt1

Summary: Active Directory domain environment diagnostic tool
License: GPLv3
Group: System/Configuration/Other
BuildArch: noarch

Url: https://altlinux.space/alterator/diag-domain-client
Source: %name-%version.tar

Requires: alterator-module-executor >= 0.1.29
Requires: alterator-interface-diag

BuildRequires(pre): rpm-macros-alterator
%ifnarch %e2k
BuildRequires: shellcheck
%endif
BuildRequires: alterator-entry

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
%ifnarch %e2k
shellcheck -e SC2329 %name
%endif
find ./alterator/ -type f -exec alterator-entry validate {} \+

%files
%_bindir/%name
%_man1dir/%name.*
%_alterator_datadir/backends/%name.backend
%_alterator_datadir/diagnostictools/%diagnostic_tool.diag
%_iconsdir/hicolor/scalable/apps/%name.svg

%changelog
* Fri Nov 28 2025 Kirill Sharov <sheriffkorov@altlinux.org> 0.5.1-alt1
- NMU: add 'exit_status = true' for new version of executor

* Fri Sep 12 2025 Evgeny Sinelnikov <sin@altlinux.org> 0.5-alt2
- spec: exclude warnings SC2329 as error

* Thu Jul 24 2025 Andrey Limachko <liannnix@altlinux.org> 0.5-alt1
- fix: shell script sourcing with shellcheck directives
- fix: remove unused message helper functions
- fix: refactor init_vars function for better variable initialization
- feat: refactor message formatting
- fix: update shell script includes to use full paths
- fix: verbose logging in __log function
- fix: shell quoting in _command return value
- fix: update __not_root_skip to use simpler message format
- fix: only run kdestroy as root in _check_domain_controller
- fix: use ldapsearch -H option (Closes: #51685)
- fix: resolve shellcheck warnings
- fix: format script with shfmt

* Fri Apr 18 2025 Evgeny Sinelnikov <sin@altlinux.org> 0.4-alt1
- fix: diag: add category adtCategory

* Wed Apr 09 2025 Andrey Limachko <liannnix@altlinux.org> 0.3-alt2
- spec: switch to new alterator-entry

* Mon Dec 23 2024 Andrey Limachko <liannnix@altlinux.org> 0.3-alt1
- Add Alterator Entry validation to .spec (thx Kozyrev Yuri)
- Translate Alterator Entry files to toml (thx Kozyrev Yuri)
- fix: add -v for logs in ADT (thx Elena Dyatlenko)

* Fri Sep 27 2024 Michael Shigorin <mike@altlinux.org> 0.2.8-alt2
- E2K: avoid shellcheck due to ghc still lacking

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
