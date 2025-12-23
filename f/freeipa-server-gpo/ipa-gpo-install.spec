Name:           freeipa-server-gpo
Version:        0.0.3
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
make install PREFIX=%{_prefix} DESTDIR=%{buildroot} PYTHON_SITELIBDIR=%{python3_sitelibdir}

%files
%doc README.md
%doc README.ru.md
%{_bindir}/ipa-gpo-install
%{python3_sitelibdir}/ipa_gpo_install/
%dir %{_datadir}/freeipa-server-gpo
%dir %{_datadir}/freeipa-server-gpo/staging
%dir %{_datadir}/freeipa-server-gpo/staging/plugin
%dir %{_datadir}/freeipa-server-gpo/staging/plugin/ipaserver
%dir %{_datadir}/freeipa-server-gpo/staging/plugin/ipaserver/plugins
%dir %{_datadir}/freeipa-server-gpo/staging/plugin/ui
%dir %{_datadir}/freeipa-server-gpo/staging/plugin/ui/grouppolicy
%dir %{_datadir}/freeipa-server-gpo/staging/plugin/schema.d
%dir %{_datadir}/freeipa-server-gpo/staging/plugin/update
%dir %{_datadir}/freeipa-server-gpo/staging/plugin/dbus_handlers
%{_datadir}/freeipa-server-gpo/staging/plugin/ipaserver/plugins/gpo.py*
%{_datadir}/freeipa-server-gpo/staging/plugin/ipaserver/plugins/chain.py*
%{_datadir}/freeipa-server-gpo/staging/plugin/ipaserver/plugins/gpmaster.py*
%{_datadir}/freeipa-server-gpo/staging/plugin/ui/grouppolicy/chain.js
%{_datadir}/freeipa-server-gpo/staging/plugin/ui/grouppolicy/gpo.js
%{_datadir}/freeipa-server-gpo/staging/plugin/schema.d/75-gpc.ldif
%{_datadir}/freeipa-server-gpo/staging/plugin/schema.d/75-chain.ldif
%{_datadir}/freeipa-server-gpo/staging/plugin/schema.d/75-gpmaster.ldif
%{_datadir}/freeipa-server-gpo/staging/plugin/update/75-gpc.update
%{_datadir}/freeipa-server-gpo/staging/plugin/update/75-chain.update
%{_datadir}/freeipa-server-gpo/staging/plugin/update/75-gpmaster.update
%{_datadir}/freeipa-server-gpo/staging/plugin/dbus_handlers/ipa-gpo.conf
%{_datadir}/freeipa-server-gpo/staging/plugin/dbus_handlers/org.freeipa.server.create-gpo-structure
%{_datadir}/freeipa-server-gpo/staging/plugin/dbus_handlers/org.freeipa.server.delete-gpo-structure
%{_mandir}/man8/ipa-gpo-install.8*
%{_mandir}/ru/man8/ipa-gpo-install.8*
%{_datadir}/bash-completion/completions/ipa-gpo-install
%{_datadir}/locale/ru/LC_MESSAGES/ipa-gpo-install.mo

%post
echo "********************************************************************"
echo "FreeIPA Group Policy plugins have been installed in staging directory."
echo "To activate them, run: ipa-gpo-install"
echo "This will copy the plugins to their proper locations and configure"
echo "the necessary schema and services."
echo "********************************************************************"

%postun
if [ $1 -eq 0 ]; then
    # Package removal (not upgrade)
    # Remove plugin files that were copied by ipa-gpo-install
    rm -f %{python3_sitelibdir}/ipaserver/plugins/chain.py
    rm -f %{python3_sitelibdir}/ipaserver/plugins/gpmaster.py
    rm -f %{python3_sitelibdir}/ipaserver/plugins/gpo.py

    rm -f %{_datadir}/ipa/ui/js/plugins/chain/chain.js
    rm -f %{_datadir}/ipa/ui/js/plugins/chain/gpo.js

    rm -f %{_datadir}/ipa/schema.d/75-chain.ldif
    rm -f %{_datadir}/ipa/schema.d/75-gpc.ldif
    rm -f %{_datadir}/ipa/schema.d/75-gpmaster.ldif

    rm -f %{_datadir}/ipa/updates/75-chain.update
    rm -f %{_datadir}/ipa/updates/75-gpc.update
    rm -f %{_datadir}/ipa/updates/75-gpmaster.update

    rm -f %{_sysconfdir}/oddjobd.conf.d/ipa-gpo.conf
    rm -f %{_prefix}/libexec/ipa/oddjob/org.freeipa.server.create-gpo-structure
    rm -f %{_prefix}/libexec/ipa/oddjob/org.freeipa.server.delete-gpo-structure
fi

%changelog
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