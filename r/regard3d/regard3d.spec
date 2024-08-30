%define        _unpackaged_files_terminate_build 1

Name:          regard3d
Version:       1.0.0
Release:       alt1
Summary:       A open source structure-from-motion program based on OpenMVG
License:       MIT
Group:         Graphics
Url:           http://www.regard3d.org/
Vcs:           https://github.com/rhiestan/Regard3D.git
ExclusiveArch: x86_64

Source:        %name-%version.tar
Patch:         %name-%version-%release.patch
BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(eigen3)
BuildRequires: pkgconfig(assimp)
BuildRequires: pkgconfig(lapack)
BuildRequires: pkgconfig(flann) >= 1.9.1
BuildRequires: pkgconfig(openblas)
BuildRequires: pkgconfig(opencv4)
BuildRequires: pkgconfig(libglvnd)
BuildRequires: libwxGTK3.0-devel
BuildRequires: libOpenSceneGraph-devel
BuildRequires: libglvnd-devel
BuildRequires: tbb-devel
BuildRequires: boost-devel
BuildRequires: boost-filesystem-devel
BuildRequires: boost-locale-devel
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

%description
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
* Thu Jul 30 2020 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt1
- initial build for Sisyphus
