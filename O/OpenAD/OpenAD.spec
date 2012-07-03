%define sover 0

Name: OpenAD
Version: 20120321
Release: alt1
Summary: A tool for automatic differentiation (AD) of numerical computer programs
License: BSD
Group: Sciences/Mathematics
Url: http://www.mcs.anl.gov/OpenAD/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
Source1: setenv2.sh
Source2: XAIFOBJS

BuildPreReq: gcc-fortran python-modules gcc-c++ libxerces-c28-devel
BuildPreReq: tcsh libsexpr-devel boost-devel /usr/bin/latex
BuildPreReq: doxygen graphviz

Requires: lib%name = %version-%release

%description
OpenAD is a tool for automatic differentiation (AD) of numerical
computer programs.

The main goals for OpenAD initially defined for the  ACTS project are:

1. Develop a flexible, modular, open source tool that can generate
   adjoint codes of numerical simulation programs,
2. Establish a platform for easy implementation and testing of source
   transformation algorithms via a language-independent abstract
   intermediate representation
3. Support for source code written in C and Fortan,
4. Generate  an adjoint for the MIT general circulation model.  The
   example on  the right (animated gif)  shows a sensitivity map of the
   heat transport in the north atlantic to temperature in a depth of
   1590 meters over a period of 10 years going backwards in time. There
   are also results of a 100 year simulation at three depth levels.

The intention of this project summary is to give potential users of
adjoint compiler technology an overview of the current capabilities of
OpenAD together with pointers to more detailed information in the form
of online documentation and published papers. It should substantiate the
following important points:

* OpenAD has been used successfully to implement a source transformation
  tool for the automatic generation of adjoint Fortran code.
* The automatic generation of adjoint code for large-scale numerical
  simulations is a highly complex and work intensive task in terms of
  algorithmic and software-technological problems.
* The ACTS project made an important first step in the right direction.
  Further funding is required to continue the work on open software for
  the automatic generation of robust and efficient adjoint code.

%package -n lib%name
Summary: Shared libraries of OpenAD
Group: System/Libraries

%description -n lib%name
OpenAD is a tool for automatic differentiation (AD) of numerical
computer programs.

This package contains shared libraries of OpenAD.

%package -n lib%name-devel
Summary: Development files of OpenAD
Group: Development/C++
Requires: lib%name = %version-%release

%description -n lib%name-devel
OpenAD is a tool for automatic differentiation (AD) of numerical
computer programs.

This package contains development files of OpenAD.

%package docs
Summary: Documentation and examples for OpenAD
Group: Documentation
BuildArch: noarch

%description docs
OpenAD is a tool for automatic differentiation (AD) of numerical
computer programs.

This package contains documentation and examples for OpenAD.

%package -n libxaifBooster
Summary: Shared libraries of XML Abstract Interface Form (XAIF)
Group: System/Libraries

%description -n libxaifBooster
The XML Abstract Interface Form (XAIF) provides a language-independent
representation of constructs common in imperative languages, such as C
and Fortran. The main role of the XAIF is to define a layer of
abstraction, so that various automatic differentiation (AD) algorithms
can be expressed in a language-neutral manner.

%package -n libxaifBooster-devel
Summary: Development files of XML Abstract Interface Form (XAIF)
Group: Development/C++
Requires: libxaifBooster = %version-%release

%description -n libxaifBooster-devel
The XML Abstract Interface Form (XAIF) provides a language-independent
representation of constructs common in imperative languages, such as C
and Fortran. The main role of the XAIF is to define a layer of
abstraction, so that various automatic differentiation (AD) algorithms
can be expressed in a language-neutral manner.

This package contains development files of XAIF.

%package -n libxaifBooster-devel-doc
Summary: Documentation for XML Abstract Interface Form (XAIF)
Group: Development/Documentation
BuildArch: noarch

%description -n libxaifBooster-devel-doc
The XML Abstract Interface Form (XAIF) provides a language-independent
representation of constructs common in imperative languages, such as C
and Fortran. The main role of the XAIF is to define a layer of
abstraction, so that various automatic differentiation (AD) algorithms
can be expressed in a language-neutral manner.

This package contains development documentation for XAIF.

%prep
%setup
install -m755 %SOURCE1 %SOURCE2 .

rm -fR boost xercesc

%build
pushd xaifBooster/doc
%make
popd

pushd OpenADFortTk
doxygen
popd

mv Open64/documentation Open64.doc

%install
alias strip=echo
%ifarch x86_64
export BITS=64
export LIB_SUFFIX=64
export TARG=targ_ia64_ia64_linux
export BUILDARCH=build-x86_64-Linux
export FortTkARCH=x86_64
%else
export BITS=32
export TARG=targ_ia32_ia64_linux
export BUILDARCH=build-x86-Linux
export FortTkARCH=x86
%endif
export DESTDIR=%buildroot
export TOPDIR=$PWD

install -d %buildroot%_libdir/whirl2f

source ./setenv.sh
%make -C Open64
cp Open64/osprey1.0/targ*linux/be/be.so \
	Open64/osprey1.0/targ*linux/be/itanium.so \
	%buildroot%_libdir/
ln -s ../be.so %buildroot%_libdir/whirl2f/be.so

for i in OpenAnalysis OpenADFortTk
do
	pushd $i
	%autoreconf
	popd
done

source ./setenv2.sh
export LD_LIBRARY_PATH=%buildroot%_libdir
%make

export CC=
export CXX=
export CFLAGS=
export CXXFLAGS=
export F90CFLAGS=
export F77FLAGS=
export FFLAGS=
export XERCESCROOT=

%make open64_install

source ./setenv2.sh
%makeinstall_std

for i in $(find ./xaifBooster/ -name '*.h*') \
	$(find ./xaifBooster/ -name '*.cpp') \
	$(find ./xaifBooster/ -name '*.inc')
do
	cp --parents $i %buildroot%_includedir/
done

mkdir lib
cp $(find ./xaifBooster -name '*.a') lib/
pushd lib
rm -f libxaifBoosterInlinableXMLRepresentation.a
for i in libxaifBoosterutils \
	$(ls -1 |sed 's|\.a||' |egrep -v libxaifBoosterutils)
do
	if [ "$i" = "libxaifBoosterutils" ]; then
		OBJS="$(cat ../XAIFOBJS)"
	else
		OBJS=
	fi
	if [ "$i" != "libxaifBoosterCrossCountryInterface" -a \
		"$i" != "libxaifBoosterAdjointUtils" -a \
		"$i" != "libxaifBoosterCodeReplacement" ]; then
		g++ -shared -Wl,-whole-archive $i.a $OBJS -Wl,-no-whole-archive \
			-Wl,-soname,$i.so.%sover -o %buildroot%_libdir/$i.so.%sover \
			$LIBS -lxerces-c
		ln -s $i.so.%sover %buildroot%_libdir/$i.so
	fi
	LIBS="-L%buildroot%_libdir -lxaifBoosterutils"
done
popd

install -d %buildroot%_bindir
mv %buildroot$TOPDIR/OpenADFortTk/OpenADFortTk-$FortTkARCH-Linux/bin/* \
	%buildroot%_bindir/

sed -i 's|\./tools|/usr/lib64/OpenAD/tools|' \
	%buildroot%_libdir/%name/setenv.sh

echo '#!/bin/sh' >openad
echo '. %_libdir/%name/setenv.sh' >>openad
echo '%_libdir/%name/bin/openad $@' >>openad
install -m755 openad %buildroot%_bindir

#pushd %buildroot%_libdir
#g++ -shared -Wl,-whole-archive ../lib/libOAul.a -Wl,-no-whole-archive \
#	-Wl,-soname,libOAul.so.0 -o libOAul.so.0
#ln -s libOAul.so.0 libOAul.so
#popd

%files
%_bindir/*
%_libdir/%name

%files -n lib%name
%_libdir/libbe.so
%_libdir/be.so
%_libdir/itanium.so
%_libdir/*.so.*
%exclude %_libdir/libxaif*.so.*

%files -n lib%name-devel
%_includedir/OpenAnalysis
%_libdir/*.so
%exclude %_libdir/libbe.so
%exclude %_libdir/be.so
%exclude %_libdir/itanium.so
%exclude %_libdir/libxaif*.so

%files docs
%doc Examples doc/* Open64.doc OpenADFortTk/doc/htmlOpenADFortTkPlain

%files -n libxaifBooster
%_libdir/libxaif*.so.*

%files -n libxaifBooster-devel
%_includedir/xaifBooster
%_libdir/libxaif*.so

%files -n libxaifBooster-devel-doc
%doc xaifBooster/doc/*.ps

%changelog
* Tue Apr 03 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20120321-alt1
- Initial build for Sisyphus

