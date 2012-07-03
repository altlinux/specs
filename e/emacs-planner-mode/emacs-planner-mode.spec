# -*- coding: utf-8; mode: rpm-spec -*-
# $Id: emacs-planner-mode.spec,v 1.3 2006/05/30 09:50:28 eugene Exp $

%define mode_name planner

Version: 3.41
Release: alt2
Name: emacs-%mode_name-mode
License: GPL
Group: Editors
Url: http://wjsullivan.net/PlannerMode
Summary: Planner mode for Emacs
Requires: emacs-common emacs-misc-modes emacs-muse-mode

Packager: Emacs Maintainers Team <emacs@packages.altlinux.org>

Source: http://download.gna.org/planner-el/%mode_name-%version.tar.gz
Source1: %mode_name.el

Patch0: %name-3.41-fix-quoting.patch

BuildArch: noarch

BuildPreReq: emacs-misc-modes >= 0.2-alt3
BuildPreReq: emacs-devel >= 0.0.1-alt2
BuildPreReq: emacs-muse-mode emacs-w3m emacs-bbdb emacs-erc emacs-gnus

%description
Planner is a Personal Information Manager (PIM) by John Wiegley. You can
use it to manage your tasks, schedule, notes, and anything else you want
to store in a free-text richly-hyperlinked personal information manager
integrated into Emacs. Because it's in Emacs, it can easily be tweaked to
support your particular way of planning, and it can draw upon the data
and functions you already have in Emacs.

%prep
%setup -q -n %mode_name-%version
%patch0 -p1

%build
cp contrib/schedule.el .
%__subst -p s,string-to-int,string-to-number,g schedule.el
%__make PREFIX=%prefix

%install
%__mkdir_p %buildroot%_emacslispdir/%mode_name
%__install -m 644 *.el* %buildroot%_emacslispdir/%mode_name

%__mkdir_p %buildroot%_infodir
%__install -m 644 *.info* %buildroot%_infodir/

%__mkdir_p %buildroot%_emacs_sitestart_dir
%__install -m 644 %SOURCE1 %buildroot%_emacs_sitestart_dir/%mode_name.el

%add_lisp_loadpath %buildroot%_emacslispdir/%mode_name
%byte_recompile_lispdir

# gzip -f -9 ChangeLog*

%files
%doc AUTHORS COMMENTARY NEWS README
%_infodir/*
%dir %_emacslispdir/%mode_name
%_emacslispdir/%mode_name/*.el*
%config(noreplace) %_emacs_sitestart_dir/*


%changelog
* Sat Oct 24 2009 Igor Vlasenko <viy@altlinux.ru> 3.41-alt2
- applied repocop patch: removed obsolete (un)install_info macros

* Mon Jan 01 2007 Eugene Vlasov <eugvv@altlinux.ru> 3.41-alt1
- New version
- Fixed quoting bug with recent emacs22 builds
- Don't pack Changelog*
- Fixed Url

* Tue May 30 2006 Eugene Vlasov <eugvv@altlinux.ru> 3.40-alt1
- New version, Muse mode based
- Updated requires and build requires

* Sat Feb 04 2006 Eugene Vlasov <eugvv@altlinux.ru> 1.0-alt0.1.20050820
- Initial build for Sisyphus

