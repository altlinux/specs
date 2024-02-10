Name: libso5extra
Version: 1.3.1.1
Release: alt1

Summary: so5extra is a collection of various SObjectizer's extensions

License: BSD-3-CLAUSE
Group: Development/C++
Url: https://github.com/Stiffstream/so5extra

Packager: Pavel Vainerman <pv@altlinux.ru>

# Source-url: https://github.com/Stiffstream/so5extra/archive/v.%{version}.tar.gz
Source: %name-%version.tar
Source1: so5extra.pc

BuildRequires: libsobjectizer-devel

%description
so5extra is a collection of various SObjectizer's extensions. so5extra is built on top of SObjectizer and intended to simplify development of SObjectizer-based applications.

%package devel
Group: Development/C++
Summary: so5extra is a collection of various SObjectizer's extensions

%description devel
so5extra is a collection of various SObjectizer's extensions. so5extra is built on top of SObjectizer and intended to simplify development of SObjectizer-based applications.

%prep
%setup

%build

%install
mkdir -p %buildroot%_docdir/%name
cp LICENSE %buildroot%_docdir/%name/
cp README.md %buildroot%_docdir/%name/

mkdir -p %buildroot/%_includedir/so_5_extra
cd dev/so_5_extra
find . -name '*.hpp' -exec cp --parents \{\} %buildroot/%_includedir/so_5_extra \;

mkdir -p %buildroot%_libdir/pkgconfig
cp %SOURCE1 %buildroot%_libdir/pkgconfig/
%__subst 's|@VERSION@|%{version}|g' %buildroot%_libdir/pkgconfig/*.pc

%files devel
%_docdir/%name/
%_includedir/so_5_extra/
# %_libdir/cmake/so_5_extra/*.cmake
%_libdir/pkgconfig/*.pc

%changelog
* Sun Mar 08 2020 Pavel Vainerman <pv@altlinux.ru> 1.3.1.1-alt1
- new version (1.3.1.1) with rpmgs script

* Tue Jan 28 2020 Pavel Vainerman <pv@altlinux.ru> 1.4.0-alt1
- initial commit
