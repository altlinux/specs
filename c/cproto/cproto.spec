Name: cproto
Version: 4.7j
Release: alt2
Summary: Generating prototypes and declarations from C source code
License: Public
Group: Development/Tools
Url: http://invisible-island.net/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# ftp://invisible-island.net/cproto/
Source: %name-%version.tar.gz

BuildPreReq: /usr/bin/lex

%description
Cproto is a program that generates function prototypes and variable
declarations from C source code.  It can also convert function definitions
between the old style and the ANSI C style.  This conversion overwrites the
original files, so make a backup copy of your files in case something goes
wrong.

The program isn't confused by complex function definitions as much as other
prototype generators because it uses a yacc generated parser.  By ignoring all
the input between braces, I avoided implementing the entire C language grammar.

%prep
%setup

%build
%add_optflags -DOPT_LINTLIBRARY
%configure
%make_build

%install
%makeinstall

%files
%_bindir/*
%_man1dir/*

%changelog
* Thu Dec 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.7j-alt2
- Changed URL

* Mon Aug 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.7j-alt1
- Version 4.7j (thnx viy@)

* Sun Mar 13 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.6-alt2
- Rebuilt for debuginfo

* Fri May 29 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.6-alt1
- Initial build for Sisyphus

