%define oname pandas

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.21.0
Release: alt2

Summary: Python Data Analysis Library
License: BSD
Group: Development/Python

Url: http://pandas.pydata.org/

# https://github.com/pandas-dev/pandas.git
Source: %name-%version.tar
Patch1: %oname-%version-alt-docs.patch

BuildRequires(pre): rpm-macros-sphinx
BuildRequires(pre): rpm-build-python
BuildRequires: python-devel
BuildRequires: libnumpy-devel python-module-Cython python-module-notebook python-module-numpy-testing python-module-pathlib
BuildRequires: python-module-objects.inv
BuildRequires: gcc-c++ pandoc
BuildRequires: xvfb-run python2.7(nbsphinx)
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: libnumpy-py3-devel python3-module-Cython python3-module-notebook python3-module-numpy-testing
BuildRequires: xvfb-run python3(nbsphinx)
BuildRequires: python3(scipy) python3(xlrd) python3(tables.tests) python3(openpyxl)
%endif

%setup_python_module %oname
%py_requires pytz pandas.util.testing dateutil numpy sqlalchemy numexpr
%py_requires scipy boto bs4 xlrd openpyxl xlsxwriter xlwt httplib2
%py_requires oauth2client apiclient gflags tables
%py_requires statsmodels.stats.multitest

%description
pandas is an open source, BSD-licensed library providing
high-performance, easy-to-use data structures and data analysis tools
for the Python programming language.

%if_with python3
%package -n python3-module-%oname
Summary: Python Data Analysis Library
Group: Development/Python3
%add_python3_req_skip feather
%py3_requires pytz pandas.util.testing dateutil numpy sqlalchemy numexpr
%py3_requires scipy boto bs4 xlrd openpyxl xlsxwriter xlwt httplib2 rpy2
%py3_requires oauth2client apiclient gflags tables statsmodels
%py3_requires statsmodels.stats.multitest

%description -n python3-module-%oname
pandas is an open source, BSD-licensed library providing
high-performance, easy-to-use data structures and data analysis tools
for the Python programming language.

%package -n python3-module-%oname-tests
Summary: Tests for pandas
Group: Development/Python3
Requires: python3-module-%oname = %EVR
%py3_requires numpy.ma.testutils pymysql psycopg2

%description -n python3-module-%oname-tests
pandas is an open source, BSD-licensed library providing
high-performance, easy-to-use data structures and data analysis tools
for the Python programming language.

This package contains tests for pandas.

%package -n python3-module-%oname-docs
Summary: Documentation for pandas
Group: Development/Documentation
BuildArch: noarch

%description -n python3-module-%oname-docs
pandas is an open source, BSD-licensed library providing
high-performance, easy-to-use data structures and data analysis tools
for the Python programming language.

This package contains documentation for pandas.
%endif

%package tests
Summary: Tests for pandas
Group: Development/Python
Requires: %name = %EVR
%py_requires numpy.ma.testutils pymysql psycopg2

%description tests
pandas is an open source, BSD-licensed library providing
high-performance, easy-to-use data structures and data analysis tools
for the Python programming language.

This package contains tests for pandas.

%prep
%setup
%patch1 -p1

# fix version info
sed -i \
	-e "s/git_refnames\s*=\s*\"[^\"]*\"/git_refnames = \" \(tag: v%version\)\"/" \
	%oname/_version.py

%if_with python3
cp -fR . ../python3
pushd ../python3
%prepare_sphinx doc
ln -s ../objects.inv doc/source/

sed -i 's|@PYPATH@|%buildroot%python3_sitelibdir|' doc/make.py
popd
%endif

%build
%add_optflags -fno-strict-aliasing
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

# It is the file in the package whose name matches the format emacs or vim uses 
# for backup and autosave files. It may have been installed by  accident.
find $RPM_BUILD_ROOT \( -name '.*.swp' -o -name '#*#' -o -name '*~' \) -print -delete
# failsafe cleanup if the file is declared as %%doc
find . \( -name '.*.swp' -o -name '#*#' -o -name '*~' \) -print -delete

pushd doc
PYTHONPATH=$(echo ../build/lib.*) xvfb-run ./make.py html
popd
popd
%endif

%check
xvfb-run python setup.py test
%if_with python3
pushd ../python3
xvfb-run python3 setup.py test
popd
%endif

%files
%doc *.md
%python_sitelibdir/%oname
%python_sitelibdir/%oname-%version-py*.egg-info
%exclude %python_sitelibdir/*/tests
%exclude %python_sitelibdir/*/*/test*

%files tests
%python_sitelibdir/*/tests
%python_sitelibdir/*/*/test*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-py*.egg-info
%exclude %python3_sitelibdir/*/tests
%exclude %python3_sitelibdir/*/*/test*
%exclude %python3_sitelibdir/*/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%python3_sitelibdir/*/*/test*
%python3_sitelibdir/*/*/*/test*

%files -n python3-module-%oname-docs
%doc ../python3/doc/build/html
#doc doc/source
#doc examples
%endif

%changelog
* Thu Nov 23 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.21.0-alt2
- Updated runtime dependencies of python-2 package.

* Tue Nov 07 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.21.0-alt1
- Updated to upstream version 0.21.0.

* Fri Oct 20 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.20.3-alt2
- Fixed version in egg-info.
- Explicitely stated egg-info including valid version.

* Thu Oct 19 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.20.3-alt1
- Updated to upstream version 0.20.3.
- Fixed version in egg-info.

* Fri Aug 18 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.20.2-alt3
- Updated build dependencies for python-3 build.

* Tue Jul 25 2017 Terechkov Evgenii <evg@altlinux.org> 0.20.2-alt2
- Skip findreq on some modules

* Wed Jun 21 2017 Terechkov Evgenii <evg@altlinux.org> 0.20.2-alt1
- 0.20.2

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.16.2-alt1.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.16.2-alt1.1
- NMU: Use buildreq for BR.

* Sun Aug 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.16.2-alt1
- Version 0.16.2

* Sun Mar 01 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.15.2-alt1
- Version 0.15.2

* Tue Nov 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.15.1-alt1
- Version 0.15.1

* Tue Jul 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14.1-alt2
- Added module for Python 3

* Mon Jul 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14.1-alt1
- Version 0.14.1

* Thu Nov 07 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.12.0-alt3
- Applied repocop patch

* Wed Nov 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.12.0-alt2
- Fixed build

* Wed Sep 18 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.12.0-alt1
- Version 0.12.0

* Wed Apr 03 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.1-alt1
- Initial build for Sisyphus

