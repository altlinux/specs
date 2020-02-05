%define _unpackaged_files_terminate_build 1

%define oname pandas

%def_disable check

Name: python-module-%oname
Version: 0.23.4
Release: alt3

Summary: Python Data Analysis Library
License: BSD
Group: Development/Python

Url: http://pandas.pydata.org/

# https://github.com/pandas-dev/pandas.git
Source: %name-%version.tar
Patch1: %oname-alt-static-variables.patch

BuildRequires(pre): rpm-build-python
BuildRequires: python-devel
BuildRequires: libnumpy-devel python-module-Cython python-module-notebook python-module-numpy-testing python-module-pathlib
BuildRequires: gcc-c++
BuildRequires: xvfb-run python2.7(nbsphinx)

%setup_python_module %oname
%py_requires pytz pandas.util.testing dateutil numpy sqlalchemy numexpr
%py_requires scipy boto bs4 xlrd openpyxl xlsxwriter xlwt httplib2
%py_requires oauth2client apiclient gflags tables

%description
pandas is an open source, BSD-licensed library providing
high-performance, easy-to-use data structures and data analysis tools
for the Python programming language.

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

%check
xvfb-run python setup.py test

%files
%doc *.md
%python_sitelibdir/%oname
%python_sitelibdir/%oname-%version-py*.egg-info
%exclude %python_sitelibdir/*/tests
%exclude %python_sitelibdir/*/*/test*

%files tests
%python_sitelibdir/*/tests
%python_sitelibdir/*/*/test*

%changelog
* Wed Feb 05 2020 Vitaly Lipatov <lav@altlinux.ru> 0.23.4-alt3
- Drop wrong statsmodels.stats.multitest require

* Thu Jan 16 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 0.23.4-alt2
- Rebuilt without python-3 support.

* Wed Aug 08 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.23.4-alt1
- Updated to upstream version 0.23.4.

* Mon Mar 26 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.22.0-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Tue Mar 13 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.22.0-alt1
- Updated to upstream version 0.22.0.
- Updated runtime dependencies of python-3 package.

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

