%define oname openpyxl

%def_with python3

Name: python-module-%oname
Version: 2.3.0
Release: alt1.b1.1.1
Summary: A Python library to read/write Excel 2007 xlsx/xlsm files
License: MIT/Expat
Group: Development/Python
Url: https://pypi.python.org/pypi/openpyxl/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-jdcal python-modules-json
#BuildPreReq: python-module-et_xmlfile
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-jdcal
#BuildPreReq: python3-module-et_xmlfile
%endif

%py_provides %oname
%py_requires jdcal json et_xmlfile

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-pytest python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base python3-module-pytest python3-module-setuptools
BuildRequires: python-module-jdcal python-module-setuptools-tests python-modules-json python3-module-jdcal python3-module-setuptools-tests rpm-build-python3

%description
openpyxl is a Python library to read/write Excel 2010 xlsx/xlsm files.

It was born from lack of existing library to read/write natively from
Python the Office Open XML format.

%package -n python3-module-%oname
Summary: A Python library to read/write Excel 2007 xlsx/xlsm files
Group: Development/Python3
%py3_provides %oname
%py3_requires jdcal et_xmlfile

%description -n python3-module-%oname
openpyxl is a Python library to read/write Excel 2010 xlsx/xlsm files.

It was born from lack of existing library to read/write natively from
Python the Office Open XML format.

%prep
%setup

%if_with python3
cp -fR . ../python3
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

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.3.0-alt1.b1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.3.0-alt1.b1.1
- NMU: Use buildreq for BR.

* Sun Aug 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.0-alt1.b1
- Version 2.3.0-b1

* Wed Feb 11 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.4-alt1
- Initial build for Sisyphus

