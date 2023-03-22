%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%define soname 1.8

Name: alembic
Version: 1.8.3
Release: alt2
Summary: Open framework for storing and sharing scene data
Group: Graphics
License: BSD-3-Clause and BSL-1.0
URL: https://www.alembic.io

# https://github.com/alembic/alembic.git
Source: %name-%version.tar

# Patches from Gentoo
Patch1: alembic-1.7.11-gentoo-0002-Find-IlmBase-by-setting-a-proper-ILMBASE_ROOT-value.patch
Patch2: alembic-1.8.0-gentoo-0001-set-correct-libdir.patch

BuildRequires: boost-devel
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libhdf5-devel

# Per https://github.com/alembic/alembic/blob/master/README.txt
# alembic actually needs ilmbase, not OpenEXR.
BuildRequires: imath-devel
BuildRequires: openexr-devel
BuildRequires: python3-module-imath-devel
BuildRequires: pkgconfig(zlib)

%description
Alembic is an open computer graphics interchange framework. Alembic distills
complex, animated scenes into a non-procedural, application-independent set of
baked geometric results. This 'distillation' of scenes into baked geometry is
exactly analogous to the distillation of lighting and rendering scenes into
rendered image data.

%package -n lib%name%soname
Summary: Core Alembic libraries
Group: System/Libraries

%description -n lib%name%soname
Alembic is an open computer graphics interchange framework. Alembic distills
complex, animated scenes into a non-procedural, application-independent set of
baked geometric results. This 'distillation' of scenes into baked geometry is
exactly analogous to the distillation of lighting and rendering scenes into
rendered image data.

%package devel
Summary: Development files for %name
Group: Development/C++
Requires: %name = %EVR

%description devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%prep
%setup
%patch1 -p1
%patch2 -p1

iconv -f iso8859-1 -t utf-8 ACKNOWLEDGEMENTS.txt > ACKNOWLEDGEMENTS.txt.conv && \
	mv -f ACKNOWLEDGEMENTS.txt.conv ACKNOWLEDGEMENTS.txt

%build
%add_optflags -D_FILE_OFFSET_BITS=64

%cmake \
	%_cmake_skip_rpath \
	-DALEMBIC_LIB_INSTALL_DIR=%_libdir \
	-DALEMBIC_BUILD_LIBS:BOOL=ON \
	-DALEMBIC_SHARED_LIBS=ON \
	-DDOCS_PATH:BOOL=OFF \
	-DUSE_ARNOLD:BOOL=OFF \
	-DUSE_BINARIES=ON \
	-DUSE_HDF5=ON \
	-DUSE_EXAMPLES=ON \
	-DUSE_MAYA:BOOL=OFF \
	-DUSE_PRMAN:BOOL=OFF \
	-DUSE_PYALEMBIC=OFF \
	-DUSE_STATIC_BOOST=OFF \
	-DUSE_STATIC_HDF5=OFF \
	-DUSE_TESTS=ON \
	%nil

%cmake_build

%install
%cmakeinstall_std

%files
%_bindir/abcconvert
%_bindir/abcdiff
%_bindir/abcecho
%_bindir/abcechobounds
%_bindir/abcls
%_bindir/abcstitcher
%_bindir/abctree

%files -n lib%name%soname
%doc LICENSE.txt
%doc ACKNOWLEDGEMENTS.txt FEEDBACK.txt NEWS.txt README.txt
%_libdir/libAlembic.so.%{soname}
%_libdir/libAlembic.so.%{soname}.*

%files devel
%_includedir/Alembic
%_libdir/cmake/Alembic
%_libdir/libAlembic.so

%changelog
* Tue Mar 21 2023 Alexander Burmatov <thatman@altlinux.org> 1.8.3-alt2
- Fix build requires.

* Mon Oct 04 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.8.3-alt1
- Updated to upstream version 1.8.3.

* Fri Jun 18 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.8.2-alt1
- Updated to upstream version 1.8.2.

* Thu Jun 03 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.8.1-alt1
- Updated to upstream version 1.8.1.

* Fri Nov 06 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.7.16-alt1
- Updated to upstream version 1.7.16.

* Thu Sep 17 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.7.15-alt1
- Updated to upstream version 1.7.15.

* Tue Sep 01 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.7.14-alt1
- Initial build for ALT.

* Fri Jul 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.13-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 13 2020 Luya Tshimbalanga <luya@fedoraproject.org> - 1.7.13-1
- Update to 1.7.13 (#1856031)	

* Thu Jun 25 2020 Orion Poplawski <orion@cora.nwra.com> - 1.7.12-3
- Rebuild for hdf5 1.10.6

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Oct 26 2019 Luya Tshimbalanga <luya@fedoraproject.org> - 1.7.12-1
- Update to 1.7.12
- Patch from Gentoo addressing ilbmbase root detection
- Drop ldconfig scriptlets

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat May 18 2019 Luya Tshimbalanga <luya@fedoraproject.org> - 1.7.11-1
- Update to 1.7.11

* Thu Apr 11 2019 Richard Shaw <hobbes1069@gmail.com> - 1.7.8-4
- Rebuild for Ilmbase 2.3.0.

* Sat Mar 16 2019 Orion Poplawski <orion@nwra.com> - 1.7.8-3
- Rebuild for hdf5 1.10.5

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 17 2018 Simone Caronni <negativo17@gmail.com> - 1.7.8-1
- Update to 1.7.8.

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Mar 27 2018 Luya Tshimbalanga <luya@fedoraproject.org> - 1.7.7-1
- Update to 1.7.7

* Sat Mar 24 2018 Luya Tshimbalanga <luya@fedoraproject.org> - 1.7.6-1
- Update to 1.7.6

* Sun Mar 04 2018 Luya Tshimbalanga <luya@fedoraproject.org> - 1.7.5-3
- Added gcc-c++ dependency for BuildRequires

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Dec 25 2017 Luya Tshimbalanga <luya@fedoraproject.org> - 1.7.5-1
- Update to 1.7.5.

* Sat Oct 28 2017 Luya Tshimbalanga <luya@fedoraproject.org> - 1.7.4-1
- Update to 1.7.4.

* Mon Sep 11 2017 Simone Caronni <negativo17@gmail.com> - 1.7.3-1
- Update to 1.7.3.

* Sun Aug 06 2017 Björn Esser <besser82@fedoraproject.org> - 1.7.2-4
- Rebuilt for AutoReq cmake-filesystem

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jul 23 2017 Simone Caronni <negativo17@gmail.com> - 1.7.2-1
- Update to 1.7.2.

* Tue May 09 2017 Simone Caronni <negativo17@gmail.com> - 1.7.1-3
- Link to hdf5 libraries, fixes undefined references on some architectures.

* Sat May 06 2017 Simone Caronni <negativo17@gmail.com> - 1.7.1-2
- Review fixes.

* Mon Apr 24 2017 Simone Caronni <negativo17@gmail.com> - 1.7.1-1
- First build.
