%define _unpackaged_files_terminate_build 1
%define pypi_name PyMuPDF
%define mod_name pymupdf

%def_with check

Name: python3-module-%mod_name
Version: 1.26.5
Release: alt3

Summary: PyMuPDF is a high performance Python library for data extraction, analysis, conversion & manipulation of PDF (and other) documents
License: AGPL-3.0-or-later
Group: Development/Python3
Url: https://pymupdf.readthedocs.io
VCS: https://github.com/pymupdf/PyMuPDF.git

Source0: %name-%version.tar
Patch0: %name-%version-alt.patch

Provides: python3-module-PyMuPDF = %EVR
Obsoletes: python3-module-PyMuPDF < %EVR

BuildRequires(pre): rpm-build-python3
BuildRequires: swig
BuildRequires: libmupdf-devel
BuildRequires: python3-module-mupdf
BuildRequires: gcc gcc-c++
BuildRequires: libfreetype-devel
BuildRequires: python3-dev
%if_with check
BuildRequires: /proc
BuildRequires: tesseract-langpack-en
BuildRequires: python3-module-pytest
BuildRequires: python3-modules-sqlite3
BuildRequires: python3-module-psutil
BuildRequires: python3-module-Pillow
BuildRequires: python3-module-fonttools
%endif

Requires: python3-module-mupdf

%description
%summary.

%prep
%setup
%autopatch -p1

%build
export PYMUPDF_SETUP_MUPDF_BUILD_TYPE='release'
export PYMUPDF_SETUP_MUPDF_BUILD=''
export PYMUPDF_SETUP_IMPLEMENTATIONS='b'
export PYMUPDF_SETUP_PY_LIMITED_API=0
export CFLAGS="$CFLAGS -I/usr/include -I/usr/include/freetype2 -I/usr/include/mupdf"
export LDFLAGS="$LDFLAGS -lfreetype -lmupdf"
%pyproject_build

%install
%pyproject_install

%check
# linters have no place in distro build tests
SKIP="not test_codespell and not test_pylint"
# test_fontarchives tries to download special module via pip
SKIP="$SKIP and not test_fontarchive"
# flake8 has no place in downstream packaging
SKIP="$SKIP and not test_flake8"
# test_2791 fails sporadically with its empiric bounds
SKIP="$SKIP and not test_2791 and not test_4090 and not test_4125"
# test_3050 is known to fail for distribution builds
SKIP="$SKIP and not test_3050 and not test_3854"
# test_subset_fonts needs pymupdf_fonts
SKIP="$SKIP and not test_subset_fonts"
# test_spikes uses a binary diff on rendered images
SKIP="$SKIP and not test_spikes"
# these compare renderings with system fonts or missing fonts
SKIP="$SKIP and not test_4180"
# tries to download / install stuff through git and pip
SKIP="$SKIP and not test_4445 and not test_4457 and not test_barcode"
SKIP="$SKIP and not test_open2 and not test_4533 and not test_4702"
# Swig returns different results
SKIP="$SKIP and not test_4392"
%ifarch %ix86
# On the i586 architecture, some tests related to text rendering and positioning,
# may give minor discrepancies in pixels.
SKIP="$SKIP and not test_2246 and not test_4415 and not test_4245 and not test_4182"
%endif
%pyproject_run_pytest -k "$SKIP"

%files
%doc COPYING README.*
%_bindir/%mod_name
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/fitz/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Oct 21 2025 Martynenko Evgeniy <enimalojd@altlinux.org> 1.26.5-alt3
- Renamed package to python3-module-pymupdf.

* Tue Oct 21 2025 Martynenko Evgeniy <enimalojd@altlinux.org> 1.26.5-alt2
- Added support swig p11 compatibility.

* Mon Oct 13 2025 Martynenko Evgeniy <enimalojd@altlinux.org> 1.26.5-alt1
- New version (1.26.5).
- Added runtime dependency on python3-module-mupdf (closes: #56207).

* Wed May 07 2025 Martynenko Evgeniy <enimalojd@altlinux.org> 1.25.5-alt1
- Initial build for ALT.
