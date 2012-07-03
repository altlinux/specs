# -*- coding: utf-8; mode: rpm-spec -*-
# $Id: emacs-template.spec,v 1.1 2005/10/04 18:54:55 eugene Exp $

Version: 3.1c
Release: alt1
Name: emacs-template
Copyright: GPL
Group: Editors
Url: http://emacs-template.sourceforge.net/
Summary: Template package for Emacs

Packager: Emacs Maintainers Team <emacs@packages.altlinux.org>

Source: template-%version.tar.gz
Source1: template-emacs.el

BuildArch: noarch
Requires: emacs-common

# Automatically added by buildreq on Thu Aug 05 2002
BuildRequires: emacs-common


%description
When you create a new file with Emacs, package Template supplies an initial
buffer content via a template: a file with normal text and expansion
forms. There is a menu to easily create such templates. You can also use new
commands to decorate comments and update the buffer contents.


%prep
%setup -q -n template

%build
cd lisp
for i in *.el ; do
        emacs -batch --eval "(progn
        (setq load-path (append (list \".\")  load-path))
        (byte-compile-file \"$i\"))"
done
cd ..

%install
%__mkdir_p %buildroot%_emacslispdir/
%__install -m 644 lisp/*.el* %buildroot%_emacslispdir/

%__mkdir_p %buildroot%_datadir/emacs/etc/template/
%__install -m 644 templates/*.tpl* %buildroot%_datadir/emacs/etc/template/

%__mkdir_p %buildroot%_sysconfdir/emacs/site-start.d
%__install -m 644 %SOURCE1 %buildroot%_sysconfdir/emacs/site-start.d/template.el

%files
%doc README INSTALL
%_emacslispdir/*.el*
%dir %_datadir/emacs/etc/template/
%_datadir/emacs/etc/template/*
%_sysconfdir/emacs/site-start.d/*

%changelog
* Tue Oct 04 2005 Eugene Vlasov <eugvv@altlinux.ru> 3.1c-alt1
- New version
- Cleanup spec
- Removed russian translation in summary and description

* Sat Feb 08 2003 Ott Alex <ott@altlinux.ru> 3.1a-alt3
- fixing spec

* Wed Dec 25 2002 Ott Alex <ott@altlinux.ru> 3.1a-alt1
- Initial build
