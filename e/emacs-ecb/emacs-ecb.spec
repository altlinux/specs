# -*- coding: utf-8; mode: rpm-spec -*-
# $Id: emacs-ecb.spec,v 1.6 2005/12/14 22:27:41 eugene Exp $

Version: 2.40
Release: alt3.cvs20100518
Name: emacs-ecb
License: GPL
Group: Editors
Url: http://ecb.sf.net
Summary: Emacs Code Browser
Summary(ru_RU.UTF-8): Броузер кода для Emacs

Packager: Emacs Maintainers Team <emacs@packages.altlinux.org>

Requires: emacs-common emacs-elib
Requires: emacs-cedet
Source: ecb-%version.tar.gz
Source1: ecb-emacs.el

# Use correct path to info and html help, NEWS file
Patch1: %name-2.32-doc_path.patch

BuildArch: noarch

BuildPreReq: emacs-X11-program
BuildRequires(build): emacs-cedet >= 1.0-alt0.13.pre7

# Automatically added by buildreq on Mon Nov 01 2004
BuildRequires: emacs-common emacs-elib emacs-jdee

%description
This is code browser for Emacs for C, C++, Java

All Emacs Lisp code is byte-copmpiled, install %name-el for sources.

%description -l ru_RU.UTF-8
ECB представляет собой среду разработки для языков C, C++, Java и других, поддержка
которых имеется в emacs-cedet

Весь код на Emacs Lisp откомпилирован, для получения исходных текстов установите
пакет %name-el

%package el
Summary: The Emacs Lisp sources for bytecode included in %name
Group: Development/Other
Requires: %name = %version-%release

%description el
%name-el contains the Emacs Lisp sources for the bytecode
included in the %name package, that extends the Emacs editor.

You need to install %name-el only if you intend to modify any of the
%name code or see some Lisp examples.

%description el -l ru_RU.UTF-8
Пакет %name-el содержит исходные тексты для пакета %name, который
является дополнением к редактору Emacs.

%name-el необходим вам только, если вы собираетесь изменять файлы
входящие в %name, или хотите посмотреть некоторые примеры.

%prep
%setup -q -n ecb-%version
%patch1 -p1

%build
make LOADPATH="%_emacslispdir/elib" CEDET= all

%install
mkdir -p %buildroot%_emacslispdir/ecb
install -m 644 *.el* %buildroot%_emacslispdir/ecb
cp -R ecb-images %buildroot%_emacslispdir/ecb

