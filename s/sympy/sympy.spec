%define _unpackaged_files_terminate_build 1

%ifnarch ppc64le
%def_with check
%else
%def_without check
%endif

%def_without doc

Name: sympy
Epoch: 1
Version: 1.13.2
Release: alt2
Summary: A Python library for symbolic mathematics
License: BSD-3-Clause
Group: Sciences/Mathematics
Url: https://sympy.org/
VCS: https://github.com/sympy/sympy.git

BuildArch: noarch

Source: %name-%version.tar
Source1: %pyproject_deps_config_name
%pyproject_runtimedeps_metadata

Patch1: sympy-1.13.1-alt-build.patch

# https://github.com/sympy/sympy/pull/27069
Patch2: sympy-1.13.2-alt-fix-races-in-tests.patch

BuildRequires(pre): rpm-build-intro >= 2.2.4
BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3-module-pytest-xdist
BuildRequires: dvipng ImageMagick-tools graphviz librsvg-utils

%if_with check
BuildRequires: python3-module-pytest python3-module-mpmath python3-module-numpy-testing python3-module-hypothesis
%endif

Requires: python3-module-%name = %EVR

%add_python3_req_skip py.__.test.item py.__.test.terminal.terminal

%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%endif

%description
SymPy is a Python library for symbolic mathematics. It aims to become a
full-featured computer algebra system (CAS) while keeping the code as
simple as possible in order to be comprehensible and easily extensible.

%package -n python3-module-%name
Summary: A Python 3 module for symbolic mathematics
Group: Development/Python3

%description -n python3-module-%name
SymPy is a Python library for symbolic mathematics. It aims to become a
full-featured computer algebra system (CAS) while keeping the code as
simple as possible in order to be comprehensible and easily extensible.

This package contains python module of SymPy.

%package -n python3-module-%name-examples
Summary: Examples for SymPy
Group: Development/Documentation
Requires: python3-module-%name = %EVR

%description -n python3-module-%name-examples
SymPy is a Python library for symbolic mathematics. It aims to become a
full-featured computer algebra system (CAS) while keeping the code as
simple as possible in order to be comprehensible and easily extensible.

This package contains examples for SymPy.

%package -n python3-module-%name-pickles
Summary: Pickles for SymPy
Group: Development/Python
Requires: python3-module-%name = %EVR

%description -n python3-module-%name-pickles
SymPy is a Python library for symbolic mathematics. It aims to become a
full-featured computer algebra system (CAS) while keeping the code as
simple as possible in order to be comprehensible and easily extensible.

This package contains pickles for SymPy.

%package -n python3-module-%name-doc
Summary: Documentation for SymPy
Group: Development/Documentation
BuildArch: noarch

%description -n python3-module-%name-doc
SymPy is a Python library for symbolic mathematics. It aims to become a
full-featured computer algebra system (CAS) while keeping the code as
simple as possible in order to be comprehensible and easily extensible.

This package contains development documentation for SymPy.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%patch1 -p1
%patch2 -p1

for i in $(find ./ -name tests); do
	touch $i/__init__.py
done

sed -i 's|@PYVER@|%_python3_version|g' doc/Makefile
%if_with doc
%prepare_sphinx3 .
%endif

%build
export LC_ALL=en_US.UTF-8
%pyproject_build

%if_with doc
pushd doc
%make html
popd

rm -fR doctrees
cp -fR doc/_build/doctrees doc/src/
export PYTHONPATH=$PYTHONPATH:$PWD
cp -fR doc/_build/doctrees ./

%generate_pickles3 $PWD $PWD/doc/_build/html %name
%endif

%install
%pyproject_install

%if_with doc
cp -fR pickle %buildroot%python3_sitelibdir/%name/
%endif

# remove tests files
%python3_prune
# by some reason sympy.testing is wide used in the project modules
#rm -rfv %buildroot%python3_sitelibdir/%name/testing/
rm -rfv %buildroot%python3_sitelibdir/%name/conftest.py
rm -rfv %buildroot%python3_sitelibdir/%name/utilities/{*test.py,_compilation/}
rm -rfv %buildroot%python3_sitelibdir/%name/parsing/autolev/test-examples/

%check
py.test-3 -vv -n %_smp_build_ncpus \
	--deselect=sympy/integrals/tests/test_failing_integrals.py::test_issue_15227 \
	--deselect=sympy/matrices/tests/test_matrices.py::test_pinv_rank_deficient_when_diagonalization_fails \
	--deselect=sympy/solvers/ode/tests/test_systems.py::test_linear_new_order1_type2_de_lorentz_slow_check \
	%nil

