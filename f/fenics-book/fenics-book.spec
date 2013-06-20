Name: fenics-book
Summary: A book about FEniCS project
Version: 20130430
Release: alt1
Group: Documentation
License: FDL
URL: http://fenicsproject.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://bitbucket.org/fenics-project/fenics-book.git
Source: %name-%version.tar.gz
Source1: http://www.tug.org/texlive/devsrc/Master/texmf-dist/tex/latex/emptypage/emptypage.sty
Source2: http://www.tug.org/texlive/devsrc/Master/texmf-dist/tex/latex/todonotes/todonotes.sty

BuildArch: noarch

BuildPreReq: texlive-latex-recommended texlive-latex-extra
BuildPreReq: texlive-pictures /usr/bin/ps2pdf

%description
This is a FEniCS book. The book discuss the theoretical foundations for the
current components of FEniCS, function as a reference for users, and showcase
interesting applications built with FEniCS. The tentative title for the book is
Automated Scientific Computing.

It is also emphasized that chapters either discuss current FEniCS projects (in a
tutorial style), summarize (already published) theoretical results relevant for
the FEniCS software, or discuss the use of FEniCS in applications.

%prep
%setup

install -p -m644 %SOURCE1 %SOURCE2 packages

%build
%make_build final

%files
%doc book.pdf

%changelog
* Thu Jun 20 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20130430-alt1
- Updated

* Fri Jan 27 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20120123-alt1
- Updated

* Tue Dec 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20111125-alt1
- Updated

* Thu Sep 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20110811-alt1
- Updated

* Fri Apr 15 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20110415-alt1
- Updated

* Mon Jun 21 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20100603-alt1
- Updated

* Mon Dec 21 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20091209-alt1
- Updated
- Rebuilt tex: psfig -> epsfig

* Sun Aug 16 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20090816-alt1
- Updated

* Tue Aug 04 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20090708-alt2
- Fixed build requirements

* Thu Jul 09 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20090708-alt1
- Initial build for Sisyphus

