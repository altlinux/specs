%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

# TODO: build docs

%define oname opencolorio
%define soname 2.2

Name:           lib%oname%soname
Version:        2.2.1
Release:        alt2
Summary:        Enables color transforms and image display across graphics apps

License:        BSD-3-Clause
Group:          System/Libraries
URL:            https://opencolorio.org/

# https://github.com/imageworks/OpenColorIO.git
Source:         %name-%version.tar

Patch1: opencolorio-alt-install.patch
Patch2: opencolorio-alt-armh-multiple-definition.patch

# Utilities
BuildRequires: cmake gcc-c++
BuildRequires: help2man

# WARNING: OpenColorIO and OpenImageIO are cross dependent.
# If an ABI incompatible update is done in one, the other also needs to be
# rebuilt.
BuildRequires: openexr-devel

# Libraries
BuildRequires: libGL-devel libGLU-devel
BuildRequires: libX11-devel libXmu-devel libXi-devel
BuildRequires: libfreeglut-devel
BuildRequires: libGLEW-devel
BuildRequires: zlib-devel
BuildRequires: libexpat-devel
BuildRequires: pystring-devel
BuildRequires: pybind11-devel
BuildRequires: python3-devel
BuildRequires: liblcms2-devel
BuildRequires: libyaml-cpp-devel
BuildRequires: boost-devel
BuildRequires: libimath29-devel
BuildRequires: python3-module-imath
BuildRequires: libminizip-ng-devel

# Test dependencies
BuildRequires: ctest
BuildRequires: python3-module-numpy

%description
OCIO enables color transforms and image display to be handled in a consistent
manner across multiple graphics applications. Unlike other color management
solutions, OCIO is geared towards motion-picture post production, with an
emphasis on visual effects and animation color pipelines.

%package -n %oname%soname-tools
Summary:        Command line tools for %oname
Group:          Other
Provides:       opencolorio-tools = %version
Provides:       opencolorio2.0-tools = %EVR
Obsoletes:      opencolorio2.0-tools < %EVR

%description -n %oname%soname-tools
Command line tools for %oname.

%package devel
Summary:        Development libraries and headers for %oname
Group:          Development/Other
Provides:       libopencolorio-devel = %version
Provides:       libopencolorio2.0-devel = %EVR
Obsoletes:      libopencolorio2.0-devel < %EVR

%description devel
Development libraries and headers for %oname.

%package -n python3-module-%oname
Summary:        %oname python3 module
Group:          Development/Python3

%description -n python3-module-%oname
%oname python3 module.

