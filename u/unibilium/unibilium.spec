Name: unibilium
Version: 2.0.0
Release: alt1

Summary: Unibilium is a very basic terminfo library
License: GPLv3
Group: System/Legacy libraries

Url: https://github.com/mauke/unibilium/
Source: %name-%version.tar
Packager:Konstantin Artyushkin <akv@altlinux.org>

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  libtool
# For docs
BuildRequires:  %{_bindir}/pod2man
# For tests
BuildRequires:  %{_bindir}/prove

%description
Unibilium is a very basic terminfo library. It doesn't depend on curses
or any other library. It also doesn't use global variables, so it should
be thread-safe.

%package devel
Summary: Headers for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
Headers for building software that uses %name

%package devel-static
Summary: Static libraries for %name
Group: Development/C
Requires: %name-devel = %version-%release

%description devel-static
Static libs for building statically linked software that uses %name

%prep
%setup

%build
%make_build PREFIX=%{_prefix} LIBDIR=%{_libdir}

%install
%makeinstall_std PREFIX=%{_prefix} LIBDIR=%{_libdir}

%check
make test

%files
%doc README.md LICENSE Changes
%_libdir/lib%name.so.*
%_man3dir/*

%files devel
%_includedir/*
%_libdir/lib%name.so
%_pkgconfigdir/%name.pc

%files devel-static
%_libdir/lib%name.a

%changelog
* Wed Jul 10 2018 Vladimir Didenko <cow@altlinux.org> 2.0.0-alt1
- new version

* Mon Dec 14 2015 Konstantin Artyushkin <akv@altlinux.org> 1.2.0-alt1
- initial build for ALT Linux Sisyphus
