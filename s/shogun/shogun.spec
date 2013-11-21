Name: shogun
Version: 3.0.0
Release: alt1
Summary: A Large Scale Machine Learning Toolbox
Group: Sciences/Mathematics
License: GPL v3 or later
URL: http://www.shogun-toolbox.org/
Source: %name-%version.tar
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

BuildPreReq: python-devel gcc-c++ liblapack-devel /proc cmake
BuildPreReq: python-module-matplotlib python-module-wx2.9 libsnappy-devel
BuildPreReq: libglpk-devel libnumpy-devel libreadline-devel
BuildPreReq: liblpsolve-devel liblzma-devel swig doxygen graphviz
BuildPreReq: liblzo2-devel bzlib-devel zlib-devel boost-devel libjson-devel
BuildPreReq: texlive-latex-extra python-module-docutils ghostscript-classic
BuildPreReq: libarpack-devel libsuperlu-devel libhdf5-devel libxml2-devel
BuildPreReq: libnlopt-devel libcolpack-devel libarprec-devel
BuildPreReq: libcurl-devel ccache

Requires: lib%name = %version-%release
#Requires: %name-data = %version-%release

%description
The machine learning toolbox's focus is on large scale kernel methods and
especially on Support Vector Machines (SVM). It provides a generic SVM
object interfacing to several different SVM implementations, among them the
state of the art LibSVM and SVMlight.  Each of the SVMs can be
combined with a variety of kernels. The toolbox not only provides efficient
implementations of the most common kernels, like the Linear, Polynomial,
Gaussian and Sigmoid Kernel but also comes with a number of recent string
kernels as e.g. the Locality Improved, Fischer, TOP, Spectrum,
Weighted Degree Kernel (with shifts). For the latter the efficient
LINADD optimizations are implemented.  Also SHOGUN offers the freedom of
working with custom pre-computed kernels.  One of its key features is the
``combined kernel'' which can be constructed by a weighted linear combination
of a number of sub-kernels, each of which not necessarily working on the same
domain. An optimal sub-kernel weighting can be learned using Multiple Kernel
Learning.

Currently SVM 2-class classification and regression problems can be dealt
with. However SHOGUN also implements a number of linear methods like Linear
Discriminant Analysis (LDA), Linear Programming Machine (LPM), (Kernel)
Perceptrons and features algorithms to train hidden markov models.
The input feature-objects can be dense, sparse or strings and
of type int/short/double/char and can be converted into different feature types.
Chains of ``preprocessors'' (e.g. substracting the mean) can be attached to
each feature object allowing for on-the-fly pre-processing.

%package -n lib%name
Summary: Shared libraries of SHOGUN
Group: System/Libraries

%description -n lib%name
The machine learning toolbox's focus is on large scale kernel methods and
especially on Support Vector Machines (SVM). It provides a generic SVM
object interfacing to several different SVM implementations, among them the
state of the art LibSVM and SVMlight.  Each of the SVMs can be
combined with a variety of kernels. The toolbox not only provides efficient
implementations of the most common kernels, like the Linear, Polynomial,
Gaussian and Sigmoid Kernel but also comes with a number of recent string
kernels as e.g. the Locality Improved, Fischer, TOP, Spectrum,
Weighted Degree Kernel (with shifts). For the latter the efficient
LINADD optimizations are implemented.  Also SHOGUN offers the freedom of
working with custom pre-computed kernels.  One of its key features is the
``combined kernel'' which can be constructed by a weighted linear combination
of a number of sub-kernels, each of which not necessarily working on the same
domain. An optimal sub-kernel weighting can be learned using Multiple Kernel
Learning.

This package contains shared libraries of SHOGUN.

%package -n lib%name-devel
Summary: Development files of SHOGUN
Group: Development/C++
Requires: lib%name = %version-%release

%description -n lib%name-devel
The machine learning toolbox's focus is on large scale kernel methods and
especially on Support Vector Machines (SVM). It provides a generic SVM
object interfacing to several different SVM implementations, among them the
state of the art LibSVM and SVMlight.  Each of the SVMs can be
combined with a variety of kernels. The toolbox not only provides efficient
implementations of the most common kernels, like the Linear, Polynomial,
Gaussian and Sigmoid Kernel but also comes with a number of recent string
kernels as e.g. the Locality Improved, Fischer, TOP, Spectrum,
Weighted Degree Kernel (with shifts). For the latter the efficient
LINADD optimizations are implemented.  Also SHOGUN offers the freedom of
working with custom pre-computed kernels.  One of its key features is the
``combined kernel'' which can be constructed by a weighted linear combination
of a number of sub-kernels, each of which not necessarily working on the same
domain. An optimal sub-kernel weighting can be learned using Multiple Kernel
Learning.