mkdir -p %buildroot%_infodir
install -m 644 info-help/* %buildroot%_infodir

mkdir -p %buildroot/etc/emacs/site-start.d
install -m 644 %SOURCE1 %buildroot/etc/emacs/site-start.d/ecb.el
touch %buildroot%_emacslispdir/ecb/ecb-images/.nosearch

mkdir -p %buildroot%_docdir/%name
cp -R html-help %buildroot%_docdir/%name
install -m 644 RELEASE_NOTES %buildroot%_docdir/%name/
install -m 644 README %buildroot%_docdir/%name/
install -m 644 NEWS %buildroot%_docdir/%name/


%files
%doc %_docdir/%name/
%dir %_emacslispdir/ecb/
%_emacslispdir/ecb/*.elc
%_emacslispdir/ecb/ecb-images/
%config(noreplace) /etc/emacs/site-start.d/ecb.el
%_infodir/*

%files el
%_emacslispdir/ecb/*.el


%changelog
* Tue Apr 05 2011 Eugene Vlasov <eugvv@altlinux.ru> 2.40-alt3.cvs20100518
- Rebuild with cedet-1.0

* Tue May 18 2010 Eugene Vlasov <eugvv@altlinux.ru> 2.40-alt2.cvs20100518
- Updated to 20100518 cvs snapshot
- Rebuild with cedet-1.0pre7

* Sun Dec 13 2009 Eugene Vlasov <eugvv@altlinux.ru> 2.40-alt1
- ECB 2.40
- Removed deprecated post/postun install_info/uninstall_info calls
- Cleanup %%__ macro

* Thu Mar 05 2009 Eugene Vlasov <eugvv@altlinux.ru> 2.32-alt5
- Rebuild with cedet-1.0pre6
- Used any emacs-X11 program for build, removed build requires on
  emacs22-X11-athena
- Removed strict requires on emacs-cedet

* Sat Jun 16 2007 Eugene Vlasov <eugvv@altlinux.ru> 2.32-alt4
- Rebuild with cedet-1.0pre4
- Used emacs22-X11 for build
- Strict requires on version of emacs-cedet, used in build environment

* Thu Dec 08 2005 Eugene Vlasov <eugvv@altlinux.ru> 2.32-alt3
- Removed requires on emacs-jdee

* Tue Sep 27 2005 Eugene Vlasov <eugvv@altlinux.ru> 2.32-alt2
- Removed obsolete variable semantic-before-toplevel-bovination-hook
- Corrected default value of path to info, html help, NEWS file
- Modified ECB message dialogs look for emacs22

* Tue Sep 13 2005 Eugene Vlasov <eugvv@altlinux.ru> 2.32-alt1
- New version
- Removed load-path modification from ecb-emacs.el
- Added %_emacslispdir/ecb/ecb-images/.nosearch (#7592)
- Dir %_emacslispdir/ecb now belongs to package

* Mon Nov 01 2004 Ivan Fedorov <ns@altlinux.ru> 2.27-alt1
- New release

* Wed Apr 07 2004 Ott Alex <ott@altlinux.ru> 2.23-alt1
- New release

* Wed Mar 10 2004 Ott Alex <ott@altlinux.ru> 2.22-alt1
- New release, many bugfixes

* Tue Feb 17 2004 Ott Alex <ott@altlinux.ru> 2.21-alt1
- New release

* Tue Feb 03 2004 Ott Alex <ott@altlinux.ru> 2.20-alt1
- New release

* Sat Jan 24 2004 Ott Alex <ott@altlinux.ru> 2.11-alt2
- Fix dependences

* Sat Nov 15 2003 Ott Alex <ott@altlinux.ru> 2.11-alt1
- New release

* Sun Nov 09 2003 Ott Alex <ott@altlinux.ru> 2.01-alt1
- New release
- Rebuild with cedet

* Mon Sep 15 2003 Ott Alex <ott@altlinux.ru> 1.96-alt1
- New release

* Thu Jul 17 2003 Ott Alex <ott@altlinux.ru> 1.95.1-alt1
- New release

* Sat Jul 12 2003 Ott Alex <ott@altlinux.ru> 1.95-alt1
- New version

* Mon Jun 23 2003 Ott Alex <ott@altlinux.ru> 1.94-alt1
- New release

* Sun Apr 27 2003 Alex Ott <ottalex@narod.ru> 1.93-alt1.1
- Fixing spec file

* Mon Mar 31 2003 Ott Alex <ott@altlinux.ru> 1.93-alt1
- 1.93

* Thu Mar 13 2003 Ott Alex <ott@altlinux.ru> 1.92.1-alt2
- Fixing startup file

* Sun Mar 09 2003 Ott Alex <ott@altlinux.ru> 1.92.1-alt1
- New release

* Tue Feb 25 2003 Ott Alex <ott@altlinux.ru> 1.92-alt1
- New release.

* Mon Feb 17 2003 Ott Alex <ott@altlinux.ru> 1.91.1-alt2
- Fixing spec file

* Thu Feb 13 2003 Ott Alex <ott@altlinux.ru> 1.91.1-alt1
- New release. many bugfixes

* Sat Feb 08 2003 Ott Alex <ott@altlinux.ru> 1.90-alt2
- fixing spec

* Fri Feb 07 2003 Ott Alex <ott@altlinux.ru> 1.90-alt1
- New version of package

* Mon Jan 13 2003 Ott Alex <ott@altlinux.ru> 1.80-alt5
- fixinf spec file

* Mon Aug 26 2002 Ott Alex <ott@altlinux.ru> 1.80-alt3
- fixinf spec file

* Thu Aug 22 2002 Ott Alex <ott@altlinux.ru> 1.80-alt2
- Splitting on byte-compiled & source packages

* Wed Aug 14 2002 Ott Alex <ott@altlinux.ru> 1.80-alt1
- New version with many improvments

* Mon Aug 12 2002 Ott Alex <ott@altlinux.ru> 1.70-alt3
- Correcting spec file

* Tue Aug 06 2002 Ott Alex <ott@altlinux.ru> 1.70-alt2
- Adding right Requires to spec

* Thu Jul 18 2002 Ott Alex <ott@altlinux.ru> 1.70-alt1
- Initial build

