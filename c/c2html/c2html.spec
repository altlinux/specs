Name: c2html
Version: 0.9.4
Release: alt2
Summary: Syntax highlighter for C source
License: GPL
Group: Development/Tools
Url: http://ftp.mcs.anl.gov/pub/petsc/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: http://ftp.mcs.anl.gov/pub/petsc/c2html.tar.gz

BuildPreReq: flex

%description
The  c2html  program is a syntax  highlighter  for C source  code that
produces a highlighted html file as output. The output  can be read by
any graphical WWW-Browser.    If the browser  understands the  tags to
change  font colors (as Netscape    does) the output  will look   like
highlighted  by  emacs.  Otherwise  it  will  not  look  so nice,  but
readability is increased too.

%prep
%setup

%build
%configure --enable-fhs
%make_build

%install
%makeinstall

%files
%_bindir/*
%_docdir/%name
%_man1dir/*

%changelog
* Sat Mar 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.4-alt2
- Rebuilt for debuginfo

* Sat Apr 25 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.4-alt1
- Initial build for Sisyphus
