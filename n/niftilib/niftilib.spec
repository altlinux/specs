%define libznz_soname 3
%define libniftiio_soname 2
%define libnifti2_soname 2
%define libnifticdf_soname 2

Name: niftilib
Version: 3.0.1
Release: alt1
Summary: A set of i/o libraries for reading and writing nifti-1 files
License: ALT-Public-Domain
Group: File tools
Url: https://github.com/NIFTI-Imaging/nifti_clib
VCS: https://github.com/NIFTI-Imaging/nifti_clib.git
Source: %name-%version.tar
Patch0: niftilib-3.0.1-fedora-dont-get-version-from-git.patch

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: zlib-devel
BuildRequires: ctest
BuildRequires: doxygen
BuildRequires: /usr/bin/help2man
BuildRequires: libexpat-devel
BuildRequires: /proc

%description
Niftilib is a set of i/o libraries for reading and writing files in the
nifti-1 data format. nifti-1 is a binary file format for storing medical
image data, e.g. magnetic resonance image (MRI) and functional MRI
(fMRI) brain images.

%package -n libznz%libznz_soname
Summary: Low-level library for handling read/write of compressed files
Group: System/Libraries

%description -n libznz%libznz_soname
Low-level library for handling read/write of compressed files.
This is part of the Niftilib package.

%package -n libniftiio%libniftiio_soname
Summary: Core i/o routines for reading and writing nifti-1 format files
Group: System/Libraries

%description -n libniftiio%libniftiio_soname
Core i/o routines for reading and writing nifti-1 format files.
Primarily routines to read/write and manipulate the header field
information, including orientation matrices.

%package -n libnifti2_%libnifti2_soname
Summary: Core i/o routines for reading and writing nifti-2 format files
Group: System/Libraries

%description -n libnifti2_%libnifti2_soname
Core i/o routines for reading and writing nifti-2 format files.

%package -n libnifticdf%libnifticdf_soname
Summary: Functions to compute cumulative distributions and their inverses
Group: System/Libraries

%description -n libnifticdf%libnifticdf_soname
Functions to compute cumulative distributions and their inverses.
This is part of the Niftilib package.

%package -n lib%name-devel
Summary: Development files of Niftilib
Group: Development/C
Requires: libznz%libznz_soname = %EVR
Requires: libniftiio%libniftiio_soname = %EVR
Requires: libnifti2_%libnifti2_soname = %EVR
Requires: libnifticdf%libnifticdf_soname = %EVR

%description -n lib%name-devel
Niftilib is a set of i/o libraries for reading and writing files in the
nifti-1 data format. nifti-1 is a binary file format for storing medical
image data, e.g. magnetic resonance image (MRI) and functional MRI
(fMRI) brain images.

This package contains development files of Niftilib.

%package -n lib%name-devel-doc
Summary: Documentation for Niftilib
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-doc
Niftilib is a set of i/o libraries for reading and writing files in the
nifti-1 data format. nifti-1 is a binary file format for storing medical
image data, e.g. magnetic resonance image (MRI) and functional MRI
(fMRI) brain images.

This package contains development documentation for Niftilib.

%prep
%setup
%patch0 -p0

%build

%cmake \
    -DGIT_REPO_VERSION:STRING="%{version}" \
    -DBUILD_SHARED_LIBS=ON \
    -DNIFTI_BUILD_APPLICATIONS=ON \
    -DNIFTI_BUILD_TESTING=ON \
    -DNIFTI_INSTALL_NO_DOCS=OFF \
    -DBUILD_TESTING=ON \
    -DDOWNLOAD_TEST_DATA=OFF \
    -DUSE_NIFTI2_CODE=ON \
    -DUSE_CIFTI_CODE=ON \
    -DUSE_FSL_CODE=OFF \
    -DNIFTI_INSTALL_LIBRARY_DIR=%{_lib} \
    -DNIFTI_INSTALL_DOC_DIR=%{_docdir}/%{name}/ \
    -Dfetch_testing_data_SOURCE_DIR:PATH=%{_builddir}/nifti-test-data-3.0.2 \
    .

%cmake_build

%install
%cmake_install

# Rename man pages (they are installed with _manpage suffix)
for f in nifti1_tool nifti_stats nifti_tool; do
    if [ -f %buildroot%_mandir/man1/${f}_manpage.1* ]; then
        mv %buildroot%_mandir/man1/${f}_manpage.1* %buildroot%_mandir/man1/${f}.1
    fi
done


%files
%doc LICENSE Updates.txt
%_bindir/*
%_man1dir/*

%files -n libznz%libznz_soname
%_libdir/libznz.so.%libznz_soname
%_libdir/libznz.so.%libznz_soname.*

%files -n libniftiio%libniftiio_soname
%_libdir/libniftiio.so.%libniftiio_soname
%_libdir/libniftiio.so.%libniftiio_soname.*

%files -n libnifti2_%libnifti2_soname
%_libdir/libnifti2.so.%libnifti2_soname
%_libdir/libnifti2.so.%libnifti2_soname.*

%files -n libnifticdf%libnifticdf_soname
%_libdir/libnifticdf.so.%libnifticdf_soname
%_libdir/libnifticdf.so.%libnifticdf_soname.*

%files -n lib%name-devel
%_datadir/cmake/NIFTI
%_includedir/nifti/
%_libdir/libznz.so
%_libdir/libniftiio.so
%_libdir/libnifti2.so
%_libdir/libnifticdf.so
%_libdir/libcifti.so

%files -n lib%name-devel-doc
%_docdir/%name

%changelog
* Sat Jan 10 2026 Anton Farygin <rider@altlinux.org> 3.0.1-alt1
- 0.20100720 -> 3.0.1
- split libraries into separate packages according to SharedLibsPolicy

* Sat Apr 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.20100720-alt4
- Fixed build

* Mon Mar 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.20100720-alt3
- Added -g into compiler flags

* Fri Feb 11 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.20100720-alt2
- Rebuilt for debuginfo

* Mon Oct 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.20100720-alt1
- New snapshot
- Rebuilt for soname set-versions

* Thu Jul 01 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.20100428-alt1.cvs20100428
- New snapshot

* Thu Sep 24 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.20090303.1-alt1.cvs20090924
- Initial build for Sisyphus

