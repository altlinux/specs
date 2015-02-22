%define mname zopyx
%define oname %mname.convert2
Name: python-module-%oname
Version: 2.4.5
Release: alt1.git20121105
Summary: A Python interface for the conversion of HTML to PDF, RTF, DOCX, WML and ODT)
License: ZPL
Group: Development/Python
Url: https://pypi.python.org/pypi/zopyx.convert2/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/zopyx/zopyx.convert2.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests %_bindir/fop
BuildPreReq: python-module-elementtree python-module-BeautifulSoup
BuildPreReq: python-module-pisa python-module-Reportlab
BuildPreReq: python-module-pypdf python-module-html5lib
BuildPreReq: python-module-nose

%py_provides %oname
Requires: %_bindir/fop
%py_requires %mname elementtree BeautifulSoup sx.pisa3 reportlab pyPdf
%py_requires html5lib

%description
The zopyx.convert2 package helps you to convert HTML to PDF, RTF, ODT,
DOCX and WML using XSL-FO technology or using PrinceXML. This package is
used as the low-level API for zopyx.smartprintng.core.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
The zopyx.convert2 package helps you to convert HTML to PDF, RTF, ODT,
DOCX and WML using XSL-FO technology or using PrinceXML. This package is
used as the low-level API for zopyx.smartprintng.core.

This package contains tests for %oname.

%prep
%setup

%build
%python_build_debug

%install
%python_install

rm -fR %buildroot%python_sitelibdir_noarch
install -d %buildroot%python_sitelibdir/%mname
cp -fR src/zopyx/convert2 %buildroot%python_sitelibdir/%mname/
cp -fR src/*.egg-info %buildroot%python_sitelibdir/

%check
python setup.py test

%files
%doc docs/source/*.rst
%_bindir/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests

%files tests
%python_sitelibdir/%mname/*/tests

%changelog
* Sun Feb 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.5-alt1.git20121105
- Initial build for Sisyphus

