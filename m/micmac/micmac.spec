%define        _unpackaged_files_terminate_build 1

%ifarch        loongarch64 riscv64
# workaround for:
#  error: cpio archive too big - 6558M
%define        optflags_debug -g1
%endif

Name:          micmac
Version:       1.1.1
Release:       alt2.1
Summary:       MicMac is a free open-source photogrammetric suite
License:       CECILL-B
Group:         Graphics
Url:           https://micmac.ensg.eu/
Vcs:           https://github.com/micmacIGN/micmac.git
Source:        %name-%version.tar
ExcludeArch:   %arm

BuildRequires(pre): rpm-macros-cmake
BuildRequires: /proc
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: git
BuildRequires: doxygen
BuildRequires: ImageMagick
BuildRequires: libgomp-devel
BuildRequires: libann-devel
BuildRequires: boost-devel
BuildRequires: boost-filesystem-devel
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(glu)
BuildRequires: pkgconfig(xproto)
BuildRequires: pkgconfig(libglvnd)
BuildRequires: pkgconfig(libcgraph)
BuildRequires: pkgconfig(ImageMagick)
BuildRequires: pkgconfig(tinyxml)
BuildRequires: pkgconfig(qpbo)
BuildRequires: pkgconfig(Qt5Widgets)

%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
%add_optflags -std=gnu17 -Wno-template-body

%description
MicMac is a free open-source (Cecill-B licence) photogrammetric suite that can
be used in a variety of 3D reconstruction scenarios. In aims mainly at
professionnal or academic users but constant efforts are made to make it more
accessible to the general public.

One of MicMac strengths is its high degree of versatility. It can indeed be
used in various fields : cartography, environment, industry, forestry, heritage,
archaeology,...

MicMac allows both the creation of 3D models and of ortho-imagery when
appropriate.

The software is suitable to every type of objects of any scale : from small
object or statues with acquisition from the ground, to church, castle through
drone acquisitions, to buildings, cities or natural areas through aerial or
satellite acquisitions. The tools also allow for the georeferencing of the end
products in local/global/absolute coordinates system. Some complementary tools
opens the fields of metrology and site surveying.


%package       -n qt5-micmac
Group:         System/Libraries
Summary:       MicMac for QT is a free open-source photogrammetric suite

%description   -n qt5-micmac
MicMac is a free open-source (Cecill-B licence) photogrammetric suite that can
be used in a variety of 3D reconstruction scenarios. In aims mainly at
professionnal or academic users but constant efforts are made to make it more
accessible to the general public.

One of MicMac strengths is its high degree of versatility. It can indeed be
used in various fields : cartography, environment, industry, forestry, heritage,
archaeology,...

MicMac allows both the creation of 3D models and of ortho-imagery when
appropriate.

The software is suitable to every type of objects of any scale : from small
object or statues with acquisition from the ground, to church, castle through
drone acquisitions, to buildings, cities or natural areas through aerial or
satellite acquisitions. The tools also allow for the georeferencing of the end
products in local/global/absolute coordinates system. Some complementary tools
opens the fields of metrology and site surveying.


%package       -n libelise
Group:         System/Libraries
Summary:       Elise library is a free open-source photogrammetric suite

%description   -n libelise
MicMac is a free open-source (Cecill-B licence) photogrammetric suite that can
be used in a variety of 3D reconstruction scenarios. In aims mainly at
professionnal or academic users but constant efforts are made to make it more
accessible to the general public.

One of MicMac strengths is its high degree of versatility. It can indeed be
used in various fields : cartography, environment, industry, forestry, heritage,
archaeology,...

MicMac allows both the creation of 3D models and of ortho-imagery when
appropriate.

The software is suitable to every type of objects of any scale : from small
object or statues with acquisition from the ground, to church, castle through
drone acquisitions, to buildings, cities or natural areas through aerial or
satellite acquisitions. The tools also allow for the georeferencing of the end
products in local/global/absolute coordinates system. Some complementary tools
opens the fields of metrology and site surveying.


%package       -n libelise-devel
Group:         Development/C
Summary:       a free open-source photogrammetric suite elise devel package

%description   -n libelise-devel
MicMac is a free open-source (Cecill-B licence) photogrammetric suite that can
be used in a variety of 3D reconstruction scenarios. In aims mainly at
professionnal or academic users but constant efforts are made to make it more
accessible to the general public.

One of MicMac strengths is its high degree of versatility. It can indeed be
used in various fields : cartography, environment, industry, forestry, heritage,
archaeology,...

MicMac allows both the creation of 3D models and of ortho-imagery when
appropriate.