%if_with doc
python3 bin/doctest -v ||:
%endif

%files
%doc AUTHORS LICENSE README* CODE_OF_CONDUCT.md
%_bindir/*
%_man1dir/*

%files -n python3-module-%name
%python3_sitelibdir/*
%if_with doc
%exclude %python3_sitelibdir/%name/pickle
%endif

%files -n python3-module-%name-examples
%doc examples/*

%if_with doc
%files -n python3-module-%name-pickles
%python3_sitelibdir/%name/pickle

%files -n python3-module-%name-doc
%doc doc/_build/html/*
%endif

%changelog
* Tue Sep 17 2024 Ivan A. Melnikov <iv@altlinux.org> 1:1.13.2-alt2
- Run tests in parallel
- Fix file-related race condition in the test suite
  (fixes FTBFS on loongarch64).

* Mon Sep 09 2024 Andrey Kovalev <ded@altlinux.org> 1:1.13.2-alt1
- Updated to upstream version 1.13.2.
- Returned the test check.

* Thu Sep 05 2024 Andrey Kovalev <ded@altlinux.org> 1:1.13.1-alt1
- Updated to upstream version 1.13.1.
- Changed the package build scheme.

* Fri Feb 25 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 1:1.9-alt1
- Updated to upstream version 1.9.

* Wed Aug 25 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1:1.8-alt1
- Updated to upstream version 1.8.

* Thu Jan 14 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1:1.7.1-alt1
- Updated to upstream version 1.7.1.

* Wed Nov 04 2020 Vitaly Lipatov <lav@altlinux.ru> 1:1.6.1-alt3
- NMU: drop tests subpackage

* Fri Oct 30 2020 Vitaly Lipatov <lav@altlinux.ru> 1:1.6.1-alt2
- NMU: drop require tests submodule
- NMU: more strict masks for tests and remove duplicated pickle exclude

* Wed Jul 08 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1:1.6.1-alt1
- Updated to upstream version 1.6.1.
- Disabled build for python-2.

* Sat Apr 27 2019 Michael Shigorin <mike@altlinux.org> 1:1.1.1-alt1.1.1
- introduce doc knob (on by default)

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1:1.1.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Oct 02 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1:1.1.1-alt1
- Updated to upstream version 1.1.1.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:0.7.7-alt1.dev.git20150830.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Aug 31 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.7.7-alt1.dev.git20150830
- New snapshot

* Fri May 01 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.7.7-alt1.dev.git20150430
- Version 0.7.7.dev

* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.7.6-alt1.git20141120
- Version 0.7.6

* Sat Aug 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.7.5-alt1.git20140814
- New snapshot
- Added module for Python 3

* Thu Jul 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.7.5-alt1.git20140710
- New snapshot

* Mon Jun 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.7.5-alt1.git20140609
- Version 0.7.5

* Tue Nov 19 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.7.3-alt1.git20131118
- New snapshot

* Fri Jul 26 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.7.3-alt1.git20130725
- Version 0.7.3

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 1:0.7.2-alt1.git20130210.1
- Rebuild with Python-3.3

* Mon Feb 11 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.7.2-alt1.git20130210
- Version 0.7.2

* Sun Jun 24 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.7.1-alt1.git20120623
- New snapshot
- Applied repocop patch

* Sat May 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.7.1-alt1.git20120511
- New snapshot
- Added module for Python 3

* Fri Jan 27 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.7.1-alt1.git20120124
- Version 0.7.1

* Thu Dec 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.6.7-alt2.git20110405
- Enabled docs

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1:0.6.7-alt1.git20110405.1
- Rebuild with Python-2.7

* Tue Apr 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.6.7-alt1.git20110405
- New snapshot

* Tue Apr 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.6.7-alt1.git20101102.2
- Rebuilt with python-module-sphinx-devel

* Wed Nov 17 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.6.7-alt1.git20101102.1
- Fixed bad imports from tests

* Mon Nov 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.6.7-alt1.git20101102
- New snapshot
- Corrected version number

* Mon Mar 08 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.0-alt1.svn20100302
- Version 0.7.0
- Extracted examples and tests into separate packages
- Added pickles packages

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.5-alt2
- Rebuilt with python 2.6

* Sun Sep 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.5-alt1
- Initial build for Sisyphus

