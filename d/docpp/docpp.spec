%define oname doc++
Name: docpp
Version: 3.4.10
Release: alt3
Summary: Documentation system for C, C++, IDL and Java
License: GPL v2
Group: Development/Tools
Url: http://docpp.sourceforge.net/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# cvs -z3 -d:pserver:anonymous@docpp.cvs.sourceforge.net:/cvsroot/docpp co -P docpp
Source: %name-%version.tar.gz

BuildPreReq: gcc-c++ flex ghostscript ghostscript-utils
BuildPreReq: graphviz bison gettext-tools texlive-latex-recommended

%description
DOC++ is a documentation system for C, C++, IDL and Java generating both
TeX output for high quality hardcopies and HTML output for sophisticated
online browsing of your documentation. The documentation is extracted
directly from the C/C++/IDL header/source files or Java class files.

Here is a short list of highlights:

  - hierarchically structured documentation

  - automatic class graph generation (as Java applets for HTML)

  - cross references

  - high end formatting support including typesetting of equations

%package -n %oname
Summary: Documentation system for C, C++, IDL and Java
Group: Development/Tools

%description -n %oname
DOC++ is a documentation system for C, C++, IDL and Java generating both
TeX output for high quality hardcopies and HTML output for sophisticated
online browsing of your documentation. The documentation is extracted
directly from the C/C++/IDL header/source files or Java class files.

Here is a short list of highlights:

  - hierarchically structured documentation

  - automatic class graph generation (as Java applets for HTML)

  - cross references

  - high end formatting support including typesetting of equations

%package -n %oname-manual
Summary: User manual for DOC++
Group: Documentation
BuildArch: noarch

%description -n %oname-manual
DOC++ is a documentation system for C, C++, IDL and Java generating both
TeX output for high quality hardcopies and HTML output for sophisticated
online browsing of your documentation. The documentation is extracted
directly from the C/C++/IDL header/source files or Java class files.

This package contains user manual for DOC++.

%prep
%setup

%build
%add_optflags -DSTDC_HEADERS -DHAVE_UNISTD_H
%configure
%make_build

pushd doc/manual
%make pdf
popd

%install
%makeinstall_std

pushd po
%makeinstall
popd

install -d %buildroot%_docdir/%oname/html
install -m644 doc/manual/html/* %buildroot%_docdir/%oname/html
install -m644 doc/manual/*.pdf %buildroot%_docdir/%oname

%find_lang %oname

%files -n %oname -f %oname.lang
%doc COPYING CREDITS NEWS README REPORTING-BUGS
%_bindir/*

%files -n %oname-manual
%_docdir/%oname

%changelog
* Wed Mar 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.10-alt3
- Rebuilt for debuginfo

* Mon Nov 09 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.10-alt2
- Rebuilt with texlive instead of tetex

* Thu Sep 17 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.10-alt1.1
- Rebuilt without included gettext

* Thu Sep 17 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.10-alt1
- Initial build for Sisyphus

