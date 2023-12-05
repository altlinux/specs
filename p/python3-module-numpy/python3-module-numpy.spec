%def_with check
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%ifarch %ix86 ppc64le armh
%define relax_tests 1
%endif

# LTO causes errors, disable it
%global optflags_lto %nil

%define pypi_name numpy
%define oname %pypi_name

Name: python3-module-%oname
Epoch: 1
Version: 1.25.2
Release: alt2
Summary: Fundamental package for array computing in Python
License: BSD-3-Clause
Group: Development/Python3
Url: https://www.numpy.org/
VCS: https://github.com/numpy/numpy.git
Source: %name-%version.tar
Source3: svml.tar
Source4: x86-simd-sort.tar
Source1: %pyproject_deps_config_name
Patch: numpy-1.20.2-Remove-strict-dependency-on-testing-package.patch
Patch1: numpy-1.21.1-alt-use-system-fallocate-declaration.patch
Patch4: numpy-1.21.4-alt-use-sleep-in-auxv-test.patch
Patch5: numpy-1.25.2-alt-loongarch64-selected_real_kind.patch

# E2K patchset with MCST numbering scheme
%ifarch %e2k
Patch1001: 0001-arch_e2k_define.patch
Patch1002: 0002-bug92804.patch
Patch1003: 0003-lcc-1.24-compat.patch
%endif
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
BuildRequires: gcc-c++ gcc-fortran liblapack-devel swig
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
# some tests want /proc/meminfo
BuildRequires: /proc
%endif

# numpy provides the hook for PyInstaller via entry_points mechanism
# PyInstaller will call this hook
# see https://github.com/numpy/numpy/issues/17184
%filter_from_requires /python3(PyInstaller\(\..*\)\?)/d

# numpy.distutils is deprecated and will be removed with Python 3.12
# https://numpy.org/doc/stable/reference/distutils.html
# https://numpy.org/doc/stable/reference/distutils_status_migration.html#distutils-status-migration
# https://bugzilla.altlinux.org/35103
%filter_from_requires /python3(distutils\(\..*\)\?)/d
%filter_from_requires /python3(setuptools\(\..*\)\?)/d

# code_generators is only available in source tree and is not
# shipped, but we ship code that may use it, for example, numpy.core.cversions
%filter_from_requires /python3(code_generators\(\..*\)\?)/d
# sys.path is prepended with code_generators path
%add_python3_req_skip genapi
%add_python3_req_skip numpy_api

