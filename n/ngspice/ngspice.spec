%define _pkgdocdir %_docdir/%name-%version

Name: ngspice
Version: 27
Release: alt1
Summary: A mixed level/signal circuit simulator

License: BSD
Group: Engineering
Url: http://ngspice.sourceforge.net

Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar
Source1: https://downloads.sourceforge.net/project/ngspice/ng-spice-rework/%version/ngspice-%version-manual.pdf

# Link libspice.so with -lBLT or -lBLIlite, depending on whether in tk mode or
# not (bug 1047056, debian bug 737279)
Patch: ngspice-26-blt-linkage-workaround.patch

# Automatically added by buildreq on Sat Oct 07 2017
# optimized out: glibc-kernheaders-x86 gnu-config libICE-devel libSM-devel libX11-devel libXmu-devel libXt-devel perl python-base python-modules xorg-xproto-devel
BuildRequires: flex glibc-kernheaders-generic libXaw-devel libXext-devel libtinfo-devel mot-adms

Requires: %name-data = %version-%release
    
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

%package devel
Group: Engineering
Summary: Header files for %name, a circuit simulator
Buildarch: noarch
Requires: %name = %version-%release

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
# Adding BLT support
export CFLAGS="%optflags -I%_includedir/blt"

%configure \
    --disable-silent-rules \
    --${opt} \
    --disable-xgraph \
    --enable-adms \
    --enable-xspice \
    --enable-maintainer-mode \
    --enable-dependency-tracking \
    --enable-capzerobypass \
    --enable-cider \
    --enable-newpred \
    --enable-expdevices \
    --enable-intnoise \
    --enable-openmp \
    --enable-predictor \
    --enable-numparam \
    --enable-dot-global \
    --enable-shared \
    --enable-ndev \
    %nil
%make_build

%install
%makeinstall_std

# ADMS support
# It seems that the below is not needed, compiled into binary already
# (mtasaka, 20160628)
cp -pr ./src/spicelib/devices/adms/ %buildroot%_datadir/%name

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

%files data
%_datadir/%name/
%_man1dir/*
%doc %_pkgdocdir

%files devel
%_includedir/%name

%changelog
* Thu Nov 02 2017 Anton Midyukov <antohami@altlinux.org> 27-alt1
- Initial build for ALT Sisyphus.
