%define _unpackaged_files_terminate_build 1
%define pypi_name pytest

%define tomli %(%__python3 -c 'import sys;print(int(sys.version_info < (3, 11)))')
%define exceptiongroup %(%__python3 -c 'import sys;print(int(sys.version_info < (3, 11)))')

%def_with check

Name: python3-module-%pypi_name
Version: 7.2.0
Release: alt1

Summary: Python test framework
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pytest/
VCS: https://github.com/pytest-dev/pytest.git

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(setuptools_scm)

%if_with check
# install_requires:
%if %tomli
BuildRequires: python3(tomli)
%endif
%if %exceptiongroup
BuildRequires: python3(exceptiongroup)
%endif
BuildRequires: python3(attr)
BuildRequires: python3(iniconfig)
BuildRequires: python3(packaging)
BuildRequires: python3(pluggy)

# extras_require:
BuildRequires: python3(argcomplete)
BuildRequires: python3(hypothesis)
BuildRequires: python3(mock)
BuildRequires: python3(requests)
BuildRequires: python3(xmlschema)
BuildRequires: python3-module-Pygments > 2.4.2

BuildRequires: /dev/pts
BuildRequires: /dev/shm

# optional
BuildRequires: python3(decorator)
BuildRequires: python3(jinja2)
BuildRequires: python3(numpy)
BuildRequires: python3(pexpect)
%endif

BuildArch: noarch

%py3_requires packaging
%if %tomli
%py3_requires tomli
%endif
%if %exceptiongroup
%py3_requires exceptiongroup
%endif

# don't provide limited compat shim for python3(py) from python3-module-py
%add_findprov_skiplist %python3_sitelibdir/py.py

%description
The pytest framework makes it easy to write small tests, yet
scales to support complex functional testing for applications and libraries.

%package -n pytest3
Summary: Additional executable for pytest
Group: Development/Python3
Requires: python3-module-%pypi_name = %EVR
# It simply has executables with the same filename:
Conflicts: python3-module-logilab-common < 1.0.2-alt2.hg20150708

%description -n pytest3
The pytest framework makes it easy to write small tests, yet
scales to support complex functional testing for applications and libraries.

%prep
%setup
%patch -p1
# setuptools_scm implements a file_finders entry point which returns all files
# tracked by SCM.
if [ ! -d .git ]; then
    git init
    git config user.email author@example.com
    git config user.name author
    git add .
    git commit -m 'release'
    git tag '%version'
fi

%build
%pyproject_build

%install
%pyproject_install
mv %buildroot%_bindir/py.test -T %buildroot%_bindir/py.test3
mv %buildroot%_bindir/pytest -T %buildroot%_bindir/pytest3
ln -s py.test3 %buildroot%_bindir/py.test-3
ln -s pytest3 %buildroot%_bindir/pytest-3

%check
# add workaround for https://github.com/pytest-dev/pytest/issues/6297
export TERM=xterm
%tox_check_pyproject -- -vra

%files
%doc CHANGELOG.rst README.rst
%_bindir/py.test3
%_bindir/py.test-3
%python3_sitelibdir/pytest/
%python3_sitelibdir/_pytest/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/
%python3_sitelibdir/py.py
%python3_sitelibdir/__pycache__/py.*

%files -n pytest3
%_bindir/pytest3
%_bindir/pytest-3

%changelog
* Fri Nov 11 2022 Stanislav Levin <slev@altlinux.org> 7.2.0-alt1
- 7.1.3 -> 7.2.0.

* Wed Sep 21 2022 Stanislav Levin <slev@altlinux.org> 7.1.3-alt1
- 7.1.2 -> 7.1.3.

* Wed Jul 20 2022 Stanislav Levin <slev@altlinux.org> 7.1.2-alt1
- 7.1.1 -> 7.1.2.

* Fri Mar 18 2022 Stanislav Levin <slev@altlinux.org> 7.1.1-alt1
- 7.0.1 -> 7.1.1.

* Fri Feb 25 2022 Stanislav Levin <slev@altlinux.org> 7.0.1-alt1
- 6.2.5 -> 7.0.1.

* Wed Sep 08 2021 Stanislav Levin <slev@altlinux.org> 6.2.5-alt1
- 6.2.4 -> 6.2.5.

* Thu Jul 29 2021 Stanislav Levin <slev@altlinux.org> 6.2.4-alt2
- Fixed build without check (thanks to grenka@).

* Fri May 07 2021 Stanislav Levin <slev@altlinux.org> 6.2.4-alt1
- 6.2.3 -> 6.2.4.

* Thu Apr 15 2021 Stanislav Levin <slev@altlinux.org> 6.2.3-alt1
- 6.1.1 -> 6.2.3.

* Mon Oct 12 2020 Stanislav Levin <slev@altlinux.org> 6.1.1-alt1
- 6.0.1 -> 6.1.1.

