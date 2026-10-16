Name:           freeipa-server-gpo
Version:        0.2.0
Release:        alt1

Summary:        Prepare FreeIPA for Group Policy Management
License:        GPLv3+
Group:          System/Configuration/Other
Url:            https://github.com/danila-Skachedubov/ipa-gpo-install
ExcludeArch: %ix86

BuildRequires: rpm-build-python3
BuildRequires: gettext-tools
BuildRequires: python3-module-pytest
BuildRequires: python3-module-coverage
BuildRequires: python3-module-freeipa
BuildRequires: python3-module-ipaserver
BuildRequires: python3-module-dbus
BuildRequires: python3-module-ldap

Requires: python3-module-freeipa
Requires: python3-module-ipaserver
Requires: freeipa-server-core
Requires: freeipa-server-trust-ad
Requires: samba-common-tools
Requires: admx-basealt
Requires: sdmx-basealt >= 1.0.0
Requires: sdmx-schemas >= 1.0.0
Requires: python3-module-admix >= 0.3.0
Requires: python3-module-admix < 0.4.0
Requires: acl
Requires: coreutils
Requires: libgio
Requires: oddjob
Requires: systemd
Requires: util-linux
Source0: %name-%version.tar

%description
A utility for preparing FreeIPA for Group Policy Management.
Extends the LDAP schema with Group Policy related object classes
and creates the necessary directory structure.

%prep
%setup -q

%build
%make_build compile-po

%install
make install PREFIX=%_prefix DESTDIR=%buildroot PYTHON_SITELIBDIR=%python3_sitelibdir
%find_lang ipa-gpo-install

%check
%make check-po
%make test-coverage

%files -f ipa-gpo-install.lang
%doc README.md
%doc README.ru.md
%doc doc/ARCHITECTURE.md
%doc doc/ARCHITECTURE.ru.md
%_bindir/ipa-gpo-install
%python3_sitelibdir/ipa_gpo_install/
%python3_sitelibdir/ipaserver/plugins/gpo.py*
%python3_sitelibdir/ipaserver/plugins/chain.py*
%python3_sitelibdir/ipaserver/plugins/gpmaster.py*
%python3_sitelibdir/ipaserver/plugins/__pycache__/gpo.*
%python3_sitelibdir/ipaserver/plugins/__pycache__/chain.*
%python3_sitelibdir/ipaserver/plugins/__pycache__/gpmaster.*
%_datadir/ipa/ui/js/plugins/chain
%_datadir/ipa/schema.d/75-gpc.ldif
%_datadir/ipa/schema.d/75-chain.ldif
%_datadir/ipa/schema.d/75-gpmaster.ldif
%_datadir/ipa/updates/75-gpc.update
%_datadir/ipa/updates/75-chain.update
%_datadir/ipa/updates/75-gpmaster.update
%config(noreplace) %_sysconfdir/oddjobd.conf.d/ipa-gpo.conf
%_prefix/libexec/ipa/oddjob/org.freeipa.server.create-gpo-structure
%_prefix/libexec/ipa/oddjob/org.freeipa.server.delete-gpo-structure
%_mandir/man8/ipa-gpo-install.8*
%_mandir/ru/man8/ipa-gpo-install.8*
%_datadir/bash-completion/completions/ipa-gpo-install

%changelog
* Mon Oct 12 2026 Danila Skachedubov <skachedubov@altlinux.org> 0.2.0-alt1
- Use allocated FreeIPA OIDs and ipaGpo-prefixed LDAP schema names
  (thx Alexander Bokovoy).
- Add Security Settings and Advanced Audit editors with libadmix 0.3
  and external SDMX/SDML 1.0 definitions (thx Korney Gedert).
- Add unified policy search, editor dialogs and keyboard navigation
  (thx Korney Gedert).
- Expand Preferences editing with item-level targeting and collection
  controls (thx vladimirovicp and Korney Gedert).
- Improve Scripts editing and add revision-checked script downloads
  (thx vladimirovicp and Korney Gedert).
- Add drag-and-drop reordering for chains and linked GPOs
  (thx vladimirovicp).
- Improve GPO renaming in the Web UI (thx vladimirovicp).
- Disable chain renaming in the Web UI.
- Complete Russian installer translations and expand Web UI localization
  (thx vladimirovicp and Korney Gedert).
- Validate Group Policy LDAP infrastructure and verify installation
  updates (thx Korney Gedert).
- Gate RPM publication on live FreeIPA integration tests of the same
  artifact.

