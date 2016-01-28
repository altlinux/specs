%define oname PyX

Name: python3-module-%oname
Version: 0.13
Release: alt2.1
Summary: Python graphics package
License: GPLv2+
Group: Development/Python3
Url: http://pyx.sourceforge.net/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %oname-%version.tar


BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel /usr/bin/tex /usr/bin/gs
#BuildPreReq: libkpathsea-devel python-module-imaging
#BuildPreReq: python3-module-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: fontconfig ghostscript-classic libgpg-error python-base python-modules python3 python3-base python3-module-Pygments python3-module-alabaster python3-module-babel python3-module-cssselect python3-module-docutils python3-module-jinja2 python3-module-markupsafe python3-module-pytz python3-module-setuptools python3-module-six python3-module-snowballstemmer python3-module-sphinx python3-module-sphinx_rtd_theme tex-common texlive-base texlive-common texlive-latex-base xz
BuildRequires: ghostscript-common libkpathsea-devel python3-devel python3-module-html5lib python3-module-jinja2-tests python3-module-sphinx-sphinx-build-symlink rpm-build-python3 texlive-base-bin time

#BuildRequires: python3-module-sphinx-sphinx-build-symlink

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
* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 0.13-alt2.1
- NMU: Use buildreq for BR.

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

