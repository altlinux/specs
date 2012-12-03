Name: nlopt
Version: 2.3
Release: alt1
Summary: Library for nonlinear optimization
License: MIT, LGPL
Group: Sciences/Mathematics
Url: http://ab-initio.mit.edu/wiki/index.php/NLopt
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: gcc-c++ gcc-fortran python-devel
BuildPreReq: libnumpy-devel libhdf5-devel

%description
NLopt is a free/open-source library for nonlinear optimization,
providing a common interface for a number of different free optimization
routines available online as well as original implementations of various
other algorithms.

%package -n lib%name
Summary: Shared libraries of NLopt
Group: System/Libraries

%description -n lib%name
NLopt is a free/open-source library for nonlinear optimization,
providing a common interface for a number of different free optimization
routines available online as well as original implementations of various
other algorithms.

This package contains shared libraries of NLopt.

%package -n lib%name-cxx
Summary: Shared libraries of NLopt (C++ interface)
Group: System/Libraries

%description -n lib%name-cxx
NLopt is a free/open-source library for nonlinear optimization,
providing a common interface for a number of different free optimization
routines available online as well as original implementations of various
other algorithms.

This package contains shared libraries of NLopt (C++ interface).

%package -n lib%name-devel
Summary: Development files of NLopt
Group: Development/C++
Requires: lib%name = %version-%release
Requires: lib%name-cxx = %version-%release

%description -n lib%name-devel
NLopt is a free/open-source library for nonlinear optimization,
providing a common interface for a number of different free optimization
routines available online as well as original implementations of various
other algorithms.

This package contains development files of NLopt.

%package tests
Summary: Tests for NLopt
Group: Sciences/Mathematics
Requires: lib%name = %version-%release

%description tests
NLopt is a free/open-source library for nonlinear optimization,
providing a common interface for a number of different free optimization
routines available online as well as original implementations of various
other algorithms.

This package contains tests for NLopt.

%package -n python-module-%name
Summary: Python wrapper for NLopt 
Group: Development/Python
Requires: lib%name = %version-%release

%description -n python-module-%name
NLopt is a free/open-source library for nonlinear optimization,
providing a common interface for a number of different free optimization
routines available online as well as original implementations of various
other algorithms.

This package contains python wrapper for NLopt.

%package docs
Summary: Documentation for NLopt
Group: Development/Documentation
BuildArch: noarch

%description docs
NLopt is a free/open-source library for nonlinear optimization,
providing a common interface for a number of different free optimization
routines available online as well as original implementations of various
other algorithms.

This package contains development documentation for NLopt.

%prep
%setup

%autoreconf
mkdir .cxx
cp -fR * .cxx/

%build
%add_optflags -fno-strict-aliasing $(pkg-config hdf5 --cflags)
for i in c cxx; do
	if [ "$i" = "cxx" ]; then
		pushd .cxx
	fi
	sed -i 's|get_python_lib(0|get_python_lib(1|' configure
	%configure \
		--enable-shared=yes \
		--enable-static=no \
		--with-$i \
		--without-guile \
		--without-octave \
		--without-matlab
	%make_build
	if [ "$i" = "cxx" ]; then
		make install DESTDIR=$PWD/_
		popd
	fi
done

%install
%makeinstall_std

cp -P .cxx/_%_libdir/*.so* %buildroot%_libdir/

install -d %buildroot%_docdir/%name
for i in auglag bobyqa cdirect cobyla crs isres mlsl mma neldermead \
	newuoa praxis slsqp
do
	pushd $i
		for j in README*; do
			install -p -m644 $j %buildroot%_docdir/%name/$i.$j
		done
	popd
done
pushd direct
	for i in README AUTHORS COPYING *.pdf; do
		install -p -m644 $i %buildroot%_docdir/%name/direct.$i
	done
popd
for i in luksan stogo; do
	pushd $i
	for j in COPYRIGHT README *.pdf; do
		install -p -m644 $j %buildroot%_docdir/%name/$i.$j
	done
	popd
done

install -d %buildroot%_bindir
install -m755 test/.libs/* %buildroot%_bindir/

%files -n lib%name
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%_libdir/*.so.*
%exclude %_libdir/*_cxx.so.*

%files -n lib%name-cxx
%_libdir/*_cxx.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*
%_man3dir/*

%files tests
%doc test/*.c* test/*.h
%_bindir/*

%files docs
%_docdir/%name

%files -n python-module-%name
%python_sitelibdir/*
%exclude %python_sitelibdir/*.la

%changelog
* Mon Dec 03 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3-alt1
- Initial build for Sisyphus

