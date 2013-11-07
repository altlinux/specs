%define oname pandas

Name: python-module-%oname
Version: 0.12.0
Release: alt3

Summary: Python Data Analysis Library
License: BSD
Group: Development/Python

Url: http://pandas.pydata.org/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python
BuildPreReq: libnumpy-devel python-module-Cython
BuildPreReq: python-module-sphinx-devel python-module-json ipython

%setup_python_module %oname

%description
pandas is an open source, BSD-licensed library providing
high-performance, easy-to-use data structures and data analysis tools
for the Python programming language.

%package tests
Summary: Tests for pandas
Group: Development/Python
Requires: %name = %EVR

%description tests
pandas is an open source, BSD-licensed library providing
high-performance, easy-to-use data structures and data analysis tools
for the Python programming language.

This package contains tests for pandas.

%package docs
Summary: Documentation for pandas
Group: Development/Documentation
BuildArch: noarch

%description docs
pandas is an open source, BSD-licensed library providing
high-performance, easy-to-use data structures and data analysis tools
for the Python programming language.

This package contains documentation for pandas.

%prep
%setup

%prepare_sphinx doc
ln -s ../objects.inv doc/source/

sed -i 's|@PYPATH@|%buildroot%python_sitelibdir|' doc/make.py

%build
%add_optflags -fno-strict-aliasing
%python_build_debug

%install
%python_install

# It is the file in the package whose name matches the format emacs or vim uses 
# for backup and autosave files. It may have been installed by  accident.
find $RPM_BUILD_ROOT \( -name '.*.swp' -o -name '#*#' -o -name '*~' \) -print -delete
# failsafe cleanup if the file is declared as %%doc
find . \( -name '.*.swp' -o -name '#*#' -o -name '*~' \) -print -delete

#pushd doc
#./make.py html
#popd

%files
%doc README.rst RELEASE.md
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests
%exclude %python_sitelibdir/*/*/test*

%files tests
%python_sitelibdir/*/tests
%python_sitelibdir/*/*/test*

%files docs
#doc doc/build/html
%doc doc/source
%doc examples

%changelog
* Thu Nov 07 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.12.0-alt3
- Applied repocop patch

* Wed Nov 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.12.0-alt2
- Fixed build

* Wed Sep 18 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.12.0-alt1
- Version 0.12.0

* Wed Apr 03 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.1-alt1
- Initial build for Sisyphus

