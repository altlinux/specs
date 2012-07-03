Name: alternatives
Version: 0.4.4
Release: alt1

Summary: alternatives support
License: GPLv2+
Group: System/Base
Url: http://alternatives.sourceforge.net
BuildArch: noarch

Source: %name-%version.tar

# for filetrigger
Requires: grep

Requires: getopt mktemp

Provides: %_sysconfdir/%name/packages.d
Provides: lib%name = %version, lib%name-devel = %version, lib%name-devel-static = %version
Obsoletes: lib%name, lib%name-devel, lib%name-devel-static

#utilities that use alternatives
Conflicts: gcc-common <= 1.4.3-alt1, gnupg2 <= 1.9.7-alt2

# due to PackagedFiles()
BuildPreReq: rpm >= 4.0.4-alt87

# due to verioned paths
Conflicts: rpm-build < 4.0.4-alt93

BuildPreReq: libshell help2man
Requires: rpm-macros-%name = %version-%release

%description
Alternatives subsystem. This package contains common utilites for it.

%package -n rpm-macros-%name
Summary: Set of RPM macros for packaging %name-based applications
Group: Development/Other
Conflicts: alternatives < 0.4

%description -n rpm-macros-%name
Set of RPM macros for packaging %name-based applications for ALT Linux.
Install this package if you want to create RPM packages that use %name.

%prep
%setup -n %name-%version

%build
%install
mkdir -p $RPM_BUILD_ROOT%_sysconfdir/%name/{auto,packages.d,links}
touch $RPM_BUILD_ROOT%_sysconfdir/%name/manual
%makeinstall

mkdir -p $RPM_BUILD_ROOT%_sysconfdir/rpm/macros.d
cat >$RPM_BUILD_ROOT%_sysconfdir/rpm/macros.d/%name<<EOF
%%_altdir %%([ ! -f %_datadir/%name/functions ])%_sysconfdir/%name/packages.d
%%force_update_alternatives [ -x %_sbindir/%name-update ] && %_sbindir/%name-update ||:

%%register_alternatives  %%{warning %%%%register_alternatives is obsolete}%_sbindir/%name-helper --install
%%reg_alts %%register_alternatives
%%post_register_alternatives %%register_alternatives
%%post_reg_alts %%post_register_alternatives

%%unregister_alternatives %%{warning %%%%unregister_alternatives is obsolete}[ "\$1" = 0 ] || exit 0; [ -x %_sbindir/%name-helper ] && %_sbindir/%name-helper --remove
%%unreg_alts %%unregister_alternatives
%%preun_unregister_alternatives %%unregister_alternatives
%%preun_unreg_alts %%preun_unregister_alternatives

%%unregister_alternatives_always %%{warning %%%%register_alternatives_always is obsolete}[ -x %_sbindir/%name-helper ] && %_sbindir/%name-helper --remove
%%unreg_alts_always %%unregister_alternatives_always

%%update_alternatives() %%{warning %%%%update_alternatives is obsolete}[ -x %_sbindir/%name-update ] && %_sbindir/%name-update %%* ||: %%nil
%%update_alts %%update_alternatives
%%post_update_alternatives %%update_alternatives
%%post_update_alts %%update_alternatives

%%remove_alternatives %%{warning %%%%remove_alternatives is obsolete}[ "\$1" = 0 ] || exit 0; [ -x %_sbindir/%name-update ] && %_sbindir/%name-update --ignore
%%remove_alts %%remove_alternatives
%%preun_remove_alternatives %%remove_alternatives
%%preun_remove_alts %%preun_remove_alternatives
EOF

install -pD -m755 alternatives.prov %buildroot%_rpmlibdir/alternatives.prov
install -pD -m755 alternatives.prov.files %buildroot%_rpmlibdir/alternatives.prov.files
install -pD -m755 alternatives.filetrigger %buildroot%_rpmlibdir/alternatives.filetrigger

