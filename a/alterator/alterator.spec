Name: alterator
Version: 4.22
Release: alt1

Summary: ALT Linux configurator engine
License: GPLv2+
Group: System/Configuration/Other
Url: http://wiki.sisyphus.ru/Alterator
Packager: Stanislav Ievlev <inger@altlinux.org>

Source: %name-%version.tar

#backward compatibility
Provides: %name-common = %version , %name-menu = %version, %name-help = %version, %name-sdk = %version, %name-autoinstall = %version
Obsoletes: %name-common, %name-menu, %name-help, %name-sdk, %name-autoinstall

Requires: rpm-macros-%name = %version-%release
Requires: alterator-l10n >= 2.0-alt2
Requires: guile18 >= 1.6.8-alt4

Requires(pre): libguile-vhttpd >= 0.7-alt1
Requires(pre): shadow-utils

#incompatibility
Conflicts: alterator-lookout < 1.3-alt13
Conflicts: alterator-fbi < 5.24-alt1
Conflicts: alterator-xkb < 2.0-alt3
Conflicts: alterator-vm <= 0.3-alt31
Conflicts: installer-stage2 <= 0.8-alt1

# Automatically added by buildreq on Fri Dec 29 2006
BuildRequires: guile18-devel libexpat-devel pam_userpass-devel

%define guile_version 1.8

%define _alterator_datadir %_datadir/%name
%define _alterator_libdir %_libexecdir/%name

