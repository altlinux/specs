Name: libbpf
Version: 0.0.8
Release: alt1
Summary: Stand-alone build of libbpf from the Linux kernel
Group: System/Libraries
License: BSD-2-Clause or LGPL-2.1
Url: https://github.com/libbpf/libbpf

Source: %name-%version.tar

BuildRequires: libelf-devel
BuildRequires: zlib-devel

%description
Library to access Linux kernel BPF API.

%package devel
Summary: Libbpf library and headers
Group: Development/C
License: LGPLv2 or BSD
Requires: %name = %EVR

%description devel
Library and header files to build with libbpf.

%package devel-static
Summary: Libbpf static library
Group: Development/C
License: LGPLv2 or BSD
Requires: %name-devel = %EVR

%description devel-static
Static libbpf library.

%prep
%setup

%build
cd src
%make_build

%install
cd src
%makeinstall_std LIBSUBDIR=%_lib

%files
%_libdir/libbpf.so.*

%files devel
%_includedir/bpf
%_libdir/libbpf.so
%_pkgconfigdir/libbpf.pc

%files devel-static
%_libdir/libbpf.a

%changelog
* Mon Apr 27 2020 Vitaly Chikunov <vt@altlinux.org> 0.0.8-alt1
- First import of v0.0.8.