* Mon Aug 03 2020 Stanislav Levin <slev@altlinux.org> 6.0.1-alt1
- 5.4.3 -> 6.0.1.

* Wed Jun 03 2020 Stanislav Levin <slev@altlinux.org> 5.4.3-alt1
- 5.4.1 -> 5.4.3.

* Tue May 05 2020 Stanislav Levin <slev@altlinux.org> 5.4.1-alt1
- 5.3.2 -> 5.4.1.

* Tue Apr 28 2020 Stanislav Levin <slev@altlinux.org> 5.3.2-alt3
- Fixed FTBFS.

* Mon Mar 30 2020 Igor Vlasenko <viy@altlinux.ru> 5.3.2-alt2
- NMU: added py.test-3 & pytest-3 compat symlinks

* Mon Dec 16 2019 Stanislav Levin <slev@altlinux.org> 5.3.2-alt1
- 5.3.1 -> 5.3.2.

* Tue Nov 26 2019 Stanislav Levin <slev@altlinux.org> 5.3.1-alt1
- 5.2.4 -> 5.3.1.

* Sat Nov 16 2019 Stanislav Levin <slev@altlinux.org> 5.2.4-alt1
- 5.2.3 -> 5.2.4.

* Fri Nov 15 2019 Stanislav Levin <slev@altlinux.org> 5.2.3-alt1
- 5.2.2 -> 5.2.3.

* Wed Nov 06 2019 Stanislav Levin <slev@altlinux.org> 5.2.2-alt1
- 5.2.1 -> 5.2.2.

* Mon Oct 07 2019 Stanislav Levin <slev@altlinux.org> 5.2.1-alt1
- 5.2.0 -> 5.2.1.

* Mon Sep 30 2019 Stanislav Levin <slev@altlinux.org> 5.2.0-alt1
- 5.1.2 -> 5.2.0.

* Mon Sep 02 2019 Stanislav Levin <slev@altlinux.org> 5.1.2-alt1
- 5.1.1 -> 5.1.2.

* Thu Aug 29 2019 Stanislav Levin <slev@altlinux.org> 5.1.1-alt2
- Fixed FTBFS ('/dev/shm').

* Thu Aug 22 2019 Stanislav Levin <slev@altlinux.org> 5.1.1-alt1
- 5.1.0 -> 5.1.1.

* Fri Aug 16 2019 Stanislav Levin <slev@altlinux.org> 5.1.0-alt1
- 5.0.1 -> 5.1.0.

* Mon Aug 05 2019 Stanislav Levin <slev@altlinux.org> 5.0.1-alt1
- 4.6.2 -> 5.0.1.

* Wed Jun 05 2019 Stanislav Levin <slev@altlinux.org> 4.6.2-alt1
- 4.5.0 -> 4.6.2
  ~ The 4.6.X series will be the last series to support Python 2
  ~ https://docs.pytest.org/en/latest/py27-py34-deprecation.html

* Mon May 27 2019 Stanislav Levin <slev@altlinux.org> 4.5.0-alt1
- 3.10.1 -> 4.5.0.

* Sun Mar 31 2019 Stanislav Levin <slev@altlinux.org> 3.10.1-alt5
- Fixed testing against py 1.8.0.

* Thu Feb 07 2019 Stanislav Levin <slev@altlinux.org> 3.10.1-alt4
- Fixed "test_pdb_unittest_postmortem" test.

* Wed Jan 23 2019 Stanislav Levin <slev@altlinux.org> 3.10.1-alt3
- Fixed "test_raises_exception_looks_iterable" test.

* Sun Jan 13 2019 Stanislav Levin <slev@altlinux.org> 3.10.1-alt2
- Added workaround for request_garbage test.

* Mon Dec 17 2018 Stanislav Levin <slev@altlinux.org> 3.10.1-alt1
- 3.9.3 -> 3.10.1.

* Sun Oct 28 2018 Stanislav Levin <slev@altlinux.org> 3.9.3-alt1
- 3.9.1 -> 3.9.3.

* Sun Oct 21 2018 Stanislav Levin <slev@altlinux.org> 3.9.1-alt1
- 3.8.2 -> 3.9.1.

* Thu Oct 04 2018 Stanislav Levin <slev@altlinux.org> 3.8.2-alt1
- 3.7.3 -> 3.8.2.

* Wed Aug 29 2018 Stanislav Levin <slev@altlinux.org> 3.7.3-alt1
- 3.7.2 -> 3.7.3.

* Mon Aug 20 2018 Stanislav Levin <slev@altlinux.org> 3.7.2-alt1
- 3.4.2 -> 3.7.2.

* Tue Mar 20 2018 Stanislav Levin <slev@altlinux.org> 3.4.2-alt1
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

