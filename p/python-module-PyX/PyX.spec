%define oname PyX
Name: python-module-%oname
Version: 0.11.1
Release: alt2
Summary: Python graphics package
License: GPLv2+
Group: Development/Python
Url: http://pyx.sourceforge.net/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %oname-%version.tar

BuildPreReq: python-devel texlive-latex-recommended
BuildPreReq: libkpathsea-devel python-module-imaging
BuildPreReq: python-module-sphinx-devel

%description
PyX is a Python package for the creation of PostScript and PDF files. It
combines an abstraction of the PostScript drawing model with a TeX/LaTeX
interface. Complex tasks like 2d and 3d plots in publication-ready
quality are built out of these primitives.

%package docs
Summary: Documentation for PyX
Group: Development/Documentation
BuildArch: noarch

%description docs
PyX is a Python package for the creation of PostScript and PDF files. It
combines an abstraction of the PostScript drawing model with a TeX/LaTeX
interface. Complex tasks like 2d and 3d plots in publication-ready
quality are built out of these primitives.

This package contains documentation for PyX.

%package examples
Summary: Examples for PyX
Group: Development/Documentation
BuildArch: noarch

%description examples
PyX is a Python package for the creation of PostScript and PDF files. It
combines an abstraction of the PostScript drawing model with a TeX/LaTeX
interface. Complex tasks like 2d and 3d plots in publication-ready
quality are built out of these primitives.

This package contains examples for PyX.

%prep
%setup

%prepare_sphinx .
ln -s ../objects.inv manual

%build
%python_build_debug build_ext -i

%make -C manual html

#mkdir -p pdf
#mv manual/_build/latex/*.pdf pdf/

%install
%python_install

%files
%doc AUTHORS CHANGES LICENSE README
%python_sitelibdir/*

%files docs
%doc faq/*.pdf
%doc manual/_build/html
#doc pdf

%files examples
%doc examples

%changelog
* Thu Dec 15 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11.1-alt2
- Fixed build

* Fri Dec 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11.1-alt1
- Initial build for Sisyphus

