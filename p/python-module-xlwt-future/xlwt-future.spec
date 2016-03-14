%define oname xlwt-future

%def_with python3

Name: python-module-%oname
Version: 0.8.0
Release: alt1.1
Summary: Library to create spreadsheet files compatible with MS Excel 97/2000/XP/2003 XLS files
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/xlwt-future/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel
%endif

Conflicts: python-module-xlwt

%description
xlwt is a library for generating spreadsheet files that are compatible
with Excel 97/2000/XP/2003, OpenOffice.org Calc, and Gnumeric. xlwt has
full support for Unicode. Excel spreadsheets can be generated on any
platform without needing Excel or a COM server. The only requirement is
Python 2.6, 2.7, or 3.3.

%package examples
Summary: Examples for xlwt
Group: Development/Python
Requires: %name = %EVR

%description examples
xlwt is a library for generating spreadsheet files that are compatible
with Excel 97/2000/XP/2003, OpenOffice.org Calc, and Gnumeric. xlwt has
full support for Unicode. Excel spreadsheets can be generated on any
platform without needing Excel or a COM server. The only requirement is
Python 2.6, 2.7, or 3.3.

This package contains examples for xlwt.

%package -n python3-module-%oname
Summary: Library to create spreadsheet files compatible with MS Excel 97/2000/XP/2003 XLS files
Group: Development/Python3

%description -n python3-module-%oname
xlwt is a library for generating spreadsheet files that are compatible
with Excel 97/2000/XP/2003, OpenOffice.org Calc, and Gnumeric. xlwt has
full support for Unicode. Excel spreadsheets can be generated on any
platform without needing Excel or a COM server. The only requirement is
Python 2.6, 2.7, or 3.3.

%package -n python3-module-%oname-examples
Summary: Examples for xlwt
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-examples
xlwt is a library for generating spreadsheet files that are compatible
with Excel 97/2000/XP/2003, OpenOffice.org Calc, and Gnumeric. xlwt has
full support for Unicode. Excel spreadsheets can be generated on any
platform without needing Excel or a COM server. The only requirement is
Python 2.6, 2.7, or 3.3.

This package contains examples for xlwt.

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

%files
%doc PKG-INFO
%python_sitelibdir/*
%exclude %python_sitelibdir/*/examples

%files examples
%python_sitelibdir/*/examples

%if_with python3
%files -n python3-module-%oname
%doc PKG-INFO
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/examples

%files -n python3-module-%oname-examples
%python3_sitelibdir/*/examples
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.8.0-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jul 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0-alt1
- Initial build for Sisyphus

