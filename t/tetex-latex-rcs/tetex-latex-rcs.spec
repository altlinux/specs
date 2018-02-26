Name: tetex-latex-rcs
Version: 3.1
Release: alt2.1

Group: Publishing
Summary: Tools for inclusion of RCS supplied data in LaTeX documents
URL: http://www.ctan.org/tex-archive/macros/latex/contrib/rcs/
License: GPL

Packager: Ivan Zakharyaschev <imz@altlinux.ru>

BuildArchitectures: noarch
Requires: tetex-latex
# No requirement for rcs, since can be used to process LaTeX files
# checked out from RCS on another system.

Source: ftp://ftp.dante.de/tex-archive/macros/latex/contrib/rcs.tar.gz
# from Debian's rcs-latex-3.0-4 (adapted to 3.1):
Patch: tetex-latex-rcs-3.1-date-babel.patch

%define texmfdir %_datadir/texmf

%define __emacsbin emacs
BuildRequires(build): emacs emacs-mode-auctex

%description
With this LaTeX2e package, you can easily
 -- access values of every RCS field (e.g., revision number) 
 in your LaTeX document;
 -- put the checkin date on the titlepage;
 -- put RCS fields in a footline.

You can typeset revision logs. Not in verbatim -- real LaTeX text!

You can also configure the rcs package easily to do special
things for any keyword.

This bundle for teTeX comes with a user manual, an internal interface
description, full documentation of the implementation, 
and style information for AUC-TeX.

(References:
 RCS -- package: rcs;
 teTeX, LaTeX -- packages: tetex-*;
 AUC-TeX -- package: emacs-mode-auctex.)

%prep
%setup -n rcs
%patch -p0

%build
%__emacsbin -batch \
	-l auctex/latex \
	-f batch-byte-compile rcs.el

# unify & save space:
%__ln_s -f %_licensedir/GPL-2 License

%install
TEXMF="$RPM_BUILD_ROOT"%texmfdir
AUCTEX="$RPM_BUILD_ROOT"%_emacslispdir/auctex
%__mkdir_p \
	"$TEXMF"/tex/latex/misc \
	"$TEXMF"/doc/latex/styles \
	"$AUCTEX"/style
%make install TEXMF="$TEXMF" AUCTEX="$AUCTEX"
%__install -m0644 rcs.elc "$AUCTEX"/style/

%files 
%doc CATALOG History README
%doc --no-dereference License
%texmfdir/tex/latex/misc/*
%doc %texmfdir/doc/latex/styles/*
%_emacslispdir/auctex/style/*

%changelog
* Thu Nov 05 2009 Repocop Q. A. Robot <repocop@altlinux.org> 3.1-alt2.1
- NMU (by repocop): the following fixes applied:
  * altlinux-policy-tex-obsolete-util-calls-in-post for tetex-latex-rcs

* Mon May 10 2004 Ivan Zakharyaschev <imz@altlinux.ru> 3.1-alt2
- declare %texmfdir/doc/latex/styles/* as %%doc.

* Fri May  7 2004 Ivan Zakharyaschev <imz@altlinux.ru> 3.1-alt1
- initial release for ALT Sisyphus;
- used a patch from Debian to honor babel when typesetting dates;
- compile rcs.el (AUCTeX module).
