%define  prefixname python3-module-sphinxcontrib
%define  modulename svg2pdfconverter

Name:    %prefixname-%modulename
Version: 1.0.1
Release: alt1

Summary: Sphinx SVG to PDF converter extension
License: BSD-2-Clause
Group:   Development/Python3
URL:     https://pypi.org/project/sphinxcontrib-svg2pdfconverter
# https://github.com/missinglinkelectronics/sphinxcontrib-svg2pdfconverter

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools
BuildRequires: python3-module-sphinx

BuildArch: noarch

Source:  %modulename-%version.tar

%description
Converts SVG images to PDF in case the builder does not support SVG images
natively (e.g. LaTeX).

%package common
Summary: Sphinx SVG to PDF Converter Extension - common files
Group:   Development/Python3

%description common
Converts SVG images to PDF in case the builder does not support SVG images
natively (e.g. LaTeX).
This package contains common files.


%package -n %prefixname-inkscapeconverter
Summary: Sphinx SVG to PDF Converter Extension - Inkscape converter
Group:   Development/Python3

Requires: /usr/bin/inkscape
Requires: %name-common = %EVR

%description -n %prefixname-inkscapeconverter
Converts SVG images to PDF in case the builder does not support SVG images
natively (e.g. LaTeX).
This package contains converter using Inkscape.


%package -n %prefixname-rsvgconverter
Summary: Sphinx SVG to PDF Converter Extension - libRSVG converter
Group:   Development/Python3

Requires: /usr/bin/rsvg-convert
Requires: %name-common = %EVR

%description -n %prefixname-rsvgconverter
Converts SVG images to PDF in case the builder does not support SVG images
natively (e.g. LaTeX).
This package contains converter using libRSVG.

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install

%check
%{__python3} setup.py test

# Note that there is no %%files section for the unversioned python module
%files common
%doc README.rst
%dir %python3_sitelibdir/sphinxcontrib/__pycache__
%python3_sitelibdir/sphinxcontrib_svg2pdfconverter*nspkg.pth
%python3_sitelibdir/sphinxcontrib_svg2pdfconverter-*.egg-info


%files -n %prefixname-inkscapeconverter
%python3_sitelibdir/sphinxcontrib/__pycache__/inkscapeconverter.*.pyc
%python3_sitelibdir/sphinxcontrib/inkscapeconverter.py


%files -n %prefixname-rsvgconverter
%python3_sitelibdir/sphinxcontrib/__pycache__/rsvgconverter.*.pyc
%python3_sitelibdir/sphinxcontrib/rsvgconverter.py

%changelog
* Tue Dec 31 2019 Grigory Ustinov <grenka@altlinux.org> 1.0.1-alt1
- Initial build for Sisyphus.
