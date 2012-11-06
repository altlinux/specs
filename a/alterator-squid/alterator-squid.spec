Name: alterator-squid
Version: 1.3
Release: alt1

Packager: Stanislav Ievlev <inger@altlinux.org>

BuildArch: noarch

Source:%name-%version.tar

Summary: Alterator module for Squid proxy server configuration
License: GPL
Group: System/Configuration/Other
Requires: alterator >= 4.8-alt1
Requires: metalterator >= 1.2-alt3
Requires: verborum-caterva >= 2.0-alt2
Requires: caterva-alterator-kit-sh >= 2.0-alt1
Requires: alterator-net-iptables >= 4.4-alt1
Requires: alterator-ldap-groups >= 0.1-alt2
Requires: alterator-fbi >= 5.11-alt2
Requires: squid >= 3.0.STABLE15-alt2
Requires: alterator-openldap-functions >= 0.1-alt1
Requires: alterator-service-functions >= 1.0-alt4
Conflicts: alterator >= 5.0
Conflicts: metalterator >= 2.0
Conflicts: verborum-caterva >= 3.0
Conflicts: caterva-alterator-kit-sh >= 3.0
Conflicts: alterator-net-iptables >= 5.0
Conflicts: alterator-ldap-groups >= 1.0
Conflicts: alterator-fbi >= 6.0
Conflicts: alterator-openldap-functions >= 2.0
Conflicts: alterator-service-functions >= 2.0

BuildRequires(Pre): rpm-macros-alterator

# Automatically added by buildreq on Wed Apr 08 2009
BuildRequires: alterator rpm-macros-fillup

%description
Alterator module for Squid proxy server configuration

%prep
%setup -q

%build
%make_build

