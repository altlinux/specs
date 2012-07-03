%define oname pydicom
Name: python-module-%oname
Version: 0.9.6
Release: alt1
Summary: Pure python package for DICOM medical file reading and writing
License: MIT
Group: Development/Python
Url: http://code.google.com/p/pydicom/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %oname-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python
BuildPreReq: python-devel python-module-setuptools

%description
pydicom is a pure python package for parsing DICOM files. DICOM is a
standard for communicating medical images and related information such
as reports and radiotherapy objects.

pydicom makes it easy to read these complex files into natural pythonic
structures for easy manipulation. Modified datasets can be written again
to DICOM format files.

%package tests
Summary: Tests for pydicom
Group: Development/Python
Requires: %name = %version-%release

%description tests
pydicom is a pure python package for parsing DICOM files. DICOM is a
standard for communicating medical images and related information such
as reports and radiotherapy objects.

This package contains tests for pydicom.

%package examples
Summary: Examples for pydicom
Group: Development/Python
Requires: %name = %version-%release

%description examples
pydicom is a pure python package for parsing DICOM files. DICOM is a
standard for communicating medical images and related information such
as reports and radiotherapy objects.

This package contains examples for pydicom.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%files
%python_sitelibdir/*
%exclude %python_sitelibdir/dicom/test*
%exclude %python_sitelibdir/dicom/examples

%files tests
%python_sitelibdir/dicom/test*

%files examples
%python_sitelibdir/dicom/examples

%changelog
* Mon Dec 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.6-alt1
- Version 0.9.6

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.5-alt2.1
- Rebuild with Python-2.7

* Sun Apr 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.5-alt2
- Extracted examples into separate package

* Sat Apr 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.5-alt1
- Initial build for Sisyphus

