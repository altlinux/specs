
%def_disable static

Name: dapl
%define lname lib%name

Version: 2.1.10
Release: alt1
Summary: A Library for userspace access to RDMA devices using OS Agnostic DAT APIs
Group: System/Libraries
License: %gpl2only, %bsdstyle, CPL
Url: http://www.openfabrics.org/
# git://git.openfabrics.org/~ardavis/dapl.git
Source: %name-%version.tar

Patch: %name-%version.patch

BuildRequires(pre): rpm-build-licenses
BuildRequires: rdma-core-devel

%description
Along with the OpenFabrics kernel drivers, libdat and libdapl provides
a userspace RDMA API that supports DAT 2.0 specification and IB
transport extensions for atomic operations and rdma write with
immediate data.


%package -n lib%name
Summary: A Library for userspace access to RDMA devices using OS Agnostic DAT APIs
Group: System/Libraries
Provides: lib%{name}2 = %version-%release
Obsoletes: lib%{name}2 < %version-%release

%description -n lib%name
Along with the OpenFabrics kernel drivers, libdat and libdapl provides
a userspace RDMA API that supports DAT 2.0 specification and IB
transport extensions for atomic operations and rdma write with
immediate data.


%package -n lib%name-devel
Summary: Development files for the libdat and libdapl libraries
Group: Development/C
Requires: lib%name = %version-%release
Provides: lib%{name}2-devel = %version-%release
Obsoletes: lib%{name}2-devel < %version-%release

%description -n lib%name-devel
Header files for libdat and libdapl library.

%package -n lib%name-devel-static
Summary: Static development files for libdat and libdapl library
Group: Development/C
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-static
Static libraries for libdat and libdapl library.

%package utils
Summary: Test suites for uDAPL library
Group: Development/Other
Requires: lib%name = %version-%release
Provides: %{name}2-utils = %version-%release
Obsoletes: %{name}2-utils < %version-%release

%description utils
Useful test suites to validate uDAPL library API's.

%prep
%setup
%patch -p1


%build
mkdir -p config m4
%autoreconf
%configure \
    --with-pic \
    --with-gnu-ld \
    --enable-ext-type=ib \
    %{subst_enable static} \
    --sysconfdir=/etc/rdma

%make_build

%install
%make_install DESTDIR=%buildroot install{-datlibLTLIBRARIES,}

%files -n lib%name
%doc AUTHORS README ChangeLog
%_libdir/*.so.*
%config(noreplace) %_sysconfdir/rdma/dat.conf
%_man5dir/*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/dat2

%if_enabled static
%files -n %lname-devel-static
%_libdir/*.a
%endif

%files utils
%_bindir/*
%_man1dir/*

%changelog
* Thu Apr 12 2018 Alexey Shabalin <shaba@altlinux.ru> 2.1.10-alt1
- 2.1.10

* Mon Apr 09 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.30-alt3
- fixed build on aarch64

* Tue Dec 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.30-alt2.1
- Fixed build with glibc 2.16

* Thu Mar 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.30-alt2
- Rebuilt for debuginfo
- Disabled static package

* Tue Dec 07 2010 Andriy Stepanov <stanv@altlinux.ru> 2.0.30-alt1
- New version (OFED 1.5.2_v2)

* Mon Aug 16 2010 Andriy Stepanov <stanv@altlinux.ru> 2.0.27-alt2
- New version (OFED 1.5.1)

* Mon Jul 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.20-alt2
- Added default %_sysconfdir/dat2.conf (thnx led@)

* Wed Jul 08 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.20-alt1.1
- Build from upstream git repository

* Wed Jul 08 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.20-alt1
- Version 2.0.20

* Wed Jun 24 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.19-alt2.1
- Build for Sisyphus

* Tue Jun 23 2009 Led <led@altlinux.ru> 2.0.19-alt2
- fixed linking
- cleaned up spec

* Sun Jun 21 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.19-alt1.1
- Build for Sisyphus

* Wed May 20 2009 Led <led@altlinux.ru> 2.0.19-alt1
- 2.0.19

* Thu Apr 23 2009 Led <led@altlinux.ru> 2.0.16-alt1
- initial build for ALT

