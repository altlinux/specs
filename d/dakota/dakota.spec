%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl
%set_compress_method gzip

%define teuver 10
Name: dakota
Version: 5.2
%define somver 0
%define sover %somver.0.0
Release: alt4
Epoch: 1
Summary: Design Analysis Kit for Optimization and Terascale Applications
License: LGPL v2.1
Group: Sciences/Mathematics
Url: http://www.cs.sandia.gov/dakota/software.html
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: Dakota_stable.src.tar

Requires: lib%name = %epoch:%version-%release

BuildPreReq: libltdl-devel boost-signals-devel boost-filesystem-devel
BuildPreReq: gcc-fortran gcc-c++ libnumpy-devel python-devel cmake
BuildPreReq: liblapack-devel doxygen libXtst-devel librandom-devel
BuildPreReq: libteuchos%teuver-devel libnewmat-devel libfftw3-mpi-devel
BuildPreReq: libICE-devel libSM-devel libX11-devel libXau-devel graphviz
BuildPreReq: libXext-devel libXt-devel zlib-devel libplplot-devel
BuildPreReq: boost-devel cppunit-devel flex imake libXmu-devel libXp-devel
BuildPreReq: libXpm-devel libarprec-devel libexpat-devel libfreetype-devel
BuildPreReq: libgd2-devel libjpeg-devel libcurl-devel ghostscript-utils
BuildPreReq: libopenmotif-devel libpng-devel libtrilinos%teuver-devel
BuildPreReq: libxml2-devel openmpi-devel svgalib-devel plplot-tk
BuildPreReq: texlive-fonts-recommended texlive-generic-recommended
BuildPreReq: texlive-xetex cmake libxkbfile-devel chrpath
BuildPreReq: libplplot-fortran-devel libstdc++-devel liblinpack-devel
BuildPreReq: boost-program_options-devel libgsl-devel libXScrnSaver-devel
BuildPreReq: libXcomposite-devel libXdamage-devel libXdmcp-devel
BuildPreReq: libXxf86misc-devel libXxf86vm-devel
Requires: plplot-tk libnewmat

%description
A Multilevel Parallel Object-Oriented Framework for Design Optimization,
Parameter Estimation, Uncertainty Quantification, and Sensitivity
Analysis.

%package doc
Summary: Documentation for DAKOTA
Group: Documentation
BuildArch: noarch

%description doc
A Multilevel Parallel Object-Oriented Framework for Design Optimization,
Parameter Estimation, Uncertainty Quantification, and Sensitivity
Analysis.

This package contains documentation for DAKOTA.


%package -n lib%name
Summary: Shared libraries of DAKOTA
Group: System/Libraries
Requires: libteuchos%teuver
Requires: libplplot libnewmat

%description -n lib%name
A Multilevel Parallel Object-Oriented Framework for Design Optimization,
Parameter Estimation, Uncertainty Quantification, and Sensitivity
Analysis.

This package contains shared libraries of DAKOTA.

%package -n lib%name-devel
Summary: Development files of DAKOTA
Group: Development/C++
Requires: lib%name = %epoch:%version-%release
#Requires: libteuchos%teuver-devel libfftw3-mpi-devel
#Requires: libplplot-devel libplplot-fortran-devel libnewmat-devel
#Requires: boost-devel

%description -n lib%name-devel
A Multilevel Parallel Object-Oriented Framework for Design Optimization,
Parameter Estimation, Uncertainty Quantification, and Sensitivity
Analysis.

This package contains development files of DAKOTA.

%prep
%setup

cp packages/pecos/packages/LHS/mods/Cparam.f90 \
	packages/pecos/packages/LHS/mods/cparam.mod
cp packages/OPTPP/include/Constraint.h \
	packages/OPTPP/include/DConstraint.h
rm -fR methods/OPTPP/newmat11 \
	packages/plplot packages/boost packages/teuchos \
	packages/pecos/packages/fftw packages/OPTPP/newmat11

sed -i 's|@SOVERSION@|%somver|g' src/CMakeLists.txt \
	packages/pecos/packages/VPISparseGrid/src/CMakeLists.txt
sed -i 's|@VERSION@|%sover|g' src/CMakeLists.txt \
	packages/pecos/packages/VPISparseGrid/src/CMakeLists.txt

%ifarch x86_64
LIB64=64
%endif
sed -i "s|@64@|$LIB64|g" packages/acro/config/siteconfig.ini

