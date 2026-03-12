%define _unpackaged_files_terminate_build 1
%define abiversion 0

Name:    yaksa
Version: 0.3
Release: alt2

Summary: Yaksa: High-performance Noncontiguous Data Management
License: BSD-3-Clause
Group:   System/Libraries
Url:     https://github.com/pmodels/yaksa

Source: %name-%version.tar

BuildRequires: python3
BuildRequires: libuthash-devel

%description
Yaksa is a high-performance noncontiguous datatype engine that can be used to
express and manipulate noncontiguous data. The library sports features related
to packing/unpacking, I/O vectors, and flattening noncontiguous datatypes.

%package -n lib%name%abiversion
Group: System/Libraries
Summary: %summary

%description -n lib%name%abiversion
Yaksa is a high-performance noncontiguous datatype engine that can be used to
express and manipulate noncontiguous data. The library sports features related
to packing/unpacking, I/O vectors, and flattening noncontiguous datatypes.

%package -n lib%name-devel
Summary: Development files for lib%name
Group: Development/C
Requires: lib%name%abiversion = %EVR

%description -n lib%name-devel
%summary.

%prep
%setup -n %name-%version

%build
./autogen.sh
%configure \
	--disable-static
%make_build

%install
%makeinstall_std

rm %buildroot%_libdir/libyaksa.la

%check
%make_build check

%files -n lib%name%abiversion
%doc *.md COPYRIGHT
%_libdir/lib%name.so.%{abiversion}*

%files -n lib%name-devel
%_includedir/*.h
%_libdir/lib%name.so
%_pkgconfigdir/%name.pc

%changelog
* Wed Mar 11 2026 Nikita Shmatko <nash@altlinux.org> 0.3-alt2
- Minor spefile fixes.

* Mon Oct 13 2025 Nikita Shmatko <nash@altlinux.org> 0.3-alt1
- Initial build for Sisyphus.
