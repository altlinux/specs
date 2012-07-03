%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

%define libtool_ver 2.4
%define iversion 1.0.0
Name: sundials
Version: 2.6.0
Release: alt11
Summary: SUite of Nonlinear and DIfferential/ALgebraic equation Solvers
License: BSD
Group: Sciences/Mathematics
Url: http://acts.nersc.gov/sundials/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

#Source: %name-2.4.0.tar.gz
Source1: cvode-%version.tar.gz
Source2: cvodes-%version.tar.gz
Source3: ida-%version.tar.gz
Source4: kinsol-%version.tar.gz
Source5: idas-%iversion.tar.gz
Source6: pvode.tar.gz
Source7: autogen.sh

Requires: lib%name = %version-%release

BuildPreReq: liblapack-devel
BuildPreReq: %mpiimpl-devel

%description
The family of solvers referred to as SUNDIALS consists of the following solvers:
 CVODE  - for integration of ordinary differential equation systems (ODEs)
          CVODE treats stiff and nonstiff ODE systems of the form
          y' = f(t,y), y(t0) = y0
 CVODES - for integration and sensitivity analysis of ODEs
          CVODES treats stiff and nonstiff ODE systems of the form
          y' = f(t,y,p), y(t0) = y0(p)
 IDA    - for integration of differential-algebraic equation systems (DAEs)
          IDA treats DAE systems of the form
          F(t,y,y') = 0, y(t0) = y0, y'(t0) = y0'
 IDAS   - for integration and sensitivity analysis of DAEs
          IDAS treats DAE systems of the form
          F(t,y,y',p) = 0, y(t0) = y0(p), y'(t0) = y0'(p)
 KINSOL - for solution of nonlinear algebraic systems
          KINSOL treats nonlinear systems of the form
          F(u) = 0

%package -n lib%name
Summary: Shared libraries of SUNDIALS, double precision
Group: System/Libraries
Requires: %name = %version-%release

%description -n lib%name
SUite of Nonlinear and DIfferential/ALgebraic equation Solvers.

This package contains shared libraries of SUNDIALS, with serial and
parallel implementations, double precision.

%package -n lib%name-devel
Summary: Development files of SUNDIALS, double precision
Group: Development/Other
Requires: %name = %version-%release
Requires: lib%name = %version-%release

%description -n lib%name-devel
SUite of Nonlinear and DIfferential/ALgebraic equation Solvers.

This package contains development files of SUNDIALS, with serial and
parallel implementations, double precision.

%package -n lib%name-single-devel-static
Summary: Static libraries of SUNDIALS, single precision
Group: Development/Other
Requires: %name = %version-%release
Requires: lib%name-devel = %version-%release

%description -n lib%name-single-devel-static
SUite of Nonlinear and DIfferential/ALgebraic equation Solvers.

This package contains static libraries of SUNDIALS, with serial and
parallel implementations, single precision.

%package -n lib%name-double-devel-static
Summary: Static libraries of SUNDIALS, double precision
Group: Development/Other
Requires: %name = %version-%release
Requires: lib%name-devel = %version-%release

%description -n lib%name-double-devel-static
SUite of Nonlinear and DIfferential/ALgebraic equation Solvers.

This package contains static libraries of SUNDIALS, with serial and
parallel implementations, double precision.

%package -n lib%name-extended-devel-static
Summary: Static libraries of SUNDIALS, long double precision
Group: Development/Other
Requires: %name = %version-%release
Requires: lib%name-devel = %version-%release

%description -n lib%name-extended-devel-static
SUite of Nonlinear and DIfferential/ALgebraic equation Solvers.

This package contains static libraries of SUNDIALS, with serial and
parallel implementations, long double precision.

%package -n lib%name-devel-doc
Summary: Documentation for SUNDIALS
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-doc
SUite of Nonlinear and DIfferential/ALgebraic equation Solvers.

This package contains development documentation for SUNDIALS.

%package examples
Summary: Examples of using SUNDIALS
Group: Development/Documentation
Requires: lib%name = %version-%release
Requires: %name-examples-src = %version-%release

%description examples
SUite of Nonlinear and DIfferential/ALgebraic equation Solvers.

This package contains compiled examples of using SUNDIALS.

%package examples-src
Summary: Examples sources and documentation of using SUNDIALS
Group: Development/Documentation
BuildArch: noarch

%description examples-src
SUite of Nonlinear and DIfferential/ALgebraic equation Solvers.

This package contains examples sources and documentation of using SUNDIALS.

%prep
tar -xzf %SOURCE1
tar -xzf %SOURCE2
tar -xzf %SOURCE3
tar -xzf %SOURCE4
tar -xzf %SOURCE5
tar -xzf %SOURCE6
install -p -m755 %SOURCE7 .

%install
mkdir _ex
mkdir _ex-doc
mv $(find ./ -name '*examples.pdf') _ex-doc/

mpi-selector --set %mpiimpl
source %_sysconfdir/profile.d/mpi-selector.sh
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

TOPDIR=$PWD
%add_optflags %optflags_shared

function buildIt() {
	mkdir -p $TOPDIR/_ex-src/$1
	cp -fR examples/* $TOPDIR/_ex-src/$1/
	#autoreconf
	$TOPDIR/autogen.sh %libtool_ver
	for p in single extended double; do
		rm -f %buildroot%_libdir/*fnvec*.so*
		sed -ri \
			's|^(hardcode_libdir_flag_spec\|runpath_var)=.*|\1=-Wl,-rpath,%mpidir/lib|' \
			configure
		%configure \
			--enable-shared \
			--with-mpi-root=%mpidir \
			--with-mpi-libs="-lmpi" \
			--with-precision=$p \
			--with-blas="-lgoto2" \
			--with-lapack="-llapack" \
			--enable-examples
		sed -i -e 's/^\(available_tags\).*/\1=/' libtool
		%make MPILIB=%mpilib
		%makeinstall includedir=%buildroot%_includedir/%name-$p
		case $p in
			single) suff=_s ;;
			extended) suff=_l ;;
			*) suff= ;;
		esac
		if [ "$suff" != "" ]; then
			pushd %buildroot%_libdir
			mkdir -p store
			for i in $(ls *.a|sed -e 's/\.a//'); do
				if [ ! -f store/${i}$suff.a ]; then
					mv $i.a store/${i}$suff.a
				else
					rm -f $i.a
				fi
			done
			popd
		fi
		for f in $(find examples -type f -perm -u=x); do
			cp -f $f $TOPDIR/_ex/
		done
		%make clean
	done
}

