# -*- coding: utf-8; mode: rpm-spec -*-
# $Id: emacs-base.spec,v 1.10 2006/05/03 08:50:57 eugene Exp $

Name: emacs-base
Version: 0.0.7
Release: alt1

Group: Editors
Summary: Common site start scripts for GNU Emacs
License: GPL

Packager: Emacs Maintainers Team <emacs@packages.altlinux.org>

BuildArch: noarch

Provides: %_sysconfdir/emacs/site-start.d
Provides: %_emacslispdir
Provides: %_datadir/emacs
Provides: %_datadir/emacs/etc
Provides: emacsen-startscripts
Obsoletes: emacsen-startscripts

Conflicts: rootfiles <= alt-alt4
# from now on xemacs has its own start-scripts
Conflicts: xemacs < 21.4.9
# pc-select.el is updated:
Conflicts: emacs-common < 21.3-alt6
Conflicts: emacs21-common < 21.3-alt6

# Mdk's and ALT's global config merged:
Source0: %name-ALT-%version.tar
Source1: %name.buildreq

%description
The common site start scripts for Emacsen contain the default
configuration for Emacsen suggetsted by ALT. It also implements a
mechanism for installing additional Emacs Lisp modules at the site
and making them visible for users. Administrators can add some scripts
of their own to customize Emacsen even more.

The start scripts are itnended to be excuted by GNU Emacs, so some
of them contain Emacsen specific parts (embraced by special macros).
This package is always installed if you install any of the Emacsen.

The idea of compatibility with XEmacs has been dropped, XEmacs has its own
configuration.

%prep
%setup -q -n emacs

