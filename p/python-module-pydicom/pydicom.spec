%define oname pydicom

%def_with python3

Name: python-module-%oname
Version: 0.9.9
Release: alt1.1
Summary: Pure python package for DICOM medical file reading and writing
License: MIT
Group: Development/Python
Url: http://code.google.com/p/pydicom/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %oname-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python
#BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
#BuildPreReq: python-tools-2to3
%endif

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-logging python-modules-unittest python-tools-2to3 python3 python3-base
BuildRequires: python-module-setuptools python3-module-setuptools rpm-build-python3 time

%description
pydicom is a pure python package for parsing DICOM files. DICOM is a
standard for communicating medical images and related information such
as reports and radiotherapy objects.

pydicom makes it easy to read these complex files into natural pythonic
structures for easy manipulation. Modified datasets can be written again
to DICOM format files.

%package -n python3-module-%oname
Summary: Pure python package for DICOM medical file reading and writing
Group: Development/Python3
%add_python3_req_skip wx

%description -n python3-module-%oname
pydicom is a pure python package for parsing DICOM files. DICOM is a
standard for communicating medical images and related information such
as reports and radiotherapy objects.

pydicom makes it easy to read these complex files into natural pythonic
structures for easy manipulation. Modified datasets can be written again
to DICOM format files.

%package -n python3-module-%oname-tests
Summary: Tests for pydicom
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
pydicom is a pure python package for parsing DICOM files. DICOM is a
standard for communicating medical images and related information such
as reports and radiotherapy objects.

This package contains tests for pydicom.

%package -n python3-module-%oname-examples
Summary: Examples for pydicom
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-examples
pydicom is a pure python package for parsing DICOM files. DICOM is a
standard for communicating medical images and related information such
as reports and radiotherapy objects.

This package contains examples for pydicom.

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

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec \
	sed -i 's|#!/usr/bin/python|#!/usr/bin/python3|' '{}' +
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%python_sitelibdir/*
%exclude %python_sitelibdir/dicom/test*
%exclude %python_sitelibdir/dicom/examples

%files tests
%python_sitelibdir/dicom/test*

%files examples
%python_sitelibdir/dicom/examples

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/*
%exclude %python3_sitelibdir/dicom/test*
%exclude %python3_sitelibdir/dicom/*/test*
%exclude %python3_sitelibdir/dicom/examples

%files -n python3-module-%oname-tests
%python3_sitelibdir/dicom/test*
%python3_sitelibdir/dicom/*/test*
%exclude %python3_sitelibdir/dicom/test/shell_all

%files -n python3-module-%oname-examples
%python3_sitelibdir/dicom/examples
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.9.9-alt1.1
- NMU: Use buildreq for BR.

* Mon Nov 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.9-alt1
- Version 0.9.9

* Sat Aug 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.8-alt3
- Added module for Python 3

* Wed Sep 25 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.8-alt2
- Fixed build

* Tue Apr 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.8-alt1
- Version 0.9.8

* Mon Dec 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.6-alt1
- Version 0.9.6

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.5-alt2.1
- Rebuild with Python-2.7

* Sun Apr 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.5-alt2
- Extracted examples into separate package

* Sat Apr 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.5-alt1
- Initial build for Sisyphus

