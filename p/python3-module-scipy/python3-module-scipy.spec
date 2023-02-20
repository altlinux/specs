%define _unpackaged_files_terminate_build 1

%def_without check
%ifarch x86_64 aarch64
%def_with pythran
%else
%def_without pythran
%endif

%define modname scipy
%define ver_major 1.10
%define ver_minor 0

%define numpy_version 1.16.5

Name: python3-module-%modname
Version: %ver_major.%ver_minor
Release: alt1

Summary: SciPy is the library of scientific codes
License: BSD-3-Clause
Group: Development/Python3

Url: https://www.scipy.org/
VCS: git://github.com/scipy/scipy.git
Patch0: %name-%version-%release.patch
Source0: %name-%version.tar
Source1: site.cfg
# submodules  by update-submodules.sh
Source2: %name-%version-doc-source-_static-scipy-mathjax.tar
Source3: %name-%version-scipy-_lib-boost.tar
Source4: %name-%version-scipy-_lib-highs.tar
Source5: %name-%version-scipy-_lib-unuran.tar
Source6: %name-%version-scipy-sparse-linalg-_propack-PROPACK.tar

# will be released with scipy 1.8.0

BuildRequires(pre): rpm-macros-make
BuildRequires(pre): rpm-macros-sphinx3
BuildRequires(pre): rpm-build-python3
BuildRequires: gcc-c++ gcc-fortran
BuildRequires: python3-devel
BuildRequires: libnumpy-py3-devel python3-module-numpy-testing
BuildRequires: python3-module-Cython
BuildRequires: python3-module-html5lib
BuildRequires: python3-module-matplotlib
BuildRequires: python3-module-pybind11
%if_with pythran
BuildRequires: python3-module-pythran
%endif
BuildRequires: libflexiblas-devel

%ifarch %e2k
BuildRequires: eml-devel-compat-lapack
BuildRequires: eml-devel-compat-blas
%else
BuildRequires: liblapack-devel
%endif

Requires: %python3_sitelibdir_noarch
Requires: python3-module-numpy >= %numpy_version
%add_python3_req_skip _min_spanning_tree _shortest_path _tools
%add_python3_req_skip _traversal sympy
%add_python3_req_skip distutils
%if_with check
BuildRequires: /usr/bin/pytest3
BuildRequires: python3-module-numpy-tests
BuildRequires: /proc
BuildRequires: python3-module-pooch
%add_python3_req_skip scipy.fft.tests
%else
%add_python3_req_skip numpy.testing
%endif

%description
SciPy is the library of scientific codes built on top of NumPy.

%package devel
Summary: Development files of SciPy (Python 3)
Group: Development/Python3
Requires: %name = %EVR
Requires: python3-devel
Requires: libnumpy-py3-devel

%description devel
SciPy is the library of scientific codes built on top of NumPy.

This package contains development files of SciPy.

%prep
%setup -a2 -a3 -a4 -a5 -a6
%patch0 -p1
install -p -m644 %SOURCE1 .
sed -i 's|@LIBDIR@|%_libdir|g' site.cfg doc/Makefile
sed -i 's|@PYVER@|%_python_version|g' doc/Makefile
sed -i 's|@PYSUFF@|3|' site.cfg

%if_without check
# Find and comment out Pytest imports, since main package should
# not require test deps
grep -zPqsr '[ ]*from scipy._lib._testutils import PytestTester\n[ ]*test = PytestTester\(__name__\)\n[ ]*del PytestTester\n' || exit 1
grep -zPrl '[ ]*from scipy._lib._testutils import PytestTester\n[ ]*test = PytestTester\(__name__\)\n[ ]*del PytestTester\n' | xargs \
sed -i '/from scipy._lib._testutils import PytestTester/,/del PytestTester/ {s/^/# /}'
%endif

mkdir -p ~/.matplotlib
cp %_datadir/matplotlib/mpl-data/matplotlibrc \
	~/.matplotlib/
sed -i 's|^\(backend\).*|\1 : Agg|' ~/.matplotlib/matplotlibrc

%build
%ifarch %e2k
# as of lcc 1.25.17 (mcst#6255)
%add_optflags -DPOCKETFFT_NO_VECTORS
# fixup "EML instead of OpenBLAS/LAPACK" setup
sed -i -e 's/lapack, /clapack, eml_algebra_mt, /g' -e 's/openblas, /blas, /g' site.cfg
%endif

export SCIPY_USE_PYTHRAN=0%{?with_pythran}
%add_optflags -I%_includedir/suitesparse -fno-strict-aliasing %optflags_shared
%python3_build_debug build_ext build_py build_clib \
	config_fc --fcompiler=gnu95

%install
export SCIPY_USE_PYTHRAN=0%{?with_pythran}
%python3_install install_lib install_headers \
	install_data config_fc
find %buildroot%python3_sitelibdir -type f -exec \
	sed -i 's|#! %_bindir/env python|#!%_bindir/python3|' -- '{}' + ||:
