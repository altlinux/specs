%define _unpackaged_files_terminate_build 1
%define pypi_name PyMuPDF
%define mod_name pymupdf

%def_with check

Name: python3-module-%mod_name
Version: 1.27.2.2
Release: alt1

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
# Linters and static checks have no place in distro build tests
SKIP="not test_codespell and \
      not test_pylint and \
      not test_py_typed and \
      not test_flake8"

# Flaky / environment‑dependent tests
SKIP="$SKIP and not test_3842 and \
             not test_2791 and \
             not test_4090 and \
             not test_4125 and \
             not test_3050 and \
             not test_3854 and \
             not test_spikes and \
             not test_4180 and \
             not test_4392"

# Tests pulling extra data or network / packaging tools
SKIP="$SKIP and not test_fontarchive and \
             not test_subset_fonts and \
             not test_4445 and \
             not test_4457 and \
             not test_barcode and \
             not test_open2 and \
             not test_4533 and \
             not test_4702"

%ifarch %ix86
# On i586, some rendering / positioning tests give minor pixel differences
SKIP="$SKIP and not test_2246 and \
             not test_4415 and \
             not test_4245 and \
             not test_4182 and \
             not test_4435 and \
             not test_4699"
%endif
%pyproject_run_pytest -k "$SKIP"

%files
%doc COPYING README.*
%_bindir/pymupdf
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/fitz/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Mar 24 2026 Evgeniy Martynenko <enimalojd@altlinux.org> 1.27.2.2-alt1
- New version (1.27.2.2).

* Tue Mar 10 2026 Evgeniy Martynenko <enimalojd@altlinux.org> 1.27.2-alt1
- New version (1.27.2).

* Thu Feb 12 2026 Martynenko Evgeniy <enimalojd@altlinux.org> 1.27.1-alt1
- New version (1.27.1).

* Tue Oct 21 2025 Martynenko Evgeniy <enimalojd@altlinux.org> 1.26.5-alt3
- Renamed package to python3-module-pymupdf.

* Tue Oct 21 2025 Martynenko Evgeniy <enimalojd@altlinux.org> 1.26.5-alt2
- Added support swig p11 compatibility.

* Mon Oct 13 2025 Martynenko Evgeniy <enimalojd@altlinux.org> 1.26.5-alt1
- New version (1.26.5).
- Added runtime dependency on python3-module-mupdf (closes: #56207).

* Wed May 07 2025 Martynenko Evgeniy <enimalojd@altlinux.org> 1.25.5-alt1
- Initial build for ALT.
