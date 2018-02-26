%define srcName examplep

Name: tetex-latex-%srcName
Version: 0.03
Release: alt1
Summary: Verbatim phrases and listings in LaTeX
License: LPPL (LaTeX Project Public License)
Group: Publishing
Url: http://www.ctan.org/tex-archive/macros/latex/contrib/examplep
Packager: Kirill Maslinsky <kirill@altlinux.org>

BuildArch: noarch

Requires: tetex-core tetex-latex

Source0: %srcName-%version.tar.bz2

# Automatically added by buildreq on Tue Sep 04 2007
BuildRequires: tetex-latex

%description
Examplep provides sophisticated features for typesetting verbatim
source code listings, including the display of the source code and
its compiled LaTeX or METAPOST output side-by-side, with automatic
width detection and enabled page breaks (in the source), without
the need for specifying the source twice.  Special care is taken
that section, page and footnote numbers do not interfere with the
main document.  For typesetting short verbatim phrases, a
replacement for the \verb command is also provided in the package,
which can be used inside tables and moving arguments such as
footnotes and section titles.  The
listings package is used for syntax
highlighting.

The accompanying codep package and the wrfiles.pl Perl script
provide a convenient interface to the examplep package for authors
of manuals.  With codep it is possible to generate the source
code, the LaTeX or METAPOST output and the compilable example file
from a single source embedded into the appropriate place of the
.tex document file.

%prep
%setup -q -n %srcName-%version

%build

%install
%__mkdir_p %buildroot%_datadir/texmf/tex/latex/%srcName
install -pD -m644 examplep.sty codep.sty verbfwr.sty %buildroot%_datadir/texmf/tex/latex/%srcName/

%post
[ -x %_bindir/texhash ] && %_bindir/texhash 2>/dev/null ||:

%postun
[ -x %_bindir/texhash ] && %_bindir/texhash 2>/dev/null ||:

%files
%_datadir/texmf/tex/latex/%srcName/
%doc README eurotex_2005_examplep.pdf houses.pdf pexaminipage.pdf shorthyp_t1xtts.pdf houses.eps pexaminipage.eps shorthyp_t1xtts.eps wrfiles.pl eurotex_2005_examplep.tex 

%changelog
* Thu Nov 22 2007 Kirill Maslinsky <kirill@altlinux.org> 0.03-alt1
- Initial build for Sisyphus

