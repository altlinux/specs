# -*- coding: latin-1; mode: rpm-spec -*-
%define sname oopango

Name: liboopango
Version: 1.0
Release: alt2

Summary: oopango is Lua binding to the Pango library, allowing text rendering
License: MIT, GPLv2+
Group: System/Libraries
Url: http://oocairo.naquadah.org
Source: %name-%version.tar
Patch: %name-%version-%release.patch

Packager: Evgenii Terechkov <evg@altlinux.org>

BuildRequires: liblua5-devel liboocairo-devel libpango-devel

%description
oopango is Lua binding to the Pango library, allowing text rendering

%package devel
Group: Development/C
Summary: Header files for developing programs using %name
Requires: %name = %version-%release

%description devel
This package contains the header files you need to develop programs
based on %name

%prep
%setup
%patch -p1

%build
%autoreconf
%configure --enable-shared
make

%install
%makeinstall_std

# Fix for crazy upstream:
cd %buildroot%_libdir/lua5
realpath="$(readlink %sname.so)"
ln -sf "../`basename $(readlink %buildroot$realpath)`" %sname.so

%files
%_libdir/%name.so.*
%_libdir/lua5/%sname.so

%files devel
%_pkgconfigdir/%sname.pc
%_libdir/%name.so
%_includedir/*

%changelog
* Sun May 15 2011 Terechkov Evgenii <evg@altlinux.org> 1.0-alt2
- Dependency on %name-devel fixed

* Sat May  7 2011 Terechkov Evgenii <evg@altlinux.org> 1.0-alt1
- Initial build for ALT Linux Sisyphus (git-20110507)

