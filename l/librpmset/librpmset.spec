Name: librpmset
Version: 0.1.0
Release: alt1
Summary: Library for RPM set-version comparison and generation

License: LGPL-2.0-or-later
Group: System/Libraries
Url: https://git.altlinux.org/people/lav/packages/librpmset.git
Source: %name-%version.tar

%description
librpmset provides RPM-compatible comparison and generation of set-versions
used for ABI symbol dependencies.

%package -n librpmset1
Summary: Shared library for RPM set-versions
Group: System/Libraries

%description -n librpmset1
Shared library for RPM-compatible comparison and generation of set-versions.

%package devel
Summary: Development files for librpmset
Group: Development/C
Requires: librpmset1 = %EVR

%description devel
Header and development files for librpmset.

%prep
%setup

%build
%configure --disable-static
%make_build

%check
make check

%install
%makeinstall_std
rm -f %buildroot%_libdir/librpmset.la

%files -n librpmset1
%_libdir/librpmset.so.1
%_libdir/librpmset.so.1.*

%files devel
%_includedir/rpmset.h
%_libdir/librpmset.so
%doc AUTHORS COPYING README.md

%changelog
* Sun Aug 16 2026 Vitaly Lipatov <lav@altlinux.ru> 0.1.0-alt1
- Initial package.
