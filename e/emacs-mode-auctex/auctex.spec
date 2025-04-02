%def_without texmf
%define ModeName auctex

Name: emacs-mode-%ModeName
Version: 13.3
Release: alt2.2

Summary: Enhanced LaTeX mode for GNU Emacs
License: GPLv3
Group: Editors
Url: http://www.gnu.org/software/auctex/index.html
Packager: Emacs Maintainers Team <emacs@packages.altlinux.org>
BuildArch: noarch

#Source0: ftp://sunsite.auc.dk/packages/auctex/%ModeName-%version.tar.bz2
Source0: ftp://ftp.gnu.org/pub/gnu/auctex/%ModeName-%version.tar.gz

# Due to patches 1 and 2, the administrator of a system won't have to set
# any site-specific variables for AUC TeX.

Requires: common-licenses
%if_with texmf
Requires: texmf-latex-preview
%else
Requires: tex(preview.sty)
%endif

Provides: preview-latex
Provides: emacs-preview-latex = %version-%release
Obsoletes: emacs-preview-latex < 11.82
Obsoletes: auctex

Requires: gnu-ghostscript /usr/bin/dvips /usr/bin/latex

BuildRequires(pre): rpm-build-tex
BuildRequires: texlive-dist
BuildRequires: /usr/bin/emacs /usr/bin/dvips /usr/bin/latex

%description
AUC TeX is a comprehensive, customizable, integrated environment for
writing, editing and processing input files for LaTeX using GNU Emacs.
This mode also supports graphic preview for formulas and figures.

(Emacs Lisp code is principally byte-compiled, install %name-el for sources.)

%package el
Summary: The Emacs Lisp sources for bytecode included in %name
Group: Development/Other

Requires: %name = %version-%release
Provides: emacs-preview-latex-el = %version-%release

%description el
%name-el contains the Emacs Lisp sources for the bytecode included in the %name package,
that extends the Emacs editor.

You need to install %name-el only if you intend to modify any of the
%name code or see some Lisp examples.

#FIXME: fix install to texlive
%package doc
Summary: 	Documentation for %name
Group: 		Editors

Requires: emacs-mode-auctex 
Requires: /usr/share/texmf/doc

%description -n emacs-mode-auctex-doc
Does your neck hurt from turning between previewer windows and the
source too often? This Elisp/LaTeX package will render your displayed
LaTeX equations right into the editing window where they belong. 

This package contains the documentation.

%package -n texmf-latex-preview
Summary: Preview style for TeX subsystems.
Group: Development/Other
BuildArch: noarch

%description -n texmf-latex-preview
%name-el contains the Emacs Lisp sources for the bytecode included in the %name package,
that extends the Emacs editor.

You need to install %name-el only if you intend to modify any of the
%name code or see some Lisp examples.

%prep
%setup -q -n %ModeName-%version

%build
%configure --with-tex-input-dirs=/usr/share/texmf/tex \
           --with-auctexstartfile=%_datadir/emacs/site-lisp/auctex.el \
           --with-previewstartfile=%_datadir/emacs/site-lisp/preview-latex.el
%make_build 

%install
%makeinstall_std

ln -s -f %_licensedir/GPL-2 COPYING
rm -f %buildroot%_infodir/dir

# Create these .nosearch files to keep the directories from the elisp search path
touch %buildroot%_emacslispdir/auctex/style/.nosearch

%global _customdocdir %_defaultdocdir/auctex

