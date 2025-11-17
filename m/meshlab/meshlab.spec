%global vcglibver 2025.07
%define glew_version %(rpm -q --queryformat='%%{version}' glew-devel | sed -nr 's/([0-9.]+).*/\\1/p')

Name: meshlab
Version: 2025.07
Release: alt2

Summary: A system for processing and editing unstructured 3D triangular meshes
License: BSD-3-Clause AND GPL-2.0-or-later
Group: Graphics
URL: https://www.meshlab.net
VCS: https://github.com/cnr-isti-vclab/meshlab

Provides: bundled(vcglib) = %vcglibver

# Source0-url: https://github.com/cnr-isti-vclab/meshlab/archive/refs/tags/MeshLab-%version.tar.gz
Source0: %name-%version.tar
# Probably belongs in its own package, but nothing else seems to depend on it.
# Source1-url: https://github.com/cnr-isti-vclab/vcglib/archive/refs/tags/%vcglibver.tar.gz
Source1: vcglib-%vcglibver.tar

Patch1: meshlab-2025.07-MESHLAB_LIB_INSTALL_DIR-fix.patch
# adjust plugin and shader search path
Patch2: 0001-Use-same-paths-for-shader-plugin-lookup-as-used-for-.patch
# https://github.com/cnr-isti-vclab/vcglib/issues/210
Patch3: 0001-Remove-unused-return-value-in-unused-function.patch
Patch4: meshlab-2025.07-system-levmar.patch

Requires: flexiblas-netlib

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake

BuildRequires: libgomp-devel
BuildRequires: bzlib-devel
BuildRequires: pkgconfig(glew)
BuildRequires: pkgconfig(gl)
BuildRequires: pkgconfig(glu)
BuildRequires: pkgconfig(xerces-c)
BuildRequires: pkgconfig(lib3ds)
BuildRequires: levmar-devel
BuildRequires: libgmpxx-devel
BuildRequires: qhull-devel
BuildRequires: %_bindir/qhull
BuildRequires: qt5-base-devel
BuildRequires: pkgconfig(eigen3)
BuildRequires: pkgconfig(Qt5XmlPatterns)
BuildRequires: pkgconfig(Qt5Script)
BuildRequires: qt5-declarative-devel
BuildRequires: qtsoap5-devel
#BuildRequires: libexif-devel
BuildRequires: boost-devel
# disables filter_mesh_booleans plugin on e2k
# because of "incomplete type is not allowed" errors
%ifnarch %e2k
BuildRequires: cgal-devel
%endif
BuildRequires: libmuparser-devel
#BuildRequires: chrpath
#BuildRequires: patchelf
BuildRequires: desktop-file-utils
BuildRequires: ImageMagick-tools

%description
MeshLab is an open source, portable, and extensible system for the
processing and editing of unstructured 3D triangular meshes.  The
system is aimed to help the processing of the typical not-so-small
unstructured models arising in 3D scanning, providing a set of tools
for editing, cleaning, healing, inspecting, rendering and converting
these kinds of meshes.

%prep
%setup -a1
rmdir src/vcglib
mv vcglib-%vcglibver src/vcglib

%autopatch -p1

# unbundle levmar
sed -i 's/^#include "levmar.h"/#include <levmar.h>/' $(find . -name "*.h")

%ifarch %e2k
%define num_threads_fix() \
	sed -i "/num_threads( %1 )/{s/ %1 /nthreads/;s/.*/int nthreads=%1; (void)nthreads;\\n&/}" \\\
	src/meshlabplugins/filter_screened_poisson/%2
%num_threads_fix threads Src/MultiGridOctreeData{,.IsoSurface,.System}.inl
%num_threads_fix Threads.value Src/PoissonRecon.cpp
%num_threads_fix pp.ThreadsVal poisson_utils.h
sed -i "/pragma omp/{s/.*/int loop_count=mesh.vert.size();\n&/;:a;n;s/i < (int)mesh.vert.size()/i < loop_count/;ba}" \
	src/vcglib/vcg/complex/algorithms/point_outlier.h
%endif

# Remove bundled library sources, since we use the packaged libraries
rm -r src/external/glew*/*

# Change defaults for MESHLAB_ALLOW_DOWNLOAD_*
sed -i '/option/ s|\(MESHLAB_ALLOW_DOWNLOAD.*\) ON|\1 OFF|' src/external/*.cmake
grep -E 'option.*MESHLAB_ALLOW_DOWNLOAD.*' src/external/*.cmake

# set plugin and shader search path
sed -i 's|PLUGIN_DIR|QString("%{_libdir}/meshlab/plugins")|g'  src/common/globals.cpp
sed -i 's|SHADER_DIR|QString("%{_datadir}/meshlab/shaders")|g' src/common/globals.cpp

%build
%add_optflags -fopenmp -DSYSTEM_QHULL -I%_includedir/libqhull

%cmake \
	-DGLEW_VERSION=%glew_version \
	%nil
%cmake_build

%install
%cmake_install

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
* Mon Nov 17 2025 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 2025.07-alt2
- e2k build fix

* Thu Oct 30 2025 Anton Midyukov <antohami@altlinux.org> 2025.07-alt1
- New version 2025.07.
- Update License tag.

* Tue Oct 21 2025 Anton Midyukov <antohami@altlinux.org> 2021.10-alt4
- fix BR for build with eigen 5.0.

* Fri Nov 01 2024 Anton Midyukov <antohami@altlinux.org> 2021.10-alt3
- rebuild without mpir-devel

* Sat Jun 24 2023 Anton Midyukov <antohami@altlinux.org> 2021.10-alt2
- fix build with gcc13
-  add 'Requires: flexiblas-netlib'

* Wed May 04 2022 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 2021.10-alt1.1
- fixed build for Elbrus

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

