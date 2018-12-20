
Name: libvzctl
Summary: OpenVZ Containers API library
Version: 7.0.499
Release: alt1
License: LGPLv2.1
Group: System/Libraries
Source: %name-%version.tar
Patch: %name-%version.patch

ExclusiveArch: x86_64

Requires: libvzevent >= 5.0.0
Requires: libploop >= 7.0.92
Requires: cgroup
Requires: crtools >= 2.8.0.15
Requires: libvcmmd = 7.0.22
BuildRequires: kernel-headers-ovz-el7 >= 3.10.0
BuildRequires: libvzevent-devel >= 5.0.0
BuildRequires: libploop-devel >= 7.0.92
BuildRequires: libvcmmd-devel >= 7.0.14
BuildRequires: libe2fs-devel
BuildRequires: libxml2-devel >= 2.6.16
BuildRequires: libuuid-devel
BuildRequires: libdbus-devel

%add_findreq_skiplist %_datadir/%name/dists/scripts/*
%filter_from_requires /^\/etc\/vz\/vz.conf/d
%define _pkglibdir %_libdir/%name

%description
OpenVZ Containers API library

%package devel
Summary: OpenVZ Containers API development library
Group: Development/C
License: LGPLv2.1
Requires: %name  = %version-%release

%description devel
OpenVZ Containers API development library

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%_libdir/*.so.*
%_pkglibdir
%_pkglibdir/exec_wrap
%_pkglibdir/action_wrap
%_datadir/%name

%files devel
%_libdir/*.so
%_includedir/vzctl

%changelog
* Sun Nov 04 2018 Alexey Shabalin <shaba@altlinux.org> 7.0.499-alt1
- 7.0.499

* Mon Feb 19 2018 Alexey Shabalin <shaba@altlinux.ru> 7.0.463-alt1
- Initial build