%files
%_infodir/*
%_emacslispdir/*.el
%_emacslispdir/auctex
%_datadir/texmf/tex/latex/preview
%exclude %_texmfmain/tex/latex/preview/preview.sty
%exclude %_emacslispdir/auctex/*.el
%exclude %_emacslispdir/auctex/style/*.el
%_emacslispdir/auctex/style/.nosearch

%files el 
%_emacslispdir/auctex/*.el
%_emacslispdir/auctex/style/*.el

%files -n %name-doc
%_datadir/texmf/doc/latex/styles/*
%_datadir/doc/auctex
%doc --no-dereference COPYING
%doc ChangeLog*

%if_with texmf
%files -n texmf-latex-preview
%_texmfmain/tex/latex/preview/preview.sty
%endif

%changelog
* Wed Apr 02 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 13.3-alt2.2
- FTBFS fixed

* Wed Jan 22 2025 Ivan A. Melnikov <iv@altlinux.org> 13.3-alt2.1
- NMU: update emacs_version macro to match emacs 30
  extension installation path (fixes FTBFS)

* Mon Apr 15 2024 Ilya Mashkin <oddity@altlinux.ru> 13.3-alt2
- use emacs_version macro

* Mon Apr 15 2024 Ilya Mashkin <oddity@altlinux.ru> 13.3-alt1
- 13.3

* Wed Mar 30 2022 Ilya Mashkin <oddity@altlinux.ru> 13.1-alt1
- add BR emacs-common rpm-build-emacs to fix FTBFS
- skip patches
- Update License tag

* Fri Feb 22 2019 Dmitry V. Levin <ldv@altlinux.org> 11.87-alt3
- NMU: updated build dependencies.

* Tue Mar 06 2018 Igor Vlasenko <viy@altlinux.ru> 11.87-alt2
- fixed build
- build with rpm-build-tex

* Thu Jan 24 2013 Kirill Maslinsky <kirill@altlinux.org> 11.87-alt1
- 11.87
- drop auctex-11.86-biber.patch, biber support is now upstream
- adapt printerlist patch

* Wed Nov 02 2011 Kirill Maslinsky <kirill@altlinux.org> 11.86-alt1
- 11.86
- drop auctex-11.85-use-system-pdf-viewer.patch
  (see https://bugzilla.altlinux.org/show_bug.cgi?id=19236#c4 for comment)
- add support for biblatex-biber
  (based on auctex-biber.zip distributed along with biber)

* Fri Feb 05 2010 Igor Vlasenko <viy@altlinux.ru> 11.85-alt5
- explicit TexLive dependencies changed to /usr/bin/{dvips,latex}

* Sat Jan 30 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 11.85-alt4.1
- Extracted preview.sty into separate package (ALT #22807)

* Mon Oct 26 2009 Igor Vlasenko <viy@altlinux.ru> 11.85-alt4
- TeXLive friendly BuildRequires.
- cleaned obsolete calls from %%post

* Sat May 02 2009 Alexander Borovsky <partizan@altlinux.ru> 11.85-alt3
- Fixed #19236 (used xdg-open instead of xpdf)

* Sun Mar 15 2009 Alexander Borovsky <partizan@altlinux.ru> 11.85-alt2
- Fixed #19072
- Merged emacs-mode-auctex and emacs-latex-preview packages
- Fixed dependencies: emacs-mode-auctex now can be installed with texlive

* Mon Feb 18 2008 Alexander Borovsky <partizan@altlinux.ru> 11.85-alt1
- Updated to 11.85
- Russian match patch reverted. Now for input f.e. \varepsilon you should type `v e

* Tue Mar 20 2007 Alexander Borovsky <partizan@altlinux.ru> 11.84-alt1
- New version

* Tue Sep 26 2006 Alexander Borovsky <partizan@altlinux.ru> 11.83-alt2
- Fixed update from old auctex + latex-preview
 
* Thu Feb 16 2006 Alexander Borovsky <partizan@altlinux.ru> 11.83-alt1
- New version

* Mon Oct 10 2005 Alexander Borovsky <partizan@altlinux.ru> 11.81-alt1
- New version
- Integrate with latex-preview

* Fri Jan 14 2005 Alexander Borovsky <partizan@altlinux.ru> 11.54-alt1
- New version
- Updated patches

* Wed Dec 01 2004 Alexander Borovsky <partizan@altlinux.ru> 11.53-alt1
- New version
- Changed "Index" program to rumakeindex
- Changed some keybindings in math mode (`f to \\varphi and `e to \\varepsilon)

* Sun May  9 2004 Ivan Zakharyaschev <imz@altlinux.ru> 11.14-alt7
- Fix hard-coded path constant in tex-site.el (spoilt by build env);
- include .nosearch files.

* Mon Feb 17 2003 Ott Alex <ott@altlinux.ru> 11.14-alt6
- Fixing spec file

* Sat Jan 11 2003 Ott Alex <ott@altlinux.ru> 11.14-alt5
- New version of package
- fixing problems with wrong number of arguments in font-latex-setup function

* Thu Sep 19 2002 Ott Alex <ott@altlinux.ru> 11.11-alt4
- put tex-site.el on standart place. Call it from /etc/emacs/site-start.d/auctex.el

* Tue Apr 16 2002 Ivan Zakharyaschev <imz@altlinux.ru> 11.11-alt3
- package:
  + more accurate description;
  + more accurate group for el subpkg (resolves \#836 at bugs.altlinux.ru);
- files:
  + do not include hilit-LaTeX.el (useful for old Emacs 19 only);

* Mon Apr  8 2002 Ivan Zakharyaschev <imz@altlinux.ru> 11.11-alt2
- require the current Emacs version or later;

* Thu Feb 28 2002 Ivan Zakharyaschev <imz@altlinux.ru> 11.11-alt1
- new mainstream version (11.11);
- spec-file: use el-pkgutils for generating filelists;
- %name-el requires %name (strict %%release deps);

* Thu Feb 28 2002 Ivan Zakharyaschev <imz@altlinux.ru> 11.10-alt4
- Run the start-script only for GNUEmacs (XEmacs has its own AUCTeX).

* Wed Feb 20 2002 Dmitry V. Levin <ldv@alt-linux.org> 11.10-alt3
- Updated buildrequires.
- Updated nosource logic.

* Sat Dec  8 2001 Ivan Zakharyaschev <imz@altlinux.ru> 11.10-alt2
- fix the name of the /etc/emacs/site-start.d/ entry.

* Sat Dec  8 2001 Ivan Zakharyaschev <imz@altlinux.ru> 11.10-alt1
- new mainstream version (11.10)
- renamed: auctex -> emacs-mode-auctex
- splitted into main package (bytecode) and a package with the sources
- "hand-generated" style descriptions should work: the path for them fixed
  (it was wrongly patched in previous pkg releases)
- linked the license from common-licenses (GPL-2)
- auto/ excluded from %_emacslispdir/%ModeName/ for it empty and not used
- for packagers:
  + using global def %%_emacslispdir

* Wed Jul 25 2001 Ivan Zakharyaschev <imz@altlinux.ru> 10.0g-alt2
- update info about special customization in the pkg
- change the printerlist patch for better handling error msgs

* Wed Jul 25 2001 Ivan Zakharyaschev <imz@altlinux.ru> 10.0g-alt1
- new version (10.0g).

* Wed Jul 25 2001 Ivan Zakharyaschev <imz@altlinux.ru> 9.9p-alt4
- The default value for TeX-master changed: now it makes AUC TeX
  ask you about the master file if the file doesn't seem to be a master
  (i.e. doesn't contain \docuemtnclass).

* Sat Jul 21 2001 Ivan Zakharyaschev <imz@altlinux.ru> 9.9p-alt3
- put generated data to %_aucstatedir

* Sat Jul 21 2001 Ivan Zakharyaschev <imz@altlinux.ru> 9.9p-alt2
- add patches for setting variables with site-specific values
- tried to make more modules (hilit and japanese) -- hilit didn't
  compile.
- add more documentation (plain text and DVIs)

* Thu Jul 19 2001 Ivan Zakharyaschev <imz@altlinux.ru> 9.9p-alt1
- first ALT build

* Sat Apr 14 2001 Francis Galiegue <fg@mandrakesoft.com> 9.9p-5mdk

- BuildRequires emacs-X11 and not only emacs

* Wed Dec 13 2000 Pixel <pixel@mandrakesoft.com> 9.9p-4mdk
- requires the emacs version used for building
(don't need to have a xemacs version, xemacs bundles it)

* Mon Nov 27 2000 Pixel <pixel@mandrakesoft.com> 9.9p-3mdk
- add build_req

* Sat Sep  2 2000 Pixel <pixel@mandrakesoft.com> 9.9p-2mdk
- mandrake adaptation
- cleanup

* Fri Jul 10 1998 W.L. Estes <wlestes@wlestes.uncg.edu>
- build root now used
- cleaned up file list
- fixed url tag
- added CHANGES and ChangeLog to doc files
- now requires emacs >= 20
- added \%clean
- misc spec file cosmetic cleanups

* Wed Mar 11 1998 Martin Schimschak <masch@theo-phys.uni-essen.de>
- initial revision for auctex 9.8l
