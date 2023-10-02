%define oname coverage

%def_without check
%def_without doc

Name: python3-module-coverage
Version: 7.3.1
Release: alt1

Summary: A tool for measuring code coverage of Python programs

License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/coverage/

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildRequires(pre): rpm-build-intro >= 2.2.5
BuildRequires(pre): rpm-build-python3

%if_with doc
BuildRequires: libenchant python3-module-sphinx
#BuildRequires: python3-module-sphinx_rtd_theme
%endif

%if_with check
BuildRequires: python3(eventlet)
BuildRequires: python3(flaky)
BuildRequires: python3(gevent)
BuildRequires: python3(mock)
BuildRequires: python3(PyContracts)
BuildRequires: python3(pytest-xdist)
BuildRequires: python3(tox)
BuildRequires: python3(unittest_mixins)
%endif

Conflicts: python-module-coverage

%description
Coverage.py is a tool for measuring code coverage of Python programs. It
monitors your program, noting which parts of the code have been
executed, then analyzes the source to identify code that could have been
executed but was not.

Coverage measurement is typically used to gauge the effectiveness of
tests. It can show which parts of your product code are being exercised
by tests, and which are not.

%package doc
Summary: Documentation for Coverage python module
Group: Development/Documentation
BuildArch: noarch

%description doc
Coverage.py is a tool for measuring code coverage of Python programs. It
monitors your program, noting which parts of the code have been
executed, then analyzes the source to identify code that could have been
executed but was not.

This package contains documentation for Coverage.py.

%prep
%setup

%build
%add_optflags -fno-strict-aliasing
%python3_build_debug

export PYTHONPATH=$PWD
%if_with doc
%make_build dochtml
#make_build pickle
%endif

%install
%python3_install
ln -s coverage3 %buildroot%_bindir/python3-coverage

%if_with doc
install -d %buildroot%_docdir/%name
cp -fR doc/_build/html/* %buildroot%_docdir/%name/
#cp -fR doc/_build/pickle %buildroot%python_sitelibdir/%oname/
%endif

%check
# don't measure coverage of ourselves
export COVERAGE_COVERAGE=no
pytest3

%files
%doc CHANGES.rst README.rst
%_bindir/coverage
%_bindir/coverage3
%_bindir/coverage-%_python3_version
%_bindir/python3-coverage
%python3_sitelibdir/%oname
%python3_sitelibdir/*.egg-info

%if_with doc
%files doc
%_docdir/%name
%endif

%changelog
* Sun Oct 01 2023 Vitaly Lipatov <lav@altlinux.ru> 7.3.1-alt1
- new version 7.3.1 (with rpmrb script)

* Sun Apr 23 2023 Vitaly Lipatov <lav@altlinux.ru> 6.5.0-alt1
- new version 6.5.0 (with rpmrb script)

* Sat Aug 27 2022 Vitaly Lipatov <lav@altlinux.ru> 6.4.2-alt1
- new version 6.4.2 (with rpmrb script)

* Sun Jul 17 2022 Vitaly Lipatov <lav@altlinux.ru> 6.3.3-alt1
- new version 6.3.3 (with rpmrb script)

* Sun Aug 15 2021 Vitaly Lipatov <lav@altlinux.ru> 5.5-alt1
- build python3 module separately, build from pypi release tarball

* Sat Aug 14 2021 Vitaly Lipatov <lav@altlinux.ru> 5.3-alt2
- drop lab subdir (see README, it is not part of the installed coverage.py code)

* Fri Sep 25 2020 Grigory Ustinov <grenka@altlinux.org> 5.3-alt1
- 5.2 -> 5.3.

* Mon Jul 06 2020 Grigory Ustinov <grenka@altlinux.org> 5.2-alt1
- 5.0.4 -> 5.2 (Closes: #38318).
- Build without docs.
- Build without check.

* Tue Mar 17 2020 Grigory Ustinov <grenka@altlinux.org> 5.0.4-alt1
- 4.5.4 -> 5.0.4.
- Enable check.

* Wed Jan 15 2020 Grigory Ustinov <grenka@altlinux.org> 4.5.4-alt3
- Bootstrap for python3.8.

* Wed Aug 21 2019 Stanislav Levin <slev@altlinux.org> 4.5.4-alt2
- Fixed testing against Pytest 5.1.

* Wed Aug 14 2019 Stanislav Levin <slev@altlinux.org> 4.5.4-alt1
- 4.5.3 -> 4.5.4.

* Mon Apr 22 2019 Stanislav Levin <slev@altlinux.org> 4.5.3-alt1
- 4.5.1 -> 4.5.3.
- Enabled testing for Python3 package.

* Wed Mar 13 2019 Igor Vlasenko <viy@altlinux.ru> 4.5.1-alt3
- NMU: added _bindir/python3-coverage compat symlink

* Wed Feb 20 2019 Stanislav Levin <slev@altlinux.org> 4.5.1-alt2
- Dropped dependency on sphinxcontrib-napoleon.

* Fri May 25 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 4.5.1-alt1
- Updated to upstream version 4.5.1.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 4.4.1-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Mon Oct 23 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 4.4.1-alt1
- Updated to upstream version 4.4.1.

* Mon Jan 02 2017 Michael Shigorin <mike@altlinux.org> 4.0-alt1.a7.git20150730.1.3
- BOOTSTRAP:
  + made python3 knob *really* work
  + added doc knob (on by default) to avoid hairy sphinx BRs

* Sun Jan 01 2017 Michael Shigorin <mike@altlinux.org> 4.0-alt1.a7.git20150730.1.2
- BOOTSTRAP: made python3 knob actually work

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0-alt1.a7.git20150730.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 4.0-alt1.a7.git20150730.1
- NMU: Use buildreq for BR.

* Fri Jul 31 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0-alt1.a7.git20150730
- Version 4.0a7

* Tue Feb 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0-alt1.a6.git20150216
- Version 4.0a6

* Sat Jul 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0-alt1.a0.hg20140719
- New snapshot

* Fri Jul 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0-alt1.a0.hg20140708
- Version 4.0a0

* Thu Nov 28 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.1-alt1.hg20131027
- Version 3.7.1

* Mon Sep 16 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt2.a1.hg20130915
- Version 3.6.1a1

* Sun Feb 17 2013 Aleksey Avdeev <solo@altlinux.ru> 3.6.1-alt2.a0.hg20130202
- Fix build with Python3-3.3.x

* Wed Feb 13 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt1.a0.hg20130202
- Version 3.6.1a0

* Tue Apr 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.2-alt2.b1.hg20120329
- New snapshot
- Avoid requirement for %name on Python 3

* Wed Feb 08 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5.2-alt2.b1.hg20111031
- Build with Python3

* Fri Dec 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.2-alt1.b1.hg20111031
- Version 3.5.2b1
- Added pickles subpackage

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5-alt1.a1.hg20110502.1
- Rebuild with Python-2.7

* Tue May 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5-alt1.a1.hg20110502
- New snapshot

* Fri Mar 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5-alt1.a1.hg20101120.1
- Rebuilt for debuginfo

* Mon Nov 22 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5-alt1.a1.hg20101120
- Version 3.5a1

* Mon Jul 26 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4-alt1.a1.hg20100725
- Version 3.4a1

* Wed Nov 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.0b1-alt1.hg20090922.1
- Rebuilt with python 2.6

* Wed Sep 23 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.0b1-alt1.hg20090922
- Initial build for Sisyphus

