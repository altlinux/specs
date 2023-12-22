%define _unpackaged_files_terminate_build 1

%define oname pandas

%def_with bootstrap
%def_disable check
%def_without docs

Name: python3-module-%oname
Version: 2.1.4
Release: alt1.1
Summary: Python Data Analysis Library
License: BSD-3-Clause
Group: Development/Python3

Url: https://pandas.pydata.org

# https://github.com/pandas-dev/pandas.git
Source: %name-%version.tar
Patch1: pandas-fix-generate-version.patch
Patch2: pandas-2.1.4-alt-remove-tests-dependency.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: gcc-c++
BuildRequires: python3-devel
BuildRequires: libnumpy-py3-devel python3-module-Cython python3-module-numpy
BuildRequires: python3(scipy) python3(xlrd)
BuildRequires: python3-module-mesonpy
BuildRequires: meson
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
%if_enabled check
BuildRequires: xvfb-run
BuildRequires: python3(openpyxl)
BuildRequires: python3-module-numpy-testing python3(tables.tests)
%endif
%if_with docs
BuildRequires(pre): rpm-macros-sphinx3
BuildRequires: python3-module-objects.inv
BuildRequires: pandoc
BuildRequires: xvfb-run python3(nbsphinx)
BuildRequires: python3-module-notebook
BuildRequires: python3(numpydoc) python3(matplotlib.sphinxext) python3(matplotlib.sphinxext.plot_directive)
BuildRequires: python3-module-sphinx python3-module-sphinx-sphinx-build-symlink
%endif

%add_python3_req_skip feather
%add_python3_req_skip numba
%add_python3_req_skip numba.extending
%add_python3_req_skip pyarrow
%py3_requires pytz dateutil numpy sqlalchemy numexpr
%py3_requires scipy bs4 xlrd openpyxl xlsxwriter xlwt
%py3_requires tables
%if_without bootstrap
BuildRequires: python3-module-scikits.statsmodels
%endif

%description
pandas is an open source, BSD-licensed library providing
high-performance, easy-to-use data structures and data analysis tools
for the Python programming language.

%package tests
Summary: Tests for pandas
Group: Development/Python3
Requires: %name = %EVR
%py3_requires numpy.ma.testutils pymysql psycopg2
%if_without bootstrap
%py3_requires statsmodels.stats.multitest
%endif

%description tests
pandas is an open source, BSD-licensed library providing
high-performance, easy-to-use data structures and data analysis tools
for the Python programming language.

This package contains tests for pandas.

%package docs
Summary: Documentation for pandas
Group: Development/Documentation
BuildArch: noarch
Requires: %name = %EVR

%description docs
pandas is an open source, BSD-licensed library providing
high-performance, easy-to-use data structures and data analysis tools
for the Python programming language.

This package contains documentation for pandas.

%prep
%setup
%patch1 -p1
%patch2 -p1

sed -i "s/@VERSION@/%version/" generate_version.py

%if_with docs
%prepare_sphinx3 doc
ln -s ../objects.inv doc/source/
%endif

%build
%add_optflags -fno-strict-aliasing
%pyproject_build

%install
%pyproject_install

%if_with docs
pushd doc
PYTHONPATH=$(echo ../build/lib.*) xvfb-run ./make.py html
popd
%endif

%check
xvfb-run python3 setup.py test

%files
%doc *.md
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info
%exclude %python3_sitelibdir/*/tests
%exclude %python3_sitelibdir/*/testing.py
%exclude %python3_sitelibdir/*/_testing*
%exclude %python3_sitelibdir/*/conftest.py
%exclude %python3_sitelibdir/*/*/test*
%exclude %python3_sitelibdir/*/*/_test*
%exclude %python3_sitelibdir/*/*/conftest.*
%exclude %python3_sitelibdir/*/*/*/test*
%exclude %python3_sitelibdir/*/*/*/_test*

%files tests
%python3_sitelibdir/*/tests
%python3_sitelibdir/*/testing.py
%python3_sitelibdir/*/_testing*
%python3_sitelibdir/*/conftest.py
%python3_sitelibdir/*/*/test*
%python3_sitelibdir/*/*/_test*
%python3_sitelibdir/*/*/conftest.*
%python3_sitelibdir/*/*/*/test*
%python3_sitelibdir/*/*/*/_test*

%if_with docs
%files docs
%doc doc/build/html
%endif

%changelog
* Fri Dec 22 2023 Ivan A. Melnikov <iv@altlinux.org> 2.1.4-alt1.1
- NMU: numba is an optional dependency, so let's skip it
  (fixes FTBFS on loongarch64 and riscv64).

* Thu Dec 21 2023 Anton Vyatkin <toni@altlinux.org> 2.1.4-alt1
- New version 2.1.4.

* Mon Dec 06 2021 Grigory Ustinov <grenka@altlinux.org> 1.3.1-alt3
- Bootstrap for python3.10.

* Tue Aug 17 2021 Vitaly Lipatov <lav@altlinux.ru> 1.3.1-alt2
- NMU: statsmodels is a dev dependency (see requirements-dev.txt)

* Fri Aug 06 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.3.1-alt1
- Updated to upstream version 1.3.1.

* Wed Mar 17 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.2.3-alt1
- Updated to upstream version 1.2.3.
- Disabled bootstrapping.

* Mon Feb 08 2021 Grigory Ustinov <grenka@altlinux.org> 1.2.0-alt2
- Bootstrap for python3.9.

* Fri Jan 15 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.2.0-alt1
- Updated to upstream version 1.2.0.

* Mon Nov 09 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.1-alt5
- Removed dependency from python3-module-pandas to python3-module-pandas-tests (Closes: #39222).

* Fri Nov 06 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.1-alt4
- Updated runtime dependencies.

* Wed Nov 04 2020 Vitaly Lipatov <lav@altlinux.ru> 1.1.1-alt3
- NMU: fix require tests subpackage from the main package

* Tue Sep 08 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.1-alt2
- Updated runtime dependencies.

* Tue Aug 25 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.1-alt1
- Updated to upstream version 1.1.1.

* Thu Jan 16 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 0.25.3-alt1
- Updated to upstream version 0.25.3 (Closes: #37445).
- Built python-2 subpackage separately.

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