#for i in $(find ./ -name Makefile.in); do
#	sed -i 's|\-rpath \$(libdir)||g' $i
#done

%build
mpi-selector --set %mpiimpl
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath=%mpidir/lib -L%mpidir/lib"

DEFS="-DOPT_COMPATIBLE -DArith_Kind_ASL=1 -DIEEE_8087=1 -DUSING_DOUBLE"
DEFS="$DEFS -Duse_namespace -DHAVE_TEUCHOS_BLASFLOAT -DOMPI_SKIP_MPICXX"
DEFS="$DEFS -DWITH_MPI"
INCS="-I%_includedir/X11 -I%mpidir/include -I%_includedir/arprec"
INCS="$INCS -I%_includedir/numpy -I%_includedir/newmat"
INCS="$INCS -I%_includedir/plplot -I%_includedir/fftw3-mpi"
INCS="$INCS -I%_includedir/plplot"
%add_optflags $INCS -fno-strict-aliasing $DEFS %optflags_shared
LIBS="-larprec -lexpat -lxml2 -ldl -lXmu -lXm -lXt -lpthread -lm"
LIBS="$LIBS -lteuchos -llapack -lgoto2 -lgfortran"
LIBS="$LIBS -L%mpidir/lib -lmpi_cxx -lmpi -Wl,-R%mpidir/lib -lstdc++"
export MPIDIR=%mpidir
export LIBTOOLDIR=$PWD
#sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' \
#	configure ltmain.sh *.m4 packages/*/ltmain.sh packages/*/*.m4 \
#	packages/*/configure
%configure \
       --includedir=%_includedir/%name \
       --enable-shared \
       --disable-static \
       --enable-docs \
       --without-acro \
       --with-teuchos-include=%_includedir \
       --with-teuchos-lib=%_libdir \
       --with-incdirs="$INCS" \
       --with-blas=goto2 \
       --with-lapack=lapack \
       --enable-f77 \
       --with-boost=%_includedir \
       --with-x \
       --with-gsl=%prefix \
       --enable-teuchos-arprec \
       --with-libs="$LIBS" \
       --enable-teuchos-expat \
       --enable-teuchos-libxml2 \
       --enable-teuchos-boost \
       --enable-mpi \
       --with-mpi=%mpidir \
       --with-python \
       --with-graphics \
       --with-plugin \
			 --without-ampl

sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' libtool
%make_build

pushd docs
%make pdf
%make -C latex-user pdf-local
doxygen
popd

%install
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath=%mpidir/lib -L%mpidir/lib"

export MPIDIR=%mpidir
export LIBTOOLDIR=$PWD

%makeinstall_std