find %buildroot%python3_sitelibdir -type f -exec \
	sed -i 's|#!%_bindir/env python|#!%_bindir/python3|' -- '{}' + ||:

# headers
pushd %modname
for i in $(find ./ -name '*.h'); do
    dir=$(echo $i|sed 's|\(.*\)/.*|\1|')
    install -d %buildroot%_includedir/%modname-py3/$dir
    install -p -m644 $i \
	%buildroot%_includedir/%modname-py3/$dir
done
popd

install -p -m644 $(find ./ -name fortranobject.h | head -n 1) \
	%buildroot%_includedir/%modname-py3
pushd %buildroot%python3_sitelibdir/%modname/sparse/csgraph
for i in $(ls *.so); do
	ln -s %python3_sitelibdir/%modname/sparse/csgraph/$i \
		%buildroot%python3_sitelibdir/
done
popd

%if_without check
# don't package tests and tests'check
for i in $(find %buildroot%python3_sitelibdir \
               -name tests -type d \
               -o -name 'conftest.*' -type f \
               -o -name '_testutils.*' -type f \
               -o -name 'gammainc_data.*' -type f \
               -o -name '_mptestutils.*' -type f)
do
	rm -r "$i"
done
%endif

%find_lang %name

%check
pushd %{buildroot}/%{python3_sitelibdir}
pytest3 scipy
popd