%install
%makeinstall
mkdir -p -m0755 %buildroot%_sysconfdir/metalterator && \
cp -rp metalterator/squid %buildroot%_sysconfdir/metalterator/
mkdir -p -m0755 %buildroot%_sysconfdir/caterva/squid && \
cp -rp caterva/* %buildroot%_sysconfdir/caterva/squid/

%files
%_alterator_datadir/applications/*
%_alterator_datadir/ui/squid
%_alterator_datadir/interfaces/guile/backend/squid.scm
%_alterator_datadir/interfaces/guile/type/*
%config(noreplace) %_sysconfdir/metalterator/squid
%_sysconfdir/caterva/squid
%_alterator_backend3dir/squid-commit
%_bindir/*

%changelog
* Tue Nov 06 2012 Paul Wolneykien <manowar@altlinux.ru> 1.3-alt1
- Backup the squid.conf before making any changes.
- Remove the configuration migration script.
- Do not redirect the 21st (FTP) port in transparent mode.
- Parse the Squid configuration on the fly.

* Fri Jul 06 2012 Cronbuild Service <cronbuild@altlinux.org> 1.2-alt17
- repocop cronbuild 20120706. At your service.

* Mon Apr 23 2012 Cronbuild Service <cronbuild@altlinux.org> 1.2-alt16
- repocop cronbuild 20120423. At your service.

* Tue Oct 18 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2-alt15
- repocop cronbuild 20111018. At your service.

* Thu Sep 15 2011 Paul Wolneykien <manowar@altlinux.ru> 1.2-alt14
- Do not output empty ACLs (closes: 26281).

* Wed Sep 07 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2-alt13
- repocop cronbuild 20110907. At your service.

* Fri Jul 29 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2-alt12
- repocop cronbuild 20110729. At your service.

* Mon Apr 11 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2-alt11
- repocop cronbuild 20110411. At your service.

* Wed Mar 09 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2-alt10
- repocop cronbuild 20110309. At your service.

* Wed Mar 09 2011 Paul Wolneykien <manowar@altlinux.ru> 1.2-alt9
- Fix the Cronbuild rooter script access mode.

* Tue Mar 08 2011 Paul Wolneykien <manowar@altlinux.ru> 1.2-alt8
- Add a Cronbuild rooter script.

* Thu Feb 17 2011 Paul Wolneykien <manowar@altlinux.ru> 1.2-alt7
- Install squid-server package and use provided default configuration
  for cronbuild update.

* Tue Feb 15 2011 Paul Wolneykien <manowar@altlinux.ru> 1.2-alt6
- Specify rpm-build pre-requisites (rpm-macros-alterator) to use
  macros properly.

* Tue Feb 08 2011 Paul Wolneykien <manowar@altlinux.ru> 1.2-alt5
- Do not deny access to the listed SSL ports (if any).

* Mon Jan 31 2011 Paul Wolneykien <manowar@altlinux.ru> 1.2-alt2
- Remove duplicate ports from the default safe port list.

* Wed Jan 12 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2-alt4
- repocop cronbuild 20110112. At your service.

* Wed Jan 12 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2-alt3
- repocop cronbuild 20110112. At your service.

* Tue Nov 23 2010 Paul Wolneykien <manowar@altlinux.ru> 1.2-alt1
- Define deny policies first.
- Check for an allow policy for all and authenticated users.

* Thu Dec 17 2009 Paul Wolneykien <manowar@altlinux.ru> 1.1-alt8
- Fix missing read of the auth-mode value (closes: 22548).

* Mon Dec 14 2009 Paul Wolneykien <manowar@altlinux.ru> 1.1-alt7
- Ignore ldap-groups backend errors with empty list.
- Fix authenticated users access configuration with empty domain list.

* Thu Dec 03 2009 Paul Wolneykien <manowar@altlinux.ru> 1.1-alt6
- Do not reload data on "mode" change.
- New procedure to write parameters on "Apply" click (closes: 22411)

* Tue Nov 01 2009 Paul Wolneykien <manowar@altlinux.ru> 1.1-alt5
- Fix procedure name in action binding (closes: 22411).

* Tue Oct 20 2009 Paul Wolneykien <manowar@altlinux.ru> 1.1-alt4
- Do not use "form" workflow.
- Remove unused Groups page.

* Tue Oct 20 2009 Paul Wolneykien <manowar@altlinux.ru> 1.1-alt3
- Restart the service if authentication mode was modified (closes: 21921).

* Tue Oct 20 2009 Paul Wolneykien <manowar@altlinux.ru> 1.1-alt2
- Transparent redirection port option (closes: 20985).
- Set transparent redirection by default for conventional protocols.

* Mon Oct 19 2009 Paul Wolneykien <manowar@altlinux.ru> 1.1-alt1
- Access rules revisited (closes: 20396).
- New main page layout (closes: 21283).
- Remove domain entity.
- Add suffix property to the group entity.

* Mon Oct 12 2009 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt21
- Reload the service if it is already running (closes: 21921).
- Widen the network input field to 19 symbols (closes: 21918).

* Fri Oct 09 2009 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt20
- Manage port redirection rules async of iptables.

* Thu Oct 08 2009 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt19
- Fix domain acl usage condition (closes: 21675).

* Thu Oct 08 2009 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt18
- Use port redirection script (closes: 20985).
- Move helper code to the commit backend.

* Fri Aug 28 2009 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt17
- Use network address/network bits specification for internal networks (closes: 21218)
- Navigation simplyfied (closes: 21201).

* Sat Aug 17 2009 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt16
- Improved error reporting with the use of nameref and catch/message (closes: 21220)

* Sat Aug 17 2009 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt15
- Fix error on empty list of available groups (closes: 21202).
- Navigation revisited (closes: 21201).

* Sat Aug 17 2009 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt14
- Manage authentication mode in accordance with proxying mode.
- Update IP filter tables via alterator-net-iptables helper (closes: 20985).
- Disable record controls when there are no records in the list.

* Fri Aug 14 2009 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt13
- Allow authenticated access when no groups defined.
- Fix empty item list issues.

* Wed Aug 05 2009 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt12
- On-demand output of a new template record (closes: 20412).

* Wed Jul 01 2009 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt11
- Use synchronous access to the configuration via metalterator-cmdline.
- Use squid_ldap_group helper.
- Reconfigure Squid service on the fly (reload action).
- Wait up to 5 s for the service to start/stop/reload.

* Wed Jun 10 2009 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt10
- Fix pre-start/stop scripts packaging.
- Fix Caterva invocation argument (-b).
- Create Alterator configuration subdirectory.
- Check if Squid default configuration directory exists.

* Mon Jun 01 2009 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt9
- Using Caterva v2.0.
- PAM and Kerberos+PAM authentication methods (closes: 20145, 20152).
- Default Alterator SSL port passthrough (closes: 20153).
- Depends on Squid package (closes: 20120).

* Thu May 07 2009 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt8
- Closes #19963.

* Mon May 04 2009 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt7
- Use alterator-ldap-groups as user group source.

* Thu Apr 23 2009 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt6
- Use textual language parameter.
- Default configuration counters fixed.

* Tue Apr 21 2009 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt5
- Network interface management left for the iptables_helper.
- Domain suffix list data type.
- Domain management page has been moved to the Groups.
- Default configuration updated in accordance with the Squid package.

* Tue Apr 14 2009 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt4
- Service control interface added.

* Sat Apr 11 2009 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt3
- Using woo-case pattern syntax.
- Domain suffix field data type.
- Service pre-start and pre-stop scripts generating.

* Thu Apr 09 2009 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt2
- Using "link" and "read-next" new meta-backend operations.
- Verborum Caterva configuration generator.

* Wed Apr 08 2009 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt1
- Metalterator-based release.

* Tue Jan 27 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.4-alt6
- move help and translations to alterator-l10n

* Mon Dec 08 2008 Stanislav Ievlev <inger@altlinux.org> 0.4-alt5
- resurrect default settings tuning

* Fri Dec 05 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.4-alt4
- use help from l10n, rebuild

* Mon Oct 13 2008 Stanislav Ievlev <inger@altlinux.org> 0.4-alt3
- fix requires

* Fri Oct 10 2008 Stanislav Ievlev <inger@altlinux.org> 0.4-alt2
- add unit-tests

* Fri Sep 26 2008 Stanislav Ievlev <inger@altlinux.org> 0.4-alt1
- rewrite backend and UI

* Mon Aug 11 2008 Stanislav Ievlev <inger@altlinux.org> 0.3-alt1
- update html templates:
   * replace template-* backend with modern schema
   * remove <h1> and <title>
   * move design to /usr/share/alterator/design
- update build system:
   * use global support for awk based backends
   * use module.awk

* Tue Jun 17 2008 Grigory Batalov <bga@altlinux.ru> 0.2-alt15
- Require alterator-services instead of alterator-chkconfig.

* Fri Jun 06 2008 Grigory Batalov <bga@altlinux.ru> 0.2-alt14
- Replace label tag with a translation on the help page.

* Wed May 28 2008 Grigory Batalov <bga@altlinux.ru> 0.2-alt12.M41.1
- Update translations.
- Update service restart link.
- Backport to branch 4.1.

* Tue Mar 04 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.2-alt12
- Change help paths to the new style.

* Wed Aug 15 2007 Grigory Batalov <bga@altlinux.ru> 0.2-alt11
- Help content updated.

* Mon Aug 06 2007 Grigory Batalov <bga@altlinux.ru> 0.2-alt10
- Switch to new menu system.

* Tue May 22 2007 Grigory Batalov <bga@altlinux.ru> 0.2-alt9
- Backend rewritten in Awk.
- Site blacklist added.
- Cache manager password added.

* Wed May 02 2007 Grigory Batalov <bga@altlinux.ru> 0.2-alt8
- Accept acl our_networks if not yet (fix #11657).

* Sat Apr 28 2007 Grigory Batalov <bga@altlinux.ru> 0.2-alt7
- Ukrainian localization (tanks to Serhii Hlodin). 

* Wed Apr 25 2007 Grigory Batalov <bga@altlinux.ru> 0.2-alt6
- Add link for service configuration.
- Update for recent CSS.

* Wed Apr 11 2007 Grigory Batalov <bga@altlinux.ru> 0.2-alt5
- Constraints on listen host/port.
- Check if range mask is numerical.

* Wed Apr 11 2007 Grigory Batalov <bga@altlinux.ru> 0.2-alt4
- Reload service on write command too.
- Constraint on domain.

* Tue Apr 03 2007 Grigory Batalov <bga@altlinux.ru> 0.2-alt3
- Reload service after new/delete action.
- Constraint on network range.
- Listen and networks table headers were translated.
- Documentation updated (by kirill@).

* Thu Mar 29 2007 Grigory Batalov <bga@altlinux.ru> 0.2-alt2
- Documentation included.

* Mon Mar 26 2007 Grigory Batalov <bga@altlinux.ru> 0.2-alt1
- Russian translation was added.
- Store allowed networks in separate file.

* Wed Mar 14 2007 Grigory Batalov <bga@altlinux.ru> 0.1-alt1
- Initial release


