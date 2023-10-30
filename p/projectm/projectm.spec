%define oname	projectM

%define major 4
%define sover %major
Name: projectm
Version: 4.0.0
Release: alt1

%define libprojectm libprojectm%{major}_%{sover}
%define libprojectm_playlist libprojectm%{major}-playlist_%{sover}

Group: System/Libraries
Summary: Awesome music visualizer
License: LGPL-2.1-or-later
Url: http://projectm.sourceforge.net/

Source: %name-%version.tar

# Automatically added by buildreq on Mon Oct 30 2023 (-bi)
# optimized out: cmake-modules debugedit elfutils glibc-kernheaders-generic glibc-kernheaders-x86 libX11-devel libctf-nobfd0 libglvnd-devel libgpg-error libp11-kit libsasl2-3 libstdc++-devel python-modules python2-base python3 python3-base python3-dev python3-module-paste rpm-build-file rpm-build-python3 sh5 tzdata xorg-proto-devel
#BuildRequires: cmake gcc-c++ git-core libGLU-devel libgomp-devel libprojectM-devel libssl-devel python3-module-setuptools python3-module-zope tbb-devel
BuildRequires: cmake gcc-c++ libGLU-devel libgomp-devel libssl-devel

%description
projectM is a reimplementation of Milkdrop under OpenGL. It is an
awesome music visualizer. There is nothing better in the world of
Unix.

%package -n %libprojectm
Summary: Awesome music visualizer library
Group: System/Libraries
%description -n %libprojectm
projectM is a reimplementation of Milkdrop under OpenGL. It is an
awesome music visualizer. There is nothing better in the world of
Unix.

%package -n %libprojectm_playlist
Summary: Awesome music visualizer library
Group: System/Libraries
%description -n %libprojectm_playlist
projectM is a reimplementation of Milkdrop under OpenGL. It is an
awesome music visualizer. There is nothing better in the world of
Unix.

%package devel
Summary: Header files for projectM library
Group: Development/C
Requires: %libprojectm
%description devel
Header files for projectM library.

%package static
Summary: Static projectM library
Group: Development/Libraries
Requires: %name-devel
%description static
Static projectM library.

%prep
%setup
%ifarch %e2k
# This line from "libvisual.h" is poisonous to some system headers:
# "#define inline  inline __attribute__ ((always_inline))"
#sed -i '/<libvisual\/libvisual\.h>/i #include <sstream>' \
#	src/projectM-libvisual/actor_projectM.cpp
%endif

%build
%cmake \
	-G "Unix Makefiles" \
	-DBUILD_SHARED_LIBS:BOOL=TRUE \
	-DBUILD_TESTING:BOOL=FALSE \
	-DENABLE_CXX_INTERFACE:BOOL=TRUE \
	-DINCLUDE-PROJECTM-PULSEAUDIO:BOOL=TRUE \
	-DINCLUDE-PROJECTM-JACK:BOOL=TRUE \
	#
%cmake_build

%install
%cmakeinstall_std

%files -n %libprojectm
%doc AUTHORS.txt
%_libdir/libprojectM-%{major}.so.%{sover}
%_libdir/libprojectM-%{major}.so.*

%files -n %libprojectm_playlist
%doc AUTHORS.txt
%_libdir/libprojectM-%{major}-playlist.so.%{sover}
%_libdir/libprojectM-%{major}-playlist.so.*

%files devel
%doc AUTHORS.txt README.md
%_includedir/projectM-%{major}/
%_libdir/lib*.so
%_libdir/cmake/projectM%{major}*/

%changelog
* Fri Oct 27 2023 Sergey V Turchin <zerg@altlinux.org> 4.0.0-alt1
- initial build
