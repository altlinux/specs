%define        _unpackaged_files_terminate_build 1

Name:          micmac
Version:       1.1.1
Release:       alt1
Summary:       MicMac is a free open-source photogrammetric suite
License:       Cecill-B
Group:         Graphics
Url:           https://micmac.ensg.eu/
Vcs:           https://github.com/micmacIGN/micmac.git
Source:        %name-%version.tar
Patch:         %name-%version-%release.patch
ExcludeArch:   %arm

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: git
BuildRequires: doxygen
BuildRequires: libgomp-devel
BuildRequires: xorg-proto-devel
BuildRequires: libX11-devel
BuildRequires: libGLU-devel
BuildRequires: libglvnd-devel
BuildRequires: libImageMagick-devel
BuildRequires: boost-devel
BuildRequires: boost-filesystem-devel
BuildRequires: libqt4-devel
BuildRequires: libgraphviz-devel
BuildRequires: pkgconfig(tinyxml)
BuildRequires: pkgconfig(qpbo)
BuildRequires: pkgconfig(Qt5Widgets)

%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}

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


#%package       libelise
#Group:         Graphics
#Summary:       libElise library to use with Micmac suite
#
#%description   libelise
#libElise library to use with Micmac suite.
#
%package       libelise-devel-static
Group:         Development/C++
Summary:       libElise library to use with Micmac suite development files

%description   libelise-devel-static
libElise library to use with Micmac suite development files.


#%package       libann
#Group:         Graphics
#Summary:       libANN library to use with Micmac suite
#
#%description   libann
#libANN library to use with Micmac suite.
#
%package       libann-devel-static
Group:         Development/C++
Summary:       libANN library to use with Micmac suite development files

%description   libann-devel-static
libANN library to use with Micmac suite development files.


%prep
%setup
%autopatch -p1

%build
%cmake_insource \
   -DBUILD_PATH_LIB=%_libdir \
   -DBUILD_PATH_BIN=%_bindir \
   -DBIN_AUX_FULL_PATH=%_bindir \
   -DWERROR=OFF \
   -DWITH_QPBO=ON \
   -DWITH_INTERFACE=OFF \
   -DWITH_KAKADU=OFF \
   -DWITH_IGN_ORI=OFF \
   -DWITH_HEADER_PRECOMP=ON \
   -DWITH_RNX2RTKP=ON \
   -DWITH_OPENCL=ON \
   -DWITH_OPEN_MP=ON \
   -DWITH_QT5=ON \
   -DWITH_GRAPHVIZ=OFF \
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

#%files         libelise
#%doc *.md COPYING
#%_libdir/libelise*.so*
#
%files         libelise-devel-static
%doc *.md COPYING
%_libdir/libelise*.a

#%files         libann
#%doc *.md COPYING
#%_libdir/libANN*.so.*
#
%files         libann-devel-static
%doc *.md COPYING
%_libdir/libANN*.a


%changelog
* Sun Feb 11 2024 Pavel Skrylev <majioa@altlinux.org> 1.1.1-alt1
- initial build v1.1.1 for Sisyphus
