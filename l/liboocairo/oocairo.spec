# -*- coding: latin-1; mode: rpm-spec -*-
%define sname oocairo

Name: liboocairo
Version: 1.3
Release: alt2

Summary: oocairo is Lua binding to the Cairo library, allowing graphic rendering
License: MIT, GPLv2+
Group: System/Libraries
Url: http://oocairo.naquadah.org
Source: %name-%version.tar
Patch: %name-%version-%release.patch

Packager: Evgenii Terechkov <evg@altlinux.org>

BuildRequires: gcc-c++ libcairo-devel liblua5-devel perl-podlators

%description
oocairo is Lua binding to the Cairo library, allowing graphic rendering

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
%_man3dir/*%{sname}*

%files devel
%_pkgconfigdir/%sname.pc
%_libdir/%name.so
%_includedir/*

%changelog
* Sun May 15 2011 Terechkov Evgenii <evg@altlinux.org> 1.3-alt2
- Dependency on %name-devel fixed

* Tue May  3 2011 Terechkov Evgenii <evg@altlinux.org> 1.3-alt1
- Initial build for ALT Linux Sisyphus (git-20110506)
