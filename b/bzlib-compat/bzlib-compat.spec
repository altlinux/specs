Name: bzlib-compat
Version: 1.0.8
Release: alt1

Summary: Compatibility symlink for the upstream bzip2 soname libbz2.so.1.0
Summary(ru_RU.UTF-8): Симлинк совместимости для апстримного soname bzip2 libbz2.so.1.0
License: bzip2-1.0.6
Group: System/Libraries
Url: https://bugzilla.altlinux.org/35320

Requires: bzlib

# Compat dependency for binaries built against the upstream soname
# libbz2.so.1.0 (our soname is libbz2.so.1), see #35320.
%if "%_lib" == "lib64"
%define hacked_lib_suffix ()(64bit)
%else
%define hacked_lib_suffix %nil
%endif
Provides: libbz2.so.1.0%hacked_lib_suffix

%description
The upstream bzip2 library uses soname libbz2.so.1.0, while ALT Linux
builds it with soname libbz2.so.1.  This package provides a compatibility
symlink libbz2.so.1.0 -> libbz2.so.1 so that foreign binaries (proprietary
applications, Debian/Ubuntu builds) linked against the upstream soname can
be loaded without modifying the main bzlib package.

%description -l ru_RU.UTF-8
Апстримная библиотека bzip2 использует soname libbz2.so.1.0, тогда как в
ALT Linux она собирается с soname libbz2.so.1.  Этот пакет добавляет симлинк
совместимости libbz2.so.1.0 -> libbz2.so.1, чтобы сторонние бинарники
(проприетарные приложения, сборки Debian/Ubuntu), слинкованные с апстримным
soname, могли загружаться без изменения основного пакета bzlib.

%install
# This package ships no files of its own.  The compat symlink
# libbz2.so.1.0 -> libbz2.so.1 would be dangling at build time (its target is
# owned by bzlib) and ldconfig (048-adjust_libraries.brp) drops it from the
# buildroot; %%ghost in turn requires the file to exist at build time.  So the
# symlink is created from scriptlets, and the soname is declared via Provides.
mkdir -p %buildroot

%post
ln -snf libbz2.so.1 /%_lib/libbz2.so.1.0

%postun
if [ "$1" = 0 ]; then
	rm -f /%_lib/libbz2.so.1.0
fi

%files

%changelog
* Sat Jun 13 2026 Vitaly Lipatov <lav@altlinux.ru> 1.0.8-alt1
- Initial build: libbz2.so.1.0 compat symlink (closes: #35320).
