Name: libdapl
Version: 1.2.16
Release: alt2

Summary: Userspace DAT and DAPL API
License: GPL/BSD/CPL
Group: System/Libraries

Url: http://openfabrics.org/
Source: http://openfabrics.org/~ardavis/dapl-%version.tar
Patch0: dapl-1.2.14-alt-build.patch
Patch1: dapl-1.2.7-alt-gcc.patch
Packager: Stanislav Ievlev <inger@altlinux.org>

BuildPreReq: librdmacm-devel-static >= 1.0.8-alt1
Requires: librdmacm >= 1.0.8-alt1

# Automatically added by buildreq on Fri Aug 24 2007
BuildRequires: gcc-c++ gcc-fortran librdmacm-devel libstdc++-devel-static

%description
Along with the OpenIB kernel drivers, libdat and libdapl provides
a userspace RDMA API that supports DAT 1.2 specification

%package devel
Summary: Development files for the libdat and libdapl libraries
Group: Development/C
Requires: %name = %version-%release libibverbs-devel librdmacm-devel
Conflicts: libdapl2-devel

%description devel
Shared libraries and header files for the libdat and libdapl library.

%package devel-static
Summary: Static development files for the libdat and libdapl libraries
Group: Development/C
Requires: %name-devel = %version-%release
Requires: libibverbs-devel-static librdmacm-devel-static

%description devel-static
Static libraries for the libdat and libdapl library.

%package utils
Summary: Test suites for uDAPL library
Group: System/Base
Requires: %name = %version-%release

%description utils
Useful test suites to validate uDAPL library APIs.

%prep
%setup -n dapl-%version
%patch0 -p2
%patch1 -p1

%build
touch NEWS ChangeLog
%autoreconf
%configure
%make_build

%install
#_hackaround over broken author's mind
install -Dpm644 /dev/null %buildroot/%_sysconfdir/dat.conf
#_hackaround over broken automake mind
%make DESTDIR=%buildroot install-datlibLTLIBRARIES
%makeinstall_std

%files
%doc AUTHORS README
%_libdir/*.so.*
%config(noreplace) %_sysconfdir/dat.conf
%_man5dir/*

%files devel
%_libdir/*.so
%_includedir/*

%files devel-static
%_libdir/*.a

%files utils
%_bindir/*
%_man1dir/*

%changelog
* Wed Feb 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.16-alt2
- Rebuilt for debuginfo

* Sun Oct 17 2010 Michael Shigorin <mike@altlinux.org> 1.2.16-alt1.qa1
- fix FTBFS (macro name)
- dropped BR: rpm-build-compat
- minor spec cleanup according to packaging policy

* Mon Aug 16 2010 Andriy Stepanov <stanv@altlinux.ru> 1.2.16-alt1
- 1.2.16 (OFED-1.5.1)

* Fri Dec 18 2009 Stanislav Ievlev <inger@altlinux.org> 1.2.14-alt1
- 1.2.14 (OFED-1.4.2)

* Wed Apr 29 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.12-alt1
- Version 1.2.12

* Sat Nov 01 2008 Stanislav Ievlev <inger@altlinux.org> 1.2.7-alt2
- fix build with gcc 4.3

* Mon Oct 13 2008 Stanislav Ievlev <inger@altlinux.org> 1.2.7-alt1
- OFED-1.3.1

* Fri Aug 24 2007 Stanislav Ievlev <inger@altlinux.org> 1.2.1-alt1
- Initial build
