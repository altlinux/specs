%define soname 1
%def_enable tests

Name: libgbinder

Version: 1.1.33
Release: alt0.1
Summary: Binder client library
License: BSD
Group: System/Libraries
Url: https://github.com/mer-hybris/libgbinder
Source: %name-%version.tar

%define libglibutil_version 1.0.52

BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(libglibutil) >= %libglibutil_version
BuildRequires: pkgconfig
BuildRequires: bison
BuildRequires: flex
%if_enabled tests
BuildRequires: pkgconfig(gio-2.0) pkgconfig(gio-unix-2.0)
%endif

%description
C interfaces for Android binder

%package -n %{name}%{soname}
Summary: Binder client library
Group: System/Libraries

%description -n %{name}%{soname}
C interfaces for Android binder

%package devel
Summary: Development library for %name
Group: Development/C

%description devel
This package contains the development library for %name.

# Tools
%package tools
Summary: Binder tools
Group: System/Configuration/Other

%description tools
Binder command line utilities

%prep
%setup

%build
make %_smp_mflags CFLAGS="%optflags" LIBDIR=%_libdir KEEP_SYMBOLS=1 release pkgconfig
make -C test/binder-bridge KEEP_SYMBOLS=1 release
make -C test/binder-list KEEP_SYMBOLS=1 release
make -C test/binder-ping KEEP_SYMBOLS=1 release
make -C test/binder-call KEEP_SYMBOLS=1 release

%install
make LIBDIR=%_libdir DESTDIR=%buildroot install-dev
make -C test/binder-bridge DESTDIR=%buildroot install
make -C test/binder-list DESTDIR=%buildroot install
make -C test/binder-ping DESTDIR=%buildroot install
make -C test/binder-call DESTDIR=%buildroot install

%if_enabled tests
%check
make -C unit test
%endif

%files -n %{name}%{soname}
%_libdir/%name.so.*
%doc LICENSE README AUTHORS

%files devel
%dir %_includedir/gbinder
%_libdir/pkgconfig/*.pc
%_libdir/%name.so
%_includedir/gbinder/*.h

%files tools
%_bindir/binder-bridge
%_bindir/binder-list
%_bindir/binder-ping
%_bindir/binder-call

%changelog
* Thu Mar 30 2023 L.A. Kostis <lakostis@altlinux.ru> 1.1.33-alt0.1
- Initial build for ALTLinux.
