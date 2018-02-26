Name: gri
Summary: A language for scientific illustration
Version: 2.12.23
Release: alt1
Group: Development/Tools
License: GPL v2
URL: http://gri.sourceforge.net
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar.gz
Source1: http://gri.sourceforge.net/refcard.pdf
Source2: http://gri.sourceforge.net/cmdrefcard.pdf
Source3: http://gri.sourceforge.net/gri.pdf

BuildPreReq: gcc-c++ ImageMagick-tools texlive-base-bin info
BuildPreReq: ghostscript-classic perl4-compat

%description
Gri is a language for scientific graphics programming.  It is a
command-driven application, as opposed to a click/point application.
It is analogous to latex, and shares the property that extensive power
is the reward for tolerating a modest learning curve.  Gri output is
in industry-standard PostScript, suitable for incorporation in
documents prepared by various text processors.

Gri can make x-y graphs, contour-graphs, and image graphs.  In
addition to high-level capabilities, it has enough low-level
capabilities to allow users to achieve a high degree of customization.
Precise control is extended to all aspects of drawing, including
line-widths, colors, and fonts.  Text includes a subset of the tex
language, so that it is easy to incorporate Greek letters and
mathematical symbols in labels.

The following is a terse yet working Gri program.  If it is stored in
a file called 'example.gri', and executed with the unix command 'gri
example', it will create a postscript file called 'example.ps' with
a linegraph connecting data points in the file called `file.dat'.

   open file.dat        # open a file with columnar data
   read columns x * y   # read first column as x and third as y
   draw curve           # draw line through data (autoscaled axes)

%package doc
Summary: Documentation for Gri
Group: Documentation
BuildArch: noarch

%description doc
Gri is a language for scientific graphics programming.  It is a
command-driven application, as opposed to a click/point application.
It is analogous to latex, and shares the property that extensive power
is the reward for tolerating a modest learning curve.  Gri output is
in industry-standard PostScript, suitable for incorporation in
documents prepared by various text processors.

This package contains documentation for Gri.

%prep
%setup

%build
%autoreconf
%configure --enable-linux_redhat
%make_build

%install
%makeinstall_std

mv %buildroot%_docdir/%name-%version %buildroot%_docdir/%name
install -p -m644 %SOURCE1 %SOURCE2 %SOURCE3 %buildroot%_docdir/%name

%files
%doc AUTHORS COPYING ChangeLog NEWS README THANKS license.txt copyright.txt
%_bindir/*
%_datadir/%name
%_man1dir/*
%_infodir/*
%_emacslispdir/*

%files doc
%_docdir/%name

%changelog
* Mon Sep 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.12.23-alt1
- Version 2.12.23

* Wed Apr 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.12.22-alt1
- Version 2.12.22

* Fri Mar 18 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.12.21-alt4
- Really rebuilt for debuginfo

* Thu Mar 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.12.21-alt3
- Rebuilt for debuginfo

* Tue Nov 16 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.12.21-alt2
- Fixed build

* Mon Jun 21 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.12.21-alt1
- Version 2.12.21

* Mon Nov 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.12.19-alt1
- Version 2.12.19

* Tue Jun 23 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.12.18-alt1
- Initial build for Sisyphus

* Fri Jul 20 2007 <Dan.Kelley@Dal.Ca>
- release 2.12.16
- Fix Debian bug #130802 (postscript problem in landscape mode, refreshed in gv viewer)
- Fix Debian bug #434010 ('set page landscape' requires 'set page size' first, but it should really default to something reasonable instead)
- release 2.12.17
- Add history and editing of commands in interactive mode
- Fix SourceForge bug 1913577 (superscripts did not end correctly, if preceded by a {} block)
- Fix SourceForge bug #1761562 (y axis name is upside down, for log axis with decreasing values)
* Sun Apr 15 2007 <Dan.Kelley@Dal.Ca>
- Fix SourceForge bug #1700978 (html concept index mostly broken)
- Fix SourceForge bug 1698924 (box plots show missing data)
- Fix Debian bug 417217 (will not compile in GCC 4.3)
- Fix SourceForge bug 1698116 (poorly-positioned name of RHS y-axis)
* Mon Jan  8 2007 <Dan.Kelley@Dal.Ca>
- Fix SourceForge bug 1630768 (segfault with clipped images)
* Mon Nov  6 2006 <Dan.Kelley@Dal.Ca>
-Fix SourceForge bug 1591475 (to compile in Solaris CC)
-Fix SourceForge bug 1591062 (to compile in OpenBSD)
-Add Century font
* Sat Jul 15 2006 <Dan.Kelley@Dal.Ca>
-Fix SourceForge bug #1523033 (malloc warning)
-Fix SourceForge bug #1523032 ('create columns from function' fails if existing local 'tmp' directory)
-Fix SourceForge bug #1491105 ('set x axis labels' had no effect for log axes; same for y axis)
* Sat Mar 25 2006 <Dan.Kelley@Dal.Ca>
-Fix SourceForge bug #1449546 (x/y axis limits not correctly inferred from 'set x/ grid').
-Fix SourceForge bug #1285180 (NaN was mishandled in recent versions).
-Port to FreeBSD.  (Thanks to Christopher Illies and Roman Neuhauser for helping.)
* Mon Jan 16 2006 <Dan.Kelley@Dal.Ca>
Add -private and -no_private commandline options
* Tue May 11 2005 <Dan.Kelley@Dal.Ca>
Fix SourceForge bug 1196613 (user-supplied x-axis labels can run offscale)
Fix SourceForge bug 1198341 (x-axis labels sometimes rotated)
* Tue May 10 2005 <Dan.Kelley@Dal.Ca>
Fix SourceForge bug 1199280 (malloc warning for RPN assignment)
* Mon May 5 2005 <Dan.Kelley@Dal.Ca>
Fix SourceForge bug 1196115 (gri_merge and gri_unpage mis-installed)
* Mon Mar 2 2005 <Dan.Kelley@Dal.Ca>
Fix SourceForge bug 1153209 (Emacs mode incompatible with new version of 'gv'
* Wed Jan 12 2005 <Dan.Kelley@Dal.Ca>
Fix SourceForge bug 1101172 ('gri -help' incorrectly stated meaning of last argument(s))
* Sat Jan  8 2005 <Dan.Kelley@Dal.Ca>
Fix SourceForge bug 835711 ('draw gri logo' fails)
* Sat Jan  8 2005 <Dan.Kelley@Dal.Ca>
Fix SourceForge bug 875881 (failed compilation with gcc 2.95.3)
* Sat Jan  8 2005 <Dan.Kelley@Dal.Ca>
Fix SourceForge bug 867515 (problem with junk in images)
* Fri Jan  7 2005 <Dan.Kelley@Dal.Ca>
- Fix SourceForge bug 1094087 (failed gcc-4.0 AMD64 compilation; solution provided by Andreas Jochens, a Debian user)
* Mon Jan  3 2005 <Dan.Kelley@Dal.Ca>
- Fix SourceForge bug 1094087 ('set path to' gave incorrect results)
* Sun Dec 19 2004 <Dan.Kelley@Dal.Ca>
- Fix SourceForge bug 1085788 ('image *=' gave incorrect results)
* Mon Dec 13 2004 <Dan.Kelley@Dal.Ca>
- Fix SourceForge bug 1084123 (Fink packaging put info files in wrong place)
* Mon Aug 30 2004 <Dan.Kelley@Dal.Ca>
- Fix SourceForge bug 1019141 ('draw arc' ignores the present pen color)
* Sun Jul 25 2004 <Dan.Kelley@Dal.Ca>
- Fix SourceForge bug 997741 (PostScript-clipped images broken if y-axis decreases)
* Thu Jun 24  2004 <Dan.Kelley@Dal.Ca>
- fix SF bug 978822 (doc error on 'set path to')
* Sun Jun 13  2004 <Dan.Kelley@Dal.Ca>
- add 'set transparency'
* Thu Apr 15  2004 <Dan.Kelley@Dal.Ca>
- fix SF bug 932203 (misplaced labels caused by 'set x axis labels')
* Tue Apr 6  2004 <Dan.Kelley@Dal.Ca>
- fix SF bug 930259 ('draw arc' had an extra line [thanks for fix by Wolfgang Voegeli])
* Fri Apr 2  2004 <Dan.Kelley@Dal.Ca>
- fix SF bug 928277 ('draw polygon' should take 'cm' and 'pt' units)
* Mon Mar 29 2004 <Dan.Kelley@Dal.Ca>
- fix SF bug 923719 ('draw curve overlying' ignored effect of 'set dash')
* Thu Mar 11 2004 <Dan.Kelley@Dal.Ca>
- fix SF bug 914125 (all offpage points reported to have been drawn by 'draw curve')
* Thu Jan 15 2004 <Dan.Kelley@Dal.Ca>
- fix SF bug 877613 ('help' broken; cannot use temporary files)
- fix SF bug 875881 ('draw image' broken with GCC 2.95)
- fix SF bug 867515 ('convert grid to image' error)
* Sun Jan 11 2004 <Dan.Kelley@Dal.Ca>
- fix SF bug 874483 ('dash' properties ignored by 'save state')
* Thu Jan 8 2004 <Dan.Kelley@Dal.Ca>
- fix SF bug 873245 (inaccurate warnings on slow operations)
* Wed Jan 7 2004 <Dan.Kelley@Dal.Ca>
- fix SF bug 871477 by making 'set missing value none' the default
* Wed Sep 3 2003 <Dan.Kelley@Dal.Ca>
- RELEASE as version 2.12.7
- switch to automake-1.7 from automake-1.6
* Mon Sep 1 2003 <Dan.Kelley@Dal.Ca>
- RELEASE as version 2.12.6
* Sat Aug 30 2003 <Dan.Kelley@Dal.Ca>
- add 'age' RPN function, for testing file ages
* Sat Jul 19 2003 <Dan.Kelley@Dal.Ca>
- fix Sourceforge bug 773850 (bbox increased by 'draw symbol' even if (rectangular) postscript clipping is on)
* Thu Jun 27 2003 <Dan.Kelley@Dal.Ca>
- add 'age' RPN operator
* Tue Jun 24 2003 <Dan.Kelley@Dal.Ca>
- fix Sourceforge bug 760130 (solaris cannot compile with Ctl-l in Makefile)
* Sat Jun 14 2003 <Dan.Kelley@Dal.Ca>
- fix Sourceforge bug 750561 (make rebuilt HTML docs even if up-to-date)
* Sun Jun 7 2003 <Dan.Kelley@Dal.Ca>
- fix Sourceforge bug 743134 (bounding box not limited by 'set clip postscript')
* Sat May 31 2003 <Dan.Kelley@Dal.Ca>
- alter some target names to match the Automake Makefiles.
* Sat May 03 2003 <Dan.Kelley@Dal.Ca> (fix by Kawamura Masao)
- fix several typos on filenames, plus a compilation error hidden behind a precompilation flag
* Tue Apr 15 2003 <Dan.Kelley@Dal.Ca> (fix by Peter Galbraith)
- fix Sourceforge bug 720607 (emacs mode couldn't find html docs in redhat)
* Sun Apr 06 2003 Dan Kelley <Dan.Kelley@Dal.Ca>
- fix SourceForge bug 696073 (incorrect handling of \$() syntax)
* Sat Apr 05 2003 Dan Kelley <Dan.Kelley@Dal.Ca>
- fix SourceForge bug 715884 (mixup on quoted strings)
* Sat Mar 29 2003 Dan Kelley <Dan.Kelley@Dal.Ca>
- fix SourceForge bug 711354 (program name wrong in PostScript Creator: comment)
- fix SourceForge bug 706202 (Page orientation hint missing in Postscript)
* Thu Mar 01 2003 Dan Kelley <Dan.Kelley@Dal.Ca>
- +++ VERSION 2.12.3 +++
- fix SourceForge bug 685919 (cannot understand '.eps' file extension)
* Fri Feb  7 2003 Dan Kelley <Dan.Kelley@Dal.Ca>
- +++ VERSION 2.12.2 +++
* Tue Jan 28 2003 Dan Kelley <Dan.Kelley@Dal.Ca>
- fix SourceForge bug 675304 (segfault on 'read image pgm')
* Sat Jan 25 2003 Dan Kelley <Dan.Kelley@Dal.Ca>
- fix SourceForge bug 647234 (will not compile on Mac OS X 10.1.5)
* Mon Jan 20 2003 Dan Kelley <Dan.Kelley@Dal.Ca>
- fix SourceForge bug 671022 (error on 'flip image x|y')
* Sat Jan 18 2003 Dan Kelley <Dan.Kelley@Dal.Ca>
- fix SourceForge bug 669603 ('skip backward .n.' did not work)
* Tue Jan 14 2003 Dan Kelley <Dan.Kelley@Dal.Ca>
- fix SourceForge bug 667754 ('read image pgm' segfaults on memory)
* Wed Jan 8 2003  Dan Kelley <Dan.Kelley@Dal.Ca>
- fix SourceForge bug 664388 ('read image pgm' broken)
* Sun Dec 15 2002 Dan Kelley <Dan.Kelley@Dal.Ca>
- fix SourceForge bug 654129 (ignores ~/.grirc file)
- fix SourceForge bug 654127 (configure scripts are broken)
* Sat Dec 7 2002  Dan Kelley <Dan.Kelley@Dal.Ca>
- fix SourceForge bug 649132 (LDFLAGS not used in Makefile.in)
- fix SourceForge bug 649134 (tweak gcc optimization)
- fix SourceForge bug 649136 (examples 8 and 9 out-dated)
- fix SourceForge bug 641406 (RPN too aggressive on missing values)
* Wed Sep 25 2002  Dan Kelley <Dan.Kelley@Dal.Ca>
- Version 2.12.1
- fix SourceForge bug 613075 (sin, cos, tan problem in RPN)
* Sun Sep 15 2002  Dan Kelley <Dan.Kelley@Dal.Ca>
- Version 2.12.0
- add 'sed' RPN operator
- add 'skewness' RPN operator
- add 'kurtosis' RPN operator
- fix SourceForge bug 606303 (web pages were not valid html)
- fix SourceForge bug 593958 (should ignore 'missingvalue' if it occurs 
  within an intermediate result of an RPN calculation)
- fix SourceForge bug 600395 (won't compile with recently released version (3.2) of GCC compiler)
- fix SourceForge bug 600233 (segfaults if some RPN operators are used on too-small stack)
* Sun Jun 16 2002  Dan Kelley <Dan.Kelley@Dal.Ca>
- Add 'hex2dec' and 'dec2hex' rpn operators.
* Wed Jun  5 2002  Dan Kelley <Dan.Kelley@Dal.Ca>
- Add 'sed' rpn operator.
* Sat Jun  1 2002  Dan Kelley <Dan.Kelley@Dal.Ca>
- Version 2.10.1
- Fix Sourceforge bug 562911 (won't build with gcc-3.0)
- Fix Sourceforge bug 562558 ('draw title' confusion with log axes)
- Fix Sourceforge bug 562014 (won't build if popt library is unavailable)
- Fix SourceForge bug 558463 (in HTML docs, the ``press'' margin tag was misdirected)
- Fix SourceForge bug 562017 (parser fails with DOS end-of-line)
- Fix SourceForge bug 562017 ('new page' postscript error in gv viewer)

* Tue May 07 2002  Dan Kelley <Dan.Kelley@Dal.Ca>
- Version 2.10.0

* Sat Apr 20 2002 Dan Kelley <Dan.Kelley@Dal.Ca>
- Fix Sourceforge bug 546109 (bounding box wrong if postscript clipping used)

* Mon Mar 18 2002 Dan Kelley <Dan.Kelley@Dal.Ca>
- Permit 'draw label' coordinates in pt

* Sat Mar 16 2002 Dan Kelley <Dan.Kelley@Dal.Ca>
- Fix Sourceforge bug 508657 (missing backslash in drawing undefined synonyms)
- Fix Sourceforge bug 482120 ('regress' ignores data weights)

* Tue Mar 12 2002 Dan Kelley <Dan.Kelley@Dal.Ca>
- Permit 'draw box' to have coordinates in pt, as well as cm.
- Permit 'draw symbol' to have coordinates in pt, as well as cm.
- Permit 'draw line from' to have coordinates in pt, as well as cm.

* Wed Feb 27 2002 Dan Kelley <Dan.Kelley@Dal.Ca>
- Fix Sourceforge bug 523450 (log axes detect non-positive values too late)

* Thu Feb 21 2002 Dan Kelley <Dan.Kelley@Dal.Ca>
- Fix Sourceforge bug 521045 (install problem, function prototype problem)

* Thu Feb 07 2002  Dan Kelley <Dan.Kelley@Dal.Ca>
- Fix Sourceforge bug 513002 (minor error in documentation of 'set clip').

* Mon Jan 28 2002 Dan Kelley <Dan.Kelley@Dal.Ca>
- Fix Sourceforge bug 509592 (doc HTML indices misordered).

* Sat Jan 26 2002 Dan Kelley <Dan.Kelley@Dal.Ca>
- Fix SourceForge bug 506523 (map axes give wrong minutes in negative regions).

* Fri Jan 25 2002 Dan Kelley <Dan.Kelley@Dal.Ca>
- Fix SourceForge bug 508088 (grimode: gv should update, not be relaunched).
- Make RPM install/uninstall run silently.

* Wed Jan 23 2002 Dan Kelley <Dan.Kelley@Dal.Ca>
- Fix SourceForge bug 506490 ('-v' commandline option gave wrong number)

* Wed Jan 02 2002 Dan Kelley <Dan.Kelley@Dal.Ca>
- add `set clip to curve'

