%define git 2543519
%define soname 2
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: trio
Version: 1.17.1
Release: alt1.g%{git}

Summary: Portable and extendable printf and string functions
Group: System/Libraries
License: 0BSD
Url: https://daniel.haxx.se/projects/trio
Vcs: https://github.com/orbea/trio

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: gcc

%description
Trio is a fully matured and stable set of printf and string functions
designed be used by applications with focus on portability or with
the need for additional features that are not supported by standard
stdio implementation.

%package -n lib%{name}%{soname}
Summary: Portable and extendable printf and string functions
Group: System/Libraries

%description -n lib%{name}%{soname}
Trio is a fully matured and stable set of printf and string functions
designed be used by applications with focus on portability or with
the need for additional features that are not supported by standard
stdio implementation.

%package devel
Summary: development libraries and headers for %name
Group: Development/C

%description devel
Development libraries and headers for %name

%prep
%setup
%patch -p1

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std
rm -rf %buildroot{%_libdir/lib%{name}.a,%_docdir/%name}

%files -n lib%{name}%{soname}
%doc README CHANGES LICENSE
%_libdir/lib%{name}*.so.%{soname}*

%files devel
%_libdir/lib%{name}.so
%_includedir/*.h
%_libdir/pkgconfig/*.pc

%changelog
* Wed Jan 28 2026 L.A. Kostis <lakostis@altlinux.ru> 1.17.1-alt1.g2543519
- Initial build for ALTLinux.

