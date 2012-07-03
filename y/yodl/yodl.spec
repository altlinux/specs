Name: yodl
Version: 3.00.0
Release: alt1
Epoch: 1

Summary: Yet oneOther Document Language
License: GPL
Group: Text tools
Packager: Alexey Tourbin <at@altlinux.ru>

URL: http://yodl.sourceforge.net/
Source: yodl-%version.tar
Patch1: yodl-1.31.18-mdk-htmldocs.patch
Patch2: yodl-1.31.18-alt-htmlfoot.patch
Patch3: yodl-1.31.18-deb.patch
Patch4: yodl-1.31.18-suse-python25.patch

# Automatically added by buildreq on Sun Apr 13 2008
BuildRequires: flex groff-base netpbm python-modules

BuildPreReq: icmake texlive-latex-recommended ghostscript-utils

%description
Yodl is a package that implements a pre-document language and tools to
process it.  The idea of Yodl is that you write up a document in a
pre-language, then use the tools (eg. yodl2html) to convert it to some
final document language.  Current converters are for HTML, ms, man, LaTeX
SGML and texinfo, plus a poor-man's text converter.  Main document types
are "article", "report", "book" and "manpage".  The Yodl document
language is designed to be easy to use and extensible.

%package docs
Summary: Documentation for Yodl
Group: Documentation
BuildArch: noarch

%description docs
Yodl is a package that implements a pre-document language and tools to
process it.  The idea of Yodl is that you write up a document in a
pre-language, then use the tools (eg. yodl2html) to convert it to some
final document language.  Current converters are for HTML, ms, man, LaTeX
SGML and texinfo, plus a poor-man's text converter.  Main document types
are "article", "report", "book" and "manpage".  The Yodl document
language is designed to be easy to use and extensible.

This package contais documentation for Yodl.

%prep
%setup
#patch1 -p1
#patch2 -p1
#patch3 -p1
#patch4 -p0

%build
%add_optflags -D_GNU_SOURCE=1
export ac_cv_lib_intl_gettext=no
for i in programs man manual macros
do
	./build $i
done

%install
for i in programs man manual macros docs
do
	./build install $i %buildroot
done

%files
%_bindir/*
%_datadir/%name
%_mandir/man?/*

%files docs
%_docdir/%name

%changelog
* Sun Aug 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:3.00.0-alt1
- Version 3.00.0

* Wed Nov 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.31.18-alt2.1.1
- Rebuilt with python 2.6

* Sun Jun 21 2009 Alexey Tourbin <at@altlinux.ru> 1:1.31.18-alt2.1
- rebuilt

* Sun Apr 13 2008 Alexey Tourbin <at@altlinux.ru> 1:1.31.18-alt2
- suse-python25.patch

* Fri Jan 25 2008 Grigory Batalov <bga@altlinux.ru> 1:1.31.18-alt1.1
- Rebuilt with python-2.5.

* Thu Jan 19 2006 Dmitry V. Levin <ldv@altlinux.org> 1:1.31.18-alt1
- Blindly fixed implicit declaration bugs to make this cruft work on x86_64.

* Mon Oct 21 2002 Dmitry V. Levin <ldv@altlinux.org> 1.31.18-ipl5mdk
- Merged patches from Debian:
  + Make startit() and endit() correctly generate <ul></ul>
    rather than <dl></dl>.
  + ' generates \&' rather than \' for groff -man output,
    as \' is an acute accent, not an apostrophe.
- Avoid linking with libintl.
- Rebuilt with new groff.

* Sat Sep 29 2001 Sergey Vlasov <vsu@altlinux.ru> 1.31.18-ipl4mdk
- Added patch to fix HTML footer generation.

* Sat Jul 14 2001 Sergey Budnevitch <svb@altlinux.ru> 1.31.18-ipl3mdk
- Fix bad datadir
- Automatically added BuildRequires

* Wed Jun 27 2001 Stanislav Ievlev <inger@altlinux.ru> 1.31.18-ipl2mdk
- Rebuilt with python-2.1

* Wed Jan 24 2001 Peter 'Nidd' Novodvorsky <petya@logic.ru> 1.31.18-ipl1mdk
- IPLabs Linux Team adaptations.

* Wed Jul 19 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.31.18-1mdk
- 1.32.18.
- BM.

* Tue Jun 20 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.31.17-4mdk
- Use makeinstall macros.

* Wed May 31 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.31.17-3mdk
- Clean up specs.

* Thu May 04 2000 Lenny Cartier <lenny@mandrakesoft.com> 1.31.17-2mdk
- fix group
