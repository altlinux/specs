%define mpiimpl openmpi
%define mpidir %_libexecdir/%mpiimpl

Name: openfoam
Version: 1.7.1
Release: alt0.7
Summary: Free, open source computational fluid dynamics (CFD) software
License: GPL v3 or later
Group: Sciences/Physics
Url: http://www.openfoam.com/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: OpenFOAM-%version.tar.gz
Source1: ThirdParty-%version.tar.gz
Source2: %name.sh

BuildPreReq: cmake gcc-c++ libparmetis0-devel libscotch-devel
BuildPreReq: %mpiimpl-devel qt4-devel flex libmpc-devel paraview-devel
BuildPreReq: texinfo libreadline-devel libgmp-devel libiberty-devel
BuildPreReq: libmpfr-devel zlib-devel libbfd-devel libcgal-devel
BuildPreReq: libncurses-devel libvtk-devel
BuildPreReq: doxygen graphviz chrpath

Requires: lib%name = %version-%release

%description
OpenFOAM is a free, open source computational fluid dynamics (CFD)
software package produced by a commercial company, OpenCFD Ltd. It has a
large user base across most areas of engineering and science, from both
commercial and academic organisations. OpenFOAM has an extensive range
of features to solve anything from complex fluid flows involving
chemical reactions, turbulence and heat transfer, to solid dynamics and
electromagnetics.

NOTE: executable file 'R' renamed to 'foamR' for avoid conflict with
R-base.

Before first run after install You must relogon or run this command:
. /etc/profile.d/%name.sh

%package -n lib%name
Summary: Shared libraries of OpenFOAM
Group: System/Libraries

%description -n lib%name
OpenFOAM is a free, open source computational fluid dynamics (CFD)
software package produced by a commercial company, OpenCFD Ltd. It has a
large user base across most areas of engineering and science, from both
commercial and academic organisations. OpenFOAM has an extensive range
of features to solve anything from complex fluid flows involving
chemical reactions, turbulence and heat transfer, to solid dynamics and
electromagnetics.

This package contains shared libraries of OpenFOAM.

%package docs
Summary: Documentation for OpenFOAM
Group: Documentation
BuildArch: noarch

%description docs
OpenFOAM is a free, open source computational fluid dynamics (CFD)
software package produced by a commercial company, OpenCFD Ltd. It has a
large user base across most areas of engineering and science, from both
commercial and academic organisations. OpenFOAM has an extensive range
of features to solve anything from complex fluid flows involving
chemical reactions, turbulence and heat transfer, to solid dynamics and
electromagnetics.

This package contains documentation for OpenFOAM.

%package tutorials
Summary: Tutorials for OpenFOAM
Group: Development/Documentation
BuildArch: noarch

%description tutorials
OpenFOAM is a free, open source computational fluid dynamics (CFD)
software package produced by a commercial company, OpenCFD Ltd. It has a
large user base across most areas of engineering and science, from both
commercial and academic organisations. OpenFOAM has an extensive range
of features to solve anything from complex fluid flows involving
chemical reactions, turbulence and heat transfer, to solid dynamics and
electromagnetics.

This package contains tutorials for OpenFOAM.

%prep
%setup
sed -i 's|@VERSION@|%version|' etc/bashrc
sed -i 's|@BUILDROOT@|%buildroot|' etc/bashrc wmake/Makefile
sed -i "s|@TOPDIR@|$PWD|" etc/bashrc

for i in $(egrep -R '\-O3' wmake/ |awk -F : '{print $1}')
do
	sed -i 's|\-O3|-O2 -g|g' $i
done

tar -xf %SOURCE1
pushd ThirdParty
rm -fR ParMetis* metis* openmpi* paraview* scotch*
popd

install -p -m644 %SOURCE2 .
sed -i 's|@VERSION@|%version|' %name.sh
%ifarch x86_64
sed -i 's|@BITS@|64|' %name.sh
%else
sed -i 's|@BITS@|32|' %name.sh
%endif

%build
mpi-selector --set %mpiimpl
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-Rpath=%mpidir/lib -L%mpidir/lib"

