# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%define _pkgdocdir %_docdir/%name-%version

Name: ngspice
Version: 38
Release: alt1
Summary: A mixed level/signal circuit simulator

License: BSD
Group: Engineering
Url: http://ngspice.sourceforge.net

Source: %name-%version.tar
Source1: https://downloads.sourceforge.net/project/ngspice/ng-spice-rework/%version/ngspice-%version-manual.pdf

# Link libspice.so with -lBLT or -lBLIlite, depending on whether in tk mode or
# not (bug 1047056, debian bug 737279)
Patch: ngspice-37-blt-linkage-workaround.patch

BuildRequires: gcc-c++
BuildRequires: libgomp-devel flex glibc-kernheaders-generic
BuildRequires: libXaw-devel
BuildRequires: libXext-devel
BuildRequires: libtinfo-devel
BuildRequires: mot-adms
BuildRequires: libfftw3-devel
BuildRequires: libncurses-devel
BuildRequires: libreadline-devel
Requires: %name-data = %EVR
Requires: lib%name = %EVR

%description
Ngspice is a general-purpose circuit simulator program.
It implements three classes of analysis:
- Nonlinear DC analyses
- Nonlinear Transient analyses
- Linear AC analyses

Ngspice implements the usual circuits elements, like resistors, capacitors,
inductors (single or mutual), transmission lines and a growing number of
semiconductor devices like diodes, bipolar transistors, mosfets (both bulk
and SOI), mesfets, jfet and HFET. Ngspice implements the EKV model but it
cannot be distributed with the package since its license does not allow to
redistribute EKV source code.

Ngspice integrates Xspice, a mixed-mode simulator built upon spice3c1 (and
then some tweak is necessary merge it with spice3f5). Xspice provides a
codemodel interface and an event-driven simulation algorithm. Users can
develop their own models for devices using the codemodel interface.

It can be used for VLSI simulations as well.

%package data
Group: Engineering
Summary: Data files for %name, a circuit simulator
Buildarch: noarch

%description data
Data files for %name, a circuit simulator.

%package -n lib%name
Summary: Main library for %name
Group: System/Libraries

%description -n lib%name
This package contains the library needed to run programs dynamically
linked with %name.

%package devel
Group: Engineering
Summary: Header files for %name, a circuit simulator
Requires: lib%name = %EVR

%description devel
Header files for %name, a circuit simulator.

%prep
%setup
%patch -p2 -b .link

# make sure the examples are UTF-8...
for nonUTF8 in \
    examples/tclspice/tcl-testbench4/selectfromlist.tcl \
    examples/tclspice/tcl-testbench1/testCapa.cir \
    examples/tclspice/tcl-testbench1/capa.cir \
    ChangeLog \
    %nil
do
    %_bindir/iconv -f ISO-8859-1 -t utf-8 $nonUTF8 > $nonUTF8.conv
    mv -f $nonUTF8.conv $nonUTF8
done

%ifarch x86_64 sparc64 ppc64 amd64
%__subst "s|@XSPICEINIT@ codemodel @prefix@/@libname@|@XSPICEINIT@ codemodel %_libdir|" \
    src/spinit.in
%endif

# Fixed minor CVS build
sed -i \
    "s|AM_CPPFLAGS =|AM_CPPFLAGS = -I\$(top_srcdir)/src/maths/ni |" \
    src/spicelib/analysis/Makefile.am

export ACLOCAL_FLAGS=-Im4
./autogen.sh --adms

chmod +x configure

%build
for opt in without-ngshared with-ngshared
do
%configure \
    --disable-silent-rules \
    --$opt \
    --disable-xgraph \
    --enable-adms \
    --enable-xspice \
    --enable-maintainer-mode \
    --enable-dependency-tracking \
    --enable-cider \
    --enable-openmp \
    --enable-predictor \
    --with-readline=yes

make clean
%make_build

# Once install to the temp dir
rm -rf $(pwd)/INST-NGSPICE-${opt}
make INSTALL="install -p" install DESTDIR=$(pwd)/INST-NGSPICE-${opt}

done

%install
mkdir -p %buildroot%prefix
for opt in without-ngshared with-ngshared
do

pushd INST-NGSPICE-${opt}
cp -a * %buildroot
popd

done

# Ensuring that all docs are under %%_pkgdocdir
mkdir -p %buildroot%_pkgdocdir
cp -pr examples/ %buildroot%_pkgdocdir

cp -p %SOURCE1 %buildroot%_pkgdocdir/%name-%version.pdf

cp -a \
    Stuarts_Poly_Notes \
    FAQ \
    DEVICES \
    ANALYSES \
    AUTHORS \
    README* \
    BUGS \
    ChangeLog \
    NEWS \
    COPYING \
    %buildroot%_pkgdocdir

%files
%_bindir/*

%files -n lib%name
%_libdir/*.so.*
%_libdir/%name/

%files data
%_datadir/%name/
%_man1dir/*
%doc %_pkgdocdir

%files devel
%_libdir/*.so
%_includedir/%name
%_pkgconfigdir/%name.pc

%changelog
* Mon Oct 31 2022 Anton Midyukov <antohami@altlinux.org> 38-alt1
- new version 38

* Sun Jul 03 2022 Anton Midyukov <antohami@altlinux.org> 37-alt1
- new version 37

* Thu Dec 23 2021 Anton Midyukov <antohami@altlinux.org> 35-alt1
- new version 35

* Fri Nov 02 2018 Anton Midyukov <antohami@altlinux.org> 29-alt1
- new version 29

* Fri Jul 13 2018 Anton Midyukov <antohami@altlinux.org> 28-alt1
- new version 28

* Thu Jul 12 2018 Anton Midyukov <antohami@altlinux.org> 27-alt2
- build shared library
- fix buildrequires
- enable unpackaged files in buildroot should terminate build

* Thu Nov 02 2017 Anton Midyukov <antohami@altlinux.org> 27-alt1
- Initial build for ALT Sisyphus.
