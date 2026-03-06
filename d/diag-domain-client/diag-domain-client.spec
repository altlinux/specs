%define _unpackaged_files_terminate_build 1
%define diagnostic_tool domain-client

Name: diag-%diagnostic_tool
Version: 0.7.3
Release: alt2

Summary: Active Directory domain environment diagnostic tool
License: GPLv3
Group: System/Configuration/Other
BuildArch: noarch

Url: https://altlinux.space/alterator/diag-domain-client
Source: %name-%version.tar

Requires: alterator-module-executor >= 0.1.29
Requires: alterator-interface-diag = 0.1.5
Requires: apt-repo samba

BuildRequires(pre): rpm-macros-alterator
%ifnarch %e2k
BuildRequires: shellcheck
%endif
BuildRequires: alterator-entry bats
BuildRequires: apt-repo samba
BuildRequires: /dev
BuildRequires: /proc

Obsoletes: domain-diag < %EVR

%description
Active Directory domain environment diagnostic tool.

%prep
%setup

%build
%make_build

%install
%makeinstall

%check
%ifnarch %e2k
shellcheck %name
%endif
find ./alterator/ -type f -exec alterator-entry validate {} \+
bats tests/report_test.bats

%files
%_bindir/%name
%_man1dir/%name.*
%_alterator_datadir/backends/%name.backend
%_alterator_datadir/diagnostictools/%diagnostic_tool.diag
%_iconsdir/hicolor/scalable/apps/%name.svg

%changelog
* Wed Mar 04 2026 Kozyrev Yuri <kozyrevid@altlinux.org> 0.7.3-alt2
- updated interface dependency

* Mon Feb 16 2026 Kozyrev Yuri <kozyrevid@altlinux.org> 0.7.3-alt1
- fixed typos (Closes: 57830 56204)
- update man (Closes: 57843)

* Mon Feb 09 2026 Andrey Limachko <liannnix@altlinux.org> 0.7.2-alt1
- Revert "chore: add 'exit_status = true' for new version of
  executor"
- fix: update display names

* Wed Feb 04 2026 Kozyrev Yuri <kozyrevid@altlinux.org> 0.7.1-alt1
- fix: added missing description to .diag
- docs: update man page with --compact flag option (thx Andrey Limachko)
- feat: add --compact flag for minimal output mode (thx Andrey Limachko)

* Fri Jan 23 2026 Kozyrev Yuri <kozyrevid@altlinux.org> 0.7.0-alt1
- build: added some missing requirements
- fix: fixed report test (thnx liannnix@)
- build: added autotests
- build: added Makefile
- feat: added functional report

* Mon Dec 29 2025 Andrey Limachko <liannnix@altlinux.org> 0.6.0-alt1
- fix: correct kerberos cache file path handling
- feat: added kerberos tracing test (thx Kozyrev Yuri)
- chore: added tmp files cleanup (thx Kozyrev Yuri)

* Tue Dec 09 2025 Andrey Limachko <liannnix@altlinux.org> 0.5.2-alt1
- fix: adjust shellcheck directives for SC2329
- docs: update copyright year and add GPL license header
- fix: correct file permisions (thx Andrey Alekseev)
- fix: replaced uid with pid in tmp file name (thx Kozyrev Yuri)
- build: added dependency on interface (thx Kozyrev Yuri)

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
