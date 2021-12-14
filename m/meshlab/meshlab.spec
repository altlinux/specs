%global vcglibver 2021.10

Name: meshlab
Version: 2021.10
Release: alt1

Summary: A system for processing and editing unstructured 3D triangular meshes
License: GPLv2+ and BSD and Public Domain
Group: Graphics
Url: https://github.com/cnr-isti-vclab/meshlab

Provides: bundled(vcglib) = %vcglibver

ExcludeArch: armh

# Source0-url: https://github.com/cnr-isti-vclab/meshlab/archive/refs/tags/Meshlab-%version.tar.gz
Source0: %name-%version.tar
# Probably belongs in its own package, but nothing else seems to depend on it.
# Source1-url: https://github.com/cnr-isti-vclab/vcglib/archive/refs/tags/%vcglibver.tar.gz
Source1: vcglib-%vcglibver.tar

Patch0: meshlab-2021.07-MESHLAB_LIB_INSTALL_DIR-fix.patch
Patch1: meshlab-2021.07-system-levmar.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake

BuildRequires: libgomp-devel
BuildRequires: bzlib-devel
BuildRequires: pkgconfig(glew)
BuildRequires: levmar-devel
BuildRequires: lib3ds-devel
BuildRequires: libgmpxx-devel
BuildRequires: libxerces-c-devel
BuildRequires: qhull-devel qhull
BuildRequires: qt5-base-devel
BuildRequires: eigen3
BuildRequires: pkgconfig(Qt5XmlPatterns)
BuildRequires: pkgconfig(Qt5Script)
BuildRequires: qt5-declarative-devel
BuildRequires: qtsoap5-devel
#BuildRequires: libexif-devel
BuildRequires: boost-devel
BuildRequires: cgal-devel
BuildRequires: libmuparser-devel
#BuildRequires: chrpath
#BuildRequires: patchelf
BuildRequires: desktop-file-utils
BuildRequires: ImageMagick-tools
%ifnarch ppc64le
# mpir has ppc64le excluded
BuildRequires: mpir-devel
%endif

%description
MeshLab is an open source, portable, and extensible system for the
processing and editing of unstructured 3D triangular meshes.  The
system is aimed to help the processing of the typical not-so-small
unstructured models arising in 3D scanning, providing a set of tools
for editing, cleaning, healing, inspecting, rendering and converting
these kinds of meshes.

%prep
%setup -a1
%patch0 -p1 -b .MESHLAB_LIB_INSTALL_DIR-fix
%patch1 -p1 -b .system-levmar
%ifarch %e2k
%define num_threads_fix() \
	sed -i "/num_threads( %1 )/{s/ %1 /nthreads/;s/.*/int nthreads=%1; (void)nthreads;\\n&/}" \\\
	src/meshlabplugins/filter_screened_poisson/%2
%num_threads_fix threads Src/MultiGridOctreeData{,.IsoSurface,.System}.inl
%num_threads_fix Threads.value Src/PoissonRecon.cpp
%num_threads_fix pp.ThreadsVal poisson_utils.h
sed -i "/pragma omp/{s/.*/int loop_count=mesh.vert.size();\n&/;:a;n;s/i < (int)mesh.vert.size()/i < loop_count/;ba}" \
	vcglib-%vcglibver/vcg/complex/algorithms/point_outlier.h
%endif

rmdir src/vcglib
mv vcglib-%vcglibver src/vcglib

# plugin path
sed -i -e 's|"lib"|"%{_lib}"|g' src/common/globals.cpp

%build
%add_optflags -fopenmp -DSYSTEM_QHULL -I/usr/include/libqhull