This package contains development files of SHOGUN.

%package -n python-module-%name
Summary: Python interface for SHOGUN
Group: Development/Python
Requires: lib%name = %version-%release

%description -n python-module-%name
The machine learning toolbox's focus is on large scale kernel methods and
especially on Support Vector Machines (SVM). It provides a generic SVM
object interfacing to several different SVM implementations, among them the
state of the art LibSVM and SVMlight.  Each of the SVMs can be
combined with a variety of kernels. The toolbox not only provides efficient
implementations of the most common kernels, like the Linear, Polynomial,
Gaussian and Sigmoid Kernel but also comes with a number of recent string
kernels as e.g. the Locality Improved, Fischer, TOP, Spectrum,
Weighted Degree Kernel (with shifts). For the latter the efficient
LINADD optimizations are implemented.  Also SHOGUN offers the freedom of
working with custom pre-computed kernels.  One of its key features is the
``combined kernel'' which can be constructed by a weighted linear combination
of a number of sub-kernels, each of which not necessarily working on the same
domain. An optimal sub-kernel weighting can be learned using Multiple Kernel
Learning.

This package contains Python interface for SHOGUN.

%package data
Summary: Data files for SHOGUN
Group: Sciences/Mathematics
BuildArch: noarch

%description data
The machine learning toolbox's focus is on large scale kernel methods and
especially on Support Vector Machines (SVM). It provides a generic SVM
object interfacing to several different SVM implementations, among them the
state of the art LibSVM and SVMlight.  Each of the SVMs can be
combined with a variety of kernels. The toolbox not only provides efficient
implementations of the most common kernels, like the Linear, Polynomial,
Gaussian and Sigmoid Kernel but also comes with a number of recent string
kernels as e.g. the Locality Improved, Fischer, TOP, Spectrum,
Weighted Degree Kernel (with shifts). For the latter the efficient
LINADD optimizations are implemented.  Also SHOGUN offers the freedom of
working with custom pre-computed kernels.  One of its key features is the
``combined kernel'' which can be constructed by a weighted linear combination
of a number of sub-kernels, each of which not necessarily working on the same
domain. An optimal sub-kernel weighting can be learned using Multiple Kernel
Learning.

This package contains data files for SHOGUN.

%package examples
Summary: Examples for SHOGUN
Group: Documentation
%add_python_req_skip elwms generate_circle_data sg

%description examples
The machine learning toolbox's focus is on large scale kernel methods and
especially on Support Vector Machines (SVM). It provides a generic SVM
object interfacing to several different SVM implementations, among them the
state of the art LibSVM and SVMlight.  Each of the SVMs can be
combined with a variety of kernels. The toolbox not only provides efficient
implementations of the most common kernels, like the Linear, Polynomial,
Gaussian and Sigmoid Kernel but also comes with a number of recent string
kernels as e.g. the Locality Improved, Fischer, TOP, Spectrum,
Weighted Degree Kernel (with shifts). For the latter the efficient
LINADD optimizations are implemented.  Also SHOGUN offers the freedom of
working with custom pre-computed kernels.  One of its key features is the
``combined kernel'' which can be constructed by a weighted linear combination
of a number of sub-kernels, each of which not necessarily working on the same
domain. An optimal sub-kernel weighting can be learned using Multiple Kernel
Learning.

This package contains examples for SHOGUN.

%package docs
Summary: Documentation for SHOGUN
Group: Documentation
BuildArch: noarch

%description docs
The machine learning toolbox's focus is on large scale kernel methods and
especially on Support Vector Machines (SVM). It provides a generic SVM
object interfacing to several different SVM implementations, among them the
state of the art LibSVM and SVMlight.  Each of the SVMs can be
combined with a variety of kernels. The toolbox not only provides efficient
implementations of the most common kernels, like the Linear, Polynomial,
Gaussian and Sigmoid Kernel but also comes with a number of recent string
kernels as e.g. the Locality Improved, Fischer, TOP, Spectrum,
Weighted Degree Kernel (with shifts). For the latter the efficient
LINADD optimizations are implemented.  Also SHOGUN offers the freedom of
working with custom pre-computed kernels.  One of its key features is the
``combined kernel'' which can be constructed by a weighted linear combination
of a number of sub-kernels, each of which not necessarily working on the same
domain. An optimal sub-kernel weighting can be learned using Multiple Kernel
Learning.