%prep
%setup
%patch1 -p1
%patch2 -p1
%ifarch %e2k
# ld: multiple definition of LoadLutFile
sed -i "s/OCIO::LocalCachedFileRcPtr LoadLutFile/static &/" \
	tests/cpu/fileformats/*_tests.cpp
%endif

%build
%add_optflags -D_FILE_OFFSET_BITS=64

# disable debugging wrappers
%add_optflags -DNDEBUG

%cmake \
	-DBUILD_SHARED_LIBS:BOOL=ON \
	-DOCIO_BUILD_PYTHON:BOOL=ON \
	-DOCIO_BUILD_STATIC=OFF \
	-DOCIO_BUILD_DOCS=OFF \
	-DOCIO_BUILD_TESTS=ON \
	-DOCIO_BUILD_GPU_TESTS=OFF \
	-DOCIO_WARNING_AS_ERROR:BOOL=OFF \
%ifnarch x86_64 %e2k
	-DOCIO_USE_SSE=OFF \
%endif
%ifnarch %e2k
	-DOCIO_USE_GLVND:BOOL=ON \
	-DOpenGL_GL_PREFERENCE=GLVND \
%endif
	-DCMAKE_CXX_STANDARD=14 \
	%nil

%cmake_build

%install
%cmakeinstall_std

# Generate man pages
mkdir -p %buildroot%_man1dir

for i in %buildroot%_bindir/* ; do
	if [ "$(basename $i)" != "ociodisplay" ] ; then
		LD_LIBRARY_PATH=%buildroot%_libdir \
		help2man -N -s 1 --version-string=%version \
		-o %buildroot%_man1dir/$(basename $i).1 \
		$i
	fi
done
rm -fr %buildroot%_libdir/libOpenColorIOimageioapphelpers.a

%check
pushd %_cmake__builddir
# currently tests only pass on x86_64
# on other architectures there are precision issues
%ifarch x86_64
ctest
%else
ctest ||:
%endif
popd

%files -n lib%oname%soname
%doc LICENSE THIRD-PARTY.md
%doc CHANGELOG.md CONTRIBUTING.md COMMITTERS.md GOVERNANCE.md PROCESS.md README.md SECURITY.md
%_libdir/*.so.%{soname}
%_libdir/*.so.%{soname}.*

%files -n %oname%soname-tools
%_bindir/ocioarchive
%_bindir/ociobakelut
%_bindir/ociocheck
%_bindir/ociochecklut
%_bindir/ocioconvert
%_bindir/ociodisplay
%_bindir/ociolutimage
%_bindir/ociomakeclf
%_bindir/ocioperf
%_bindir/ociowrite
%_man1dir/*

%files devel
%_includedir/OpenColorIO/
%_libdir/*.so
%_pkgconfigdir/*.pc
%_libdir/cmake/OpenColorIO/

%files -n python3-module-%oname
%python3_sitelibdir/*.so

%changelog
* Tue Mar 14 2023 Sergey V Turchin <zerg@altlinux.org> 2.2.1-alt2
- obsolete libopencolorio2.0-devel

* Mon Jan 16 2023 Alexander Burmatov <thatman@altlinux.org> 2.2.1-alt1
- Updated to upstream version 2.2.1.

* Thu Jan 20 2022 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 2.0.3-alt1.1
- Fixed build for Elbrus.

* Fri Jan 14 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 2.0.3-alt1
- Updated to upstream version 2.0.3.

* Wed Dec 15 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 2.0.2-alt3
- Fixed build with new dependencies.

* Mon Sep 06 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 2.0.2-alt2
- Rebuilt with openimageio support.

* Mon Sep 06 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 2.0.2-alt1
- Updated to upstream version 2.0.2.
- Built without openimageio support.

* Mon Jun 07 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 2.0.1-alt3
- Enabled tests.

* Wed Jun 02 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 2.0.1-alt2
- Rebuilt with openimageio support.

* Tue Jun 01 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 2.0.1-alt1
- Updated to upstream version 2.0.1.
- Built without openimageio support.

* Tue Apr 14 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.1-alt4
- Rebuilt with openimageio support.

* Tue Apr 14 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.1-alt3
- Bootstrapped rebuild.

* Mon Jul 15 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.1-alt2
- Rebuilt with openimageio support.

* Sat Jul 13 2019 Michael Shigorin <mike@altlinux.org> 1.1.1-alt1.1
- E2K:
  + explicit -std=c++11
  + avoid unwarranted -Werror
  + build without libglvnd for now

* Mon May 27 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.1-alt1
- Updated to upstream version 1.1.1.

* Mon Oct 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.0-alt1
- Initial build for ALT.

* Mon Sep 24 2018 Richard Shaw <hobbes1069@gmail.com> - 1.1.0-9
- Obsolete Python2 library and build Python3 library.

* Thu Aug 23 2018 Nicolas Chauvet <kwizart@gmail.com> - 1.1.0-8
- Rebuilt for glew 2.1.0

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 22 2018 Adam Williamson <awilliam@redhat.com> - 1.1.0-6
- Rebuild with bootstrap disabled, so we get docs again

* Thu Feb 22 2018 Peter Robinson <pbrobinson@fedoraproject.org> 1.1.0-5
- Rebuild

* Tue Feb 20 2018 Rex Dieter <rdieter@fedoraproject.org> - 1.1.0-4
- support %%bootstrap (no docs, no tests)
- enable bootstrap mode on f28+ to workaround bug #1546964

* Mon Feb 19 2018 Adam Williamson <awilliam@redhat.com> - 1.1.0-3
- Fix build with yaml-cpp 0.6+ (patch out bogus hidden visibility)
- Fix build with GCC 8 (issues in Python bindings, upstream PR #518)
- Rebuild for yaml-cpp 0.6.1

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 12 2018 Richard Shaw <hobbes1069@gmail.com> - 1.1.0-1
- Update to latest upstream release.

* Sun Jan 07 2018 Richard Shaw <hobbes1069@gmail.com> - 1.0.9-20
- Rebuild for OpenImageIO 1.8.7.

* Wed Dec 06 2017 Richard Shaw <hobbes1069@gmail.com> - 1.0.9-19
- Fix ambiguous Python 2 dependency declarations
  https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3
  
* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 07 2017 Igor Gnatenko <ignatenko@redhat.com> - 1.0.9-16
- Rebuild due to bug in RPM (RHBZ #1468476)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 10 2017 Orion Poplawski <orion@cora.nwra.com> - 1.0.9-14
- Rebuild for glew 2.0.0

* Mon Oct 03 2016 Richard Shaw <hobbes1069@gmail.com> - 1.0.9-13
- Rebuild for new OpenImageIO.

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.9-12
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 14 2016 Richard Shaw <hobbes1069@gmail.com> - 1.0.9-10
- Rebuild for OpenImageIO 1.6.9.

* Thu Jan 14 2016 Adam Jackson <ajax@redhat.com> - 1.0.9-9
- Rebuild for glew 1.13

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.0.9-7
- Rebuilt for GCC 5 C++11 ABI change

* Wed Jan 28 2015 Richard Shaw <hobbes1069@gmail.com> - 1.0.9-6
- Rebuild for OpenImageIO 1.5.11.

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 21 2014 Richard Shaw <hobbes1069@gmail.com> - 1.0.9-3
- Rebuild for updated OpenImageIO 1.4.7.

* Mon Jan 13 2014 Richard Shaw <hobbes1069@gmail.com> - 1.0.9-2
- Add OpenImageIO as build requirement to build additional command line tools.
  Fixes BZ#1038860.

* Wed Nov  6 2013 Richard Shaw <hobbes1069@gmail.com> - 1.0.9-1
- Update to latest upstream release.

* Mon Sep 23 2013 Richard Shaw <hobbes1069@gmail.com> - 1.0.8-6
- Rebuild against yaml-cpp03 compatibility package.

* Mon Aug 26 2013 Richard Shaw <hobbes1069@gmail.com> - 1.0.8-5
- Fix for new F20 feature, unversion doc dir. Fixes BZ#1001264

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Dec 11 2012 Richard Shaw <hobbes1069@gmail.com> - 1.0.8-1
- Update to latest upstream release.

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Apr 26 2012 Richard Shaw <hobbes1069@gmail.com> - 1.0.7-4
- Only use SSE instructions on x86_64.

* Wed Apr 25 2012 Richard Shaw <hobbes1069@gmail.com> - 1.0.7-3
- Misc spec cleanup for packaging guidelines.
- Disable testing for now since it fails on the build servers.

* Wed Apr 18 2012 Richard Shaw <hobbes1069@gmail.com> - 1.0.7-1
- Latest upstream release.

* Thu Apr 05 2012 Richard Shaw <hobbes1069@gmail.com> - 1.0.6-1
- Latest upstream release.

* Wed Nov 16 2011 Richard Shaw <hobbes1069@gmail.com> - 1.0.2-1
- Initial release.
