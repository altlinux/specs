# -*- coding: utf-8; mode: rpm-spec -*-
# $Id: $

%define pkg_name elscreen

Version: 1.3.2
Release: alt0.2
Name: emacs-%pkg_name
Copyright: GPL
Group: Editors
Url: ftp://ftp.morishima.net/pub/morishima.net/naoto/ElScreen
Summary: ElScreen -- Screen Manager for Emacs with tabs
Summary(ru_RU.UTF-8): вкладки для Emacs со screen-подобной навигацией

Packager: Emacs Maintainers Team <emacs@packages.altlinux.org>

Source: ftp://ftp.morishima.net/pub/morishima.net/naoto/ElScreen/%{pkg_name}-%version.tar.gz
Patch: elscreen-1.3.2-add-autoload.patch
Patch1: elscreen-1.3.2-alt-color.patch

BuildArch: noarch
Requires: emacs-common emacs-apel

BuildPreReq: emacs-devel >= 0.0.1-alt2

BuildRequires: emacs-common emacs-apel

%description
It is an Emacs utility with which you can have multiple screens
(window-configuration) on your GNU Emacs as well as GNU screen on
terminal.
.
If you use emacs-lisp applications which have many windows (like
Gnus, irchat, Wanderlust, Mew...), ElScreen makes it easy to
switch to a different screen, with its configuration unchanged.
You can also create and kill screen, jump to them, rename the
screen, and so on.
.
Enable it with
M-x elscreen-mode


%description -l ru_RU.UTF-8
Поддержка вкладок (tabs) для Emacs
со screen-подобной системой навигации между ними.
.
Enable it with
M-x elscreen-mode

%prep
%setup -q -n %pkg_name-%version
%patch -p0
%patch1 -p0

%install
%__mkdir_p %buildroot%_emacslispdir/
%__install -m 644 *.el* %buildroot%_emacslispdir/

%__mkdir_p %buildroot%_emacs_sitestart_dir
#%__install -m 644 %%SOURCE1 %buildroot%_emacs_sitestart_dir/%pkg_name.el

cat > %buildroot%_emacs_sitestart_dir/%pkg_name.el <<EOF
;; %name-%version-%release 
(autoload 'elscreen-mode "elscreen" "Mode with ElScreen -- Screen Manager for Emacs with tabs." t)
EOF

%byte_recompile_lispdir

%files
%doc README ChangeLog
%_emacslispdir/*.el*
%config(noreplace) %_emacs_sitestart_dir/%pkg_name.el

%changelog
* Sun Dec 04 2005 Igor Vlasenko <viy@altlinux.ru> 1.3.2-alt0.2
- code is cleaned up: Insted of just starting elscreen 
  it provides elscreen-mode.
- first build for ALT Linux