install -d %buildroot%_datadir/%name
mv %buildroot%_bindir/%name.input.* %buildroot%_datadir/%name/
install -d %buildroot%_docdir/%name
install -m644 docs/latex-user/*.pdf %buildroot%_docdir/%name

# make all static as shared libraries
pushd %buildroot%_libdir
for i in libncsuopt libnidr
do
	mpic++ -shared -Wl,--whole-archive $i.a -Wl,--no-whole-archive \
		-o $i.so.%sover -Wl,-soname,$i.so.%somver  -L. -ldakota \
		-llapack -lgoto2 -lm \
		-L%mpidir/lib -Wl,-rpath,%mpidir/lib -lgfortran -Wl,-z,defs
	ln -s $i.so.%sover $i.so.%somver
	ln -s $i.so.%somver $i.so
done
popd

for i in %buildroot%_bindir/* %buildroot%_libdir/*.so
do
	chrpath -r %mpidir/lib $i || chrpath -d $i ||:
done

install -d %buildroot%_man3dir
install -m644 docs/man-dev/man3/* %buildroot%_man3dir

install -p -m644 \
	packages/JEGA/eddy/config/include/current_function.hpp \
	packages/JEGA/eddy/threads/include/mutex_lock.hpp \
	packages/JEGA/eddy/threads/include/mutex.hpp \
	packages/JEGA/eddy/threads/include/inline/mutex.hpp.inl \
	packages/JEGA/eddy/threads/include/inline/mutex_lock.hpp.inl \
	packages/JEGA/eddy/threads/include/thread_exceptions.hpp \
	packages/DDACE/ddace_config.h \
	%buildroot%_includedir/%name
install -d %buildroot%_includedir/%name/threads/include
install -p -m644 packages/JEGA/eddy/threads/include/config.hpp \
	%buildroot%_includedir/%name/threads/include
install -d %buildroot%_includedir/%name/utilities/include
install -p -m644 packages/JEGA/eddy/utilities/include/config.hpp \
	%buildroot%_includedir/%name/utilities/include
install -d %buildroot%_includedir/%name/detail
install -p -m644 packages/JEGA/eddy/logging/detail/macros.hpp \
	%buildroot%_includedir/%name/detail
install -d %buildroot%_includedir/%name/logging/include
install -p -m644 packages/JEGA/eddy/logging/include/config.hpp \
	%buildroot%_includedir/%name/logging/include
install -d %buildroot%_includedir/%name/config/include
install -p -m644 packages/JEGA/eddy/config/include/config.hpp \
	%buildroot%_includedir/%name/config/include
	
# fix headers

sed -i 's|\.\./\.\./threads/|threads/|' \
	%buildroot%_includedir/%name/logging/include/config.hpp \
	%buildroot%_includedir/%name/config.hpp \
	%buildroot%_includedir/%name/utilities/include/config.hpp
sed -i 's|\.\./include|threads/include|' \
	%buildroot%_includedir/%name/mutex_lock.hpp \
	%buildroot%_includedir/%name/mutex.hpp \
	%buildroot%_includedir/%name/thread_exceptions.hpp
sed -i 's|\.\./include|logging/include|' \
	%buildroot%_includedir/%name/threadsafe.hpp \
	%buildroot%_includedir/%name/detail/macros.hpp \
	%buildroot%_includedir/%name/log4j_levels.hpp \
	%buildroot%_includedir/%name/appending_log.hpp \
	%buildroot%_includedir/%name/cb_level_log_gateway.hpp \
	%buildroot%_includedir/%name/volume_levels.hpp \
	%buildroot%_includedir/%name/basic_log_gateway.hpp \
	%buildroot%_includedir/%name/minimal_levels.hpp \
	%buildroot%_includedir/%name/list_log.hpp \
	%buildroot%_includedir/%name/dakota_levels.hpp \
	%buildroot%_includedir/%name/ostream_log.hpp \
	%buildroot%_includedir/%name/text_entry.hpp \
	%buildroot%_includedir/%name/entries.hpp \
	%buildroot%_includedir/%name/file_log.hpp \
	%buildroot%_includedir/%name/ostream_entry.hpp \
	%buildroot%_includedir/%name/level_log_gateway.hpp \
	%buildroot%_includedir/%name/exceptions.hpp \
	%buildroot%_includedir/%name/file_ring_log.hpp \
	%buildroot%_includedir/%name/cougaar_levels.hpp \
	%buildroot%_includedir/%name/level_classes.hpp \
	%buildroot%_includedir/%name/decorator_log.hpp \
	%buildroot%_includedir/%name/java_util_levels.hpp \
	%buildroot%_includedir/%name/null_log.hpp
sed -i 's|\(config\.hpp\)|utilities/include/\1|' \
	%buildroot%_includedir/%name/bit_mask.hpp \
	%buildroot%_includedir/%name/RandomNumberGenerator.hpp \
	%buildroot%_includedir/%name/registry.hpp \
	%buildroot%_includedir/%name/int_types.hpp \
	%buildroot%_includedir/%name/keyed_registry.hpp \
	%buildroot%_includedir/%name/EDDY_DebugScope.hpp \
	%buildroot%_includedir/%name/extremes.hpp \
	%buildroot%_includedir/%name/Math.hpp \
	%buildroot%_includedir/%name/numeric_limits.hpp \
	%buildroot%_includedir/%name/iterator.hpp \
	%buildroot%_includedir/%name/entries.hpp
sed -i 's|\.\./\.\./config/|config/|' \
	%buildroot%_includedir/%name/threads/include/config.hpp
sed -i 's|\(config\.hpp\)|config/include/\1|' \
	%buildroot%_includedir/%name/current_function.hpp
sed -i 's|\(config\.hpp\)|logging/include/\1|' \
	%buildroot%_includedir/%name/logs.hpp \
	%buildroot%_includedir/%name/macros.hpp \
	%buildroot%_includedir/%name/log_gateways.hpp \
	%buildroot%_includedir/%name/exceptions.hpp \
	%buildroot%_includedir/%name/level_classes.hpp
sed -i 's|\.\./\(detail/macros\.hpp\)|\1|' \
	%buildroot%_includedir/%name/macros.hpp

function fixHdr() {
	sed -i "s|$1||" $(egrep -R "$1" %buildroot%_includedir |\
		awk -F : '{print $1}')
}

fixHdr '\.\/inline\/'
fixHdr '\.\.\/Utilities\/include\/'
fixHdr '\.\/include\/'
fixHdr '\.\/detail\/'
fixHdr '\.\.\/level_classes\/'
fixHdr '\.\.\/SOGA\/include\/FitnessAssessors\/'
fixHdr '\.\.\/FrontEnd\/Core\/include\/'
fixHdr '\.\.\/entries\/'
fixHdr '\.\.\/log_gateways\/'
fixHdr '\.\.\/logs\/'
fixHdr '\.\.\/\.\./'
fixHdr '\.\.\/'
fixHdr 'nidr\/'
fixHdr 'inline\/'

install -d %buildroot%_includedir/%name/logging/level_classes
install -d %buildroot%_includedir/%name/logging/entries
install -d %buildroot%_includedir/%name/Convergers
install -d %buildroot%_includedir/%name/Mutators
install -d %buildroot%_includedir/%name/Crossers
install -d %buildroot%_includedir/%name/Selectors
install -d %buildroot%_includedir/%name/Evaluators

ln -s ../../text_entry.hpp \
	%buildroot%_includedir/%name/logging/entries
ln -s ../../ostream_entry.hpp \
	%buildroot%_includedir/%name/logging/entries
ln -s ../../dakota_levels.hpp \
	%buildroot%_includedir/%name/logging/level_classes
ln -s ../../text_entry.hpp \
	%buildroot%_includedir/%name/logging/level_classes
ln -s ../../keyed_registry.hpp \
	%buildroot%_includedir/%name/utilities/include
ln -s ../../int_types.hpp \
	%buildroot%_includedir/%name/utilities/include
ln -s ../../bit_mask.hpp \
	%buildroot%_includedir/%name/utilities/include
ln -s ../../numeric_limits.hpp \
	%buildroot%_includedir/%name/utilities/include
ln -s ../../extremes.hpp \
	%buildroot%_includedir/%name/utilities/include
ln -s ../../Math.hpp \
	%buildroot%_includedir/%name/utilities/include
ln -s ../../EDDY_DebugScope.hpp \
	%buildroot%_includedir/%name/utilities/include
ln -s ../MetricTrackerConvergerBase.hpp \
	%buildroot%_includedir/%name/Convergers
ln -s ../MaxGenEvalConverger.hpp \
	%buildroot%_includedir/%name/Convergers
ln -s ../OffsetMutatorBase.hpp \
	%buildroot%_includedir/%name/Mutators
ln -s ../NPointCrosserBase.hpp \
	%buildroot%_includedir/%name/Crossers
ln -s ../RouletteWheelSelector.hpp \
	%buildroot%_includedir/%name/Selectors
ln -s ../SimpleFunctorEvaluator.hpp \
	%buildroot%_includedir/%name/Evaluators
ln -s ../../default_types.hpp \
	%buildroot%_includedir/%name/logging/include
ln -s ../../macros.hpp \
	%buildroot%_includedir/%name/logging/include

%files
%doc COPYRIGHT LICENSE README
%_bindir/*
%_datadir/%name

%files doc
%doc docs/latex-user/*.pdf
%doc docs/html-dev
%_docdir/%name
%_man3dir/*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*

%changelog
* Mon Jun 25 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:5.2-alt4
- Rebuilt with OpenMPI 1.6

* Wed Apr 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:5.2-alt3
- Rebuilt with Boost 1.49.0

* Wed Feb 15 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:5.2-alt2
- Rebuilt with Trilinos 10.10.0

* Mon Dec 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:5.2-alt1
- Version 5.2

* Tue Dec 13 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:5.1.0-alt3
- Fixed RPATH

* Fri Dec 02 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:5.1.0-alt2
- Rebuilt with Boost 1.48

* Fri Nov 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:5.1.0-alt1
- Updated

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1:5.1-alt1.1
- Rebuild with Python-2.7

* Fri Apr 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:5.1-alt1
- Version 5.1

* Thu Apr 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20101304-alt4
- Rebuilt

* Fri Apr 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20101304-alt3
- Built with GotoBLAS instead of ATLAS
- Disabled build static libraries

* Mon Mar 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20101304-alt2
- Rebuilt for debuginfo

* Sat Nov 06 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20101304-alt1
- Initial build for Sisyphus