This package contains documentation for SHOGUN.

%package tests
Summary: Tests for SHOGUN
Group: Sciences/Mathematics
BuildArch: noarch

%description tests
The machine learning toolbox's focus is on large scale kernel methods and
especially on Support Vector Machines (SVM). It provides a generic SVM
object interfacing to several different SVM implementations, among them the
state of the art LibSVM and SVMlight.  Each of the SVMs can be
combined with a variety of kernels. The toolbox not only provides efficient
implementations of the most common kernels, like the Linear, Polynomial,
Gaussian and Sigmoid Kernel but also comes with a number of recent string
kernels as e.g. the Locality Improved, Fischer, TOP, Spectrum,
Weighted Degree Kernel (with shifts). For the latter the efficient
LINADD optimizations are implemented.  Also SHOGUN offers the freedom of
working with custom pre-computed kernels.  One of its key features is the
``combined kernel'' which can be constructed by a weighted linear combination
of a number of sub-kernels, each of which not necessarily working on the same
domain. An optimal sub-kernel weighting can be learned using Multiple Kernel
Learning.

This package contains tests for SHOGUN.

%prep
%setup

%build
%ifarch x86_64
export ARCH=x86_64
%endif

%add_optflags -fpermissive -I%_includedir/openblas
cmake \
%ifarch x86_64
	-DLIB_SUFFIX:STRING=64 \
%endif
	-DCMAKE_INSTALL_PREFIX:PATH=%prefix \
	-DCMAKE_C_FLAGS:STRING="%optflags" \
	-DCMAKE_CXX_FLAGS:STRING="%optflags" \
	-DCMAKE_SKIP_RPATH:BOOL=ON \
	-DBLAS_goto2_LIBRARY:FILEPATH=%_libdir/libopenblas.so \
	-DARPACK_LIB:FILEPATH=%_libdir/libarpack_LINUX.so \
	-DPythonModular=ON \
	-DCmdLineStatic=ON \
	-DPythonStatic=ON \
	.

%make_build VERBOSE=1

pushd examples
./generate_documented.sh
popd
%make_build -C doc

%install
%makeinstall_std

rm -fR examples/documented/data examples/undocumented/data \
	tests/integration/data tests/integration/tests \
	examples/documented/java_modular/converter_locallylinearembedding_modular.py \
	examples/undocumented/java_modular/converter_locallylinearembedding_modular.py

install -d %buildroot%_libdir/%name/
%make -C examples clean
cp -fR examples %buildroot%_libdir/%name/

mv %buildroot%_datadir/%name/examples/* \
	%buildroot%_libdir/%name/examples/
chmod +x %buildroot%_libdir/%name/examples/libshogun/*

#install -d %buildroot%python_sitelibdir
#mv %buildroot%_libdir%python_sitelibdir/* \
#	%buildroot%python_sitelibdir/
#rm -f %buildroot%python_sitelibdir/elwms.so
#ln -s %_libdir/%name/elwms.so %buildroot%python_sitelibdir/elwms.so

#install -d %buildroot%_datadir/%name
#cp -fR data/* %buildroot%_datadir/%name/

%files
%doc *.md ChangeLog NEWS
%_bindir/*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*

%files -n python-module-%name
%python_sitelibdir/*

#files data
#_datadir/%name

%files docs
%doc doc/html

%files examples
%_libdir/%name/examples

%files tests
%doc tests

%changelog
* Thu Nov 21 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.0-alt1
- Version 3.0.0

* Mon Jul 29 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.0-alt1
- Version 2.1.0

* Tue Jul 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt3
- Rebuilt with new libhdf5

* Mon Feb 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt2
- Rebuilt with glpk 4.48

* Fri Jan 11 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1
- Version 2.0.0 (ALT #28174)

* Tue Dec 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt3
- Fixed build with OpenBLAS 0.2.5

* Sun Aug 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt2
- Built with OpenBLAS instead of GotoBLAS2

* Tue Mar 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1
- Version 1.1.0

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.10.0-alt1.1
- Rebuild with Python-2.7

* Fri May 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.0-alt1
- Version 0.10.0

* Fri Apr 15 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.3-alt2
- Built with GotoBLAS2 instead of ATLAS

* Tue Jul 27 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.3-alt1
- Initial build for Sisyphus

