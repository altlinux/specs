%define oname xlsxwriter

%def_with python3

Name: python-module-%oname
Version: 0.6.6
Release: alt1.git20150223
Summary: A Python module for creating Excel XLSX files
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/XlsxWriter/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/jmcnamara/XlsxWriter.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
%endif

%py_provides %oname

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
%setup

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
py.test-%_python3_version -vv
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
* Fri Feb 27 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.6-alt1.git20150223
- Initial build for Sisyphus

