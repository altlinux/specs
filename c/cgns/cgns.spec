%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}

%define longdesc The CFD General Notation System (CGNS) provides a general, portable, and \
extensible standard for the storage and retrieval of computational fluid \
dynamics (CFD) analysis data. It consists of a collection of \
conventions, and free and open software implementing those conventions. \
It is self-descriptive, machine-independent, well-documented, and \
administered by an international steering committee. It is also an \
American Institute of Aeronautics and Astronautics (AIAA) Recommended \
Practice.

Name: cgns
Version: 4.2.0
Release: alt1
Summary: CFD General Notation System
Group: Sciences/Mathematics
License: Free (see license.txt)
URL: https://github.com/CGNS/CGNS

# https://github.com/CGNS/CGNS.git
Source: %name-%version.tar

Patch1: cgns-alt-install.patch

BuildRequires: cmake gcc-c++ gcc-fortran zlib-devel libGL-devel tk-devel
BuildRequires: libGLU-devel xorg-xproto-devel libXmu-devel libXtst-devel
BuildRequires: libXcomposite-devel libXcursor-devel libXdamage-devel
BuildRequires: libXdmcp-devel libXfixes-devel libXft-devel libXi-devel
BuildRequires: libXpm-devel libXrandr-devel libXrender-devel libXv-devel
BuildRequires: libXxf86misc-devel libXinerama-devel libXxf86vm-devel
BuildRequires: libhdf5-devel

Requires: lib%name = %EVR
Obsoletes: %name-seq < %EVR

%description
%longdesc

The system consists of two parts: (1) a standard format for recording
the data, and (2) software that reads, writes, and modifies data in that
format. The format is a conceptual entity established by the
documentation; the software is a physical product supplied to enable
developers to access and produce data recorded in that format.

%package -n lib%name
Summary: Shared libraries of CFD General Notation System
Group: System/Libraries

%description -n lib%name
%longdesc

This package contains shared libraries of CGNS.

%package -n lib%name-devel
Summary: Development files of CFD General Notation System
Group: Development/C++
Requires: lib%name = %EVR
Obsoletes: lib%name-seq-devel < %EVR

%description -n lib%name-devel
%longdesc

This package contains development files of CGNS.

%package -n lib%name-devel-static
Summary: Development files of CFD General Notation System
Group: Development/C++
Requires: lib%name-devel = %EVR

%description -n lib%name-devel-static
%longdesc

This package contains development files of CGNS.

%prep
%setup
%patch1 -p1

%build
%add_optflags -D_FILE_OFFSET_BITS=64

%cmake \
	-DCGNS_ENABLE_TESTS=ON \
	-DCGNS_ENABLE_FORTRAN=ON \
	-DCGNS_BUILD_CGNSTOOLS=ON \
	-DCGNS_ENABLE_HDF5=ON \
	%nil

%cmake_build

%install
%cmakeinstall_std

%files
%_bindir/*
%_datadir/cgnstools
%_desktopdir/*.desktop

%files -n lib%name
%doc license.txt
%doc README.md
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so

%files -n lib%name-devel-static
%_libdir/*.a

%changelog
* Wed Jan 19 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 4.2.0-alt1
- Updated to upstream version 4.2.0.

* Thu Aug 26 2021 Anton Midyukov <antohami@altlinux.org> 3.2-alt6.svn20150317
- remove unpackaged static libraries

* Fri Apr 16 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 3.2-alt5.svn20150317
- Rebuilt with new libhdf5.

* Mon Feb 11 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 3.2-alt4.svn20150317
- Fixed build on other architectures with %%_lib != lib.

* Sat Jun 23 2018 Anton Midyukov <antohami@altlinux.org> 3.2-alt3.svn20150317
- Rebuilt for aarch64

* Fri Mar 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2-alt2.svn20150317
- New snapshot

* Wed May 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2-alt2.svn20140522
- New snapshot

* Mon Nov 11 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2-alt2.svn20130919
- New snapshot

* Wed Jun 26 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2-alt2.svn20130201
- Rebuilt with new libhdf5

* Tue Jun 18 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2-alt1.svn20130201
- New snapshot

* Fri Feb 01 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2-alt1.svn20121213
- New snapshot

* Wed Sep 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2-alt1.svn20120829
- Version 3.2

* Mon Jun 25 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.3-alt2.svn20111216
- Rebuilt

* Fri Dec 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.3-alt1.svn20111216
- New snapshot

* Wed Sep 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.3-alt1.svn20110816.1
- Rebuilt with libhdf5-7

* Sat Aug 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.3-alt1.svn20110816
- New snapshot

* Mon May 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.3-alt1.svn20110503
- Version 3.1.3
- Disabled devel-static package

* Tue Mar 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.8-alt1.svn20100525.4
- Rebuilt for debuginfo

* Tue Nov 02 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.8-alt1.svn20100525.3
- Rebuilt for soname set-versions

* Wed Oct 13 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.8-alt1.svn20100525.2
- Fixed overlinking of libraries

* Mon Jun 21 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.8-alt1.svn20100525.1
- Added missing %_includedir/cgnsKeywords.h

* Fri Jun 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.8-alt1.svn20100525
- Version 3.0.8

* Thu Oct 15 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.7-alt1.svn20091009
- Initial build for Sisyphus

