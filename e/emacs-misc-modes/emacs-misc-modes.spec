# -*- coding: utf-8; mode: rpm-spec -*-
# $Id: emacs-misc-modes.spec,v 1.8 2006/02/04 17:54:06 eugene Exp $

Version: 0.2
Release: alt10.5
Name: emacs-misc-modes
License: GPL
Group: Editors
Summary: Various packages for Emacs
Summary(ru_RU.UTF-8): Дополнительные пакеты для Emacs
Requires: emacs-common

Packager: Emacs Maintainers Team <emacs@packages.altlinux.org>

Source: %name.tar.gz

BuildArch: noarch

BuildRequires: emacs-devel >= 0.0.1-alt2
BuildRequires: emacs-nox

# Automatically added by buildreq on Tue Dec 24 2002
BuildRequires: emacs-cedet emacs-gnus
BuildRequires: makeinfo

%description
Various packages for Emacs.

%description -l ru_RU.UTF-8
Дополнительные пакеты Emacs для самых разных задач.

%prep
%setup -n %name

%install
mkdir -p %buildroot%_emacslispdir/
install -m 644 *.el* %buildroot%_emacslispdir/
mkdir -p %buildroot%_infodir/
install -m 644 *.info* %buildroot%_infodir/
%byte_recompile_lispdir

%files
%_emacslispdir/*.el*
%_infodir/*

%changelog
* Fri Dec 01 2023 Igor Vlasenko <viy@altlinux.org> 0.2-alt10.5
- NMU: fixed build

* Mon May 17 2021 Slava Aseev <ptrnine@altlinux.org> 0.2-alt10.4
- NMU: dropped emacs-bbdb (was removed in #268867)

* Fri Feb 22 2019 Dmitry V. Levin <ldv@altlinux.org> 0.2-alt10.3
- NMU: dropped obsolete emacs-elib.

* Sat Dec  1 2018 Terechkov Evgenii <evg@altlinux.org> 0.2-alt10.2
- Rebuild with emacs26-X11-athena

* Thu Dec 03 2015 Igor Vlasenko <viy@altlinux.ru> 0.2-alt10.1.1
- NMU: added BR: texinfo

* Sat Nov 24 2012 Terechkov Evgenii <evg@altlinux.org> 0.2-alt10.1
- Rebuild by emacs-X11 instead of emacs-nox

* Wed Nov 21 2012 Terechkov Evgenii <evg@altlinux.org> 0.2-alt10
- Requires to w3 removed

* Tue Feb 23 2010 Terechkov Evgenii <evg@altlinux.ru> 0.2-alt9
- Removed password.el

* Sat Oct 24 2009 Igor Vlasenko <viy@altlinux.ru> 0.2-alt8
- applied repocop patch: removed obsolete (un)install_info macros

* Tue Mar 11 2008 Eugene Vlasov <eugvv@altlinux.ru> 0.2-alt7
- Removed w3m-session

* Mon Nov 05 2007 Eugene Vlasov <eugvv@altlinux.ru> 0.2-alt6
- Added password.el
- Updated ascii, blank-mode, csv, highline, icicles, icicles-menu,
  spell-number, sys, xray

* Tue Dec 12 2006 Eugene Vlasov <eugvv@altlinux.ru> 0.2-alt5
- Fixed autosmiley.el compilation

* Sat Dec 09 2006 Eugene Vlasov <eugvv@altlinux.ru> 0.2-alt4
- Added autosmiley.el and osd.el (#10376)
- Updated apache-mode, bbdbpalm, bm, dirtree, dupwords, htmlize,
  icicles, icicles-menu, minibuffer-complete-cycle, remember
- fortune-util replaced by fortune
- color-theme moved to separate package
- Used emacs22-X11 for build (function mouse-choose-completion not defined
  in emacs22-nox)

* Sat Feb 04 2006 Eugene Vlasov <eugvv@altlinux.ru> 0.2-alt3
- emacs-wiki and planner moved to separate packages
- Updated bm, csv, eperiodic, htmlize, icicles
- Fixed bookmark-menu, lynx, organizer-mode
- Added all, cgi, httpd, mutt-alias, muttrc-mode
- Removed basis-utils, cua-mode, icalendar, image-mode, ljcheckf,
  newsticker, org, wotd
- Build with emacs-devel
- Fixed BuildRequires

* Wed Jan 11 2006 Eugene Vlasov <eugvv@altlinux.ru> 0.2-alt2
- Fixed color-theme for emacs-21.4 (#8537)

* Fri Oct 07 2005 Eugene Vlasov <eugvv@altlinux.ru> 0.2-alt1
- Updated bbdbpalm, bm, boxquote, browse-kill-ring, color-theme, dirtree,
  ell, escreen, eval-expr, fff, ftelnet, highline, htmlize, icalendar,
  mcomplete, minibuffer-complete-cycle, mp3play, newsticker, pb-popup,
  revbufs, rfcview, session, spell-number, ssh, u-appt, xml-rpc,
  xrdb-mode
- Added emacs-wiki, icicles, icicles-menu, mp3player, mp3player-scores
- Replaced planner.el with real elisp code (#6073)
- Removed fnexpand, iso-acc, ljupdate, rtf-support, safescrollmouse,
  vvb-mode, whitespace-mode, wmanip, xpm-mode, xterm

* Thu May 06 2004 Ott Alex <ott@altlinux.ru> 0.1-alt10
- Added new packages

* Thu May 06 2004 Ott Alex <ott@altlinux.ru> 0.1-alt9
- Remove modules, that are now in emhacks

* Wed May 05 2004 Ott Alex <ott@altlinux.ru> 0.1-alt8
- add iman and mcomplete

* Sun Nov 30 2003 Ott Alex <ott@altlinux.ru> 0.1-alt7
- New snapshot

* Sun Oct 26 2003 Ott Alex <ott@altlinux.ru> 0.1-alt5
- Adding new packages

* Tue Sep 23 2003 Ott Alex <ott@altlinux.ru> 0.1-alt4
- New snapshot

* Mon Jan 13 2003 Ott Alex <ott@altlinux.ru> 0.1-alt3
- Adding new packages

* Tue Dec 31 2002 Ott Alex <ott@altlinux.ru> 0.1-alt2
- Remove conflicting template.el from archive

* Tue Dec 24 2002 Ott Alex <ott@altlinux.ru> 0.1-alt1
- Initial build
