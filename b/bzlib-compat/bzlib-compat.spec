Name: bzlib-compat
Version: 1.0.8
Release: alt2

Summary: Compatibility symlink for the upstream bzip2 soname libbz2.so.1.0
Summary(ru_RU.UTF-8): Симлинк совместимости для апстримного soname bzip2 libbz2.so.1.0
License: bzip2-1.0.6
Group: System/Libraries
Url: https://bugzilla.altlinux.org/35320

Requires: bzlib
# bzlib must be present in the build root so the absolute compat symlink is not
# dangling at build time, otherwise ldconfig (048-adjust_libraries.brp) drops it.
BuildRequires: bzlib

# Compat dependency for binaries built against the upstream soname
# libbz2.so.1.0 (our soname is libbz2.so.1), see #35320.
%if "%_lib" == "lib64"
%define hacked_lib_suffix ()(64bit)
%else
%define hacked_lib_suffix %nil
%endif
Provides: libbz2.so.1.0%hacked_lib_suffix

# The packaged symlink makes rpm auto-require its target /%_lib/libbz2.so.1,
# which rpm canonicalizes to /usr/lib64 (usrmerge) and does not match bzlib's
# literal /lib64 file provide.  The dependency is already covered by
# Requires: bzlib, so drop the redundant file requirement.
%filter_from_requires /libbz2\.so\.1$/d

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
mkdir -p %buildroot/%_lib
# Use an absolute target: a relative symlink would resolve inside the (empty)
# buildroot and ldconfig (048-adjust_libraries.brp) would drop it as dangling.
# With BuildRequires: bzlib the absolute target exists, so the link survives the
# build and is shipped as a normal, rpm-owned file.
ln -s /%_lib/libbz2.so.1 %buildroot/%_lib/libbz2.so.1.0

%files
/%_lib/libbz2.so.1.0

%changelog
* Sat Jun 27 2026 Vitaly Lipatov <lav@altlinux.ru> 1.0.8-alt2
- Ship the compat symlink as a packaged file instead of via scriptlets.

* Sat Jun 13 2026 Vitaly Lipatov <lav@altlinux.ru> 1.0.8-alt1
- Initial build: libbz2.so.1.0 compat symlink (closes: #35320).
