%define pypi_name pillow-heif
%define mod_name pillow_heif

Name: python3-module-%pypi_name
Version: 1.8.1
Release: alt1

Summary: Python interface for libheif library and Pillow plugin

License: BSD-3-Clause
Group: Development/Python3
Url: https://github.com/bigcat88/pillow_heif

# Source-url: %__pypi_url %mod_name
Source: %name-%version.tar

# tests/overflow_test segfaults in the encoder on i586 (32-bit stride overflow)
ExcludeArch: %ix86

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: python3-devel
BuildRequires: libheif-devel

%if_disabled check
%else
BuildRequires: python3-module-pillow python3-module-pytest
BuildRequires: python3-module-defusedxml
BuildRequires: python3-module-packaging
BuildRequires: python3-module-numpy
%endif

%description
Python bindings to libheif for working with HEIF images and a plugin
for Pillow, with decoding and encoding support. It is the full version
of pi-heif (python3-module-pi-heif), which includes only the decoder.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
# tests of the encoder are skipped: libheif in ALT has only the kvazaar HEVC
# encoder (no 10/12-bit, no x265 parameters); slow tests are skipped too
export PYTHONPATH=%buildroot%python3_sitelibdir
python3 -m pytest -v tests -k "not leak" \
	--deselect tests/orientation_test.py \
	--deselect tests/metadata_etc_test.py \
	--deselect tests/metadata_exif_test.py \
	--deselect tests/metadata_xmp_test.py \
	--deselect tests/thumbnails_test.py \
	--deselect tests/options_test.py \
	--deselect tests/modes_test.py \
	--deselect tests/write_test.py \
	--deselect tests/numpy_test.py

%files
%doc README.md LICENSE.txt
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/_%{mod_name}*.so
%python3_sitelibdir/%mod_name-%version.dist-info/

%changelog
* Fri Oct 16 2026 Vitaly Lipatov <lav@altlinux.ru> 1.8.1-alt1
- initial build for Sisyphus
