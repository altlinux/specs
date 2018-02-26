# -*- coding: utf-8; mode: rpm-spec -*-
# $Id: emacs-tiny-tools.spec,v 1.14 2006/03/02 14:59:20 eugene Exp $

%define cvs_version 20060302
%define pkg_name tiny-tools

Version: 1.0.%cvs_version
Release: alt1
Name: emacs-%pkg_name
License: GPL
Group: Editors
Url: http://%pkg_name.sourceforge.net/
Summary: %pkg_name package for Emacs
Summary(ru_RU.UTF-8): пакет %pkg_name для Emacs

Packager: Emacs Maintainers Team <emacs@packages.altlinux.org>

Requires: emacs-common emacsen-startscripts

Source: %pkg_name-%cvs_version.tar.bz2
Source1: %pkg_name.el

Patch0: %pkg_name-cl-macs_noext.patch

BuildArch: noarch

BuildPreReq: emacs-devel >= 0.0.1-alt2

# Automatically added by buildreq on Sat Jun 25 2005
BuildRequires: emacs-bbdb emacs-cedet emacs-gnus emacs-prog-modes emacs-w3 emacs-common emacs-leim enscript ghostscript-classic mpage openssl xorg-x11-locales

%description
Emacs Tiny Tools is a collection of libraries and packages, which are
designed to be OS and X/Emacs platform independent. E.g. configure load-path
automatically, URL handler, easy-delete, mail complete and many more.

%description -l ru_RU.UTF-8
Tiny-tools -- набор библиотек и пакетов, которые спроектированы таким
образом, чтобы быть независимыми от операционных систем и версий
Emacs. Например, автоматически настраиваются пути загрузки, обработчики URL
и многие другие возможности.


%prep
%setup -q -n %pkg_name
%patch0 -p1


%install
%__mkdir_p %buildroot%_emacslispdir/%pkg_name/rc
%__mkdir_p %buildroot%_emacslispdir/%pkg_name/tiny
%__mkdir_p %buildroot%_emacslispdir/%pkg_name/other
%__install -m 644 lisp/other/*.el* %buildroot%_emacslispdir/%pkg_name/other/
%__install -m 644 lisp/tiny/*.el* %buildroot%_emacslispdir/%pkg_name/tiny/
#install -m 644 rc/*.el* %buildroot%_emacslispdir/tiny-tools/rc/

%__mkdir_p %buildroot%_docdir/%name/html/pic
%__mkdir_p %buildroot%_docdir/%name/txt
%__install -m 644 doc/html/*.html %buildroot%_docdir/%name/html/
%__install -m 644 doc/html/pic/*.jpg %buildroot%_docdir/%name/html/pic/
%__install -m 644 doc/txt/*.txt %buildroot%_docdir/%name/txt/
%__install -m 644 lisp/ChangeLog %buildroot%_docdir/%name/
%__gzip -f -9 %buildroot%_docdir/%name/ChangeLog

%__mkdir_p %buildroot%_docdir/%name/contrib
%__install -m 644 bin/*.pl %buildroot%_docdir/%name/contrib/
%__install -m 644 bin/admin.bashrc %buildroot%_docdir/%name/contrib/
%__install -m 644 bin/*.pl %buildroot%_docdir/%name/contrib/

%__mkdir_p %buildroot%_emacs_sitestart_dir
%__install -m 644 %SOURCE1 %buildroot%_emacs_sitestart_dir/tiny-tools.el

%add_lisp_loadpath %buildroot%_emacslispdir/%pkg_name/tiny
%add_lisp_loadpath %buildroot%_emacslispdir/%pkg_name/other
%bc_dir_with_site %buildroot%_emacslispdir/%pkg_name/tiny
%byte_recompile_dir %buildroot%_emacslispdir/%pkg_name/other

%__rm -f %buildroot%_emacslispdir/%pkg_name/tiny/tinylib-ad.elc


%files
%doc %_docdir/%name/
%dir %_emacslispdir/%pkg_name/
%dir %_emacslispdir/%pkg_name/rc
%dir %_emacslispdir/%pkg_name/other
%dir %_emacslispdir/%pkg_name/tiny
%_emacslispdir/%pkg_name/tiny/*.el*
#%_emacslispdir/tiny-tools/rc/*.el*
%_emacslispdir/%pkg_name/other/*.el*
%_emacs_sitestart_dir/*


%changelog
* Thu Mar 02 2006 Eugene Vlasov <eugvv@altlinux.ru> 1.0.20060302-alt1
- New snapshot
- Fixed BuildRequires

* Mon Nov 07 2005 Eugene Vlasov <eugvv@altlinux.ru> 1.0.20051101-alt1
- New snapshot
- Removed load-path modification from tiny-tools.el
- Build with emacs-devel

* Sat Sep 10 2005 Eugene Vlasov <eugvv@altlinux.ru> 1.0.20050908-alt1
- New snapshot
- Added more config samples to tiny-tools.el
- Fixed BuildRequires

* Sat Jun 25 2005 Eugene Vlasov <eugvv@altlinux.ru> 1.0.20050625-alt1
- New snapshot
- Fixed load cl-macs (#7197)
- Fixed tiny-tools.el

* Tue Apr 13 2004 Ott Alex <ott@altlinux.ru> 1.0.20040413-alt1
- New snapshot, many additions

* Sat Apr 03 2004 Ott Alex <ott@altlinux.ru> 1.0.20040402-alt1
- New snapshot, many additions

* Wed Nov 26 2003 Ott Alex <ott@altlinux.ru> 1.0.20031126-alt1
- New snapshot

* Wed Nov 19 2003 Ott Alex <ott@altlinux.ru> 1.0.20031119-alt1
- New snapshot

* Sun Oct 26 2003 Ott Alex <ott@altlinux.ru> 1.0.20031026-alt1
- New snapshot

* Sat Oct 11 2003 Ott Alex <ott@altlinux.ru> 1.0.20031010-alt1
- New snapshot

* Sun Sep 21 2003 Ott Alex <ott@altlinux.ru> 1.0.20030919-alt1
- New snapshot

* Mon Sep 15 2003 Ott Alex <ott@altlinux.ru> 1.0.20030915-alt1
- New snapshot

* Thu Aug 07 2003 Ott Alex <ott@altlinux.ru> 1.0.200306807-alt1
- New snapshot

* Sun Jun 22 2003 Ott Alex <ott@altlinux.ru> 1.0.20030622-alt1
- New snapshot

* Sat Jun 07 2003 Ott Alex <ott@altlinux.ru> 1.0.20030607-alt1
- New snapshot and cleaning spec file

* Sat Feb 08 2003 Ott Alex <ott@altlinux.ru> 1.0.20030207-alt1
- Fixing spec

* Mon Nov 18 2002 Ott Alex <ott@altlinux.ru> 1.0.20021118-alt1
- Initial build for ALTLinux

