%define oname tifffile

%def_with check

Name: python3-module-%oname
Version: 2024.7.21
Release: alt1

Summary: Read and write TIFF(r) files

License: BSD-3-Clause
Group: Development/Python3
URL: https://pypi.org/project/tifffile
VCS: https://github.com/cgohlke/tifffile

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-numpy-testing
BuildRequires: python3-module-lxml
BuildRequires: python3-module-fsspec
%endif

%description
Tifffile is a Python library to
* store numpy arrays in TIFF (Tagged Image File Format) files, and
* read image and metadata from TIFF-like files used in bioimaging.

Image and metadata can be read from TIFF, BigTIFF, OME-TIFF, STK, LSM, SGI,
NIHImage, ImageJ, MicroManager, FluoView, ScanImage, SEQ, GEL, SVS, SCN, SIS,
ZIF (Zoomable Image File Format), QPTIFF (QPI), NDPI, and GeoTIFF files.

Numpy arrays can be written to TIFF, BigTIFF, OME-TIFF,
and ImageJ hyperstack compatible files in multi-page, memory-mappable, tiled,
predicted, or compressed form.

A subset of the TIFF specification is supported, mainly uncompressed and
losslessly compressed 8, 16, 32 and 64-bit integer, 16, 32 and 64-bit float,
grayscale and multi-sample images. Specifically, reading slices of image data,
CCITT and OJPEG compression, chroma subsampling without JPEG compression,
color space transformations, samples with differing types,
or IPTC and XMP metadata are not implemented.

TIFF(r), the Tagged Image File Format, is a trademark and under control of
Adobe Systems Incorporated. BigTIFF allows for files larger than 4 GB.
STK, LSM, FluoView, SGI, SEQ, GEL, QPTIFF, NDPI, and OME-TIFF,
are custom extensions defined by Molecular Devices (Universal Imaging Corporation),
Carl Zeiss MicroImaging, Olympus, Silicon Graphics International,
Media Cybernetics, Molecular Dynamics, PerkinElmer, Hamamatsu,
and the Open Microscopy Environment consortium, respectively.

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
export PYTHONDONTWRITEBYTECODE=1
export PYTEST_ADDOPTS='-p no:cacheprovider'
export PYTHONPATH=%buildroot%python3_sitelibdir
# test_write_5GB_bigtiff and test_write_imagej_raw are too long and can crash builder
py.test-3 -v tests -k 'not test_write_5GB_bigtiff and not test_write_imagej_raw' \
	--deselect=tests/test_tifffile.py::test_issue_infinite_loop \
	--deselect=tests/test_tifffile.py::test_issue_jpeg_ia \
	--deselect=tests/test_tifffile.py::test_func_pformat_xml \
	--deselect=tests/test_tifffile.py::test_filehandle_seekable \
	--deselect=tests/test_tifffile.py::test_read_cfa \
	--deselect=tests/test_tifffile.py::test_read_tiles \
	--deselect=tests/test_tifffile.py::test_write_cfa \
	--deselect=tests/test_tifffile.py::test_write_volume_png \
	--deselect=tests/test_tifffile.py::test_class_omexml \
	--deselect=tests/test_tifffile.py::test_class_omexml_modulo \
	--deselect=tests/test_tifffile.py::test_class_omexml_attributes \
	--deselect=tests/test_tifffile.py::test_class_omexml_multiimage \
	--deselect=tests/test_tifffile.py::test_write_ome \
	%nil

%files
%doc LICENSE
%doc README.rst ACKNOWLEDGEMENTS.rst CHANGES.rst
%_bindir/lsm2bin
%_bindir/tifffile
%_bindir/tiff2fsspec
%_bindir/tiffcomment
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-*.egg-info

%changelog
* Mon Jul 22 2024 Grigory Ustinov <grenka@altlinux.org> 2024.7.21-alt1
- Automatically updated to 2024.7.21.

* Tue Jul 16 2024 Grigory Ustinov <grenka@altlinux.org> 2024.7.2-alt1
- Automatically updated to 2024.7.2.

* Sun Jun 30 2024 Grigory Ustinov <grenka@altlinux.org> 2024.6.18-alt1
- Automatically updated to 2024.6.18.

* Thu May 23 2024 Grigory Ustinov <grenka@altlinux.org> 2024.5.22-alt1
- Automatically updated to 2024.5.22.

* Sun May 19 2024 Grigory Ustinov <grenka@altlinux.org> 2024.5.10-alt1
- Automatically updated to 2024.5.10.

* Fri Aug 20 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 2021.8.8-alt1
- Updated to upstream version 2021.8.8.

* Tue Aug 11 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2020.7.24-alt1
- Initial build for ALT.
