Name: alterator
Version: 5.4.5
Release: alt1

Summary: ALT Linux configurator engine
License: GPLv2+
Group: System/Configuration/Other
Url: http://wiki.sisyphus.ru/Alterator

Source: %name-%version.tar
Patch0: alterator-5.1-compilation-workaround.patch
Patch1: alterator-guile20.patch
Patch2: alterator-5.4.1-call-cc-via-shift.patch
Patch3: alterator-5.1-eval-set-fix.patch
Patch4: alterator-5.4.1-fix-call-cc-via-shift-for-guile20.patch

#backward compatibility
Provides: %name-common = %version , %name-menu = %version, %name-help = %version, %name-sdk = %version, %name-autoinstall = %version
Obsoletes: %name-common, %name-menu, %name-help, %name-sdk, %name-autoinstall

Requires: rpm-macros-%name = %version-%release
Requires: alterator-l10n >= 2.9.123
Requires: alterator-sh-functions

## Set up Guile version and continuations flavour:
%ifarch %e2k
%def_without guile20 # Guile 2.2 is now ported to E2K
%def_with delimited_continuations
%else
%def_without guile20
%def_without delimited_continuations
%endif

%{?!_with_bootstrap:Requires: alterator-lookout}

Requires(pre): libguile-vhttpd >= 0.7.8-alt1
Requires(pre): shadow-utils

#incompatibility
Conflicts: alterator-lookout < 1.3-alt13
Conflicts: alterator-fbi < 5.24-alt1
Conflicts: alterator-xkb < 2.0-alt3
Conflicts: alterator-vm <= 0.3-alt31
Conflicts: installer-stage2 <= 0.8-alt1

BuildRequires: /proc
%if_with guile20
BuildRequires: guile20-devel libguile20-devel libexpat-devel pam_userpass-devel
Requires: guile20 libguile20
%else
BuildRequires: guile22-devel >= 2.2.0-alt2 libexpat-devel pam_userpass-devel
Requires: guile22
%endif
BuildRequires: libguile-vhttpd

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
%patch0 -p2

%if_with guile20
sed -i "s:guile/2.2:guile/2.0:g" build/guile-ext.mak
%patch1 -p2
%endif

%if_with delimited_continuations
%patch2 -p2
%if_with guile20
%patch4 -p2
%endif
%endif

%patch3 -p2

%build
%make_build GUILE_VERSION=%guile_version

%check
%make check-api

%install
export LTDL_LIBRARY_PATH=src/libguile-gettext:src/libguile-pipe:%_libdir/guile/%guile_version
%makeinstall GUILE_VERSION=%guile_version unitdir=%buildroot%_unitdir \
	     GUILE_LOAD_PATH=%_alterator_datadir/lookout
ln -s ../bin/alterator-cmdline %buildroot%_sbindir/

#create special directories
mkdir -p %buildroot%_cachedir/%name
mkdir -p %buildroot%_localstatedir/%name
mkdir -p %buildroot%_sysconfdir/%name
mkdir -p %buildroot%_tmpfilesdir
mkdir -p %buildroot%_rpmmacrosdir

install -Dpm640 alterator-chkpwd.pamd %buildroot%_sysconfdir/pam.d/alterator-chkpwd

cat >%buildroot%_rpmmacrosdir/%name<<EOF
%%_alterator_datadir %%_datadir/%name
%%_alterator_libdir %%_libexecdir/%name

%%_alterator_backend2dir %%_alterator_libdir/backend2
%%_alterator_backend3dir %%_alterator_libdir/backend3
EOF

cat >%buildroot%_tmpfilesdir/%name.conf<<EOF
d /run/alteratord 0710 root _alteratord -
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
%_alterator_libdir/interfaces
%{?!_with_bootstrap:%_alterator_libdir/lookout}
%_alterator_libdir/type
%_alterator_libdir/ui

%_alterator_datadir

