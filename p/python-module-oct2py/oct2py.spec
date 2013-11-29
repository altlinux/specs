%define oname oct2py

Name: python-module-%oname
Version: 1.1.1
Release: alt1

Summary: Python to GNU Octave bridge --> run m-files from python
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/oct2py

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

%setup_python_module %oname

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-scipy octave

%description
Oct2py is a means to seemlessly call m-files and Octave functions from
python. It manages the Octave session for you, sharing data behind the
scenes using MAT files.

If you want to run legacy m-files, do not have MATLAB(r), and do not
fully trust a code translator, this is your library.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Oct2py is a means to seemlessly call m-files and Octave functions from
python. It manages the Octave session for you, sharing data behind the
scenes using MAT files.

If you want to run legacy m-files, do not have MATLAB(r), and do not
fully trust a code translator, this is your library.

This package contains tests for %oname.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%files
%doc *.txt *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%changelog
* Fri Nov 29 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt1
- Version 1.1.1

* Fri Nov 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1
- Initial build for Sisyphus

