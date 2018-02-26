Name: texmf-latex-passivetex
Version: 20040310
Release: alt1
Packager: Grigory Batalov <bga@altlinux.ru>

Summary: TeX-based XSL/FO formatter
Group: Publishing
License: BSD-style and LPPL
Url: http://www.hcu.ox.ac.uk/TEI/Software/passivetex/

Provides: passivetex = %version
Obsoletes: passivetex < %version

Requires: xmltex >= 1.8
# Automatically added by buildreq on Sat Oct 17 2009
BuildRequires: docbook-utils unzip

BuildRequires(pre): rpm-build-texmf

BuildArchitectures: noarch

Source0: passivetex.zip
Source1: passivetex-addons.tar.gz

Patch: %name-%version-alt.patch

%description
PassiveTeX is a library of TeX macros which can be used to process 
an XML document which results from an XSL transformation to 
formatting objects conforming to XSL/FO specification.

%prep
%setup -q -a1 -n passivetex
%patch -p1

%build
docbook2man passivetex.sgml

%install
mkdir -p %buildroot%_mandir/man1
install -c -m644 *.1 %buildroot%_mandir/man1

mkdir -p %buildroot%_datadir/texmf/tex/latex/passivetex
install -c -m644 *.xmt %buildroot%_datadir/texmf/tex/latex/passivetex
install -c -m644 *.sty %buildroot%_datadir/texmf/tex/latex/passivetex


%files 
%doc LICENSE index.html
%_mandir/man?/*
%_datadir/texmf/tex/latex/passivetex/*

%changelog
* Tue Oct 20 2009 Grigory Batalov <bga@altlinux.ru> 20040310-alt1
- Source update.
- Package rename according to TeXPolicy.

* Thu Apr 12 2007 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20030310-alt3
- License tag fixed

* Thu Oct 17 2003 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20030310-alt2
- build requires fixed

* Thu Mar 13 2003 Anton V. Boyarshinov <boyarsh@altlunux.ru> 20030310-alt1
- new version from Sebastian Rahtz; many improvements, 
  but no official changelog exists

* Fri Jan 24 2003 Anton V. Boyarshinov <boyarsh@altlunux.ru> 20020812-alt9
- hacked long arrow to arrow, added support for URW fonts 
  by  Yury Konovalov <yurix@altlinux.ru>


* Wed Jan 15 2003 Anton V. Boyarshinov <boyarsh@altlunux.ru> 20020812-alt8
- fixed problem with margins when first page in flow is even


* Thu Dec 19 2002 Anton V. Boyarshinov <boyarsh@altlunux.ru> 20020812-alt7
- additional tuning floating placement parameters


* Fri Nov 29 2002 Anton V. Boyarshinov <boyarsh@altlunux.ru> 20020812-alt6
- tuned floating placement parameters


* Fri Nov 29 2002 Anton V. Boyarshinov <boyarsh@altlunux.ru> 20020812-alt5
- Added \sloppy

* Sun Nov 24 2002 Alexander Bokovoy <ab@altlinux.ru> 20020812-alt4.3
- Spec cleanups

* Sun Nov 24 2002 Alexander Bokovoy <ab@altlinux.ru> 20020812-alt4.2
- Fix interdependencies with xmltex (xmltex needs fotex for enabling
  XSL/FO processing but %name requires xmltex as well)

* Sun Nov 24 2002 Alexander Bokovoy <ab@altlinux.ru> 20020812-alt4.1
- Rebuild with tetex-2.0-alt0.5

* Fri Nov  15  2002 Anton V. Boyarshinov <boyarsh@altlunux.ru> 20020812-alt4
- fonts changes in alt-mlnames.sty
- text-align attribute in static content now works

* Mon Oct 21 2002 Anton V. Boyarshinov <boyarsh@altlunux.ru> 20020812-alt3
- fixed problem with header indent in toc

* Fri Sep 13 2002 Anton V. Boyarshinov <boyarsh@altlunux.ru> 20020812-alt2
- fixed (hacked) problems with 1.54.1 styles

* Thu Aug 15 2002 Anton V. Boyarshinov <boyarsh@altlunux.ru> 20020812-alt1
- new version from Sebastian Rahtz

* Thu Jul 18 2002 Anton V. Boyarshinov <boyarsh@altlunux.ru> 20020626-alt4
- nowrap blocks presentation changed

* Thu Jul 11 2002 Anton V. Boyarshinov <boyarsh@altlunux.ru> 20020626-alt4
- fixed pageref to chapter

* Wed Jul 3 2002 Anton V. Boyarshinov <boyarsh@altlunux.ru> 20020626-alt3
- page number output fixed
- list labels output fixed
- hyphenation in <screen/> partly fixed
- alt-mlnames.sty based on mlnames.sty added to change main fonts to
  computer-modern

* Mon Jul 1 2002 Anton V. Boyarshinov <boyarsh@altlunux.ru> 20020626-alt2
- page number and list label output fixed

* Fri Jun 28 2002 Anton V. Boyarshinov <boyarsh@altlunux.ru> 20020626-alt1
- new version from Sebastian Rahtz


* Thu Jun 27 2002 Anton V. Boyarshinov <boyarsh@altlunux.ru> 20020409-alt8
- pdfxmltex crashed fixed
- documentation updated

* Tue Jun 25 2002 Anton V. Boyarshinov <boyarsh@altlunux.ru> 20020409-alt7
- xmltex now is a separate package, its droped from passivetex
- space before <fo:inline> fixed (droped)

* Thu Jun 21 2002 Anton V. Boyarshinov <boyarsh@ru.echo.fr> 20020409-alt6
- basic documentation added
- added support for text-align, height and width for external-graphic element
  (thanks to Yura Zotov <yznews@hotbox.ru>)
- urls support fixed

* Wed Jun 19 2002 Anton V. Boyarshinov <boyarsh@ru.echo.fr> 20020409-alt5
- LICENSE added

* Fri Jun 14 2002 Anton V. Boyarshinov <boyarsh@ru.echo.fr> 20020409-alt4
- fixed output tables without specified width

* Wed Jun 10 2002 Anton V. Boyarshinov <boyarsh@ru.echo.fr> 20020409-alt3
- spec fix

* Wed Jun 10 2002 Anton V. Boyarshinov <boyarsh@ru.echo.fr> 20020409-alt2
- Hyphenation now works more 'right way'
- font shapes in russian texts are supported


* Wed May 29 2002 Anton V. Boyarshinov <boyarsh@ru.echo.fr> 20020409-alt1
- first build, no docs included, sorry, will be fixed soon
