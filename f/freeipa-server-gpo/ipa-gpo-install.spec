Name:           freeipa-server-gpo
Version:        0.0.4
Release:        alt1

Summary:        Prepare FreeIPA for Group Policy Management
License:        GPLv3+
Group:          System/Configuration/Other
Url:            https://github.com/danila-Skachedubov/ipa-gpo-install
ExcludeArch: %ix86

BuildRequires: rpm-build-python3
BuildRequires: gettext-tools

Requires: python3-module-freeipa
Requires: python3-module-ipaserver
Requires: freeipa-server-trust-ad
Requires: samba-common-tools
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

%files -f ipa-gpo-install.lang
%doc README.md
%doc README.ru.md
%_bindir/ipa-gpo-install
%python3_sitelibdir/ipa_gpo_install/
%python3_sitelibdir/ipaserver/plugins/gpo.py*
%python3_sitelibdir/ipaserver/plugins/chain.py*
%python3_sitelibdir/ipaserver/plugins/gpmaster.py*
%python3_sitelibdir/ipaserver/plugins/__pycache__/gpo.*
%python3_sitelibdir/ipaserver/plugins/__pycache__/chain.*
%python3_sitelibdir/ipaserver/plugins/__pycache__/gpmaster.*
%_datadir/ipa/ui/js/plugins/chain/chain.js
%_datadir/ipa/ui/js/plugins/chain/gpo.js
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
