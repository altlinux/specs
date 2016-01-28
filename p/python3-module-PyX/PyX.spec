%define oname PyX

Name: python3-module-%oname
Version: 0.13
Release: alt2
Summary: Python graphics package
License: GPLv2+
Group: Development/Python3
Url: http://pyx.sourceforge.net/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %oname-%version.tar


BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel /usr/bin/tex /usr/bin/gs
BuildPreReq: libkpathsea-devel python-module-imaging
BuildPreReq: python3-module-sphinx
BuildRequires: python3-module-sphinx-sphinx-build-symlink

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

ln -s ../objects.inv manual
ln -s ../objects.inv faq

%build
%python3_build_debug build_ext -i

%make -C manual html
%make -C faq html
mv manual/_build/html manual/_build/manual
mv faq/_build/html faq/_build/faq

%install
%python3_install

%files
%doc AUTHORS CHANGES LICENSE README
%python3_sitelibdir/*

%files docs
%doc faq/_build/faq
%doc manual/_build/manual

%files examples
%doc examples

%changelog
* Thu Jan 28 2016 Denis Medvedev <nbr@altlinux.org> 0.13-alt2
- NMU make buildable



* Tue Jul 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13-alt1
- Version 0.13 (for Python 3)

* Tue Feb 12 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.12.1-alt1
- Version 0.12.1

* Thu Dec 15 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11.1-alt2
- Fixed build

* Fri Dec 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11.1-alt1
- Initial build for Sisyphus