for i in cvode cvodes ida idas kinsol; do
	pushd $i
	buildIt $i
	popd
done

mv %buildroot%_libdir/store/* %buildroot%_libdir/

install -m755 _ex/* %buildroot%_bindir
install -d %buildroot%_docdir/lib%name-devel
install -p -m644 $(find ./ -name '*guide.pdf') \
	%buildroot%_docdir/lib%name-devel

# pvode

pushd pvode
mkdir -p lib
for dir in source precon fcmix examples fcmix/examples; do
	pushd $dir
	%make_build MPIDIR=%mpidir
	popd
done
install -m755 examples/pv?x examples/pvkxb \
	fcmix/examples/diag?f fcmix/examples/diagkbf \
	%buildroot%_bindir
install -m644 lib/* %buildroot%_libdir
install -d %buildroot%_includedir/pvode
install -p -m644 include/* %buildroot%_includedir/pvode
popd

mkdir -p _ex-src/pvode/fcmix
cp pvode/examples/*.c _ex-src/pvode/
cp pvode/fcmix/examples/*.f _ex-src/pvode/fcmix/

%files
%doc cvode/LICENSE cvode/README

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_bindir/fortran-update.sh
%_bindir/sundials-config
%_libdir/*.so
%_includedir/*

#files -n lib%name-single-devel-static
#_libdir/*_s.a

#files -n lib%name-double-devel-static
#_libdir/*.a
#exclude %_libdir/*_s.a
#exclude %_libdir/*_l.a

#files -n lib%name-extended-devel-static
#_libdir/*_l.a

%files -n lib%name-devel-doc
%_docdir/lib%name-devel

%files examples
%_bindir/*
%exclude %_bindir/fortran-update.sh
%exclude %_bindir/sundials-config

%files examples-src
%doc _ex-src
%doc _ex-doc/*

%changelog
* Sun Jun 24 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.0-alt11
- Rebuilt with OpenMPI 1.6

* Wed Apr 18 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.0-alt10
- Rebuilt with libtool_2.4

* Wed Dec 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.0-alt9
- Fixed RPATH

* Fri Apr 15 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.0-alt8
- Rebuilt

* Sun Apr 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.0-alt7
- Built with GotoBLAS2 instead of ATLAS
- Disabled devel-static packages

* Fri Feb 11 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.0-alt6
- Rebuilt for debuginfo

* Thu Oct 21 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.0-alt5
- Fixed overlinking of libraries

* Sun Jan 17 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.0-alt4
- Fixed for autoconf 2.6

* Thu Nov 05 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.0-alt3
- Rebuilt without static build requirements

* Sun Jun 14 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.0-alt2
- Added PVODE

* Sat May 30 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.0-alt1
- Initial build for Sisyphus

