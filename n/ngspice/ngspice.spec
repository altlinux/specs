# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%define _pkgdocdir %_docdir/%name-%version
%define majver 44
%define sover 0

Name: ngspice
Version: 44
Release: alt1
Summary: A mixed level/signal circuit simulator

License: BSD
Group: Engineering
Url: http://ngspice.sourceforge.net
Vcs: https://git.code.sf.net/p/ngspice/ngspice

Source: %name-%version.tar
Source1: https://downloads.sourceforge.net/project/ngspice/ng-spice-rework/%majver/ngspice-%majver-manual.pdf
Patch: %name-%version-%release.patch

# Link libspice.so with -lBLT or -lBLIlite, depending on whether in tk mode or
# not (bug 1047056, debian bug 737279)
Patch1: ngspice-37-blt-linkage-workaround.patch

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
Requires: lib%name%sover = %EVR

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
Requires: %name = %EVR

%description data
Data files for %name, a circuit simulator.

%package -n lib%name%sover
Summary: Main library for %name
Group: System/Libraries
Obsoletes: lib%name < %EVR

%description -n lib%name%sover
This package contains the library needed to run programs dynamically
linked with %name.

%package devel
Group: Engineering
Summary: Header files for %name, a circuit simulator
Requires: lib%name%sover = %EVR

%description devel
Header files for %name, a circuit simulator.

%prep
%setup
%patch -p1
%patch1 -p2 -b .link

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

%ifarch x86_64
%__subst "s|@XSPICEINIT@ codemodel @prefix@/@libname@|@XSPICEINIT@ codemodel %_libdir|" \
    src/spinit.in
%endif

# Fixed minor CVS build
sed -i \
    "s|AM_CPPFLAGS =|AM_CPPFLAGS = -I\$(top_srcdir)/src/maths/ni |" \
    src/spicelib/analysis/Makefile.am

#export ACLOCAL_FLAGS=-Im4
#./autogen.sh --adms

#chmod +x configure

%build
%autoreconf

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

%make clean
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
%_libdir/ngspice/

%files -n lib%name%sover
%_libdir/libngspice.so.%sover
%_libdir/libngspice.so.%sover.*

%files data
%_datadir/ngspice/
%_man1dir/ngspice.1.*
%doc %_pkgdocdir

%files devel
%_libdir/libngspice.so
%_includedir/ngspice
%_pkgconfigdir/ngspice.pc

%changelog
* Tue Jan 07 2025 Anton Midyukov <antohami@altlinux.org> 44-alt1
- New version 44.
- Add Vcs
- Fix pack library
- Add depenedency on ngspice for ngspice-data 

* Mon Jan 29 2024 Anton Midyukov <antohami@altlinux.org> 41-alt1
- new version 41

* Mon Jan 29 2024 Anton Midyukov <antohami@altlinux.org> 40-alt1
- new version 40

* Sun Feb 05 2023 Anton Midyukov <antohami@altlinux.org> 39.3-alt1
- new version  39.3

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
