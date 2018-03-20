%define _unpackaged_files_terminate_build 1
%define oname pytest

%def_with docs
%def_with check

Name: python-module-%oname
Version: 3.4.2
Release: alt1%ubt

Summary: py.test, a simple and popular testing tool for Python
License: MIT
Group: Development/Python
# Source-git: https://github.com/pytest-dev/pytest.git
Url: https://pypi.python.org/pypi/pytest

Source: %name-%version.tar
Patch: %oname-3.2.1-alt-docs.patch

BuildRequires(pre): rpm-build-ubt
BuildRequires(pre): rpm-build-python
BuildRequires(pre): rpm-build-python3
BuildRequires: python-module-setuptools
BuildRequires: python-module-setuptools_scm
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-setuptools_scm

%if_with check
BuildRequires: /dev/pts
BuildRequires: python-module-argcomplete
BuildRequires: python-module-attrs
BuildRequires: python-module-decorator
BuildRequires: python-module-funcsigs
BuildRequires: python-module-hypothesis
BuildRequires: python-module-mock
BuildRequires: python-module-nose
BuildRequires: python-module-numpy
BuildRequires: python-module-pexpect
BuildRequires: python-module-pluggy
BuildRequires: python-module-requests
BuildRequires: python-module-tox
BuildRequires: python-module-virtualenv
BuildRequires: python3-module-argcomplete
BuildRequires: python3-module-attrs
BuildRequires: python3-module-decorator
BuildRequires: python3-module-funcsigs
BuildRequires: python3-module-hypothesis
BuildRequires: python3-module-mock
BuildRequires: python3-module-nose
BuildRequires: python3-module-numpy
BuildRequires: python3-module-pexpect
BuildRequires: python3-module-pluggy
BuildRequires: python3-module-tox
BuildRequires: python3-module-requests
BuildRequires: python3-module-virtualenv
%endif

%if_with docs
BuildRequires: python-module-attrs
BuildRequires: python-module-numpy
BuildRequires: python-module-funcsigs
BuildRequires: python-module-pluggy
BuildRequires(pre): rpm-macros-sphinx
BuildPreReq: python-module-alabaster python-module-docutils python-module-html5lib python-module-objects.inv python-module-py
%endif

%py_requires py
%py_requires funcsigs

BuildArch: noarch

%global long_desc is a command line tool to collect, run and report about\
automated tests. It runs well on Linux, Windows and OSX and on Python\
2.4 through to 3.1 versions. It is used in many projects, ranging from\
running 10 thousands of tests to a few inlined tests on a command line\
script. As of version 1.2 you can also generate a\
no-dependency py.test-equivalent standalone script that you can\
distribute along with your application.

%description
py.test %long_desc

Install pytest package if you need the extra /usr/bin/pytest executable
in addition to the usual /usr/bin/py.test.

%package -n pytest
Summary: Additional executable for py.test
Group: Development/Python
Requires: python-module-%oname = %EVR
# It simply has executables with the same filename:
Conflicts: python-module-logilab-common < 1.0.2-alt2.hg20150708

%description -n pytest
py.test is a simple and popular testing tool for Python.
It is packaged as python-module-%oname by ALT.

This package contains the extra /usr/bin/pytest executable
in addition to /usr/bin/py.test, which has always been packaged
before.

This separate package has been made to track the dependencies on this
additional executable.

%package -n python3-module-%oname
Summary: py.test3, the simple and popular testing tool for Python 3
Group: Development/Python3

%description -n python3-module-%oname
py.test3 %long_desc

Install pytest3 package if you need the extra /usr/bin/pytest3 executable
in addition to the usual /usr/bin/py.test3
(which used to be /usr/bin/py.test-3.M).

%package -n pytest3
Summary: Additional executable for py.test3
Group: Development/Python3
Requires: python3-module-%oname = %EVR
# It simply has executables with the same filename:
Conflicts: python3-module-logilab-common < 1.0.2-alt2.hg20150708

%description -n pytest3
py.test3 is a simple and popular testing tool, the Python3 variant.
It is packaged as python3-module-%oname by ALT.

This package contains the extra /usr/bin/pytest3 executable
in addition to /usr/bin/py.test3, which has always been packaged
before (as /usr/bin/py.test-3.N).

This separate package has been made to track the dependencies on this
additional executable.

%package docs
Summary: Documentation for py.test
Group: Development/Documentation

%description docs
py.test is a command line tool to collect, run and report about
automated tests. It runs well on Linux, Windows and OSX and on Python
2.4 through to 3.1 versions. It is used in many projects, ranging from
running 10 thousands of tests to a few inlined tests on a command line
script. As of version 1.2 you can also generate a
no-dependency py.test-equivalent standalone script that you can
distribute along with your application.

This package contains documentation for py.test.

%package pickles
Summary: Pickles for py.test
Group: Development/Python

%description pickles
py.test is a command line tool to collect, run and report about
automated tests. It runs well on Linux, Windows and OSX and on Python
2.4 through to 3.1 versions. It is used in many projects, ranging from
running 10 thousands of tests to a few inlined tests on a command line
script. As of version 1.2 you can also generate a
no-dependency py.test-equivalent standalone script that you can
distribute along with your application.

This package contains pickles for py.test.

%prep
%setup
%patch0 -p1

rm -rf ../python3
cp -a . ../python3

%if_with docs
%prepare_sphinx doc
ln -s ../objects.inv doc/en/
%endif

%build
# SETUPTOOLS_SCM_PRETEND_VERSION: when defined and not empty,
# its used as the primary source for the version number in which
# case it will be a unparsed string
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python_build

