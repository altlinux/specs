%define _unpackaged_files_terminate_build 1

%define abiversion 1

%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}

Name:    libfabric
Version: 2.5.1
Release: alt2

Summary: Open Fabric Interfaces
License: BSD-2-Clause OR GPL-2.0-only
Group:   System/Libraries
Url:	 https://ofiwg.github.io/libfabric
Vcs:     https://github.com/ofiwg/libfabric.git

Source: %name-%version.tar

BuildRequires: gcc
BuildRequires: make
BuildRequires: automake
BuildRequires: autoconf
BuildRequires: libtool
BuildRequires: libnl-devel
BuildRequires: libibverbs-devel
BuildRequires: librdmacm-devel
BuildRequires: libnuma-devel

%description
OpenFabrics Interfaces (OFI) is a framework focused on exporting fabric
communication services to applications.  OFI is best described as a collection
of libraries and applications used to export fabric services.  The key
components of OFI are: application interfaces, provider libraries, kernel
services, daemons, and test applications.

Libfabric is a core component of OFI.  It is the library that defines and
exports the user-space API of OFI, and is typically the only software that
applications deal with directly.  It works in conjunction with provider
libraries, which are often integrated directly into libfabric.

%package -n %name%abiversion
Group: 	System/Libraries
Summary: Runtime library for Open Fabric Interfaces

%description -n %name%abiversion
This package contains the shared runtime library for %name.

Libfabric is a core component of OpenFabrics Interfaces (OFI).  It provides
the user-space API used by applications to access fabric communication
services through supported providers.

%package tools
Summary: Tools for Open Fabric Interfaces
Group: Networking/Other
Requires: %name%abiversion = %EVR
Obsoletes: %name < %EVR

%description tools
This package contains command line tools for %name.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name%abiversion = %EVR

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup -n %name-%version

%build
%ifarch %ix86
%add_optflags -Wno-incompatible-pointer-types
%endif
./autogen.sh
%configure --disable-static --disable-silent-rules
%make_build

%install
%makeinstall_std
find %buildroot -name '*.la' -print -delete

%files -n %name%abiversion
%_libdir/*.so.%{abiversion}*

%files tools
%doc COPYING *.md
%_bindir/fi_info
%_bindir/fi_mon_sampler
%_bindir/fi_pingpong
%_bindir/fi_strerror
%_man1dir/*.1*

%files devel
%doc AUTHORS README
%_includedir/rdma/
%_libdir/*.so
%_pkgconfigdir/%name.pc
%_mandir/man3/*.3*
%_mandir/man7/*.7*

%changelog
* Wed Jun 03 2026 Nikita Shmatko <nash@altlinux.org> 2.5.1-alt2
- Added ABI versioning.
- Split libfabric into ABI runtime and tools packages.

* Mon Apr 20 2026 Nikita Shmatko <nash@altlinux.org> 2.5.1-alt1
- New version 2.5.1.

* Wed Sep 17 2025 Nikita Shmatko <nash@altlinux.org> 2.2.0-alt1
- Initial build for Sisyphus.
