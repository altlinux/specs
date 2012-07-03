Name: sisyphus
Version: 0.9.2
Release: alt1

Summary: Helpers for Sisyphus
License: GPL
Group: Development/Other
BuildArch: noarch

Packager: Dmitry V. Levin <ldv@altlinux.org>

Requires: sisyphus_check

Source: %name-%version.tar

%description
This package contains utilities to ease Sisyphus maintainance.

%prep
%setup -q

%install
mkdir -p %buildroot%_sysconfdir/%name
install -p -m644 etc/* %buildroot%_sysconfdir/%name/

mkdir -p %buildroot%_bindir
install -p -m755 bin/* %buildroot%_bindir/

ln -s sisyphus_cleanup_incoming %buildroot%_bindir/incoming_cleanup

%files
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/config
%config %_sysconfdir/%name/functions
%_bindir/*

%changelog
* Mon Mar 10 2008 Alexey Tourbin <at@altlinux.ru> 0.9.2-alt1
- sisyphus_gen_contents: include alternatives-like virtual paths
  into contents_index file (e.g. /usr/bin/xvt -> /usr/bin/xvt)

* Fri Mar 31 2006 Alexey Gladkov <legion@altlinux.ru> 0.9.1-alt3
- Removed migration scripts: sisyphus_migration_hack, sisyphus_update_classic.
- config: Removed unused variables.
- Removed obsolete components:
  base, castle, junior, kernel, master, contrib, non-free.
- sisyphus_unpaired: Renamed --safe-index to --save-index.

* Sun Oct 02 2005 Alexey Gladkov <legion@altlinux.ru> 0.9.1-alt2
- sisyphus_movement: new program.
- sisyphus_cleanup_dups:
  + large reorganization;
  + --component removed;
- functions optimizations.

* Sat Jul 02 2005 Dmitry V. Levin <ldv@altlinux.org> 0.9.1-alt1
- sisyphus_unpaired:
  fixed typo in output file names.
- sisyphus_genhash, sisyphus_prepare:
  handle more hardened file permissions properly.

* Fri Jul 01 2005 Dmitry V. Levin <ldv@altlinux.org> 0.9-alt1
- sisyphus_unpaired: new program.
- sisyphus_cleanup_dups: added options parser.

* Fri Apr 08 2005 Dmitry V. Levin <ldv@altlinux.org> 0.8.2-alt1
- sisyphus_relink: tweaked output format.
- sisyphus_genhash:
  + fixed contents indices generation;
  + moved signing to separate loop;
  + tweaked output format.

* Wed Mar 23 2005 Dmitry V. Levin <ldv@altlinux.org> 0.8.1-alt1
- sisyphus_genhash: do not generate incomplete contents indices.
- sisyphus_cleanup_dups:
  + serialized calculation;
  + handle duplicates on per-arch basis.

* Tue Mar 22 2005 Dmitry V. Levin <ldv@altlinux.org> 0.8.0-alt1
- Migrated to new layout.

* Thu Jun 24 2004 Dmitry V. Levin <ldv@altlinux.org> 0.7.2-alt1
- Moved sisyphus_check to separate subpackage.

* Mon Jun 07 2004 Dmitry V. Levin <ldv@altlinux.org> 0.7.1-alt1
- functions: fixed quiet mode.
- sisyphus_check: added new option: verbose.
- sisyphus_add_new: enabled quiet mode by default.

* Sat Jun 05 2004 Dmitry V. Levin <ldv@altlinux.org> 0.7.0-alt1
- functions: optimized, thanks to legion@.
- functions/check_buildtime: new check.
- functions/check: use it.
- sisyphus_check: added new options:
  quiet, fast-check, show-bad-files.

* Thu May 13 2004 Dmitry V. Levin <ldv@altlinux.org> 0.6.0-alt1
- sisyphus_relink: added support for new style lists.
- functions/{check_summary,check_description}: new checks.
- functions/check: use them.

* Thu Feb 19 2004 Dmitry V. Levin <ldv@altlinux.org> 0.5.6-alt1
- functions/check_changelog: added check for empty changelog text.

* Mon Feb 09 2004 Dmitry V. Levin <ldv@altlinux.org> 0.5.5-alt1
- functions/check_deps:
  + added initscripts to the list of forbidden dependencies.
- functions/check_nvr:
  + new check (for invalid name-version-release).
- functions/check:
  + use it.

* Wed Nov 26 2003 Dmitry V. Levin <ldv@altlinux.org> 0.5.4-alt1
- functions/check_content: new check (forbidden .la files).
- config:
  + define VERSION;
  + added --no-oldhashfile to GENBASEDIR_OPT_ARGS.
- sisyphus_genhash: pass architecture and version to genbasedir.

* Sun Nov 02 2003 Dmitry V. Levin <ldv@altlinux.org> 0.5.3-alt1
- sisyphus_check:
  + new option: --no-check=LIST;
  + better error diagnostics.

* Tue Oct 28 2003 Dmitry V. Levin <ldv@altlinux.org> 0.5.2-alt1
- sisyphus/fhs: new file.
- functions: use it.
- sisyphus_check,sisyphus_add_new: turn into bash script.
- functions/check_gpg: ignore default keyring.
- functions/check*: better error checking.

* Fri Oct 17 2003 Dmitry V. Levin <ldv@altlinux.org> 0.5.1-alt1
- functions/check_changelog: added check for packager format.
- functions,sisyphus_check: added support to skip some checks.
- functions/check*: better error checking.

* Tue Sep 23 2003 Dmitry V. Levin <ldv@altlinux.org> 0.4.10-alt1
- functions/check_deps: added check for invalid dependencies.

* Thu Sep 18 2003 Dmitry V. Levin <ldv@altlinux.org> 0.4.9-alt1
- functions/check_printable: new check.
- functions/check: use it (#932).
- functions/upload_{src,bin}: remove unused functions.
- functions/check*: better error checking.

* Tue Sep 09 2003 Dmitry V. Levin <ldv@altlinux.org> 0.4.8-alt1
- functions/check_buildhost: new check.
- functions/check: use it.

* Wed Aug 20 2003 Dmitry V. Levin <ldv@altlinux.org> 0.4.7-alt1
- sisyphus_gen_contents: new script.
- functions/check_fhs: fixed possible false alarms on empty list.
- functions/check_deps: added to forbidden requires:
  fileutils, sh-utils, textutils.

* Thu Jun 05 2003 Stanislav Ievlev <inger@altlinux.ru> 0.4.6-alt1.1
- sync

* Wed May 14 2003 Dmitry V. Levin <ldv@altlinux.org> 0.4.6-alt1
- sisyphus_check: check deps.

* Tue Apr 29 2003 Dmitry V. Levin <ldv@altlinux.org> 0.4.5-alt1
- sisyphus_check: check permisions in source archive.

* Sat Apr 19 2003 Dmitry V. Levin <ldv@altlinux.org> 0.4.4-alt1
- Updated.

* Wed Feb 19 2003 Stanislav Ievlev <inger@altlinux.ru> 0.4.3-alt1
- sync. new checks (FHS)

* Tue Dec 10 2002 Stanislav Ievlev <inger@altlinux.ru> 0.4.2-alt1
- sync. new relink algo by ldv. unset LC_*

* Mon Oct 21 2002 Stanislav Ievlev <inger@altlinux.ru> 0.4.1-alt5
- sync

* Fri Sep 27 2002 Stanislav Ievlev <inger@altlinux.ru> 0.4.1-alt4
- sync

* Tue Sep 10 2002 Stanislav Ievlev <inger@altlinux.ru> 0.4.1-alt3
- sync with latest changes:
- new utils:
	sisyphus_relink
	sisyphus_add_new

* Tue Aug 13 2002 Stanislav Ievlev <inger@altlinux.ru> 0.4.1-alt2
- rebuild to fix deps

* Mon Aug 12 2002 Stanislav Ievlev <inger@altlinux.ru> 0.4.1-alt1
- sync last changes
- added changelog checking

* Thu Aug 08 2002 Stanislav Ievlev <inger@altlinux.ru> 0.4-alt1
- sync last changes
- added symlink incoming_cleanup to sisyphus_cleanup_incoming
- added automatic package group check, suid/sgid check
- added sisyphus_check utility
- check() moved to functions
- /etc/sisyphus/functions no config(noreplace) now

* Thu Jun 20 2002 Dmitry V. Levin <ldv@altlinux.org> 0.3.1-alt1
- More code cleanup.

* Thu Jun 20 2002 Dmitry V. Levin <ldv@altlinux.org> 0.3-alt1
- Specfile and code cleanup.

* Mon Jun 10 2002 Stanislav Ievlev <inger@altlinux.ru> 0.2-alt1
- added master repository
- added cleanup dups script

* Wed Jun 05 2002 Stanislav Ievlev <inger@altlinux.ru> 0.1-alt1
- Inital release for Sisyphus
