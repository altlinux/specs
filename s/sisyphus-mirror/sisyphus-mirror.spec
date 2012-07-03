Name: sisyphus-mirror
Version: 0.8.2
Release: alt1

Summary: a simple script for mirroring Sisyphus/Master/updates/etc via rsync
License: GPL
Group: Communications

BuildArch: noarch

Source0: %name-%version.tar

Requires: rsync >= 3.0.2-alt0.2.M40.1

%description
This is a simple script for mirroring Sisyphus/Master/updates/etc via rsync.
You may run it via cron.

%prep
%setup

%install

install -d -m0755 %buildroot%_sysconfdir/%name
install -d -m0755 %buildroot%_bindir

install -m0755 %name %buildroot%_bindir
install -m0644 %name.conf %buildroot%_sysconfdir/%name
install -m0644 exclude %buildroot%_sysconfdir/%name
install -m0644 include %buildroot%_sysconfdir/%name

%files
%_bindir/*
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/*
%doc AUTHORS README.UTF8

%changelog
* Mon Nov 16 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 0.8.2-alt1
- Speed up stage of $mirror movement from temp dir to main dir.
- Use shell-getopt.
- Update messages style.
- sisyphus-mirror.spec: require rsync >= 3.0.2-alt0.2.M40.1.

* Fri Nov 28 2008 Vladimir V. Kamarzin <vvk@altlinux.org> 0.8.1-alt1
- Fix user-wide config inclusion (reported by Andrey Rahmatullin)
- Add '-v' to default rsync options

* Fri Nov 21 2008 Vladimir V. Kamarzin <vvk@altlinux.org> 0.8-alt1
+ Incompatible changes:
  + Do not add "rsync-" prefix to logfile names
  + Rewrite config file inclusion (see README.UTF8)
- New features:
  + Add ability to synchronize only specified architectures
  + New command-line options:
    + -u|--url
    + -L|--logdir
    + -a|--arch
- Update default rsync options:
  + add -h in interactive mode
  + use --delete-delay instead of --delete-after
  + add -m (--prune-empty-dirs)
  + add --delete-excluded
  + remove -P from options for non-interactive mode
  + --partial-dir is always used now
- Rewrite signal handling
- Rewrite "already running" check
- Do not mail log to someone, just print warning to stdout. Good enough for
  non-interactive mode, not needed in interactive
- Do not write date to logfile in interactive mode
- Relocate pidfile from $RSHOME to $TMPDIR
- Update README.UTF8

* Thu May 29 2008 Vladimir V Kamarzin <vvk@altlinux.ru> 0.7.2-alt1
- New version:
 + sisyphus-mirror: fixed regression introduced in 0.7-alt1-2-g14a3138 - added
   check for BACKUP_DIR in --link-dest calculation (Reported by Andrey
   Rahmatullin)

* Wed May 28 2008 Vladimir V Kamarzin <vvk@altlinux.ru> 0.7.1-alt1
- New version:
  + sisyphus-mirror: pass only 20 '--link-dest' args to rsync
  + sisyphus-mirror: check that we have $timestamp_file before backing up
    (Closes: #15754)
  + sisyphus-mirror.conf: modify default rsync options - do not pass '-c'
    (Closes: #15295)
  + sisyphus-mirror.conf: reorder config parameters (Closes: #15749)

* Mon Apr 21 2008 Vladimir V Kamarzin <vvk@altlinux.ru> 0.6-alt1
- Corrected --link-dest calculation (Closes: #15359)

* Fri Apr 18 2008 Vladimir V Kamarzin <vvk@altlinux.ru> 0.5-alt1
- New version:
  + Implemented command-line options support
  + Implemented 2 types of backup - previous-state and snapshots
  + Implemented atomic synchronization (see README.UTF8)
  + Implemented overriding of repos LIST from command-line
  + Display colored information messages when mirroring in interactive mode
  + Do not allow multiple runs, better pidfile handling
  + Better default options for rsync (Closes: #15295)
  + Do not use symlinks(1) anymore
  + Rewrite documentation (README.UTF8)
  + Implemented features from other scripts (Closes: #14765)
  + Fixed bug in documentation (Closes: #15294)
  + Reduce traffic and disk-space usage (Closes: #15359)
  + Big code rewrite

* Tue Aug 29 2006 Vladimir V Kamarzin <vvk@altlinux.ru> 0.4-alt1
- More reasonable "lockfile exists" diagnostic (Closes: #9924)

* Tue May 02 2006 Vladimir V Kamarzin <vvk@altlinux.ru> 0.3-alt1
- New version:
  + Added support for multi-level repositories (thanks to Vadim Kononenko)
  + Implemented interactive mode

* Thu Jan 12 2006 Vladimir V Kamarzin <vvk@altlinux.ru> 0.2.1-alt2
- Added Packager tag
- Minor spec update
- Updated default config

* Tue Jan 10 2006 Vladimir V Kamarzin <vvk@altlinux.ru> 0.2.1-alt1
- New version:
  + Fixed multi-repos syncing bug
  + Added variable RSYNC_PROXY

* Wed Aug 24 2005 Vladimir V Kamarzin <vvk@altlinux.ru> 0.2-alt1
- New version:
  + Quote some variables
  + Default $MAINTAINER changed to root@localhost
  + Added variable PARTIAL in config (for rsync option --partial-dir)
  + Added README.KOI8-R

* Sat Aug 20 2005 Vladimir V Kamarzin <vvk@altlinux.ru> 0.1-alt1
- Initial build for Sisyphus