export FOAM_INST_DIR=$PWD
. etc/bashrc
bin/foamSystemCheck
export PATH=$PATH:$PWD/wmake
export WM_NCOMPPROCS=2
# need 2 phases for complete linking of libraries
./Allwmake
./Allwmake

%make_build -C ThirdParty/ParMGridGen-1.0

#pushd applications/utilities/postProcessing/graphics/PV3FoamReader
#./Allwmake
#pushd PV3FoamReader/PV3FoamReader
#mkdir -p Make/$WM_OPTIONS
#pushd Make/$WM_OPTIONS
#INCS="-I%_includedir/paraview-3.8 $(pkg-config --cflags QtGui)"
#cmake \
#	-DCMAKE_VERBOSE_MAKEFILE:BOOL=TRUE \
#	-DParaView_DIR:PATH=%mpidir/lib/CMake \
#	-DCMAKE_CXX_FLAGS:STRING="$INCS" \
#	-DCMAKE_C_FLAGS:STRING="$INCS" \
#	../..
#sed -i \
#	"s|\t\(.*src/OpenFOAM.*\)|\t g++ $INCS \1|" \
#	CMakeFiles/PV3FoamReader_SM.dir/build.make
#sed -i \
#	"s|\t-I%_includedir/paraview-3.8\(.*\)|\t g++ $INCS \1|" \
#	CMakeFiles/PV3FoamReader_SM.dir/build.make
#sed -i \
#	"s|\(\-name\)|rcc \1|" \
#	CMakeFiles/PV3FoamReader_SM.dir/build.make
#make
#popd
#popd
#popd

%install
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-Rpath=%mpidir/lib -L%mpidir/lib"

install -d %buildroot%_bindir
install -m755 applications/bin/*/* \
	ThirdParty/ParMGridGen-1.0/mgridgen \
	%buildroot%_bindir
mv %buildroot%_bindir/R %buildroot%_bindir/foamR

install -d %buildroot%_libdir
install -m644 lib/*/*.so %buildroot%_libdir
install -m644 lib/*/openmpi-system/*.so %buildroot%_libdir

for i in %buildroot%_libdir/*.so %buildroot%_bindir/*
do
	chrpath -r %mpidir/lib $i ||:
done

install -d %buildroot%_sysconfdir/profile.d
install -p -m644 etc/controlDict %buildroot%_sysconfdir
install -p -m644 etc/cellModels %buildroot%_sysconfdir
install -p -m755 %name.sh %buildroot%_sysconfdir/profile.d

# It is the file in the package whose name matches the format emacs or vim uses 
# for backup and autosave files. It may have been installed by  accident.
find $RPM_BUILD_ROOT \( -name '.*.swp' -o -name '#*#' -o -name '*~' \) -print -delete
# failsafe cleanup if the file is declared as %%doc
find . \( -name '.*.swp' -o -name '#*#' -o -name '*~' \) -print -delete

rm -f %buildroot%_libdir/libvtkPV3Foam.so

%files
%doc COPYING README.html ReleaseNotes*
%_bindir/*
%_sysconfdir/controlDict
%_sysconfdir/cellModels
%_sysconfdir/profile.d/*

%files -n lib%name
%_libdir/*.so

%files docs
%doc doc/Guides-a4/* doc/changes/* doc/*.pdf

%files tutorials
%doc tutorials/*

# TODO:
# - devel package?
# - PV3FoamReader

%changelog
* Sat Jun 02 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.1-alt0.7
- Rebuilt with VTK 5.10.0

* Fri Sep 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.1-alt0.6
- Rebuilt with VTK 5.8.0

* Thu Sep 15 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.1-alt0.5
- Rebuilt with libparmetis0 instead of libparmetis

* Thu Mar 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.1-alt0.4
- Rebuilt for debuginfo

* Sat Feb 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.1-alt0.3
- Rebuilt with parmetis 3.1.1-alt10

* Mon Dec 13 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.1-alt0.2
- Added config files

* Fri Dec 10 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.1-alt0.1
- Initial build for Sisyphus (collaboration with const@)