%cmake src \
	-DCMAKE_SKIP_RPATH=ON \
	-DCMAKE_VERBOSE_MAKEFILE=OFF \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
	-DALLOW_BUNDLED_EIGEN=OFF \
	-DALLOW_BUNDLED_GLEW=OFF \
	-DALLOW_BUNDLED_LEVMAR=OFF \
	-DALLOW_BUNDLED_LIB3DS=OFF \
	-DALLOW_BUNDLED_MUPARSER=OFF \
	-DALLOW_BUNDLED_NEWUOA=ON \
	-DALLOW_BUNDLED_OPENCTM=ON \
	-DALLOW_BUNDLED_QHULL=OFF \
	-DALLOW_BUNDLED_SSYNTH=ON \
	-DALLOW_BUNDLED_XERCES=OFF \
	-DALLOW_SYSTEM_EIGEN=ON \
	-DALLOW_SYSTEM_GLEW=ON \
	-DALLOW_SYSTEM_GMP=ON \
	-DALLOW_SYSTEM_LIB3DS=ON \
	-DALLOW_SYSTEM_MUPARSER=ON \
	-DALLOW_SYSTEM_OPENCTM=ON \
	-DALLOW_SYSTEM_QHULL=ON \
	-DALLOW_SYSTEM_XERCES=ON \
	-DEigen3_DIR=usr/include/eigen3 \
	-DGlew_DIR=/usr/include/GL \
	-DQhull_DIR=/usr/include/libqhull

%cmake_build

%install
%cmakeinstall_std

# create desktop file
cat <<EOF >%buildroot%_desktopdir/meshlab.desktop
[Desktop Entry]
Name=MeshLab
GenericName=MeshLab 3D triangular mesh processing and editing
Exec=env QT_QPA_PLATFORM=xcb meshlab
Icon=meshlab
Terminal=false
Type=Application
Categories=Graphics;
EOF

desktop-file-validate %buildroot%_desktopdir/meshlab.desktop

# convert icon
for x in 16 32 48; do
	mkdir -p %buildroot%_iconsdir/hicolor/$x'x'$x/apps/
	  convert %buildroot%_iconsdir/hicolor/512x512/apps/%name.png \
	  -resize $x'x'$x %buildroot/%_iconsdir/hicolor/$x'x'$x/apps/%name.png
done

%files
%doc README.md
%doc docs/readme.txt
%doc docs/privacy.txt
%_bindir/%name
%_libdir/*.so
%_libdir/%name
%_datadir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/%name.png

%changelog
* Mon Dec 13 2021 Anton Midyukov <antohami@altlinux.org> 2021.10-alt1
- new version (2021.10) with rpmgs script

* Fri Oct 22 2021 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 2021.07-alt2
- e2k: fixed OpenMP issues

* Thu Sep 30 2021 Anton Midyukov <antohami@altlinux.org> 2021.07-alt1
- new version (2021.07) with rpmgs script

* Sun Jan 10 2021 Anton Midyukov <antohami@altlinux.org> 2020.12-alt1
- 2020.12

* Wed Sep 30 2020 Sergey V Turchin <zerg@altlinux.org> 2016.12-alt8
- fix to build with Qt-5.15
- don't build on armh

* Wed Oct 16 2019 Michael Shigorin <mike@altlinux.org> 2016.12-alt6
- E2K: ftbfs workaround (partially disable OpenMP)

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 2016.12-alt5
- NMU: remove rpm-build-ubt from BR:

* Thu Feb 14 2019 Andrey Bychkov <mrdrew@altlinux.org> 2016.12-alt4
- no return statement in the non-void function fixed (according g++8)

* Tue Sep 25 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2016.12-alt3%ubt
- NMU: fixed build with Qt-5.11.

* Sat Jun 16 2018 Anton Midyukov <antohami@altlinux.org> 2016.12-alt2%ubt
- Rebuilt for aarch64

* Fri Jan 05 2018 Anton Midyukov <antohami@altlinux.org> 2016.12-alt1%ubt
- New version 2016.12

* Wed Jul 05 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.3.3-alt2.2
- Updated build with gcc-6

* Tue Jan 19 2016 Andrey Cherepanov <cas@altlinux.org> 1.3.3-alt2.1
- rebuild with new version of libmuparser

* Fri May 16 2014 Dmitry Derjavin <dd@altlinux.org> 1.3.3-alt2
- i586 build fixed.

* Thu May 15 2014 Dmitry Derjavin <dd@altlinux.org> 1.3.3-alt1
- 1.3.3;
- patches revised.

* Thu Apr 10 2014 Igor Vlasenko <viy@altlinux.ru> 1.3.2-alt1_1
- converted for ALT Linux by srpmconvert tools

