%define pkg_name sml-mode
Version: 3.9.5
Release: alt7
Name: emacs-%pkg_name
License: GPL
Group: Editors
Url: ftp://ftp.research.bell-labs.com/dist/smlnj/contrib/emacs/
Summary: Standard ML mode for Emacs
Summary(ru_RU.KOI8-R): Основной режим Emacs для работы со Standard ML
Packager: Emacs Maintainers Team <emacs@packages.altlinux.org>

Source: ftp://ftp.research.bell-labs.com/dist/smlnj/contrib/emacs/%pkg_name-%version.tar.gz
Source1: sml-mode-emacs.el

BuildArch: noarch
Requires: emacs-common

BuildPreReq: emacs-devel >= 0.0.1-alt2
# Automatically added by buildreq on Thu Aug 05 2002
BuildRequires: emacs-common

%description
This package contains an emacs major mode for editing Standard ML source code.

%description -l ru_RU.KOI8-R
Данный пакет предоставляет основной режим для редактирования исходного
текста программ на языке Standard ML.

%prep
%setup -n %pkg_name-%version

%build
make prefix=%prefix

%install
mkdir -p %buildroot%_emacslispdir/%pkg_name/
install -m 644 *.el* %buildroot%_emacslispdir/%pkg_name/

mkdir -p %buildroot%_infodir
install -m 644 %pkg_name.info %buildroot%_infodir

mkdir -p %buildroot%_sysconfdir/emacs/site-start.d
install -m 644 %SOURCE1 %buildroot%_sysconfdir/emacs/site-start.d/%pkg_name.el

%add_lisp_loadpath %buildroot%_emacslispdir/%pkg_name
%byte_recompile_lispdir

%files
%doc README ChangeLog BUGS INSTALL NEWS TODO testcases.sml
%dir %_emacslispdir/%pkg_name/
%_emacslispdir/%pkg_name/*.el*
%_infodir/*
%_sysconfdir/emacs/site-start.d/*

%changelog
* Sat Oct 24 2009 Igor Vlasenko <viy@altlinux.ru> 3.9.5-alt7
- applied repocop patch: removed obsolete (un)install_info macros

* Thu Jan 12 2006 Igor Vlasenko <viy@altlinux.ru> 3.9.5-alt6
- now maintained by Emacs Maintainers Team
- spec cleanup; added elc compilation

* Sat Dec 13 2003 Ott Alex <ott@altlinux.ru> 3.9.5-alt5
- rebuild

* Mon Sep 29 2003 Ott Alex <ott@altlinux.ru> 3.9.5-alt4
- Fixing URL 
- cleanup spec

* Sat Feb 08 2003 Ott Alex <ott@altlinux.ru> 3.9.5-alt3
- fixing spec

* Wed Dec 25 2002 Ott Alex <ott@altlinux.ru> 3.9.5-alt1
- Initial build