pushd ../python3
%python3_build
popd

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version

pushd ../python3
%python3_install
mv %buildroot%_bindir/py.test -T %buildroot%_bindir/py.test3
mv %buildroot%_bindir/pytest -T %buildroot%_bindir/pytest3
popd

%python_install

%if_with docs
export PYTHONPATH=%buildroot%python_sitelibdir
%make -C doc/en html
%make -C doc/en pickle

install -d %buildroot%python_sitelibdir/%oname
cp -fR doc/en/_build/pickle %buildroot%python_sitelibdir/%oname/
%endif

%check
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
export PYTHONPATH=%buildroot%python_sitelibdir
%buildroot%_bindir/pytest -v testing

pushd ../python3
export PYTHONPATH=%buildroot%python3_sitelibdir
# due to
# https://github.com/pytest-dev/pytest/issues/2673
# run pdb/terminal tests separately from other
%buildroot%_bindir/pytest3 -v testing \
--ignore=testing/test_pdb.py --ignore=testing/test_terminal.py --ignore=testing/test_unittest.py
%buildroot%_bindir/pytest3 -v \
testing/test_pdb.py testing/test_terminal.py testing/test_unittest.py
popd

%files
%doc AUTHORS LICENSE *.rst
%_bindir/py.test
%python_sitelibdir/*
%if_with docs
%exclude %python_sitelibdir/%oname/pickle
%endif

%files -n pytest
%_bindir/pytest

%if_with docs

%files pickles
%python_sitelibdir/%oname/pickle

%files docs
%doc doc/en/_build/html/*

%endif

%files -n python3-module-%oname
%doc AUTHORS LICENSE *.rst
%_bindir/py.test3
%python3_sitelibdir/*

%files -n pytest3
%_bindir/pytest3

%changelog
* Tue Mar 20 2018 Stanislav Levin <slev@altlinux.org> 3.4.2-alt1%ubt
- 3.2.1 -> 3.4.2

* Wed Aug 16 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 3.2.1-alt1
- Updated to upstream version 3.2.1.

* Thu Jan 26 2017 Ivan Zakharyaschev <imz@altlinux.org> 3.0.5-alt3
- %%check: enabled Python3 tests.

* Thu Jan 26 2017 Ivan Zakharyaschev <imz@altlinux.org> 3.0.5-alt2
- Separate packages for the extra /usr/bin/pytest* to track their
  users (ALT#33028).
- /usr/bin/py.test3 - Avoid dep on minor version of python3 in the filename:
  + no need to rebuild with the change of python3's minor version;
  + no need for python3 to preprocess the .spec.
- (.spec) BuildPreReq for manually written build deps.
- (.spec) put Requires before any specs how to build (they are
  externally visible).
- (.spec) A bit safer scripting.
- (.spec) more %%if_with python3 (to avoid unwanted calls to python3;
  just in case).

* Sat Jan 21 2017 Anton Midyukov <antohami@altlinux.org> 3.0.5-alt1
- New version 3.0.5
- srpm build

* Sat Mar 19 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.8.0-alt1.dev4.git20150807.2.workaround
- Rebuild with python3-3.5 to update the executable name (this is a
  workaround; this should be fixed not to depend on the minor version).
- This rebuild (with rpm-build-python3-0.1.10) will also switch to the
  new python3(*) reqs.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.8.0-alt1.dev4.git20150807.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.8.0-alt1.dev4.git20150807.1
- NMU: Use buildreq for BR.

* Sat Aug 08 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.0-alt1.dev4.git20150807
- New snapshot

* Tue Jul 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.0-alt1.dev4.git20150726
- Version 2.8.0.dev4

* Fri Oct 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7.0-alt1.dev1.hg20141030
- Version 2.7.0.dev1

* Sat Oct 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.4-alt2.dev1.hg20141025
- New snapshot

* Mon Oct 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.4-alt2.dev1.hg20141009
- Added requirement on py

* Fri Oct 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.4-alt1.dev1.hg20141009
- Version 2.6.4.dev1

* Tue Jul 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.2-alt1.dev1.hg20140109
- Version 2.5.2.dev1

* Fri Nov 29 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.3-alt1.dev2.hg20131122
- Version 2.4.3.dev2

* Thu Sep 19 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.0-alt1.dev12.hg20130909
- Version 2.4.0.dev12

* Tue Apr 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.5.dev8-alt1.hg20130328
- Version 2.3.5.dev8

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 2.3.0.dev10-alt1.hg20120813.1
- Rebuild with Python-3.3

* Wed Aug 15 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.0.dev10-alt1.hg20120813
- Version 2.3.0.dev10

* Fri Apr 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.4.dev2-alt1.hg20120331
- Version 2.2.4.dev2
- Added module for Python 3

* Fri Jan 27 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.2.dev6-alt1.hg20110120
- Version 2.2.2.dev6

* Sat Nov 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.0-alt2.hg20111119
- Fixed buildreq

* Fri Nov 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.0-alt1.hg20111119
- Version 2.2.0
- Disabled conflict with py

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0.3-alt1.hg20110501.1
- Rebuild with Python-2.7

* Tue May 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.3-alt1.hg20110501
- Version 2.0.3

* Tue Apr 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.hg20101120.2
- Rebuilt with python-module-sphinx-devel

* Mon Nov 22 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.hg20101120.1
- Added explicit conflict with py

* Sun Nov 21 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.hg20101120
- Initial build for Sisyphus