%add_findprov_skiplist %python3_sitelibdir/%oname/random/_examples/*
%add_findreq_skiplist  %python3_sitelibdir/%oname/random/_examples/*

# core.setup_common is imported from core.setup
%add_python3_self_prov_path %buildroot%python3_sitelibdir/%oname/core/
# f2py.setup: from __version__ import version
%add_python3_self_prov_path %buildroot%python3_sitelibdir/%oname/f2py/

Conflicts: python-module-numpy < 1:1.15.4-alt6

%description
NumPy is the fundamental package for scientific computing in Python. It is a
Python library that provides a multidimensional array object, various derived
objects (such as masked arrays and matrices), and an assortment of routines for
fast operations on arrays, including mathematical, logical, shape manipulation,
sorting, selecting, I/O, discrete Fourier transforms, basic linear algebra,
basic statistical operations, random simulation and much more.

%package testing
Summary: Testing part of NumPy (Python 3)
Group: Development/Python3
Requires: %name = %EVR

%description testing
This package contains testing part of NumPy.

%package tests
Summary: Tests for NumPy (Python 3)
Group: Development/Python3
Requires: %name = %EVR

%description tests
This package contains tests NumPy.

%package -n lib%oname-py3-devel
Summary: Development files of NumPy (Python 3)
Group: Development/Python3
Requires: %name = %EVR
Requires: python3-devel

%description -n lib%oname-py3-devel
This package contains development files of NumPy.

%prep
%setup -a 3 -a4
%autopatch -p1

# headers
sed -i 's|^prefix.*|prefix=%python3_sitelibdir/%oname/core|' \
	%oname/core/npymath.ini.in
sed -i 's|^includedir.*|includedir=%_includedir/python%_python3_version/%oname|' \
	%oname/core/npymath.ini.in

# fix version info
sed -i \
	-e "s/git_refnames\s*=\s*\"[^\"]*\"/git_refnames = \" \(tag: v%version\)\"/" \
	%oname/_version.py

%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile test_requirements.txt
%endif

%build
%add_optflags -fno-strict-aliasing
%pyproject_build

%check
# no-build to avoid double build
%pyproject_run -- python3 runtests.py --no-build -v -- -ra -o=addopts=-Wignore %{?relax_tests:||:}

%install
%pyproject_install

install -d %buildroot%_includedir/python%_python3_version
mv %buildroot%python3_sitelibdir/%oname/core/include/%oname \
	%buildroot%_includedir/python%_python3_version/%oname

ln -s %_includedir/python%_python3_version/%oname \
	%buildroot%python3_sitelibdir/%oname/core/include/

%files
%doc README.md
%_bindir/f2py*
%python3_sitelibdir/%oname
%python3_sitelibdir/%{pyproject_distinfo %oname}/
%exclude %python3_sitelibdir/%oname/conftest.py
%exclude %python3_sitelibdir/%oname/_pytesttester.py
%exclude %python3_sitelibdir/%oname/_pytesttester.pyi
%exclude %python3_sitelibdir/%oname/__pycache__/conftest.*
%exclude %python3_sitelibdir/%oname/__pycache__/_pytesttester.*
%exclude %python3_sitelibdir/%oname/ma/timer_comparison.py
%exclude %python3_sitelibdir/%oname/ma/__pycache__/timer_comparison.*
%exclude %python3_sitelibdir/%oname/testing
%exclude %python3_sitelibdir/%oname/tests
%exclude %python3_sitelibdir/%oname/*/tests/
%exclude %python3_sitelibdir/%oname/*/test_*
%exclude %python3_sitelibdir/%oname/*/testutils.py
%exclude %python3_sitelibdir/%oname/*/__pycache__/test_*.*
%exclude %python3_sitelibdir/%oname/*/__pycache__/testutils.*
%exclude %python3_sitelibdir/%oname/f2py/src/fortranobject.h
%exclude %python3_sitelibdir/%oname/core/lib/npy-pkg-config
%exclude %python3_sitelibdir/%oname/doc
%exclude %python3_sitelibdir/%oname/core/include
%exclude %python3_sitelibdir/%oname/distutils/mingw
%exclude %python3_sitelibdir/%oname/f2py/src
%exclude %python3_sitelibdir/%oname/core/lib/libnpymath.a
%exclude %python3_sitelibdir/%oname/random/lib/libnpyrandom.a

%files testing
%python3_sitelibdir/%oname/testing
%python3_sitelibdir/%oname/conftest.py
%python3_sitelibdir/%oname/_pytesttester.py
%python3_sitelibdir/%oname/_pytesttester.pyi
%python3_sitelibdir/%oname/__pycache__/conftest.*
%python3_sitelibdir/%oname/__pycache__/_pytesttester.*

%files tests
%python3_sitelibdir/%oname/tests/
%python3_sitelibdir/%oname/typing/tests/
%python3_sitelibdir/%oname/random/tests/
%python3_sitelibdir/%oname/polynomial/tests/
%python3_sitelibdir/%oname/matrixlib/tests/
%python3_sitelibdir/%oname/ma/tests/
%python3_sitelibdir/%oname/linalg/tests/
%python3_sitelibdir/%oname/lib/tests/
%python3_sitelibdir/%oname/fft/tests/
%python3_sitelibdir/%oname/f2py/tests/
%python3_sitelibdir/%oname/distutils/tests/
%python3_sitelibdir/%oname/core/tests/
%python3_sitelibdir/%oname/compat/tests/
%python3_sitelibdir/%oname/array_api/tests/
%python3_sitelibdir/%oname/ma/testutils.py
%python3_sitelibdir/%oname/ma/__pycache__/testutils.*
%python3_sitelibdir/%oname/_pyinstaller/test_pyinstaller.py
%python3_sitelibdir/%oname/_pyinstaller/__pycache__/test_pyinstaller.*

%files -n lib%oname-py3-devel
%_includedir/python%_python3_version/%oname
%python3_sitelibdir/%oname/core/include
%python3_sitelibdir/%oname/distutils/mingw
%python3_sitelibdir/%oname/f2py/src
%python3_sitelibdir/%oname/core/lib/npy-pkg-config
%python3_sitelibdir/%oname/core/lib/libnpymath.a
%python3_sitelibdir/%oname/random/lib/libnpyrandom.a

