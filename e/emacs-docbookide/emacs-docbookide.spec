# -*- coding: utf-8; mode: rpm-spec -*-
# $Id: emacs-docbookide.spec,v 1.1 2005/11/27 20:25:45 eugene Exp $

%define pkg_name docbookide

Version: 0.1
Release: alt5
Name: emacs-%pkg_name
Copyright: GPL
Group: Editors
Url: http://nwalsh.com/emacs/docbookide/
Summary: Docbook IDE for Emacs
Summary(ru_RU.UTF-8): Основной режим для редактирования документов DocBook

Packager: Emacs Maintainers Team <emacs@packages.altlinux.org>

Source: docbookide01.tar.gz
Source1: %pkg_name-emacs.el

BuildArch: noarch
Requires: emacs-common

BuildPreReq: emacs-devel >= 0.0.1-alt2

# Automatically added by buildreq on Thu Aug 05 2002
BuildRequires: emacs-common

%description
This package contains an emacs major mode for editing DocBook documents.

%description -l ru_RU.UTF-8
Данный пакет позволяет эффективно работать с документами с разметкой DocBook
SGML/XML.

%prep
%setup -q -n %pkg_name

%install
%__mkdir_p %buildroot%_emacslispdir/%pkg_name
%__install -m 644 *.el* %buildroot%_emacslispdir/%pkg_name/

%__mkdir_p %buildroot%_emacs_sitestart_dir
%__install -m 644 %SOURCE1 %buildroot%_emacs_sitestart_dir/%pkg_name.el

%add_lisp_loadpath %buildroot%_emacslispdir/%pkg_name
%byte_recompile_lispdir


%files
%doc README 
%dir %_emacslispdir/%pkg_name
%_emacslispdir/%pkg_name/*.el*
%config(noreplace) %_emacs_sitestart_dir/%pkg_name.el

%changelog
* Sun Nov 27 2005 Eugene Vlasov <eugvv@altlinux.ru> 0.1-alt5
- Removed load-path modification
- Fixed Url
- Cleanup spec
- Build with emacs-devel

* Thu Mar 13 2003 Ott Alex <ott@altlinux.ru> 0.1-alt4
- Fixing startup file

* Fri Jan 17 2003 Ott Alex <ott@altlinux.ru> 0.1-alt3
- Fixing spec-file

* Mon Jan 13 2003 Ott Alex <ott@altlinux.ru> 0.1-alt2
- Fixing spec-file

* Wed Dec 25 2002 Ott Alex <ott@altlinux.ru> 0.1-alt1
- Initial build
