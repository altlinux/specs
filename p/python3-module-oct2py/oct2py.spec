%define oname oct2py

Name: python3-module-%oname
Version: 1.5.0
Release: alt4

Summary: Python to GNU Octave bridge --> run m-files from python
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/oct2py
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-sphinx python3-module-sphinx-bootstrap-theme
BuildRequires: python3-module-numpydoc


%description
Oct2py is a means to seemlessly call m-files and Octave functions from
python. It manages the Octave session for you, sharing data behind the
scenes using MAT files.

If you want to run legacy m-files, do not have MATLAB(r), and do not
fully trust a code translator, this is your library.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
Oct2py is a means to seemlessly call m-files and Octave functions from
python. It manages the Octave session for you, sharing data behind the
scenes using MAT files.

If you want to run legacy m-files, do not have MATLAB(r), and do not
fully trust a code translator, this is your library.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python3

%description pickles
Oct2py is a means to seemlessly call m-files and Octave functions from
python. It manages the Octave session for you, sharing data behind the
scenes using MAT files.

If you want to run legacy m-files, do not have MATLAB(r), and do not
fully trust a code translator, this is your library.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation

%description docs
Oct2py is a means to seemlessly call m-files and Octave functions from
python. It manages the Octave session for you, sharing data behind the
scenes using MAT files.

If you want to run legacy m-files, do not have MATLAB(r), and do not
fully trust a code translator, this is your library.

This package contains documentation for %oname.

%prep
%setup

sed -i 's|@VERSION@|%version|' docs/conf.py

%build
%python3_build_debug

pushd docs
sphinx-build-3 -b pickle -d build/doctrees . build/pickle
sphinx-build-3 -b html -d build/doctrees . build/html
popd

%install
%python3_install

cp -fR docs/build/pickle %buildroot%python3_sitelibdir/%oname/

%files
%doc *.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests
%exclude %python3_sitelibdir/*/*/tests
%exclude %python3_sitelibdir/*/pickle

%files pickles
%python3_sitelibdir/*/pickle

%files docs
%doc docs/build/html/*

%files tests
%python3_sitelibdir/*/tests
%python3_sitelibdir/*/*/tests


%changelog
* Wed Nov 06 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.5.0-alt4
- disable python2

* Fri May 11 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.5.0-alt3
- rebuild for python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.5.0-alt2.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.5.0-alt2.1
- NMU: Use buildreq for BR.

* Tue Jul 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt2
- Moved all tests into tests subpackage

* Mon Jul 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt1
- Version 1.5.0
- Added module for Python 3

* Fri Nov 29 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt1
- Version 1.1.1

* Fri Nov 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1
- Initial build for Sisyphus