The software is suitable to every type of objects of any scale : from small
object or statues with acquisition from the ground, to church, castle through
drone acquisitions, to buildings, cities or natural areas through aerial or
satellite acquisitions. The tools also allow for the georeferencing of the end
products in local/global/absolute coordinates system. Some complementary tools
opens the fields of metrology and site surveying.


%package       -n micmac-devel
Group:         Development/C
Summary:       a free open-source photogrammetric suite micmac devel package

Requires:      %name = %EVR
Requires:      libelise-devel = %EVR
Requires:      cmake
Requires:      gcc-c++
Requires:      git
Requires:      doxygen
Requires:      ImageMagick
Requires:      libgomp-devel
Requires:      libann-devel
Requires:      boost-devel
Requires:      boost-filesystem-devel
Requires:      pkgconfig(x11)
Requires:      pkgconfig(glu)
Requires:      pkgconfig(xproto)
Requires:      pkgconfig(libglvnd)
Requires:      pkgconfig(libcgraph)
Requires:      pkgconfig(ImageMagick)
Requires:      pkgconfig(tinyxml)
Requires:      pkgconfig(qpbo)
Requires:      pkgconfig(Qt5Widgets)

%description   -n micmac-devel
MicMac is a free open-source (Cecill-B licence) photogrammetric suite that can
be used in a variety of 3D reconstruction scenarios. In aims mainly at
professionnal or academic users but constant efforts are made to make it more
accessible to the general public.

One of MicMac strengths is its high degree of versatility. It can indeed be
used in various fields : cartography, environment, industry, forestry, heritage,
archaeology,...

MicMac allows both the creation of 3D models and of ortho-imagery when
appropriate.

The software is suitable to every type of objects of any scale : from small
object or statues with acquisition from the ground, to church, castle through
drone acquisitions, to buildings, cities or natural areas through aerial or
satellite acquisitions. The tools also allow for the georeferencing of the end
products in local/global/absolute coordinates system. Some complementary tools
opens the fields of metrology and site surveying.


%prep
%setup

%build
%cmake \
   -DARCH:STRING=%_arch \
   -DBUILD_SHARED_LIBS=ON \
   -DCMAKE_BUILD_TYPE=RelWithDebInfo \
   -DBUILD_PATH_LIB=%_libdir \
   -DBUILD_PATH_BIN=%_bindir \
   -DBIN_AUX_FULL_PATH=%_bindir \
   -DWERROR=OFF \
   -DBUILD_POISSON=OFF \
   -DWITH_QPBO=ON \
   -DWITH_INTERFACE=OFF \
   -DWITH_KAKADU=OFF \
   -DWITH_IGN_ORI=OFF \
   -DWITH_HEADER_PRECOMP=ON \
   -DWITH_RNX2RTKP=ON \
   -DWITH_OPENCL=ON \
   -DWITH_OPEN_MP=ON \
   -DWITH_QT5=ON \
   -DWITH_GRAPHVIZ=ON \
   -DWITH_GIMMI=OFF \
   -DBUILD_BENCH=OFF \
   -DWITH_DOXYGEN=OFF \
   -DWITH_CCACHE=ON \
   -DDEPLOY=ON \
   -DUPDATE_TRANSLATIONS=OFF \
   -DBoost_USE_STATIC_LIBS=OFF \
   -DBoost_NO_SYSTEM_PATHS=OFF

%cmake_build

%install
%cmakeinstall_std
%find_lang %name

%files         -f %name.lang
%doc *.md COPYING
%_bindir/*
%exclude %_bindir/SaisieQT

%files         -n qt5-micmac -f %name.lang
%doc *.md COPYING
%_bindir/SaisieQT

%files         -n libelise
%doc *.md COPYING
%_libdir/libelise.so.*

%files         -n libelise-devel
%doc *.md COPYING
%_libdir/cmake/MICMAC
%_libdir/libelise.so

%files         -n micmac-devel


%changelog
* Sun May 03 2026 Pavel Skrylev <majioa@altlinux.org> 1.1.1-alt2.1
- !FTBFS fixed compilation for gcc15

* Wed May 07 2025 Pavel Skrylev <majioa@altlinux.org> 1.1.1-alt2
- + libelise package with shared lib for the main package
- ! fixed FTBFS, along with many internal errors

* Wed Feb 26 2025 Ivan A. Melnikov <iv@altlinux.org> 1.1.1-alt1.1
- NMU: fix build on loongarch64 and riscv64 by reducing
  debug level (with -g2 debuginfo does not fit into 4Gb limit).

* Sun Feb 11 2024 Pavel Skrylev <majioa@altlinux.org> 1.1.1-alt1
- initial build v1.1.1 for Sisyphus
