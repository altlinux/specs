%define oname xlsxwriter

%def_with python3

Name:    python-module-%oname
Version: 0.9.1
Release: alt2
Summary: A Python module for creating Excel XLSX files
License: BSD
Group:   Development/Python
Url:     https://github.com/jmcnamara/XlsxWriter
Packager: Python Development Team <python@packages.altlinux.org>

%py_provides %oname

Source: %oname-%version.tar
#VCS: https://github.com/jmcnamara/XlsxWriter
BuildArch: noarch

BuildRequires(pre): rpm-macros-sphinx
BuildRequires: python-module-alabaster
BuildRequires: python-module-docutils
BuildRequires: python-module-html5lib
BuildRequires: python-module-objects.inv
BuildRequires: python-module-pytest
BuildRequires: time

%if_with python3
BuildRequires(pre): rpm-build-python3
# Provides py.test3 for us without the minor version:
BuildRequires: python3-module-pytest >= 3.0.5-alt2
%endif

%description
XlsxWriter is a Python module for writing files in the Excel 2007+ XLSX
file format.

XlsxWriter can be used to write text, numbers, formulas and hyperlinks
to multiple worksheets and it supports features such as formatting and
many more.

%package -n python3-module-%oname
Summary: A Python module for creating Excel XLSX files
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
XlsxWriter is a Python module for writing files in the Excel 2007+ XLSX
file format.

XlsxWriter can be used to write text, numbers, formulas and hyperlinks
to multiple worksheets and it supports features such as formatting and
many more.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
XlsxWriter is a Python module for writing files in the Excel 2007+ XLSX
file format.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
XlsxWriter is a Python module for writing files in the Excel 2007+ XLSX
file format.

This package contains documentation for %oname.

%prep
%setup -q -n %oname-%version

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx dev/docs
ln -s ../objects.inv dev/docs/source/

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i ${i}3
done
popd
%endif

%python_install

%make -C dev/docs pickle
%make -C dev/docs html

cp -fR dev/docs/build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
py.test -vv
%if_with python3
pushd ../python3
python3 setup.py test
py.test3 -vv
popd
%endif

%files
%doc Changes *.md *.rst examples dev/performance
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/* dev/docs/build/html

%if_with python3
%files -n python3-module-%oname
%doc Changes *.md *.rst examples dev/performance
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Sat Jan 28 2017 Ivan Zakharyaschev <imz@altlinux.org> 0.9.1-alt2
- (.spec) adapt build to python3-module-pytest-3.0.5-alt2:
  py.test3 without minor version.

* Wed Jun 08 2016 Andrey Cherepanov <cas@altlinux.org> 0.9.1-alt1
- new version 0.9.1

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.7.3-alt1.git20150806.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.7.3-alt1.git20150806.1
- NMU: Use buildreq for BR.

* Sun Aug 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.3-alt1.git20150806
- Version 0.7.3

* Tue Mar 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.1-alt1.git20150324
- Version 0.7.1

* Fri Feb 27 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.6-alt1.git20150223
- Initial build for Sisyphus

