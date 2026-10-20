%define pypi_name pypdfium2
# chromium build number of the system pdfium (pdfium 8076 = chromium/8076)
%define pdfium_build 8076
%define pdfium_fullver 156.0.8076.0

Name: python3-module-%pypi_name
Version: 5.14.0
Release: alt1

Summary: Python bindings to PDFium
License: Apache-2.0 OR BSD-3-Clause
Group: Development/Python3
Url: https://github.com/pypdfium2-team/pypdfium2

# Source-url: %__pypi_url %pypi_name
Source: %name-%version.tar

# the same set as for pdfium
ExcludeArch: %ix86 %arm ppc64le

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(packaging)
BuildRequires: python3(wheel)
BuildRequires: libpdfium-devel >= %pdfium_build

# libpdfium is loaded via ctypes, so it can't be detected automatically
Requires: libpdfium0 >= %pdfium_build

%description
pypdfium2 is an ABI-level Python 3 binding to PDFium, a powerful and
liberal-licensed library for PDF rendering, inspection, manipulation and
creation.

This package uses the system pdfium library: the ctypes bindings are
generated at build time from the system pdfium headers.

%prep
%setup

%build
# generate bindings against the system libpdfium (no download, no bundled binary)
export PDFIUM_PLATFORM=system-search:%pdfium_build
export GIVEN_FULLVER=%pdfium_fullver
# ctypesgen can't parse C23 (nullptr_t in gcc 15 stddef.h)
export CPP="gcc -E -std=gnu17"
%pyproject_build

%install
%pyproject_install
# the ctypes bindings are generated for the arch of the system libpdfium
mkdir -p %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* %buildroot%python3_sitelibdir/

%check
cat > check_render.py <<'EOF'
import pypdfium2 as pdfium
import pypdfium2.raw as raw
print(pdfium.PDFIUM_INFO)
pdf = pdfium.PdfDocument.new()
page = pdf.new_page(200, 100)
bitmap = page.render(scale=2)
assert (bitmap.width, bitmap.height) == (400, 200), (bitmap.width, bitmap.height)
print(len(pdf), raw.FPDF_GetLastError())
EOF
PYTHONPATH=%buildroot%python3_sitelibdir %__python3 check_render.py
PYTHONPATH=%buildroot%python3_sitelibdir %__python3 -m pypdfium2_cli --version

%files
%doc README.md
%_bindir/%pypi_name
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pypi_name}_cfg/
%python3_sitelibdir/%{pypi_name}_cli/
%python3_sitelibdir/%{pypi_name}_raw/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Oct 12 2026 Vitaly Lipatov <lav@altlinux.ru> 5.14.0-alt1
- initial build for Sisyphus