* Thu Aug 27 2026 Danila Skachedubov <skachedubov@altlinux.org> 0.1.1-alt1
- ci: allow manual test package publishing
- ci: publish tagged RPM releases
- ci: build RPM in Sisyphus hasher
- ci: add Python backend checks
- build: verbose colored pytest output in %check
- build: run unit tests during package build
- fix(gpo): bound oddjob D-Bus calls
- fix(gpo): match LDAP delete callback contract
- fix(gpo): handle malformed D-Bus responses

* Fri Aug 07 2026 Danila Skachedubov <skachedubov@altlinux.org> 0.1.0-alt1
- feat: fix info help (thx vladimirovicp)
- chore(web): temporarily hide Preferences from tree (thx Korney Gedert)
- packaging: include ARCHITECTURE.md in RPM docs
- docs: add technical architecture documentation (en + ru)
- fix:list of children files, if the name is long and the infowindow
  is open , the information merges (thx vladimirovicp)
- feat: list of children, added scrolling for large lists (thx vladimirovicp)
  text than a block (thx vladimirovicp)
  is now at a9afdf0 fix:admx window height 100%% (thx vladimirovicp)
- fix:indents in the tree structure (thx vladimirovicp)
- feat(ui): show chain description in web interface
- refactor: replace displayName with description for chain entity

* Fri Jul 24 2026 Danila Skachedubov <skachedubov@altlinux.org> 0.0.9-alt1
- feat: migrate to libadmix editor API, remove gpuiservice (thx Korney Gedert)
- feat: add structured GPUI editor UI and script editor API (thx Korney Gedert)
- fix: move chains to dedicated cn=Chains,cn=System container
- fix: restore two-step LDAP write for chain/gpo reorder
- fix: add D-Bus activation file, copy UI assets on install (thx Korney Gedert)
- fix: preserve ADMX value types in Registry.pol (thx Korney Gedert)

* Mon Jun 15 2026 Danila Skachedubov <skachedubov@altlinux.org> 0.0.8-alt1
- feat: add unsaved changes confirmation modal on tree navigation (thx vladimirovicp)
- feat(admx): implemented package management (thx vladimirovicp)
- fix(gpui): restore checkbox visibility in ADMX options (thx Valery Sinelnikov)
- fix(gpui): restore preferences control buttons in header (thx Valery Sinelnikov)
- fix(gpoiservice): show policy displayName as tree root title (thx Valery Sinelnikov)
- feat(gpuiservice): add policy comments support (CMTX/CMTL) (thx Valery Sinelnikov)
- feat(gpuiservice): add scripts support (scripts.ini/psscripts.ini) (thx Valery Sinelnikov)
- feat(gpoiservice): add locale-aware UI initialization (thx Valery Sinelnikov)

* Thu Apr 30 2026 Danila Skachedubov <skachedubov@altlinux.org> 0.0.7-alt1
- feat: improved ADMX support (localization, help texts, parsing, and navigation)
- feat: added full Group Policy Preferences (GPP) support, including validation, XML generation, and DBus API
- feat: enhanced path handling (config-driven paths, normalization, sysvol mapping, update utility with rollback)
- fix: multiple fixes for policy handling, registry processing, JSON/Unicode output, and API compatibility
- fix: improved stability (thread safety, error handling, correct data parsing)
- refactor: simplified architecture, added type hints, and introduced shared configuration modules
- docs/build: added testing documentation and updated build utilities/dependencies

* Tue Mar 03 2026 Danila Skachedubov <skachedubov@altlinux.org> 0.0.6-alt1
- feat(gpuiservice): improve service management with enable --now

* Fri Feb 27 2026 Danila Skachedubov <skachedubov@altlinux.org> 0.0.5-alt1
- feat(gpuiservice): add GPUIService support with systemd integration
- feat(plugins): add ipaclient plugin for GPO operations
- fix(plugins): fix regex matching for GPO and chain names
- i18n(ru): update Russian translations for GPUIService strings

* Tue Jan 20 2026 Danila Skachedubov <skachedubov@altlinux.org> 0.0.4-alt1
- feat(plugins): add schema verification and error handling
- revert: remove staging directory for plugins, return to direct
  file installation

* Tue Dec 23 2025 Danila Skachedubov <skachedubov@altlinux.org> 0.0.3-alt1
- feat: implement staging directory for plugins and update to
  version 0.0.3
- fix: improve logging and fix oddjob service name
- fix(i18n): fix Russian translations
- fix(chain): fix display of inactive chains in chain_find

* Sat Nov 01 2025 Danila Skachedubov <skachedubov@altlinux.org> 0.0.2-alt1
- feat: add Russian README and improve SYSVOL configuration
- feat(i18n): add English translation for README

* Wed Apr 16 2025 Danila Skachedubov <skachedubov@altlinux.org> 0.0.1-alt1
- Initial build