* Thu Dec 13 2001 Dan Kelley <Dan.Kelley@Dal.Ca>
- Release as gri-2.8.5 on SourceForge.Net site.  
- Fix SourceForge bug 492472 ('inf' rpn operator caused segfault)

* Thu Oct 04 2001 Dan Kelley <Dan.Kelley@Dal.Ca>
- Release as gri-2.8.4 on SourceForge.Net site.  
- Fix SourceForge bug 467973 (`gri -version' gave wrong version
  number, breaking the Emacs Gri mode.)
- Fix SourceForge bug 468401 (`draw grid' disobeys pencolor)

* Mon Oct 01 2001 Dan Kelley <Dan.Kelley@Dal.Ca>
- Release as gri-2.8.3 on SourceForge.Net site.
- Fix SourceForge bug 462243 (endian problem in Rasterfile images, 
  plus a reading problem in PGM images).

* Mon Sep 10 2001 Dan Kelley <Dan.Kelley@Dal.Ca>
- Release as gri-2.8.2 on SourceForge.Net site.
- Really Fix SourceForge bug 454557 (wouldn't compile with the
  pre-release version 3.0.1 of the GNU c++ compiler). 
  This closes SourceForge bug 111093.

* Thu Sep 06 2001 Dan Kelley <Dan.Kelley@Dal.Ca>
- Release as gri-2.8.1 on SourceForge.Net site.
- Fix SourceForge bug 450465 (`create columns from function' was broken).
- Fix SourceForge bug 454557 (wouldn't compile with the pre-release 
  version 3.0.1 of the GNU c++ compiler; closes: sourceforge bug 111093)

* Tue Jul 24 2001 Dan Kelley <dan.kelley@dal.ca>
- Bump up version number to 2.8.0

* Mon Jul 23 2001 Dan Kelley <Dan.Kelley@Dal.Ca>
- Release as gri-2.8.0 on SourceForge.Net site.
- Add `unlink' command as a unix-familiar way to delete files.
- Add `set page size' command to clip to a given page size.
- Add `substr' RPN operator to permit extraction of sub-strings.
- Add `default' for the `set x name' and the `set y name' commands.
- Add Perl-like ability to put underscores in numerical constants
    (`.v. = 1_000' and `.v. = 1000' are completely equivalent).
- In Emacs mode, change <M-Tab> so that it completes builtin 
  variables and synonyms as well as commands. 
- In Emacs mode, add "idle-timer help" to display defaults
  for builtin variables under cursor.
- In Emacs mode, make fontification of builtin variables apply 
  only if spelled correctly.
- To Makefile, add `make source-arch-indep' target in sources.  
  This will build a source tar file in which all the 
  architecture-independent material (documentation in HTML, 
  postscript and Info formats) is pre-made.  This makes it 
  easier to install gri on a host that doesn't have  TeX and
  ImageMagick installed.
- Move gri-html-doc and gri-ps-doc documentation files to 
  the /usr/share/doc/gri directory
- Ensure that package compiles with Standards-Version: 3.5.5
  without changes.

* Thu Apr 19 2001 Dan Kelley <dan.kelley@dal.ca>
- Rename this file as gri.spec, without the version number embedded 
  in the filename.  Upgrade to version number 2.6.1.  Change url to
  point to sourceforge site (but leave ftp as it is, for now anyway).

* Tue Jan 30 2001  Dan Kelley <dan.kelley@dal.ca>
- Changing to e.g. /usr/share/info instead of /usr/info.  Same for 
  manpages.  I know, I should be using the fancy macros that are 
  defined in /usr/lib/rpm, but these seemed contradictory, with 
  respect to where things are in my Redhat 7.0 setup ... and I
  had a hard time figuring out how to use these macros anyway,
  so I just gave up and hard-wired them in, using the new 
  directories as used in Redhat 7.0, as opposed to the (different)
  directories in all the other Redhat versions I've had.  Someday
  I'll switch to using macros, but it means changing both this 
  spec-file and various Makefiles, and I need to be sure that 
  changes to the Makefiles don't hurt the distributions for 
  Debian linux, for solaris, etc.

* Thu Jun  1 2000  Dan Kelley <dan.kelley@dal.ca>
- Triv changes here; code changes are to read compressed files, and
  manual improvements.

* Fri May 12 2000 Dan Kelley <dan.kelley@dal.ca>
- Compress info files for linux-redhat.

* Thu May 11 2000 Peter S Galbraith <psg@debian.org>
- Change info files to .info file extension.
- Tweaked install-info rules.  I hope they work.

* Sat Apr 01 2000 Dan Kelley <dan.kelley@dal.ca>
- Fix spec-file error in the install-info command.  However,
  to my great frustration, this is still broken or install-info
  is broken) since the command doesn't install an entry for gri.
  After hand-editing to insert a Gri entry, I uncovered another
  bug, and so I have added a chmod of /usr/info/dir file so 
  folks other than root can use info.
- Update the version number in gri.cmd to match the number compiled 
  into gri.
- Update the startup message from the old form to the new form.
- Call this release 3 to match Tim Powers' convention (although 
  I think it should be called release 1, when it works!)

* Fri Mar 31 2000 Dan Kelley <dan.kelley@dal.ca>
- applied Tim Powers' patches directly to the sources, updating them
  so that the patches Tim had made in this spec file are no longer
  needed.  Note: I didn't apply Tim's patch to the documentation, 
  since visual inspection indicated that I had already repaired
  the errors he found (each of which which involved my having used
  an incorrect name for the example gif files.)
- renamed Tim's spec file from gri.spec to gri-2.4.3.spec since
  otherwise I'd get too confused as versions develop.

* Fri Mar 31 2000 Tim Powers <timp@redhat.com>
- changed group

* Thu Mar 30 2000 Tim Powers <timp@redhat.com>
- started changelog on Dan Kelley's origional spec file
- quiet setup
- patched Makefile so that the install goes a bit smoother since we use
  BuildRoots
- changed post and postun sections so that they operate on /usr/info/dir
  instead of /etc/info-dir
- streamlined files list so that man/info pages are picked up even if RPM
  doesn't want to gzip them
- bzipped source to conserve space
- added clean section 