%files
%doc README TODO
%dir %_sysconfdir/%name
%dir %_sysconfdir/%name/auto
%dir %_sysconfdir/%name/links
%dir %_sysconfdir/%name/packages.d
%ghost %config(noreplace,missingok) %_sysconfdir/%name/manual
%_bindir/*
%_sbindir/*
%_datadir/%name
%_man1dir/*
%_rpmlibdir/alternatives.prov
%_rpmlibdir/alternatives.prov.files
%_rpmlibdir/alternatives.filetrigger
%exclude %_sysconfdir/rpm/macros.d/*

%files -n rpm-macros-%name
%_sysconfdir/rpm/macros.d/*

%changelog
* Sun May 29 2011 Michael Shigorin <mike@altlinux.org> 0.4.4-alt1
- alternatives-update: double-check link target before removing it
  (closes: #25621) (led@)

* Tue Apr 12 2011 Dmitry V. Levin <ldv@altlinux.org> 0.4.3-alt1
- alternatives-update: fixed join usage.

* Sat Jun 20 2009 Alexey Tourbin <at@altlinux.ru> 0.4.2-alt1
- removed %%post script, updated filetrigger

* Tue May 05 2009 Alexey Tourbin <at@altlinux.ru> 0.4.1-alt2
- packaged /etc/alternatives/manual

* Tue May 05 2009 Alexey Tourbin <at@altlinux.ru> 0.4.1-alt1
- alternatives.prov: provide /usr/share/man/* and /usr/share/info/* as well

* Tue Mar 31 2009 Stanislav Ievlev <inger@altlinux.org> 0.4-alt5
- remove infinite loop on errors

* Fri Nov 28 2008 Stanislav Ievlev <inger@altlinux.org> 0.4-alt4
- rpm-macros-alternatives: add conflicts to old alternatives

* Thu Nov 27 2008 Stanislav Ievlev <inger@altlinux.org> 0.4-alt3
- alternatives update: fix manual alternatives check

* Tue Nov 25 2008 Stanislav Ievlev <inger@altlinux.org> 0.4-alt2
- add force_update_alternatives macro (Igor Vlasenko)

* Fri Nov 21 2008 Stanislav Ievlev <inger@altlinux.org> 0.4-alt1
- use libshell

* Thu Nov 20 2008 Stanislav Ievlev <inger@altlinux.org> 0.3.5-alt1
- move rpm macros to separated package (Igor Vlasenko)
- add filetrigger

* Fri Nov 07 2008 Dmitry V. Levin <ldv@altlinux.org> 0.3.4-alt1
- alternatives-{update,upgrade}: Fixed mktemp error handling.
- alternatives.prov: Provide versioned paths with weight (Alexey Tourbin).

* Sun Mar 30 2008 Alexey Tourbin <at@altlinux.ru> 0.3.3-alt1
- alternatives.prov: check that alternative target is actually
  packaged in the same package, not just exists

* Thu Nov 22 2007 Alexey Tourbin <at@altlinux.ru> 0.3.2-alt1
- alternatives.prov: provide every alternative path except for
  /usr/share/man/* and /usr/share/info/*, not just /usr/bin/*
  and /usr/sbin/*; also improved validation and diagnostics

* Sat Aug 11 2007 Alexey Tourbin <at@altlinux.ru> 0.3.1-alt1
- added alternatives.prov and alternatives.prov.files, for new rpm-build

* Thu Feb 01 2007 Stanislav Ievlev <inger@altlinux.org> 0.3-alt1
- remove obsolete alternatives-config script

* Thu Oct 20 2005 Stanislav Ievlev <inger@altlinux.org> 0.2.0-alt4
- added requires to getopt and mktemp (#8223 and #7514)

* Fri Jul 01 2005 Alexey Gladkov <legion@altlinux.ru> 0.2.0-alt3
- alternative-list quoting bugfix

* Fri Jun 17 2005 Stanislav Ievlev <inger@altlinux.org> 0.2.0-alt2
- fixes from legion

* Fri Jun 10 2005 Stanislav Ievlev <inger@altlinux.org> 0.2.0-alt1
- fixed bug in alternatives-manual (#7020)

* Thu May 12 2005 Stanislav Ievlev <inger@altlinux.org> 0.2.0-alt0.13
- fixed old hack for buildreq in macros (#5888)

* Thu Nov 18 2004 Stanislav Ievlev <inger@altlinux.org> 0.2.0-alt0.12
- improvements in alternatives-helper

* Thu Oct 14 2004 Stanislav Ievlev <inger@altlinux.org> 0.2.0-alt0.11
- more warnings about non writeable manual file
- allow multiple space symbols in config files

* Fri Oct 08 2004 Stanislav Ievlev <inger@altlinux.org> 0.2.0-alt0.10
- rc3 (minor changes in non ALT utils)

* Wed Sep 22 2004 Stanislav Ievlev <inger@altlinux.org> 0.2.0-alt0.9.3
- replace subst with ed, added first version of alternatives-display script

* Tue Sep 21 2004 Stanislav Ievlev <inger@altlinux.org> 0.2.0-alt0.9.2
- increase portability

* Tue Sep 21 2004 Stanislav Ievlev <inger@altlinux.org> 0.2.0-alt0.9.1
- use sed in more portable way

* Thu Aug 19 2004 Stanislav Ievlev <inger@altlinux.org> 0.2.0-alt0.9
- enable validator, enable warnings about old format

* Fri Aug 13 2004 Dmitry V. Levin <ldv@altlinux.org> 0.2.0-alt0.8.1
- Fixed %%post script.

* Fri Aug 13 2004 Stanislav Ievlev <inger@altlinux.org> 0.2.0-alt0.8
- conflicts with old gcc-common
- made configs readable

* Thu Aug 12 2004 Stanislav Ievlev <inger@altlinux.org> 0.2.0-alt0.7
- goto Sisyphus

* Wed Aug 04 2004 Stanislav Ievlev <inger@altlinux.org> 0.2.0-alt0.6
- second Deadalus release:
    - added validate utility
    - remove extra debug messages

* Thu Jun 17 2004 Stanislav Ievlev <inger@altlinux.org> 0.2.0-alt0.5
- first Daedalus release

* Fri Jun 11 2004 Stanislav Ievlev <inger@altlinux.org> 0.2.0-alt0.4
- changed ':' instead of tabs in config
- speed up update algorithm (use join)

* Thu Jun 10 2004 Stanislav Ievlev <inger@altlinux.org> 0.2.0-alt0.3
- added specs for testsuite from previous version, little optimization in update

* Thu Jun 10 2004 Stanislav Ievlev <inger@altlinux.org> 0.2.0-alt0.2
- fix upgrade script: also convert dump.xml to manual, remove old symlinks

* Wed Jun 09 2004 Stanislav Ievlev <inger@altlinux.org> 0.2.0-alt0.1
- rewrite in shell and awk

* Thu Jun 26 2003 Stanislav Ievlev <inger@altlinux.ru> 0.1.0-alt1
- 0.1.0
- more documentation
- minor bugfixes, code improvements

* Mon Jun 09 2003 Stanislav Ievlev <inger@altlinux.ru> 0.0.7-alt2
- added provides for /etc/alternatives/ packages.d
- don't make test by default

* Mon May 05 2003 Stanislav Ievlev <inger@altlinux.ru> 0.0.7-alt1
- next release

* Tue Apr 08 2003 Stanislav Ievlev <inger@altlinux.ru> 0.0.6-alt1
- minor features, bugfuxes

* Fri Mar 28 2003 Stanislav Ievlev <inger@altlinux.ru> 0.0.5-alt3
- trigger fix

* Thu Mar 27 2003 Stanislav Ievlev <inger@altlinux.ru> 0.0.5-alt2
- fix memory leak
- added more tests

* Wed Mar 26 2003 Stanislav Ievlev <inger@altlinux.ru> 0.0.5-alt1
- removed some dups in code, no manual dir now

* Tue Mar 25 2003 Stanislav Ievlev <inger@altlinux.ru> 0.0.4-alt6
- added RPM macros variants with post/preun suffixes
- check nested slaves support
- '-D' option for alternatives-list
- negative tests ready: make check available

* Mon Mar 24 2003 Stanislav Ievlev <inger@altlinux.ru> 0.0.4-alt5
- added testcase for various bad configs

* Fri Mar 21 2003 Stanislav Ievlev <inger@altlinux.ru> 0.0.4-alt4
- ignore now ignore slaves too

* Fri Mar 21 2003 Stanislav Ievlev <inger@altlinux.ru> 0.0.4-alt3
- fix update logic from alternatived programs to non-alternatived
  (added %%unregister_alternatives_always macro for it)
- made %%update_alternatives,
       %%remove_altenatives
       %%unregister_altenatives
  macros more friendly for nonexistent update-alternatives file
- added requires to latest libing (was changes in format config)
- more testcase

* Thu Mar 20 2003 Stanislav Ievlev <inger@altlinux.ru> 0.0.4-alt2
- fix alternatives_link creation during update

* Wed Mar 19 2003 Stanislav Ievlev <inger@altlinux.ru> 0.0.4-alt1
- now alternatives-list works under user

* Mon Mar 17 2003 Stanislav Ievlev <inger@altlinux.ru> 0.0.3-alt4.M2
- fix update from non-alternatived programs

* Sat Mar 15 2003 Stanislav Ievlev <inger@altlinux.org> 0.0.3-alt3.M2
- little improvements again

* Sat Mar 15 2003 Stanislav Ievlev <inger@altlinux.org> 0.0.3-alt2.M2
- fix latest improvements

* Fri Mar 14 2003 Stanislav Ievlev <inger@altlinux.ru> 0.0.3-alt1.M2
- some fixes and improvements

* Wed Mar 12 2003 Stanislav Ievlev <inger@altlinux.ru> 0.0.2-alt6.M2
- rebuild with lates libing
- added short variants to rpm macros
- added hack for macros to auto buildreq
- repeat update until we have no changes (helps in some ugly cases)

* Tue Mar 11 2003 Stanislav Ievlev <inger@altlinux.ru> 0.0.2-alt5.M2
- fix removing old slave links

* Fri Mar 07 2003 Stanislav Ievlev <inger@altlinux.ru> 0.0.2-alt4.M2
- alternatives --install fixes
- work only with existent files
- change macros names
- more testcase
- fix dump file usage
- little code improvements(friend classes,use default processing)

* Thu Mar 06 2003 Stanislav Ievlev <inger@altlinux.ru> 0.0.2-alt3.M2
- M2: daedalus release
- testcase and samples included

* Thu Mar 06 2003 Stanislav Ievlev <inger@altlinux.ru> 0.0.2-alt2.M2
- alternatives-setup, M2, RC1

* Wed Mar 05 2003 Stanislav Ievlev <inger@altlinux.ru> 0.0.2-alt1.M2
- alternatives-update, pre-M2

* Fri Feb 28 2003 Stanislav Ievlev <inger@altlinux.ru> 0.0.1-alt2.M1
- fix ldconfig usage according packaging policy
- minor internal fixes

* Fri Feb 21 2003 Stanislav Ievlev <inger@altlinux.ru> 0.0.1-alt1.M1
- second daedalus release:
   move some code into shared library (preparation for M2 - second utility)
   added lockfile support
   added migration info into README

* Wed Feb 05 2003 Stanislav Ievlev <inger@altlinux.ru> 0.0.0-alt2.M1
- daedalus release

* Tue Feb 04 2003 Stanislav Ievlev <inger@altlinux.ru> 0.0.0-alt1.M1
- fix map usage

* Mon Feb 03 2003 Stanislav Ievlev <inger@altlinux.ru> 0.0.0-alt0.M1
- Initial release, with some demo stuff
