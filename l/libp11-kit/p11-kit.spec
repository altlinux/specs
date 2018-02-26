%define _name p11-kit

Name: lib%_name
Version: 0.12
Release: alt1

Summary: Library for loading and sharing PKCS#11 modules
Group: System/Libraries
License: BSD
Url: http://p11-glue.freedesktop.org/p11-kit.html

Source: http://p11-glue.freedesktop.org/releases/%_name-%version.tar.gz

%description
%_name provides a way to load and enumerate PKCS#11 modules, as well
as a standard configuration setup for installing PKCS#11 modules in
such a way that they're discoverable.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
%_name provides a way to load and enumerate PKCS#11 modules, as well
as a standard configuration setup for installing PKCS#11 modules in
such a way that they're discoverable.

The %name-devel package provides libraries and headers for developing
applications that use %_name library.

%package devel-doc
Summary: Development documentation for %_name
Group: Development/C
Conflicts: %name < %version-%release
BuildArch: noarch

%description devel-doc
%_name provides a way to load and enumerate PKCS#11 modules, as well
as a standard configuration setup for installing PKCS#11 modules in
such a way that they're discoverable.

This package contains development documentation for %_name library.

%prep
%setup -q -n %_name-%version

%build
# https://bugs.freedesktop.org/show_bug.cgi?id=42459
# http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=647229
%add_optflags -D_GNU_SOURCE
%configure --disable-static
%make_build

%install
%make DESTDIR=%buildroot install
mkdir -p %buildroot%_sysconfdir/pkcs11/modules

%check
%make check

%files
%_bindir/%_name
%_libdir/lib%_name.so.*
%_libdir/%_name-proxy.so
%dir %_sysconfdir/pkcs11
%dir %_sysconfdir/pkcs11/modules
%_sysconfdir/pkcs11/pkcs11.conf.example
%doc AUTHORS COPYING NEWS README

%files devel
%_includedir/%_name-1
%_libdir/lib%_name.so
%_libdir/pkgconfig/%_name-1.pc

%files devel-doc
%_datadir/gtk-doc/html/%_name

%changelog
* Sun Mar 25 2012 Yuri N. Sedunov <aris@altlinux.org> 0.12-alt1
- 0.12
- %%check section

* Thu Nov 24 2011 Yuri N. Sedunov <aris@altlinux.org> 0.9-alt1
- 0.9

* Sun Sep 18 2011 Yuri N. Sedunov <aris@altlinux.org> 0.6-alt1
- 0.6

* Wed Aug 17 2011 Yuri N. Sedunov <aris@altlinux.org> 0.3-alt1
- first build for Sisyphus

