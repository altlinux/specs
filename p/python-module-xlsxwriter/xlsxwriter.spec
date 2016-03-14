%define oname xlsxwriter

%def_with python3

Name: python-module-%oname
Version: 0.7.3
Release: alt1.git20150806.1.1
Summary: A Python module for creating Excel XLSX files
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/XlsxWriter/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/jmcnamara/XlsxWriter.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
%endif

%py_provides %oname

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-pluggy python-module-py python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-multiprocessing python-modules-unittest python3 python3-base python3-module-pluggy python3-module-py python3-module-setuptools xz
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-objects.inv python-module-pytest python3-module-pytest rpm-build-python3 time

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