%changelog
* Tue Dec 05 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 1:1.25.2-alt2
- NMU: applied selectedrealkind check fix for loongarch64 (thanks to iv@).

* Tue Aug 01 2023 Stanislav Levin <slev@altlinux.org> 1:1.25.2-alt1
- 1.25.1 -> 1.25.2.

* Mon Jul 17 2023 Stanislav Levin <slev@altlinux.org> 1:1.25.1-alt1
- 1.22.1 -> 1.25.1.

* Wed Dec 14 2022 Grigory Ustinov <grenka@altlinux.org> 1:1.22.1-alt4
- Bootstrap for python3.11.

* Fri Feb 04 2022 Grigory Ustinov <grenka@altlinux.org> 1:1.22.1-alt3
- Enable check back.

* Sun Jan 23 2022 Grigory Ustinov <grenka@altlinux.org> 1:1.22.1-alt2
- Bootstrap for python3.10.

* Fri Jan 21 2022 Stanislav Levin <slev@altlinux.org> 1:1.22.1-alt1
- 1.21.4 -> 1.22.1.

* Tue Dec 21 2021 Ivan A. Melnikov <iv@altlinux.org> 1:1.21.4-alt3
- site.cfg: use openblas by default on mipsel

* Tue Dec 14 2021 Anton Farygin <rider@altlinux.ru> 1:1.21.4-alt2
- relaxed tests on ppc64le due to fall in
  "test_linalg.py::TestCholesky::test_basic_property" in the build for p10

* Wed Dec 08 2021 Anton Farygin <rider@altlinux.ru> 1:1.21.4-alt1
- 1.21.1 -> 1.21.4
- moved recfunctions.py from tests to main package
- added a patch to recfunctions.py for remove dependency to testing
- added a patch from the upstream for fix _GenericAlias tests
- enabled tests

* Wed Sep 01 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1:1.21.1-alt2
- Disabled LTO.

* Wed Jul 28 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1:1.21.1-alt1
- Updated to upstream version 1.21.1.

* Tue Jun 15 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1:1.20.3-alt1
- Updated to upstream version 1.20.3.

* Mon Apr 26 2021 Vitaly Lipatov <lav@altlinux.ru> 1:1.20.2-alt2
- NMU: add conflicts to old python-module-numpy

* Mon Apr 19 2021 Grigory Ustinov <grenka@altlinux.org> 1:1.20.2-alt1
- Automatically updated to 1.20.2.