%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/menu
%attr(700,root,root) %dir %_cachedir/%name
%attr(700,root,root) %dir %_localstatedir/%name
%_tmpfilesdir/%name.conf

%_datadir/guile/site/%guile_version/alterator
%guile_ccachedir/alterator
%guile_extensiondir/*.so

%_sbindir/*
%_initdir/*
%_mandir/man?/*

%_unitdir/alteratord.service
%_unitdir/alteratord.socket

%attr(640,root,root) %_sysconfdir/pam.d/alterator-chkpwd

%files doc
%doc doc/samples doc/internals

%files -n rpm-macros-%name
%_rpmmacrosdir/*

%changelog
* Sat Sep 07 2024 Ajrat Makhmutov <rauty@altlinux.org> 5.4.5-alt1
- Add a new built-in "debug" step.

* Wed May 15 2024 Paul Wolneykien <manowar@altlinux.org> 5.4.4-alt1
- Allow a hostname to start with a digit (RFC 1123).

* Thu Sep 14 2023 Anton Midyukov <antohami@altlinux.org> 5.4.3-alt1
- NMU: Replace /var/run -> /run, /var/lock -> /run/lock (closes: 35882)

* Wed Feb 22 2023 Paul Wolneykien <manowar@altlinux.org> 5.4.2-alt1
- Require alterator-l10n >= 2.9.123.
- Minor fix of error message for the 'system-computer-name' type.
- Improved error message for the 'hostname' type (closes: 42744).

* Thu Jun 30 2022 Anton Midyukov <antohami@altlinux.org> 5.4.1-alt7
- NMU: replace fgrep with grep -F

* Thu Aug 19 2021 Paul Wolneykien <manowar@altlinux.org> 5.4.1-alt6
- Fixed the last changelog entry with %%e2k macro.

* Thu Aug 19 2021 Paul Wolneykien <manowar@altlinux.org> 5.4.1-alt5
- Switch to Guile 2.2 on %%e2k.

* Mon Jun 21 2021 Paul Wolneykien <manowar@altlinux.org> 5.4.1-alt4
- Use additional fixes for delimited continuations with Guile 2.0.

* Fri Jun 11 2021 Paul Wolneykien <manowar@altlinux.org> 5.4.1-alt3
- Added "with delimited_continuations" spec option (on for E2K).
- New version of the reset/shift hack.

* Wed Aug 26 2020 Paul Wolneykien <manowar@altlinux.org> 5.4.1-alt2
- Disable auto compilation of .scm files.

* Mon Dec 16 2019 Paul Wolneykien <manowar@altlinux.org> 5.4-alt2
- Fixed failing tests: Explicitly set ru_RU.UTF-8 locale.

* Fri Jun 07 2019 Paul Wolneykien <manowar@altlinux.org> 5.4-alt1
- Added new type: ipv4-address-range ("192.168.0.1-255", etc.).
- Added new type: ipv4-address-range-list ("192.168.0.1-255
  192.168.1.1-255", etc.).

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 5.3-alt1.qa1
- NMU: applied repocop patch

* Wed Aug 29 2018 Paul Wolneykien <manowar@altlinux.org> 5.3-alt1
- Allow semicolon-separated values for the *-list types.

* Mon Aug 06 2018 Paul Wolneykien <manowar@altlinux.org> 5.2-alt3
- Use late signal-handling initialization to workaround some new
  Guile issues.

* Wed Jul 18 2018 Michael Shigorin <mike@altlinux.org> 5.2-alt2
- support e2kv4 through %e2k macro (grenka@).

* Wed Jul 18 2018 Paul Wolneykien <manowar@altlinux.org> 5.2-alt1
- Added new "hostname-or-ip" and "hostname-or-ip-list" field types.

* Thu Apr 26 2018 Paul Wolneykien <manowar@altlinux.org> 5.1-alt11
- Fix: Check that the system was booted with systemd (closes: #34844).

* Tue Mar 13 2018 Paul Wolneykien <manowar@altlinux.org> 5.1-alt10
- Update libguile-vhttpd dependency: require >= 0.7.8-alt1.

* Tue Jan 16 2018 Paul Wolneykien <manowar@altlinux.org> 5.1-alt9
- Always use UTF-8 for gettext to/from alterator I/O.

* Fri Jan 12 2018 Paul Wolneykien <manowar@altlinux.org> 5.1-alt8
- Use UTF-8 I/O by default for all ports here and then.

* Wed Dec 20 2017 Paul Wolneykien <manowar@altlinux.org> 5.1-alt7
- Use with-fluids* to restore the fluid-values just bofore
  entering the suspended context (patch).

* Mon Dec 18 2017 Paul Wolneykien <manowar@altlinux.org> 5.1-alt6
- Modify the evaluation wrapper: make it skip the (set! a b) result
  value that is undefined (patch).

* Fri Dec 15 2017 Paul Wolneykien <manowar@altlinux.org> 5.1-alt5
- Modify the evaluation wrapper: make it skip the (set! a b) result
  value (that is undefined).

* Thu Dec 07 2017 Paul Wolneykien <manowar@altlinux.org> 5.1-alt4
- Implement call/cc in terms of shift (patch, e2k).

* Mon Dec 04 2017 Paul Wolneykien <manowar@altlinux.org> 5.1-alt3
- Get rid of the circular build dependency on alterator-lookout:
  load its modules at run-time.
- Backport to guile20 for e2k (thx bircoph@).

* Wed Sep 20 2017 Andrey Cherepanov <cas@altlinux.org> 5.1-alt2
- Compile module only if guild is available

* Thu Aug 03 2017 Paul Wolneykien <manowar@altlinux.org> 5.1-alt1
- New functions to work with URI parameters.
- Fix/improve: Don\'t trim the values read from a *.desktop file.

* Mon Jul 17 2017 Paul Wolneykien <manowar@altlinux.org> 5.0-alt5
- Add iface-name and keyword types (with *-list versions).
- Add proc to simplify making of *-list types.
- Fix: allow empty strings for integer and number types.

* Thu Jul 13 2017 Paul Wolneykien <manowar@altlinux.org> 5.0-alt4
- New types: integer, number, ip-proto, mac-address, tcp-port-list.
- Always validate the parameter values against their types.

* Thu Apr 27 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.0-alt3
- do not recompile ui index files

* Tue Apr 18 2017 Ivan Zakharyaschev <imz@altlinux.org> 5.0-alt2
- _IOLBF is deprecated; adapted the buffering mode specification
  for guile > 2

* Fri Mar 31 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.0-alt1
- rebased on guile 2.2

* Thu Nov  3 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.24-alt4
- /usr/sbin/alteratord: Do not delay logging (force line-by-line).
  (Note: stderr goes to our custom log,
  stdout is captured by the system log if run as a service.)

* Thu Mar 13 2014 Mikhail Efremov <sem@altlinux.org> 4.24-alt3
- Fix permissions for /var/run/alteratord/.

* Thu Dec 20 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 4.24-alt2
- change alteratord socket name in alteratord.socket

* Thu Nov 22 2012 Mikhail Efremov <sem@altlinux.org> 4.24-alt1
- Added ip-address and ip-address-list types.
- Added tests for ipv6-* types.
- Added ipv6-address and ipv6-network types.

* Wed Nov 21 2012 Paul Wolneykien <manowar@altlinux.ru> 4.23-alt1
- Require libguile-vhttpd >= 0.7.3.
- Add the systemd unit files. Make systemd to listen on
  /var/run/alteratord/socket.
- Log the way the server was started (either new socket, or an
  existing socket).
- Try systemd-related calls first on init, connect, start and
  stop (closes: 27988).
- Add the systemctl helper script.
- Implement the `sd-listen-fds` call from the systemd API.

* Thu Oct 25 2012 Paul Wolneykien <manowar@altlinux.ru> 4.22-alt2
- Add "Version control" menu section.

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

