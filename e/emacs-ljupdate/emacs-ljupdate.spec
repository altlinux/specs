# -*- coding: utf-8; mode: rpm-spec -*-
# $Id: emacs-ljupdate.spec,v 1.1 2005/11/12 20:35:07 eugene Exp $

%define pkg_name ljupdate
%define snapshot 20050624

Version: 3.9
Release: alt0.1.%snapshot
Name: emacs-%pkg_name
License: GPL
Group: Editors
Url: http://edward.oconnor.cx/%pkg_name/
Summary: Emacs LiveJournal client
Summary(ru_RU.UTF-8): Клиент Emacs для LiveJournal
Requires: emacs-common emacs-w3

Packager: Emacs Maintainers Team <emacs@packages.altlinux.org>

Source: %pkg_name.tar.gz
Source1: %pkg_name-site-start.el
Source2: http-cookies.el
Source3: http-get.el
Source4: http-post.el

# Patch: %pkg_name-utf.diff

BuildArch: noarch

BuildPreReq: emacs-devel >= 0.0.1-alt2

# Automatically added by buildreq Mon Sep 09 2002
BuildRequires: emacs-common emacs-w3 emacs-bbdb

%description
%pkg_name is a client for LiveJournal


%package el
Summary: The Emacs Lisp sources for bytecode included in %name
Group: Development/Other
Requires: %name = %version-%release

%description el
%name-el contains the Emacs Lisp sources for the bytecode
included in the %name package, that extends the Emacs editor.

You need to install %name-el only if you intend to modify any of the
%name code or see some Lisp examples.


%prep
%setup -q -n %pkg_name
# %patch -p1


%build
echo "nothing todo"

%install
%__mkdir_p %buildroot%_emacslispdir/%pkg_name
%__install -m 644 *.el* %buildroot%_emacslispdir/%pkg_name
%__install -m 644 %SOURCE2 %buildroot%_emacslispdir/%pkg_name
%__install -m 644 %SOURCE3 %buildroot%_emacslispdir/%pkg_name
%__install -m 644 %SOURCE4 %buildroot%_emacslispdir/%pkg_name

# %__mkdir_p %buildroot%_infodir
# %__install -m 644 info/*.info* %buildroot%_infodir

%__mkdir_p %buildroot%_emacs_sitestart_dir
%__install -m 644 %SOURCE1 %buildroot%_emacs_sitestart_dir/%pkg_name.el

%add_lisp_loadpath %buildroot%_emacslispdir/%pkg_name
%byte_recompile_lispdir


# %post
# %install_info ljupdate.info

# %preun
# %uninstall_info ljupdate.info


%files
%doc README
# %doc CONTRIBUTORS ChangeLog DEV-NOTES HISTORY TODO
%dir %_emacslispdir/%pkg_name
%_emacslispdir/%pkg_name/*.elc
%config(noreplace) %_emacs_sitestart_dir/*
# %_infodir/*

%files el
%_emacslispdir/%pkg_name/*.el


%changelog
* Sat Nov 12 2005 Eugene Vlasov <eugvv@altlinux.ru> 3.9-alt0.1.20050624
- Development snapshot
- Fixed URL
- Removed utf-8 patch
- Removed load-path modification
- Fixed requires
- Build with emacs-devel
- Byte-compile elisp files
- Build separate el package

* Sat Feb 21 2004 Ott Alex <ott@altlinux.ru> 3.3-alt1
- First build for ALTLinux
- add patch for utf-8 send