%install
mkdir -p %buildroot%_sysconfdir/emacs/site-start.d
install -m 644 site-start.el %buildroot%_sysconfdir/emacs
install -m 644 site-start.d/* %buildroot%_sysconfdir/emacs/site-start.d

# Buildreq filter for emacs.
install -pD -m644 %SOURCE1 %buildroot%_sysconfdir/buildreqs/files/ignore.d/%name

mkdir -p %buildroot%_emacslispdir
mkdir -p %buildroot%_datadir/emacs/etc

%files
%dir %_sysconfdir/emacs
%dir %_sysconfdir/emacs/site-start.d
%config(noreplace) %_sysconfdir/emacs/site-start.el
%config(noreplace) %_sysconfdir/emacs/site-start.d/*.el
%dir %_datadir/emacs
%dir %_datadir/emacs/etc
%dir %_emacslispdir

%config %_sysconfdir/buildreqs/files/ignore.d/*

%doc doc/inhibit-site-start.txt
%lang(ru) %doc doc/inhibit-site-start.ru.txt

# TODO:
# 1. Добавить check-shadows?

%changelog
* Sat Sep 29 2007 Eugene Vlasov <eugvv@altlinux.ru> 0.0.7-alt1
- Removed 00auto-compr.el, 10fontlock.el, 10frames.el, 
  10more-cyrillic.el
- Modified GNUEmacs macro for work with all version emacs
- Removed next-line-add-newlines, mouse-wheel-follow-mouse, 
  pc-select-selection-keys-only variables value modification
- Fixed flyspell-mode-noerr function
- Removed key bindings for \C-d, \M-O H, \M-O F
- Removed hack for repair C-s when change XKB's group switch
- Removed mouse wheel initialization, mouse-wheel-mode turned on by default
- Cleaned up spec, removed %%__ macro

* Wed May 03 2006 Eugene Vlasov <eugvv@altlinux.ru> 0.0.6-alt1
- Fixed load xterm-mouse-mode
- Removed mode-line color modification for text terminals
- Dropped loading of obsolete auto-show library
- M-g is now prefix key, removed M-g binding to goto-line (use M-g g instead)

* Sat Oct 22 2005 Eugene Vlasov <eugvv@altlinux.ru> 0.0.5-alt2
- el-pkgutils moved to emacs-devel
- Added dir %_datadir/emacs/etc
- Removed dir %_libdir/emacs
- Added GNUEmacs21 and GNUEmacs22 macro
- Simplify and cleanup spec

* Fri Oct 21 2005 Igor Vlasenko <viy@altlinux.ru> 0.0.5-alt1
- patches merged in source
- fixed el-pkgutils to pretend to work
- x86_64, lib64 friendly: el-pkgutils moved to datadir

* Thu Sep 22 2005 Eugene Vlasov <eugvv@altlinux.ru> 0.0.4-alt5
- Removed font-lock faces modification

* Sat Sep 17 2005 Eugene Vlasov <eugvv@altlinux.ru> 0.0.4-alt4
- Modified GNUEmacs macro for work with emacs 22 too
- Really fix #6841

* Thu Sep 15 2005 Igor Vlasenko <viy@altlinux.ru> 0.0.4-alt3
- fixed bug #6841 (syntax error)

* Thu May 06 2004 Ott Alex <ott@altlinux.ru> 0.0.4-alt2
- Fix bug #2490 with XKB's groups and C-s

* Sat Jan 10 2004 Ott Alex <ott@altlinux.ru> 0.0.4-alt1
- Move pkgtools from emacs-21.x

* Wed Dec 17 2003 Ott Alex <ott@altlinux.ru> 0.0.3-alt5
- Provides /usr/share/emacs

* Sun Nov 30 2003 Ott Alex <ott@altlinux.ru> 0.0.3-alt4
- Reorganize package to use as site-lisp holders
- Rename to emacs-base

* Tue Sep 16 2003 Ott Alex <ott@altlinux.ru> 0.0.3-alt3
- Provides site-start.d dir

* Thu Feb 20 2003 Ivan Zakharyaschev <imz@altlinux.ru> 0.0.3-alt2
- drop /root/.emacs: it is said to violate FHS 2.2 (perhaps, it will be moved
  back to rootfiles pkg).

* Mon Jan 13 2003 Ivan Zakharyaschev <imz@altlinux.ru> 0.0.3-alt1
- 00macros.el: added some means of avoiding loading too match in batch mode
  (e.g., when compiling el-files; partially fixes No. 0001503): 
  + added {Interactive,Batch}-launch;
  + {X,TTY}launch: eval only if Emacs has been launched interactively;
- 00auto-compr.el: turn auto(de)compression on -- moved from 
  10initial-features;
- 10initial-features: eval only if launched interactively -- this will avoid
  the dependency on ispell when building other pkgs using emacs;

* Mon Nov 18 2002 Ivan Zakharyaschev <imz@altlinux.ru> 0.0.2-alt1
- site-start.el: make possible for users to override it as a whole, or
  each part from site-start.d/ -- more info in docs (Sergey Vlasov 
  <vsu at altlinux.ru>; a move to default.el is our future);
- 10selection.el, 10mouse.el: reflect the changes in emacs-21.2-alt11,
  pc-select should no more conflict with traditional selection keys;

* Mon Nov 11 2002 Stanislav Ievlev <inger@altlinux.ru> 0.0.1-alt4
- rebuild

* Fri Apr 13 2002 Ivan Zakharyaschev <imz@altlinux.ru> 0.0.1-alt3
- provide /root/.emacs instead of rootfiles
  (based on skel.ru_RU.KOI8-R/.emacs with a lot
  of features turned off) - fixes \#808 at bugs.altlinux.ru;

* Thu Feb 28 2002 Ivan Zakharyaschev <imz@altlinux.ru> 0.0.1-alt2
- buildreq-ignore: add the main script /etc/emacs/site-start.el
  because we don't want this pkg to appear in dependencies.

* Thu Feb 28 2002 Ivan Zakharyaschev <imz@altlinux.ru> 0.0.1-alt1
- initial version (0.0.1): extracted from emacs-common-21.1-alt11
  (taken the scripts and the pattern for buildreq);
- fix a typo in /etc/emacs/site-start.d/10mouse.el.

# Local Variables:
# compile-command: "rpmbuild -ba emacs-base.spec"
# End:
