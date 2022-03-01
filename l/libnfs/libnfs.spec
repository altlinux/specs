%def_enable snapshot
%def_enable utils
%define sover 14

Name: libnfs
Version: 5.0.1
Release: alt1

Summary: NFS client library
License: LGPLv2.1

Group: System/Libraries
Url: https://github.com/sahlberg/%name

%if_disabled snapshot
Source: %url/archive/%name-%version.tar.gz
%else
Vcs: https://github.com/sahlberg/libnfs.git
Source: %name-%version.tar
%endif

%description
LIBNFS is a client library for accessing NFS shares over a network.

%package devel
Group: Development/C
Summary: NFS client library - development files
Requires: %name = %version-%release

%description devel
LIBNFS is a client library for accessing NFS shares over a network.

This package provides libraries and header files for developing
applications that use %name.

%package utils
Summary: Utility programs for LibNFS
Group: Networking/Other
Requires: %name = %version-%release

%description utils
This package provides utilities from LibNFS package.


%prep
%setup %{?_disable_snapshot:-n %name-%name-%version}

%build
%autoreconf
%configure --disable-static \
	%{?_disable_utils:--disable-utils}

%install
%makeinstall_std

%files
%_libdir/%name.so.*
%doc README COPYING

%files devel
%_includedir/nfsc/
%_libdir/%name.so
%_pkgconfigdir/%name.pc

%if_enabled utils
%files utils
%_bindir/nfs-ls
%_bindir/nfs-cat
%_bindir/nfs-cp
%_bindir/nfs-stat
%_man1dir/nfs-ls.1.*
%_man1dir/nfs-cat.1.*
%_man1dir/nfs-cp.1.*
%endif

%changelog
* Tue Mar 01 2022 Yuri N. Sedunov <aris@altlinux.org> 5.0.1-alt1
- updated to libnfs-5.0.1-3-g1703d44

* Wed Feb 13 2019 Yuri N. Sedunov <aris@altlinux.org> 4.0.0-alt1
- 4.0.0

* Sun Jul 08 2018 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt1
- 3.0.0

* Sun Jun 25 2017 Yuri N. Sedunov <aris@altlinux.org> 2.0.0-alt1
- 2.0.0

* Thu Nov 17 2016 Yuri N. Sedunov <aris@altlinux.org> 1.11.0-alt1
- 1.11.0

* Fri Feb 05 2016 Yuri N. Sedunov <aris@altlinux.org> 1.10.0-alt1
- 1.10.0

* Tue Aug 11 2015 Yuri N. Sedunov <aris@altlinux.org> 1.9.8-alt1
- 1.9.8

* Tue Feb 10 2015 Yuri N. Sedunov <aris@altlinux.org> 1.9.7-alt1
- first build for Sisyphus
