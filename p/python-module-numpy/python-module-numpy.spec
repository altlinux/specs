%define _unpackaged_files_terminate_build 1

%define oname numpy
%define majver 1.15
%def_with addons

%define somver 0
%define sover %somver.5

Name: python-module-%oname
Version: %majver.4
Release: alt11
Epoch: 1

Summary: NumPy: array processing for numbers, strings, records, and objects
License: BSD
Group: Development/Python
Url: https://www.numpy.org/

%setup_python_module %oname

# https://bugzilla.altlinux.org/show_bug.cgi?id=18379
%add_python_req_skip Scons setuptools distutils nose number code_generators

# https://github.com/numpy/numpy
Source: %oname-%version.tar
Source1: %oname.pc
Source2: site.cfg
Source3: sphinx-theme.tar
Patch0: numpy-1.15.4-Remove-strict-dependency-on-testing-package.patch

Requires: lib%oname = %EVR
Conflicts: libsyfi-devel < 0.6.1-alt3.hg20090822
Conflicts: lib%oname-devel < %version-%release
Obsoletes: libsyfi-devel < 0.6.1-alt3.hg20090822

BuildRequires: /proc
BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: doxygen gcc-c++ gcc-fortran liblapack-devel
BuildRequires: swig
BuildRequires: python3-module-Cython

# closes unmets in autoimports
Provides: python-module-numpy-doc = %EVR
Provides: python-module-numpy-addons = %EVR
%py_provides %oname.addons

%description
NumPy is a general-purpose array-processing package designed to
efficiently manipulate large multi-dimensional arrays of arbitrary
records without sacrificing too much speed for small multi-dimensional
arrays.  NumPy is built on the Numeric code base and adds features
introduced by numarray as well as an extended C-API and the ability to
create arrays of arbitrary type.

There are also basic facilities for discrete fourier transform,
basic linear algebra and random number generation.

%package -n lib%oname
Summary: Shared libraries of NumPy
Group: System/Libraries
%if "%_lib" == "lib64"
Provides: libnpymath.so.%somver()(64bit)
%else
Provides: libnpymath.so.%somver
%endif

%description -n lib%oname
NumPy is a general-purpose array-processing package designed to
efficiently manipulate large multi-dimensional arrays of arbitrary
records without sacrificing too much speed for small multi-dimensional
arrays.  NumPy is built on the Numeric code base and adds features
introduced by numarray as well as an extended C-API and the ability to
create arrays of arbitrary type.

This package contains shared libraries of NumPy.

%package -n lib%oname-devel
Summary: Development files of NumPy
Group: Development/Python
Requires: lib%oname = %EVR
Requires: %name = %EVR
#Requires: python-module-numpydoc
Requires: %name-addons = %EVR
Requires: python-devel

%description -n lib%oname-devel
NumPy is a general-purpose array-processing package designed to
efficiently manipulate large multi-dimensional arrays of arbitrary
records without sacrificing too much speed for small multi-dimensional
arrays.  NumPy is built on the Numeric code base and adds features
introduced by numarray as well as an extended C-API and the ability to
create arrays of arbitrary type.

This package contains development files of NumPy.

%prep
%setup
%patch0 -p1

install -m644 %SOURCE1 %SOURCE2 .
tar xf %SOURCE3
sed -i 's|@LIBDIR@|%_libdir|g' site.cfg
sed -i 's|@PYVER@|%_python_version|g' site.cfg doc/Makefile
sed -i 's|@PYSUFF@||' site.cfg

# headers

sed -i 's|^prefix.*|prefix=%python_sitelibdir/%oname/core|' \
	%oname/core/npymath.ini.in
sed -i 's|^includedir.*|includedir=%_includedir/python%_python_version/%oname|' \
	%oname/core/npymath.ini.in

%install
%define optflags %optflags_default
unset CFLAGS
unset CXXFLAGS
unset FFLAGS
echo optflags = "%optflags"
INCS="-I%_includedir/suitesparse -I$PWD/numpy/core/include/numpy"
INCS="$INCS -I$PWD/numpy/core/include -I%buildroot%_includedir/python%_python_version/%oname"
INCS="$INCS -I%buildroot%_includedir"
DEFS="-DHAVE_FREXPF -DHAVE_FREXPL -DHAVE_FREXP -DHAVE_LDEXP -DHAVE_LDEXPL"
DEFS="$DEFS -DHAVE_EXPM1 -DHAVE_LOG1P -DHAVE_LDEXPF"
DEFS="$DEFS -UNPY_CPU_AMD64 -UNPY_CPU_X86"
DEFS="$DEFS -DNPY_ENABLE_SEPARATE_COMPILATION"
%add_optflags -fno-strict-aliasing $DEFS $INCS %optflags_shared

%python_build_debug --fcompiler=gnu95

%python_build_install

# private headers

install -d %buildroot%_includedir/python%_python_version
mv %buildroot%python_sitelibdir/%oname/core/include/%oname \
	%buildroot%_includedir/python%_python_version/%oname

install -d %buildroot%python_sitelibdir/%oname/core/include
ln -s %_includedir/python%_python_version/%oname \
	%buildroot%python_sitelibdir/%oname/core/include/
