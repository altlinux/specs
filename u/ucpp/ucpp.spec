Name: ucpp
Version: 1.3.5
Release: alt1

Summary: C preprocessor compliant to ISO C99
License: BSD
Group: Development/C

Url: http://gitlab.com/scarabeusiv/ucpp
Source: %name-%version.tar
Packager: Michael Shigorin <mike@altlinux.org>

%description
A C preprocessor is a part of a C compiler responsible for macro
replacement, conditional compilation and inclusion of header files.
It is often found as a stand-alone program on Unix systems.

ucpp is such a preprocessor; it is designed to be quick and light,
but anyway fully compliant to the ISO standard 9899:1999, also known
as C99. ucpp can be compiled as a stand-alone program, or linked
to some other code; in the latter case, ucpp will output tokens,
one at a time, on demand, as an integrated lexer.

%define soname 13
%define libname lib%name%soname
%define devname lib%name-devel

%package -n %libname
Summary: Shared library for C preprocessor compliant to ISO C99
Group: System/Libraries

%description -n %libname
This package contains shared library for %name.

%package -n %devname
Summary: Development headers for lib%name
Group: Development/C

%description -n %devname
This package contains development headers for for lib%name.

%prep
%setup
iconv -f iso8859-1 -t utf-8 < README > README.utf8 &&
touch -r README.utf8 README &&
mv README.utf8 README

%build
%autoreconf
%configure --disable-rpath --disable-static --disable-werror
%make_build

%install
%makeinstall_std

%files
%_bindir/*
%_man1dir/*
%doc AUTHORS ChangeLog* COPYING README*

%files -n %libname
%_libdir/*.so.*

%files -n %devname
%_includedir/lib%name
%_libdir/*.so
%_pkgconfigdir/*.pc


%changelog
* Sun Jun 09 2024 Michael Shigorin <mike@altlinux.org> 1.3.5-alt1
- initial release (spec based on mageia and opensuse ones)
