Version: 5.12
%define snap 20100721
Release: alt4.%snap
Name: emacs-ilisp
License: Custom, see COPYING
Group: Editors
Summary: ILisp mode for Common Lisp development with Emacs
Packager: Emacs Maintainers Team <emacs@packages.altlinux.org>
Requires: emacs-common
Url: http://ilisp.sourceforge.net

Source: ILISP-%snap.tar
Source1: emacs-ilisp-site-start.el
Patch: emacs22-ILISP-alt.patch
Patch1: emacs-ilisp-remove-emacs18-compatibility-alt.patch
Patch2: emacs-ilisp-set-default-emacs21-alt.patch
BuildArch: noarch

# Automatically added by buildreq on Wed Mar 10 2004
BuildRequires: emacs tetex-dvips tetex-latex tcsh

%description
ILISP is a powerful GNU Emacs interface to many dialects of Lisp, including
Lucid, Allegro, Xanalys/Harlequin LispWorks, GCL, KCL, AKCL, ECL, IBCL, and
CMUCL.  Also some Scheme implementations are supported as well as a
preliminary version of Xlisp/XlispStat.

%prep
%setup -q -n ILISP
%patch -p1
%patch1 -p1
%patch2 -p1
rm ilfsf18.el comint-v18.el

%build
make EMACS=emacs
cd docs
make ps info html
gzip ilisp.ps
gzip ilisp-refcard.ps
cd ..


%install
mkdir -p %buildroot/%_emacslispdir/ilisp/extra
install -m 644 pictures/ilisp-icon.* %buildroot/%_emacslispdir/ilisp/
install -m 644 *.el* %buildroot/%_emacslispdir/ilisp/
install -m 644 extra/*.el* %buildroot/%_emacslispdir/ilisp/extra/
install -m 644 *.lisp %buildroot/%_emacslispdir/ilisp/
install -m 644 *.scm %buildroot/%_emacslispdir/ilisp/
mkdir -p %buildroot/%_sysconfdir/emacs/site-start.d
install -m 644 %SOURCE1 %buildroot/%_sysconfdir/emacs/site-start.d/ilisp.el
mkdir -p %buildroot/%_infodir
install -m 644 docs/*.info %buildroot/%_infodir/

%files
%doc HISTORY GETTING-ILISP ACKNOWLEDGMENTS COPYING INSTALLATION Welcome README
%doc ilisp.emacs ChangeLog docs/doc-changes.txt docs/*.ps.gz docs/ilisp.html
%_emacslispdir/*
%_infodir/*
%_sysconfdir/emacs/site-start.d/*

%changelog
* Wed Jul 21 2010 Igor Vlasenko <viy@altlinux.org> 5.12-alt4.20100721
- updated CVS snapshot; fixed build (emacs 23 not recognized)

* Wed Dec 02 2009 Igor Vlasenko <viy@altlinux.ru> 5.12-alt3.20060325.qa1
- NMU (by repocop): the following fixes applied:
  * obsolete-call-in-post-install-info for emacs-ilisp
  * postclean-05-filetriggers for spec file

* Sat Mar 25 2006 Igor Vlasenko <viy@altlinux.ru> 5.12-alt3.20060325
- updated CVS snapshot;
- fixed build for emacs22.

* Mon May 03 2004 Ott Alex <ott@altlinux.ru> 5.12-alt2.20040430
- CVS snapshot with many improvements

* Wed Apr 14 2004 Ott Alex <ott@altlinux.ru> 5.12-alt2
- Rewrite startup script

* Wed Mar 10 2004 Ott Alex <ott@altlinux.ru> 5.12-alt1
- Initial build for altlinux

