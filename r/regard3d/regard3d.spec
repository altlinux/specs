%define        _unpackaged_files_terminate_build 1
%define        _stripped_files_terminate_build 1

Name:          regard3d
Version:       1.0.0
Release:       alt2
Summary:       A open source structure-from-motion program based on OpenMVG
License:       MIT
Group:         Graphics
Url:           http://www.regard3d.org/
Vcs:           https://github.com/rhiestan/Regard3D.git

Source:        %name-%version.tar
Patch:         %name-%version-%release.patch
BuildRequires(pre): rpm-macros-cmake
BuildRequires: /proc
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(eigen3-compat)
BuildRequires: pkgconfig(assimp)
BuildRequires: pkgconfig(lapack)
BuildRequires: pkgconfig(openblas)
BuildRequires: pkgconfig(opencv4)
BuildRequires: pkgconfig(libglvnd)
BuildRequires: libwxGTK3.2-devel
BuildRequires: libOpenSceneGraph-devel
BuildRequires: libglvnd-devel
BuildRequires: tbb-devel
BuildRequires: boost-devel >= 1.53.0
BuildRequires: boost-filesystem-devel
BuildRequires: boost-locale-devel
BuildRequires: boost-geometry-devel
BuildRequires: libjasper-devel
BuildRequires: libwebp-devel
BuildRequires: ceres-solver-devel
BuildRequires: libglog-devel
BuildRequires: libsuitesparse-devel
BuildRequires: libmetis-devel
BuildRequires: libvlfeat-devel
BuildRequires: libopenmvg-devel
BuildRequires: libnlopt-devel
BuildRequires: libkgraph-devel
BuildRequires: libakaze-devel
BuildRequires: minilog-devel
BuildRequires: libGLU-devel
BuildRequires: libgomp-devel
BuildRequires: hnswlib-devel
BuildRequires: libsqlite3-devel
BuildRequires: libcoinor-utils-devel
BuildRequires: libcoinor-osi-devel
BuildRequires: libcoinor-clp-devel
BuildRequires: libcoinor-osi-clp-devel
BuildRequires: libcoinor-lemon-devel
BuildRequires: libeasyexif-devel
BuildRequires: cpuid-devel
BuildRequires: kf5-kdelibs4support-devel

%add_optflags -Wno-dev

%description
Regard3D has been started as a hobby project in my spare time. I found several
great libraries and programs and decided to put them together by creating
Regard3D. As usual, the move from a hobby project to a program that everybody
can use is a big step. But since I also profited a lot from open-source
projects, I decided to release Regard3D to the public.

%package       devel
Summary:       A open source structure-from-motion program based on OpenMVG development package
Group:         Development/C

Requires:      cmake
Requires:      gcc-c++
Requires:      pkgconfig(eigen3-compat)
Requires:      pkgconfig(assimp)
Requires:      pkgconfig(lapack)
Requires:      pkgconfig(openblas)
Requires:      pkgconfig(opencv4)
Requires:      pkgconfig(libglvnd)
Requires:      libwxGTK3.0-devel
Requires:      libOpenSceneGraph-devel
Requires:      libglvnd-devel
Requires:      tbb-devel
Requires:      boost-devel >= 1.53.0
Requires:      boost-filesystem-devel
Requires:      boost-locale-devel
Requires:      boost-geometry-devel
Requires:      libjasper-devel
Requires:      libwebp-devel
Requires:      ceres-solver-devel
Requires:      libglog-devel
Requires:      libsuitesparse-devel
Requires:      libmetis-devel
Requires:      libvlfeat-devel
Requires:      libopenmvg-devel
Requires:      libnlopt-devel
Requires:      libkgraph-devel
Requires:      libakaze-devel
Requires:      minilog-devel
Requires:      libGLU-devel
Requires:      libgomp-devel
Requires:      hnswlib-devel
Requires:      libsqlite3-devel
Requires:      libcoinor-utils-devel
Requires:      libcoinor-osi-devel
Requires:      libcoinor-clp-devel
Requires:      libcoinor-osi-clp-devel
Requires:      libcoinor-lemon-devel
Requires:      libeasyexif-devel
Requires:      cpuid-devel

%description   devel
A open source structure-from-motion program based on OpenMVG development
package.

Regard3D has been started as a hobby project in my spare time. I found several
great libraries and programs and decided to put them together by creating
Regard3D. As usual, the move from a hobby project to a program that everybody
can use is a big step. But since I also profited a lot from open-source
projects, I decided to release Regard3D to the public.


%prep
%setup
%autopatch -p1

%build
cd src
%cmake_insource \
   -DMAKE_BUILD_TYPE:STRING=RelWithDebInfo \
   -DCMAKE_CONFIG_INSTALL_DIR:PATH='%_libdir/cmake/%name' \
   -DCMAKE_MODULE_PATH:PATH='%_datadir/cmake/Modules;%_libdir/cmake' \
   -DBUILD_SHARED_LIBS:BOOL=ON \
   -DOpenGL_GL_PREFERENCE:STRING=GLVND

%cmake_build

%install
cd src
%cmakeinstall_std

%files
%doc README.md
%_bindir/%name

%changelog
* Tue Jan 27 2026 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt2
- ![NBTFS] by upgrade to wx3.2
- ^ updated to novel openMVG about oct 2025
- * some dep like sqlite3, hnswlib, and easyexif moved to eternal sources
- - removed flann dep because openMVG isn't use it anymore.

* Fri May 16 2025 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt1.1
- ![NBTFS] fix lost dep to boost geometry devel
- + devel package

* Thu Jul 30 2020 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt1
- initial build for Sisyphus
