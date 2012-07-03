Name: librdmacm
Version: 1.0.13
Release: alt2.1

Summary: Userspace RDMA Connection Manager
Group: System/Libraries
License: GPL/BSD

Url: http://www.openfabrics.org/
Source: http://www.openfabrics.org/downloads/%{name}-%{version}.tar
Patch: librdmacm-1.0.13-alt-DSO.patch
Packager: Stanislav Ievlev <inger@altlinux.org>

BuildRequires(pre): rpm-build-compat
BuildPreReq: libibverbs-devel-static >= 1.1.4-alt1
Requires: libibverbs >= 1.1.4-alt1

# Automatically added by buildreq on Fri Aug 24 2007
BuildRequires: gcc-c++ gcc-fortran libibverbs-devel libstdc++-devel-static

%description
librdmacm provides a userspace RDMA Communication Managment API.

%package devel
Summary: Development files for the librdmacm library
Group: Development/C
Requires: %name = %version-%release libibverbs-devel 

%description devel
Development files for the librdmacm library.

%package devel-static
Summary: Static development files for the librdmacm library
Group: Development/C
Requires: %name-devel = %version-%release libibverbs-devel-static

%description devel-static
Static development files for the librdmacm library.

%package utils
Summary: Examples for the librdmacm library
Group: System/Base
Requires: %name = %version-%release

%description utils
Example test programs for the librdmacm library.

%prep
%setup -n %name-%version
%patch -p2

%build
./autogen.sh
%configure
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS COPYING ChangeLog README
%_libdir/*.so.*

%files devel
%_libdir/*.so
%_includedir/*
%_man3dir/*
%_man7dir/*

%files devel-static
%_libdir/*.a

%files utils
%defattr(-,root,root,-)
%_bindir/*
%_man1dir/*

%changelog
* Wed Jun 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.13-alt2.1
- Fixed build

* Wed Feb 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.13-alt2
- Rebuilt for debuginfo

* Thu Dec 16 2010 Timur Aitov <timonbl4@altlinux.org> 1.0.13-alt1
- New version

* Sun Oct 17 2010 Michael Shigorin <mike@altlinux.org> 1.0.11-alt1.qa1
- fix FTBFS (macro name)
- minor spec cleanup according to packaging policy

* Tue Aug 17 2010 Andriy Stepanov <stanv@altlinux.ru> 1.0.11-alt1
- New version (OFED 1.5.1)

* Wed Apr 29 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.8-alt1
- Version 1.0.8
- Add static devel package

* Mon Oct 13 2008 Stanislav Ievlev <inger@altlinux.org> 1.0.7-alt1
- OFED-1.3.1

* Fri Aug 24 2007 Stanislav Ievlev <inger@altlinux.org> 1.0.2-alt1
- Initial build