cp build/src.*/%oname/core/include/%oname/{*.h,*.c} \
	%buildroot%_includedir/python%_python_version/%oname/
install -d %buildroot%python_sitelibdir/%oname/core/lib/npy-pkg-config
cp -fR build/src.*/%oname/core/lib/npy-pkg-config/* \
	%buildroot%python_sitelibdir/%oname/core/lib/npy-pkg-config/

# pkg-config

sed -i 's|@VERSION@|%version|' %oname.pc
install -d %buildroot%_pkgconfigdir
install -m644 %oname.pc %buildroot%_pkgconfigdir
ln -s %oname.pc %buildroot%_pkgconfigdir/%oname-%majver.pc

# shared npymath

ar x $(find ./ -name 'libnpymath.a')
gcc -shared *.o -lm -Wl,-soname,libnpymath.so.%somver \
	-o %buildroot%_libdir/libnpymath.so.%sover
ln -s libnpymath.so.%sover \
	%buildroot%_libdir/libnpymath.so.%somver
ln -s libnpymath.so.%somver \
	%buildroot%_libdir/libnpymath.so
ln -s %_libdir/libnpymath.so.%somver \
	%buildroot%python_sitelibdir/%oname/core/lib/libnpymath.so

export PYTHONPATH=%buildroot%python_sitelibdir

# add missing files

cp -fR numpy/core/code_generators \
	%buildroot%python_sitelibdir/
install -p -m644 %oname/core/code_generators/numpy_api.py \
	%buildroot%python_sitelibdir/%oname
install -p -m644 %oname/core/code_generators/genapi.py \
	%buildroot%python_sitelibdir/%oname
install -p -m644 %oname/core/src/private/npy_config.h \
	%buildroot%_includedir/python%_python_version/%oname/

# delete unnecessary files

rm -f \
	$(find %buildroot%python_sitelibdir/%oname/ -name setup.py) \
	%buildroot%python_sitelibdir/%oname/f2py/docs/usersguide/setup_example.py

ln -s f2py%_python_version %buildroot%_bindir/f2py

# don't package tests and testing
rm -r %buildroot%python_sitelibdir/%oname/testing/
rm %buildroot%python_sitelibdir/%oname/conftest.py*
rm -r %buildroot%python_sitelibdir/%oname/*/test*
rm -r %buildroot%python_sitelibdir/%oname/tests/
rm %buildroot%python_sitelibdir/%oname/f2py/f2py_testing.py*
rm %buildroot%python_sitelibdir/%oname/ma/timer_comparison.py*

%find_lang %name

%pre
rm -f %_bindir/f2py
if [ -n %_libdir/libnpymath.so ]; then
	rm -f %_libdir/libnpymath.so
	rm -f %python_sitelibdir/%oname/core/lib/libnpymath.so
fi
if [ -d %python_sitelibdir/%oname/core/include ]; then
	rm -fR %python_sitelibdir/%oname/core/include
fi

%files -f %name.lang
%doc LICENSE.txt README.md THANKS.txt
%_bindir/*
%exclude %_bindir/f2py
%python_sitelibdir/%oname
%exclude %python_sitelibdir/%oname/f2py/src/fortranobject.h
%exclude %python_sitelibdir/%oname/random/randomkit.h
%exclude %python_sitelibdir/%oname/core/lib/npy-pkg-config
%exclude %python_sitelibdir/%oname/core/lib/libnpymath.so
%exclude %python_sitelibdir/%oname/doc
%exclude %python_sitelibdir/%oname/core/include
%exclude %python_sitelibdir/%oname/distutils/mingw
%exclude %python_sitelibdir/%oname/f2py/src
%python_sitelibdir/%oname-*.egg-info
%python_sitelibdir/code_generators

%files -n lib%oname
%_libdir/*.so.*

%files -n lib%oname-devel
%_libdir/*.so
%_pkgconfigdir/*
%python_sitelibdir/%oname/core/lib/libnpymath.so
%_includedir/python%_python_version/%oname
%python_sitelibdir/%oname/core/include
%python_sitelibdir/%oname/distutils/mingw
%python_sitelibdir/%oname/f2py/src
%python_sitelibdir/%oname/random/randomkit.h
%python_sitelibdir/%oname/core/lib/npy-pkg-config

%changelog
* Sun Aug 15 2021 Vitaly Lipatov <lav@altlinux.ru> 1:1.15.4-alt11
- build with python3-module-Cython

* Thu Aug 05 2021 Vitaly Lipatov <lav@altlinux.ru> 1:1.15.4-alt10
- drop python-module-numpydoc require from libnumpy-devel

* Tue Aug 03 2021 Grigory Ustinov <grenka@altlinux.org> 1:1.15.4-alt9
- Fixed BuildRequires.

* Thu Jul 22 2021 Stanislav Levin <slev@altlinux.org> 1:1.15.4-alt8
- Stopped shipping of tests and testing.

* Fri Oct 23 2020 Vitaly Lipatov <lav@altlinux.ru> 1:1.15.4-alt7
- drop BR:python-module-notebook

* Mon Aug 24 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1:1.15.4-alt6
- Rebuilt without python-3.

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