%add_findreq_skiplist %_alterator_datadir/build/profiles/*
%add_findreq_skiplist %_alterator_datadir/build/xgettext/*
%add_findreq_skiplist %_alterator_datadir/build/msgfmt/*

%description
ALT Linux configurator engine

%package doc
Summary: documentation and samples for %name
Group: System/Configuration/Other
BuildArch: noarch
Requires: %name = %version-%release

%description doc
documentation and samples for %name

%package -n rpm-macros-%name
Summary: Set of RPM macros for packaging %name-based applications
Group: Development/Other
BuildArch: noarch
Conflicts: %name < 4.7-alt6

%description -n rpm-macros-%name
Set of RPM macros for packaging %name-based applications for ALT Linux.
Install this package if you want to create RPM packages that use %name.

%prep
%setup

%build
%make_build GUILE_VERSION=%guile_version
%make check-api

%install
%makeinstall GUILE_VERSION=%guile_version
ln -s ../bin/alterator-cmdline %buildroot%_sbindir/

#create special directories
mkdir -p %buildroot%_runtimedir/alteratord
mkdir -p %buildroot%_cachedir/%name
mkdir -p %buildroot%_localstatedir/%name
mkdir -p %buildroot%_sysconfdir/%name
mkdir -p %buildroot%_sysconfdir/tmpfiles.d
mkdir -p %buildroot%_rpmmacrosdir

install -Dpm640 alterator-chkpwd.pamd %buildroot%_sysconfdir/pam.d/alterator-chkpwd

cat >%buildroot%_rpmmacrosdir/%name<<EOF
%%_alterator_datadir %%_datadir/%name
%%_alterator_libdir %%_libexecdir/%name

%%_alterator_backend2dir %%_alterator_libdir/backend2
%%_alterator_backend3dir %%_alterator_libdir/backend3
EOF

cat >%buildroot%_sysconfdir/tmpfiles.d/%name.conf<<EOF
d /var/run/alteratord 0755 root root -
EOF

%pre
/usr/sbin/groupadd -r -f _alteratord

%post
%post_service alteratord

%preun
%preun_service alteratord

%files
%_bindir/*

%dir %_alterator_libdir
%_alterator_libdir/backend3
%attr(700,root,root) %dir %_alterator_libdir/hooks

%_alterator_datadir

%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/menu
%attr(700,root,root) %dir %_cachedir/%name
%attr(700,root,root) %dir %_localstatedir/%name
%_sysconfdir/tmpfiles.d/%name.conf

%_datadir/guile/%guile_version/alterator
%_libdir/*.so.*
%_libdir/libguile*.so

%_sbindir/*
%_initdir/*
%_mandir/man?/*
%dir /var/run/alteratord

%attr(640,root,root) %_sysconfdir/pam.d/alterator-chkpwd

%files doc
%doc doc/samples doc/internals

%files -n rpm-macros-%name
%_rpmmacrosdir/*

%changelog
* Tue May 22 2012 Michael Shigorin <mike@altlinux.org> 4.22-alt1
- fix root alteratord socket location back to the usual one
  (as expected by installer)

* Mon May 14 2012 Michael Shigorin <mike@altlinux.org> 4.21-alt1
- add support for non-privileged execution of alteratord,
  alterator-cmdline (by Lenar Shakirov; closes: #23377)
- fix finding out current user: "cuserid" not working in hasher
  (by Lenar Shakirov)

* Wed Apr 04 2012 Michael Shigorin <mike@altlinux.org> 4.20-alt3
- add systemd support by shaba@ (closes: #26583)

* Mon Nov 07 2011 Lenar Shakirov <snejok@altlinux.ru> 4.20-alt2
- warning for wrong system-account-name fixed (closes: #11912)

* Tue Jul 19 2011 Mikhail Efremov <sem@altlinux.org> 4.20-alt1
- Restart alteratord service after exit private one.

* Thu Oct 21 2010 Sergey V Turchin <zerg@altlinux.org> 4.19-alt1
- add ipv4-addrwmask ipv4-addrwmask-list types

* Thu Sep 09 2010 Sergey V Turchin <zerg@altlinux.org> 4.18-alt1
- add ipv4-network-list type

* Fri Dec 18 2009 Stanislav Ievlev <inger@altlinux.org> 4.17-alt3
- resurrect exception unpacking

* Fri Dec 11 2009 Stanislav Ievlev <inger@altlinux.org> 4.17-alt2
- add group 'Firewall'

* Thu Dec 03 2009 Stanislav Ievlev <inger@altlinux.org> 4.17-alt1
- switch to HTTP procotol
- drop automatic daemon start support
- remove sgid helper

* Fri Nov 27 2009 Stanislav Ievlev <inger@altlinux.org> 4.16-alt2
- alterator-cmdline: more descriptive message on internal errors

* Fri Nov 13 2009 Stanislav Ievlev <inger@altlinux.org> 4.16-alt1
- add woo-call function

* Wed Nov 11 2009 Stanislav Ievlev <inger@altlinux.org> 4.15-alt1
- more information into exception of type internal-error was added.
- always start in foreground and move process to background using
  start-stop-daemon utility to avoid problems in guile at x86_64
  platform (some conflict between pthreads and fork).

* Mon Oct 19 2009 Vladislav Zavjalov <slazav@altlinux.org> 4.14-alt1
- move card-index module from alterator-fbi

* Thu Oct 15 2009 Stanislav Ievlev <inger@altlinux.org> 4.13-alt2
- fix system-error catching

* Thu Oct 15 2009 Stanislav Ievlev <inger@altlinux.org> 4.13-alt1
- fix access rights to local state directory
- replace (alterator socket) library with (vhttpd)

* Tue Sep 29 2009 Stanislav Ievlev <inger@altlinux.org> 4.12-alt2
- fix access rights to cache directory

* Fri Sep 25 2009 Stanislav Ievlev <inger@altlinux.org> 4.12-alt1
- add (alterator menu) library: optimized menu listing.
- menu backend: add list of expert_modules, alterator_api_version = 1.
- add default values into module-order-list and section-order-list

* Wed Sep 23 2009 Stanislav Ievlev <inger@altlinux.org> 4.11-alt3
- add manual page for (alterator effect) library
- add missing forward definition for (form-update-value) (closes: #21611)

* Tue Sep 22 2009 Stanislav Ievlev <inger@altlinux.org> 4.11-alt2
- improve dynamic-require function:
  Now we will see a error message if module exists, but contains a some errors

* Mon Sep 21 2009 Stanislav Ievlev <inger@altlinux.org> 4.11-alt1
- add telephone-number type

* Fri Sep 04 2009 Stanislav Ievlev <inger@altlinux.org> 4.10-alt10
- fix e-mail type: use right dictionary for translation

* Mon Aug 17 2009 Stanislav Ievlev <inger@altlinux.org> 4.10-alt9
- fix pam.d file for alterator-chkpwd (closes: #20061)

* Tue Aug 11 2009 Stanislav Ievlev <inger@altlinux.org> 4.10-alt8
- add e-mail type (closes: #20108)
- add man page for (alterator ajax)

* Wed Jun 03 2009 Vladislav Zavjalov <slazav@altlinux.org> 4.10-alt7
- build/xgettext/desktop: look for *.desktop and *.directory files
  in the whole module tree

* Thu May 21 2009 Stanislav Ievlev <inger@altlinux.org> 4.10-alt6
- add support for steps directory

* Tue May 19 2009 Stanislav Ievlev <inger@altlinux.org> 4.10-alt5
- add generic effects library

* Tue May 05 2009 Stanislav Ievlev <inger@altlinux.org> 4.10-alt4
- fix plist-filter semantics, add plist-remove

* Wed Apr 22 2009 Stanislav Ievlev <inger@altlinux.org> 4.10-alt3
- add man page and unit tests for (alterator woo)

* Thu Apr 16 2009 Stanislav Ievlev <inger@altlinux.org> 4.10-alt2
- add prereq to shadow utils
- update man pages (mike@)

* Tue Apr 14 2009 Stanislav Ievlev <inger@altlinux.org> 4.10-alt1
- move type definitions to more convenient place
- little code optimizations

* Wed Apr 08 2009 Stanislav Ievlev <inger@altlinux.org> 4.9-alt2
- fix typos in man pages and help screens

* Tue Apr 07 2009 Stanislav Ievlev <inger@altlinux.org> 4.9-alt1
- refactor ensign
- add man pages for alteratord and alterator-cmdline

* Wed Apr 01 2009 Stanislav Ievlev <inger@altlinux.org> 4.8-alt1
- improve module-skip-list, more feature for menu tuning

* Wed Mar 18 2009 Stanislav Ievlev <inger@altlinux.org> 4.7-alt7
- add module_skip_list to hide some items in configurator menu

* Thu Mar 12 2009 Dmitry V. Levin <ldv@altlinux.org> 4.7-alt6
- Fixed %_libexecdir/alteratord directory permissions.
- Moved rpm macros to rpm-macros-%name subpackage.

* Wed Mar 04 2009 Stanislav Ievlev <inger@altlinux.org> 4.7-alt5
- add system-computer-name type
- build system: fix and improve module generators

* Thu Feb 26 2009 Stanislav Ievlev <inger@altlinux.org> 4.7-alt4
- update html-ui generator for new html ui features
- remove backend and backend2 directories, add hooks directory

* Mon Feb 02 2009 Mikhail Efremov <sem@altlinux.org> 4.7-alt3
- use own PAM configuration file

* Thu Jan 29 2009 Mikhail Efremov <sem@altlinux.org> 4.7-alt2
- add alterator-chkpwd

* Tue Jan 27 2009 Vladislav Zavjalov <slazav@altlinux.org> 4.7-alt1
- move help and translations to alterator-l10n
- update translations in *.directory files
- remove build/msggrep util (moved to alterator-l10n)
- fix load-path order (by inger@)
- add ALTERATOR_DATADIR to %%load-path (by inger@)
- remove obsolete alterator-init function (by inger@)

* Fri Jan 23 2009 Stanislav Ievlev <inger@altlinux.org> 4.6-alt4
- improve work with exceptions

* Tue Jan 20 2009 Mikhail Efremov <sem@altlinux.org> 4.6-alt3
- find translates in ui dir

* Mon Jan 19 2009 Mikhail Efremov <sem@altlinux.org> 4.6-alt2
- lost changes are returned

* Fri Jan 16 2009 Mikhail Efremov <sem@altlinux.org> 4.6-alt1
- ui.scm guile module is added (resolve-path function)

* Thu Dec 11 2008 Vladislav Zavjalov <slazav@altlinux.org> 4.5-alt2
- run xgettext with LANG=C

* Thu Dec 11 2008 Vladislav Zavjalov <slazav@altlinux.org> 4.5-alt1
- remove ldconfig macros from spec

* Wed Dec 10 2008 Stanislav Ievlev <inger@altlinux.org> 4.3-alt2
- remove debug messages

* Tue Dec 09 2008 Stanislav Ievlev <inger@altlinux.org> 4.3-alt1
- switch to guile-1.8
- add manpage for alterator-dump-desktop (slazav@)
- build/msgfmt/desktop: fix problem with desktop files w/o newline on tail (slazav@)

* Fri Nov 07 2008 Stanislav Ievlev <inger@altlinux.org> 4.2-alt2
- export ALTERATOR_DEBUG variable in local mode

* Thu Nov 06 2008 Stanislav Ievlev <inger@altlinux.org> 4.2-alt1
- redesign native backend support

* Fri Oct 24 2008 Stanislav Ievlev <inger@altlinux.org> 4.1-alt1
- join with alterator-autoinstall package
- remove support for constraints

* Thu Oct 16 2008 Stanislav Ievlev <inger@altlinux.org> 4.0-alt18
- remove backend3.sh support

* Thu Oct 02 2008 Stanislav Ievlev <inger@altlinux.org> 4.0-alt17
- install-help: add support for alterator-l10n

* Thu Oct 02 2008 Stanislav Ievlev <inger@altlinux.org> 4.0-alt16
- add support for "make verify-module"

* Tue Sep 30 2008 Stanislav Ievlev <inger@altlinux.org> 4.0-alt15
- (alterator socket): fix descriptor leak
- (alterator d): d-connect: fix possible race

* Mon Sep 29 2008 Stanislav Ievlev <inger@altlinux.org> 4.0-alt14
- fix alterator-cmdline exit on errors
- new type: system-account-name

* Fri Sep 26 2008 Stanislav Ievlev <inger@altlinux.org> 4.0-alt13
- new type: ipv4-network

* Wed Sep 24 2008 Stanislav Ievlev <inger@altlinux.org> 4.0-alt12
- more portable gettext bindings

* Mon Sep 22 2008 Stanislav Ievlev <inger@altlinux.org> 4.0-alt11
- allow empty strings for tcp-port value

* Mon Sep 22 2008 Stanislav Ievlev <inger@altlinux.org> 4.0-alt10
- fix with-exit-handler usage

* Fri Sep 19 2008 Stanislav Ievlev <inger@altlinux.org> 4.0-alt9
- add unit-tests for types
- minor bugfixes

* Wed Sep 17 2008 Stanislav Ievlev <inger@altlinux.org> 4.0-alt8
- rebuild with latest alterator-l10n

* Wed Sep 17 2008 Stanislav Ievlev <inger@altlinux.org> 4.0-alt7
- new types: tcp-port, iso-3166-alpha2
- minor bugfixes

* Mon Sep 15 2008 Stanislav Ievlev <inger@altlinux.org> 4.0-alt6
- improve type-error exception processing

* Fri Sep 12 2008 Stanislav Ievlev <inger@altlinux.org> 4.0-alt5
- first version of new types system
- improve woo error handling
- minor code improvements

* Tue Sep 09 2008 Stanislav Ievlev <inger@altlinux.org> 4.0-alt4
- fix uid setup in control utility

* Mon Sep 08 2008 Stanislav Ievlev <inger@altlinux.org> 4.0-alt3
- fix and improve process execution code
- alterator-pipe: more correct quit from function

* Fri Sep 05 2008 Stanislav Ievlev <inger@altlinux.org> 4.0-alt2
- terminal port -> terminal fdes

* Fri Sep 05 2008 Stanislav Ievlev <inger@altlinux.org> 4.0-alt1
- add alteratord daemon

* Mon Aug 25 2008 Stanislav Ievlev <inger@altlinux.org> 3.9-alt9
- menu: add support for desktop file names

* Fri Aug 22 2008 Stanislav Ievlev <inger@altlinux.org> 3.9-alt8
- (alterator str): remove unused functions
- improve "Help not found" message
- improve hostname regexp

* Fri Aug 15 2008 Stanislav Ievlev <inger@altlinux.org> 3.9-alt7
- build sytem: remove support for workflow directory

* Thu Aug 14 2008 Stanislav Ievlev <inger@altlinux.org> 3.9-alt6
- fix typo

* Tue Aug 12 2008 Stanislav Ievlev <inger@altlinux.org> 3.9-alt5
- fix backend execution code (catch all errors and exit in child process)
- unload backend on any communication errors

* Mon Aug 11 2008 Stanislav Ievlev <inger@altlinux.org> 3.9-alt4
- build system: add support for awk based backends

* Fri Aug 08 2008 Stanislav Ievlev <inger@altlinux.org> 3.9-alt3
- build: add support for workflow directory
- improve backend2 loading api,
  rename (alterator ensign midshipman) to (alterator ensign backend2)

* Wed Aug 06 2008 Stanislav Ievlev <inger@altlinux.org> 3.9-alt2
- finally update menu backend, more fast section listing algo
- remove alterator-read-{desktop,directory} utilitites
- remove translated comments

* Tue Aug 05 2008 Stanislav Ievlev <inger@altlinux.org> 3.9-alt1
- menu backend: add more features, we need for new control center
- add comments to desktop-directories
- add alterator-dump-desktop - replacement of the alterator-read-{desktop,directory}

