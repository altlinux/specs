Name: lout
Version: 3.39
Release: alt2

Summary: The Lout document formatting language
License: GPL
Group: Text tools
Url: http://sourceforge.net/projects/lout/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar.gz
Source1: %name-mode.el
Source2: fontdefs.ld
Source3: %name-3.29.user.ps.bz2
Requires: urw-fonts >= 2.0-alt9
BuildRequires(pre): rpm-build-fonts
BuildPreReq: emacs

%description
Lout is a high-level language for document formatting.  Lout reads a
high-level description of a document (similar in style to LaTeX) and can
produce a PostScript(TM) file for printing or produce plain text.
Lout supports the typesetting of documents which contain floating
figures, table, diagrams, rotated and scaled text or graphics, footnotes,
running headers, footers, an index, a table of contents and bibliography,
cross-references, mathematical equations and statistical graphs.  Lout can
be extended with definitions that should be easier to write than other
languages, since Lout is a high-level language.  Lout supports (with
hyphenation) a variety of languages:  Czech, Danish, Dutch, English,
Finnish, French, German, Norwegian, Russian, Slovenian, Spanish and
Swedish.

Install the lout package if you'd like to try the Lout document formatting
system.  Unless you're already a Lout expert, you'll probably want to also
install the lout-doc package, which contains the documentation for Lout.

%package doc
Summary: The documentation for the Lout document formatting language
Group: Text tools
BuildArch: noarch

%description doc
The lout-doc package includes all of the documentation for the Lout
document formatting language.  The documentation includes manuals for
regular users and for experts, written in Lout and available as
PostScript(TM) files.  The documentation provides good examples for how to
write large documents with Lout.

If you're installing the lout package, you should install the lout-doc
package.

%prep
%setup
rm -f doc/user/.pie_intr.swp

cp %SOURCE2 data
cp %SOURCE3 .

%build
%ifarch x86_64
sed -i 's|@SUFF64@|64|' makefile
%else
sed -i 's|@SUFF64@||' makefile
%endif
%make_build RPM_OPT_FLAGS="%optflags -U_FORTIFY_SOURCE" \
	FONT_DIR="%_fontpathdir/type1" lout prg2lout

%install
install -d %buildroot%_bindir
install -d %buildroot%_libdir
install -d %buildroot%_datadir/locale
install -d %buildroot%_man1dir
install -d %buildroot%_docdir/%name

%make DESTDIR=%buildroot DATADIR=%_datadir install installman installdoc

(cd doc/user
    ../../lout all >user.ps
)

# emacs
mkdir -p %buildroot%_emacslispdir
install -m 644 %SOURCE1 %buildroot%_emacslispdir
emacs -batch -f batch-byte-compile %buildroot%_emacslispdir/%name-mode.el

install -d %buildroot%_sysconfdir/emacs/site-start.d
cat <<EOF >%buildroot%_sysconfdir/emacs/site-start.d/%name.el
(autoload 'lout-mode "lout-mode" "Major mode for editing Lout text" t)
   (setq auto-mode-alist
      (append '(("\\.lout\\'" . lout-mode)) auto-mode-alist))
EOF

install -m644 *.ps.bz2 %buildroot%_docdir/%name

# It is the file in the package whose name matches the format emacs or vim uses 
# for backup and autosave files. It may have been installed by  accident.
find $RPM_BUILD_ROOT \( -name '.*.swp' -o -name '#*#' -o -name '*~' \) -print -delete
# failsafe cleanup if the file is declared as %%doc
find . \( -name '.*.swp' -o -name '#*#' -o -name '*~' \) -print -delete

%files
%doc blurb README maillist whatsnew
%_bindir/*
%_mandir/man?/*
%_libdir/%name
%exclude %_libdir/%name/font
%_emacslispdir/*
%_sysconfdir/emacs/site-start.d/*

%files doc
%doc %_docdir/%name

%changelog
* Thu Dec 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.39-alt2
- Applied lout-3.39-alt1-digest.diff from repocop

* Wed Dec 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.39-alt1
- Version 3.39

* Sun Mar 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.38-alt2
- Rebuilt for debuginfo

* Thu Aug 20 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.38-alt1
- Version 3.38
- Fixed build for x86_64

* Fri Dec 05 2003 Stanislav Ievlev <inger@altlinux.org> 3.29-alt1
- 3.29

* Fri Mar 28 2003 Stanislav Ievlev <inger@altlinux.ru> 3.28-alt1
- 3.28
- include ps file into doc package instead all doc subdir

* Wed Oct 30 2002 Stanislav Ievlev <inger@altlinux.ru> 3.26-alt1
- 3.26
- real adaptation for urw-fonts. Previous author made a lot of hacks

* Sun Nov 25 2001 Dmitry Smirnov <dvsmirnov@comail.ru> 3.24-alt1
- adapted to urw-fonts
- added emacs mode

* Fri Jul 27 2001 Lenny Cartier <lenny@mandrakesoft.com>
- rebuild
- url

* Fri Nov 10 2000 Lenny Cartier <lenny@mandrakesoft.com>
- updated to 3.24
- merge patches
- remove useless manual stripping
- add more macros
- clean spec

* Thu Aug 31 2000 Etienne Faure <etienne@mandrakesoft.com>
- rebuild with %%doc and _mandir macros

* Wed Mar 22 2000 Lenny Cartier <lenny@mandrakesoft.com>
- fix group
- fix files section

* Sat Nov 06 1999 John Buswell <johnb@mandrakesoft.com>
- Build Release

* Tue May 11 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 7)

* Thu Jan 21 1999 Bill Nottingham <notting@redhat.com>
- no more gcc on sparc, so don't optimize instead (same egcs bug?)

* Thu Dec 17 1998 Michael Maher <mike@redhat.com>
- built package for 6.0

* Sat Aug 15 1998 Jeff Johnson <jbj@redhat.com>
- build root
- use gcc on sparc to avoid egcs bug

* Fri May 08 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc
