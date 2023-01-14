%define  prefixname python3-module-sphinxcontrib
%define  modulename svg2pdfconverter

# https://github.com/missinglinkelectronics/sphinxcontrib-svg2pdfconverter/issues/14
%def_without check

Name:    %prefixname-%modulename
Version: 1.2.2
Release: alt1

Summary: Sphinx SVG to PDF converter extension
License: BSD-2-Clause
Group:   Development/Python3
URL:     https://pypi.org/project/sphinxcontrib-svg2pdfconverter
# https://github.com/missinglinkelectronics/sphinxcontrib-svg2pdfconverter

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-sphinx

BuildArch: noarch

Source:  %name-%version.tar

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


%package -n %prefixname-cairosvgconverter
Summary: Sphinx SVG to PDF Converter Extension - CairoSVG converter
Group:   Development/Python3

Requires: /usr/bin/cairosvg
Requires: %name-common = %EVR

%description -n %prefixname-cairosvgconverter
Converts SVG images to PDF in case the builder does not support SVG images
natively (e.g. LaTeX).
This package contains converter using CairoSVG.

%prep
%setup

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


%files -n %prefixname-cairosvgconverter
%python3_sitelibdir/sphinxcontrib/__pycache__/cairosvgconverter.*.pyc
%python3_sitelibdir/sphinxcontrib/cairosvgconverter.py

%changelog
* Sat Jan 14 2023 Grigory Ustinov <grenka@altlinux.org> 1.2.2-alt1
- Automatically updated to 1.2.2.

* Mon Oct 10 2022 Grigory Ustinov <grenka@altlinux.org> 1.2.1-alt1
- Automatically updated to 1.2.1.

* Sat May 28 2022 Grigory Ustinov <grenka@altlinux.org> 1.2.0-alt1
- Automatically updated to 1.2.0.

* Mon Aug 02 2021 Grigory Ustinov <grenka@altlinux.org> 1.1.1-alt3
- Fixed requires on cairosvg.

* Tue Apr 13 2021 Grigory Ustinov <grenka@altlinux.org> 1.1.1-alt2
- Disabled check, because it isn't supported by python3.9 and upstream sleeps.

* Wed Mar 17 2021 Grigory Ustinov <grenka@altlinux.org> 1.1.1-alt1
- Automatically updated to 1.1.1.

* Fri Jul 03 2020 Grigory Ustinov <grenka@altlinux.org> 1.1.0-alt1
- Automatically updated to 1.1.0.
- Added cairosvgconverter subpackage.

* Tue Dec 31 2019 Grigory Ustinov <grenka@altlinux.org> 1.0.1-alt1
- Initial build for Sisyphus.