%files -f %name.lang
%python3_sitelibdir/*

%files devel
%_includedir/%modname-py3

%changelog
* Fri Feb 17 2023 Anton Farygin <rider@altlinux.ru> 1.10.0-alt1
- 1.6.1 -> 1.10.0

* Tue Feb 14 2023 Grigory Ustinov <grenka@altlinux.org> 1.6.1-alt4
- mpl-data moved to %%_datadir.

* Mon Jan 24 2022 Stanislav Levin <slev@altlinux.org> 1.6.1-alt3
- Fixed FTBFS (Numpy 1.22.1).

* Sat Sep 18 2021 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 1.6.1-alt2.3
- E2K: fixed issue with "chla_transtype_" for Cura

* Tue Jul 27 2021 Michael Shigorin <mike@altlinux.org> 1.6.1-alt2.2
- E2K: fix build with EML

* Thu Jul 22 2021 Michael Shigorin <mike@altlinux.org> 1.6.1-alt2.1
- E2K: build
  + with EML instead of openblas/lapack
  + without vector extension (mcst#6255; thx ilyakurdyukov@)

* Thu Jun 24 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.6.1-alt2
- drop excessive python3-module-jinja2-tests BR

* Thu Mar 18 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.6.1-alt1
- Updated to upstream version 1.6.1.

* Fri Jul 31 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.5.2-alt1
- Updated to upstream version 1.5.2.
- Built without python-2 support.

* Tue Feb 11 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.2.0-alt6
- Fixed build requires.

* Wed Oct 02 2019 Stanislav Levin <slev@altlinux.org> 1.2.0-alt5
- Dropped dependency on tests packages.

* Wed Jul 17 2019 Dmitry Terekhin <jqt4@altlinux.org> 1.2.0-alt4
- Removed dependency from python-module-numdifftools

* Mon Dec 31 2018 Mikhail Gordeev <obirvalger@altlinux.org> 1.2.0-alt3
- Add more unicode fixes
- Add Requires to numpy with version

* Fri Dec 28 2018 Mikhail Gordeev <obirvalger@altlinux.org> 1.2.0-alt2
- Fix unicode is docstrings

* Wed Dec 26 2018 Mikhail Gordeev <obirvalger@altlinux.org> 1.2.0-alt1
- update to 1.2.0

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.0-alt2.1
- (NMU) Rebuilt with python-3.6.4.

* Mon Mar 12 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.0-alt2
- Fixed build.

* Thu Oct 26 2017 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1
- 1.0.0

* Sat Jul 08 2017 Yuri N. Sedunov <aris@altlinux.org> 0.19.1-alt1
- 0.19.1

* Mon Jun 19 2017 Yuri N. Sedunov <aris@altlinux.org> 0.19.0-alt1
- 0.19.0

* Fri Mar 25 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.17.0-alt1.git20150829.2.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Mar 24 2016 Denis Medvedev <nbr@altlinux.org> 0.17.0-alt1.git20150829.2
- NMU: arranged dependencies.

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.17.0-alt1.git20150829.1
- NMU: Use buildreq for BR.

* Sun Aug 30 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.17.0-alt1.git20150829
- Version 0.17.0

* Sun Apr 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.15.1-alt1.git20150425
- Version 0.15.1

* Fri Mar 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.15.0-alt2.git20141102
- Fixed build

* Mon Nov 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.15.0-alt1.git20141102
- New snapshot

* Wed May 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.15.0-alt1.git20140506
- Version 0.15.0

* Thu Jan 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14.0-alt7.git20131020
- Rebuilt with new python-module-sphinx

* Tue Jan 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14.0-alt6.git20131020
- Disabled docs

* Wed Nov 20 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14.0-alt5.git20131020
- Don't require sympy for module for Python 3

* Wed Nov 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14.0-alt4.git20131020
- Fixed build

* Fri Oct 25 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14.0-alt3.git20131020
- Fixed linking of qhull.so

* Thu Oct 24 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14.0-alt2.git20131020
- Fixed linking

* Wed Oct 23 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14.0-alt1.git20131020
- Version 0.14.0

* Wed Jun 19 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13.0-alt2.git20130614
- Fixed build

* Sat Jun 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13.0-alt1.git20130614
- Version 0.13.0

* Sat Mar 30 2013 Aleksey Avdeev <solo@altlinux.ru> 0.12.0-alt2.git20121009.1
- Rebuild with Python-3.3
- Fix non-identical noarch packages (python{,3}-module-weave)

* Wed Dec 19 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.12.0-alt2.git20121009
- Set doc-html as noarch

* Fri Oct 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.12.0-alt1.git20121009
- Version 0.12.0

* Sun Aug 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11.0-alt5.git20120508
- Built with OpenBLAS instead of GotoBLAS2

* Sun Jun 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11.0-alt4.git20120508
- Fixed build

* Fri May 25 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11.0-alt3.git20120508
- Fixed scipy.sparse.csgraph importing in module for Python 3

* Sun May 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11.0-alt2.git20120508
- New snapshot
- Added module for Python 3

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.11.0-alt2.git20111011.1
- Rebuild to remove redundant libpython2.7 dependency

* Sun Nov 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11.0-alt2.git20111011
- Enabled docs (except pdf)

* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.11.0-alt1.git20111011.1
- Rebuild with Python-2.7

* Mon Oct 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11.0-alt1.git20111011
- Version 0.11.0

* Mon Jul 18 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.0-alt1.git20110716
- New snapshot

* Sun Apr 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.0-alt1.git20110402.3
- Built with docs

* Fri Apr 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.0-alt1.git20110402.2
- Rebuilt with GotoBLAS2 1.13-alt3
- Bootstrap (without docs)

* Thu Apr 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.0-alt1.git20110402.1
- Fixed underlinking of modules

* Thu Apr 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.0-alt1.git20110402
- Version 0.10.0
- Rebuilt with lapack-goto instead of lapack

* Tue Apr 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.0-alt1.svn20100607.6
- Rebuilt with ATLAS 3.9.35

* Mon Mar 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.0-alt1.svn20100607.5
- Rebuilt with lapack 3.3.0-alt4

* Tue Mar 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.0-alt1.svn20100607.4
- Added -g into compiler flags
- Moved all development files into devel package

* Fri Feb 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.0-alt1.svn20100607.3
- Rebuilt for debuginfo

* Tue Oct 26 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.0-alt1.svn20100607.2
- Rebuilt for soname set-versions

* Wed Oct 13 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.0-alt1.svn20100607.1
- Fixed underlinking

* Wed Jun 09 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.0-alt1.svn20100607
- Version 0.9.0

* Fri Apr 02 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0-alt2.svn20100202.2
- Rebuilt with new NumPy

* Tue Mar 02 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0-alt2.svn20100202.1
- Rebuilt with updated macro %%prepare_sphinx

* Thu Feb 04 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0-alt2.svn20100202
- Rebuilt with reformed NumPy
- Added
  + documentation (HTML & PDF)
  + pickles, devel and tests packages, plus weave in root of
    %%python_sitelibdir
  + %%check section

* Fri Jan 22 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0-alt2.svn20100121
- New snapshot
- Rebuild with new NumPy
- Extracted examples and tests into separate package
- Added docs packages

* Mon Jan 11 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0-alt2.svn20100109
- New snapshot
- Fixed error of find numpy library (ALT #22707)

* Thu Dec 31 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0-alt2.svn20091231
- New snapshot
- Rebuilt without python-module-Numeric

* Mon Nov 16 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0-alt2.svn20090913.1
- Rebuilt with python 2.6

* Sun Sep 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0-alt2.svn20090913
- New snapshot

* Fri Sep 04 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0-alt2.svn20090902.1
- Disabled strict aliasing rules

* Wed Sep 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0-alt2.svn20090902
- Rebuilt with shared libraries of SuiteSparse

* Thu Aug 27 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0-alt2.svn20090827
- New snapshot

* Sun Aug 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0-alt2.svn20090730.2
- Fixed svn version for special_version.py

* Fri Jul 31 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0-alt2.svn20090730.1
- Version 0.8.0

* Thu Dec 04 2008 Vitaly Lipatov <lav@altlinux.ru> 0.7.0-alt1
- new version 0.7.0b1
- update buildreqs, cleanup spec

* Sun Jul 06 2008 Vitaly Lipatov <lav@altlinux.ru> 0.6.0-alt1
- initial build for ALT Linux Sisyphus
