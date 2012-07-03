Version: 2.2
Release: alt9.1.qa1
Name: emacs-xslt-process
License: GPL
Group: Editors
Url: http://xslt-process.sourceforge.net/
Summary: Emacs XSLT Process Minor Mode
Summary(ru_RU.KOI8-R): Вспомогательный режим для работы с XSLT в Emacs
Requires: emacs-X11 emacs-speedbar emacs-elib
Source: xslt-process-%version.tar.gz
Source1: xslt-process-emacs.el
Patch: xslt-process.diff

BuildArch: noarch

# Automatically added by buildreq Mon Sep 09 2002
BuildRequires: emacs-X11 emacs-cedet emacs-elib ImageMagick texinfo tetex-latex tetex-afm tetex-core tetex-dvips java-devel java-common bc update-alternatives
Requires: emacs-X11 emacs-cedet emacs-elib java java-common

%description
XSLT-process is a minor mode for XEmacs or GNU Emacs which transforms
it into a powerful XML editor with XSLT processing and debugging
capabilities.

%description -l ru_RU.KOI8-R
XSLT-process является вспомогательным режимом для XEmacs или GNU Emacs, который
делает их мощными XML редакторами с возможностью отладки и работы с XSLT.

%prep
%setup -n xslt-process-%version
%patch -p1

%build
make EMACS=emacs LOADPATH="%_emacslispdir/elib %_emacslispdir/cedet/common %_emacslispdir/cedet/speedbar" all

%install
mkdir -p %buildroot%_emacslispdir/xslt-process/java
install -m 644 lisp/*.el %buildroot%_emacslispdir/xslt-process
install -m 644 java/*.jar %buildroot%_emacslispdir/xslt-process/java

mkdir -p %buildroot%_infodir
install -m 644 doc/*.info* %buildroot%_infodir

mkdir -p %buildroot/etc/emacs/site-start.d
install -m 644 %SOURCE1 %buildroot/etc/emacs/site-start.d/xslt-process.el

%files
%doc ChangeLog README doc/xslt-process.html doc/*.png doc/*.gif doc/xslt-process.pdf doc/xslt-process.ps
%_emacslispdir/xslt-process/*.el
%_emacslispdir/xslt-process/java/*
%config(noreplace) /etc/emacs/site-start.d/*
%_infodir/*

%changelog
* Wed Dec 02 2009 Igor Vlasenko <viy@altlinux.ru> 2.2-alt9.1.qa1
- NMU (by repocop): the following fixes applied:
  * obsolete-call-in-post-install-info for emacs-xslt-process
  * altlinux-java-obsolete-requires for emacs-xslt-process
  * postclean-05-filetriggers for spec file

* Thu Mar 24 2005 Sviatoslav Sviridov <svd@altlinux.ru> 2.2-alt9.1
- Get rid of dependency on j2se1.4-blackdown, using j2se instead

* Sun May 09 2004 Ott Alex <ott@altlinux.ru> 2.2-alt9
- Fix identify changes

* Sat Dec 13 2003 Ott Alex <ott@altlinux.ru> 2.2-alt8
- Rebuild with bugfix

* Sat Nov 15 2003 Ott Alex <ott@altlinux.ru> 2.2-alt7
- fixing spec

* Mon Sep 22 2003 Ott Alex <ott@altlinux.ru> 2.2-alt6
- fixing dependencies

* Sat Mar 22 2003 Ott Alex <ott@altlinux.ru> 2.2-alt5
- fixing java requires

* Sat Feb 08 2003 Ott Alex <ott@altlinux.ru> 2.2-alt4
- fixing spec

* Mon Jan 13 2003 Ott Alex <ott@altlinux.ru> 2.2-alt2
- New version of package

* Mon Sep 09 2002 Ott Alex <ott@altlinux.ru> 2.1-alt1
- Initial build