* Mon Apr 19 2021 Grigory Ustinov <grenka@altlinux.org> 1:1.20.1-alt3
- Add %%e2k support (Closes: #36684).
- Removed unused subpackages and knobs.

* Fri Mar 19 2021 Ivan A. Melnikov <iv@altlinux.org> 1:1.20.1-alt2
- site.cfg: Don't use openblas by default on mipsel.

* Mon Mar 15 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1:1.20.1-alt1
- Updated to upstream version 1.20.1.

* Tue Feb 02 2021 Grigory Ustinov <grenka@altlinux.org> 1:1.19.5-alt2
- Bootstrap for python3.9.

* Fri Jan 15 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1:1.19.5-alt1
- Updated to upstream version 1.19.5.

* Thu Aug 20 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1:1.19.1-alt1
- Updated to upstream version 1.19.1
- Disabled build for python-2.
- Cleaned up spec.

* Wed Mar 11 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1:1.15.4-alt5
- Moved include directories (Closes: #38013).

* Tue Feb 11 2020 Andrey Bychkov <mrdrew@altlinux.org> 1:1.15.4-alt4
- Fixed build requires.

* Fri Sep 13 2019 Vladimir Didenko <cow@altlinux.org> 1:1.15.4-alt3
- Remove dependency on scons (it is not required anymore)

* Tue Jun 11 2019 Stanislav Levin <slev@altlinux.org> 1:1.15.4-alt2
- Dropped dependency on testing/test packages in the main one.

* Tue Dec 25 2018 Mikhail Gordeev <obirvalger@altlinux.org> 1:1.15.4-alt1
- Update to upstream version 1.15.4
- Remove runnig 2to3 on generators

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 1:1.13.3-alt2.2.qa1
- NMU: applied repocop patch

* Fri Jun 29 2018 Anton Midyukov <antohami@altlinux.org> 1:1.13.3-alt2.2
- Skip requires from python3-module numpy (Closes:35103) to:
  - python3(setuptools.command.develop)
  - python3(setuptools.command.egg_info)

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1:1.13.3-alt2.1.1
- (NMU) Rebuilt with python-3.6.4.

* Tue Mar 06 2018 Igor Vlasenko <viy@altlinux.ru> 1:1.13.3-alt2.1
- NMU: corrected BR: for new texlive

* Mon Jan 22 2018 Igor Vlasenko <viy@altlinux.ru> 1:1.13.3-alt2
- added optional Provides: python-module-numpy-doc for autoimports

* Wed Nov 29 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1:1.13.3-alt1
- Updated to upstream version 1.13.3.
- Removed git from build dependencies.
- Cleaned up spec.
- Disabled generation of docs.

* Mon Apr 17 2017 Anton Midyukov <antohami@altlinux.org> 1:1.12.1-alt1
- New version 1.12.1
- Remove __svn_version__.py
- Disable tests
- Disable convert python 2 to python3 script

* Thu Mar 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0.0-alt15.git20150829.2.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Wed Mar 23 2016 Denis Medvedev <nbr@altlinux.org> 2.0.0-alt15.git20150829.2
- NMU: reorganized dependencies.

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.0.0-alt15.git20150829.1
- NMU: Use buildreq for BR.

* Sun Aug 30 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt15.git20150829
- New snapshot

* Fri May 01 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt14.git20150424
- Added dgetrf into lapack_lite

* Sat Apr 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt13.git20150424
- New snapshot

* Mon Nov 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt13.git20141102
- Fixed numpy.distutils.misc_util.get_num_build_jobs for cases when
  --jobs command line argument doesn't recognized by setup.py

* Mon Nov 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt12.git20141102
- New snapshot

* Tue May 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt12.git20140505
- New snapshot

* Mon May 05 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt12.git20131021
- Avoid requirement on python-devel for %name (ALT #29862)

* Wed Jan 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt11.git20131021
- Enabled docs

* Wed Jan 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt10.git20131021
- Removed dependency on devel subpackage (ALT #29723)

* Tue Jan 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt9.git20131021
- Disabled docs

* Tue Oct 22 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt8.git20131021
- New snapshot

* Fri Jun 14 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt8.git20130613
- New snapshot

* Mon Apr 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt8.git20121009
- Use 'find... -exec...' instead of 'for ... $(find...'

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 2.0.0-alt7.git20121009.1
- Rebuild with Python-3.3

* Sun Oct 14 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt7.git20121009
- Fixed upgrading of numpydoc
- Extracted tests for numpydoc into separate package

* Fri Oct 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt6.git20121009
- New snapshot

* Sun Aug 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt6.git20120502
- Built with OpenBLAS instead of GotoBLAS2

* Sun May 20 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt5.git20120502
- Fixed headers for libnumpy-py3-devel

* Fri May 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt4.git20120502
- New snapshot
- Added modules for Python 3
- Moved numpy.lib.polynomial into main package (ALT #27314)

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0.0-alt3.git20111023.1
- Rebuild to remove redundant libpython2.7 dependency

* Sat Nov 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt3.git20111023
- Rebuilt with docs (except pdf) and tests

* Tue Oct 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0.0-alt2.git20111023.1
- Rebuild with Python-2.7

* Mon Oct 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt2.git20111023
- New snapshot

* Mon Jul 18 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt2.git20110715.1
- Built with docs and tests

* Sun Jul 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt2.git20110715
- New snapshot (without docs and tests for bootstrap)

* Sat Apr 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt2.git20110422
- New snapshot
- Changed type promotion tables from char to signed char (thanks to
  manowar@ and charris)

* Sat Apr 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt2.git20110405.4
- Built with docs

* Fri Apr 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt2.git20110405.3
- Built with OpenMP
- Bootstrap with GotoBLAS2 1.13-alt3 (without docs)

* Thu Apr 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt2.git20110405.2
- Built with docs
- Don't set fake ATLAS_VERSION (it's problem somewhere)

* Thu Apr 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt2.git20110405.1
- Set fake ATLAS_VERSION for client software

* Wed Apr 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt2.git20110405
- New snapshot (from github)
- Built with GotoBLAS2 instead of ATLAS
- Bootstrap (without docs now)

* Wed Apr 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.svn20100607.11
- linalg: avoid raising LinAlgError exception

* Tue Apr 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.svn20100607.10
- Rebuilt with ATLAS 3.9.35

* Mon Mar 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.svn20100607.9
- Fixed linking with ATLAS

* Mon Mar 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.svn20100607.8
- Rebuilt with lapack 3.3.0-alt4

* Fri Mar 11 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.svn20100607.7
- Restored %_bindir/f2py

* Tue Mar 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.svn20100607.6
- Added -g into compiler flags
- Moved all headers into libnumpy-devel

* Fri Feb 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.svn20100607.5
- Rebuilt for debuginfo

* Fri Dec 24 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.svn20100607.4
- Fixed inner headers' directory (ALT #24817)

* Tue Oct 26 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.svn20100607.3
- Rebuilt for soname set-versions

* Wed Oct 13 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.svn20100607.2
- Fixed linking

* Thu Jul 29 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.svn20100607.1
- Avoid requirement on python-module-Numeric for doc

* Wed Jun 09 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.svn20100607
- Version 2.0.0

* Thu Apr 08 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt1.svn20100120.3
- Added addons packages

* Mon Feb 08 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt1.svn20100120.2
- Fixed building of PDFs
- Rebuilt with updated macro %%prepare_sphinx

* Mon Feb 01 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt1.svn20100120.1
- Added modules: numpyx, floatint, (numpydoc & pickles - in separate
  packages) files
- Built additional documentation
- Made building of docs by one command `make'

* Sun Jan 24 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt1.svn20100120
- New snapshot
- Added param `-std=f95' for NAG Fortran compiler
- Added docs packages
- Extracted tests and addons into separate package
- Generate additional submodules
- Some another minor fixes

* Mon Jan 11 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt1.svn20091231.2
- Added link to libnpymath.so into %_libdir

* Mon Jan 04 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt1.svn20091231.1
- Added __svn_version__.py and site.cfg

* Thu Dec 31 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt1.svn20091231
- Version 1.5.0

* Sat Dec 19 2009 Ivan Fedorov <ns@altlinux.org> 1.4.0-alt4.svn20090913
- Remove dependency to Numeric
- Update homepage URL

* Mon Dec 14 2009 Dmitry V. Levin <ldv@altlinux.org> 1.4.0-alt3.svn20090913
- Updated build dependencies.

* Fri Nov 06 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt2.svn20090913.1
- Rebuilt with python 2.6

* Sun Sep 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt2.svn20090913
- New snapshot

* Tue Sep 08 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt2.svn20090902.1
- Added preinstall deletion of old include directory (ALT #21473)

* Wed Sep 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt2.svn20090902
- Rebuilt with shared libraries of SuiteSparse

* Thu Aug 27 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt2.svn20090827
- New snapshot

* Tue Aug 25 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt1.svn20090822.2
- Enabled conflict with old syfi

* Tue Aug 25 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt1.svn20090822.1
- Bootstrap for syfi

* Sat Aug 22 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt1.svn20090822
- New snapshot
- Added pkg-config file

* Fri Jul 31 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt1.svn20090731.1
- Version 1.4.0
- Made %_bindir/f2py as symbolic link

* Thu Apr 23 2009 Vitaly Lipatov <lav@altlinux.ru> 1.3.0-alt1
- new version 1.3.0 (with rpmrb script)

* Sun Dec 28 2008 Vitaly Lipatov <lav@altlinux.ru> 1.2.1-alt2
- remove unneeded buildreqs
- disable scons requires (fix bug #18379)

* Mon Dec 01 2008 Vitaly Lipatov <lav@altlinux.ru> 1.2.1-alt1
- new version 1.2.1 (with rpmrb script)
- update buildreqs

* Mon Jul 07 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.0-alt2
- fix unmets

* Sat Jul 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.0-alt1
- new version 1.1.0 (with rpmrb script)
- add rpm-build-compat requires due build_python macros

* Sat Apr 07 2007 Vitaly Lipatov <lav@altlinux.ru> 1.0.2-alt1
- new version 1.0.2 (with rpmrb script)

* Sat Nov 11 2006 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt0.1
- initial build for ALT Linux Sisyphus

