Name: tcplay
Version: 2.0
Release: alt2

Summary: TrueCrypt implementation
License: BSD-2-Clause
Group: File tools
Url: https://github.com/bwalex/tc-play

Packager: Alexey Appolonov <alexey@altlinux.org>

# https://github.com/bwalex/tc-play/archive/v2.0.tar.gz
Source: %{name}-%{version}.tar

Patch1: %name-2.0-alt-glibc_update.patch

BuildRequires: libuuid-devel
BuildRequires: libdevmapper-devel
BuildRequires: libgcrypt-devel
BuildRequires: libssl-devel

%description
tcplay is a free (BSD-licensed), pretty much fully featured
(including multiple keyfiles, cipher cascades, etc)
and stable TrueCrypt implementation.

%package -n lib%{name}
Summary: Library to create/open/map TrueCrypt-compatible volumes
Group: System/Libraries
%description -n lib%{name}
The libtcplay library provides an API for creating and opening/mapping
TrueCrypt-compatible volumes.

%package -n %{name}-devel
Summary: Development files for libtcplay
Group: Development/C
Requires: lib%{name}
%description -n %{name}-devel
Files necessary to develop applications that use the libtcplay.

%prep
%setup
%patch1 -p2

%build
%make_build -f Makefile.classic PREFIX=%_prefix LIBDIR=%_libdir

%install
%makeinstall_std -f Makefile.classic PREFIX=%_prefix LIBDIR=%_libdir
rm %buildroot/%_libdir/lib%{name}.a

%files
%doc README.md LICENSE CHANGELOG
%_sbindir/%{name}
%_mandir/man3/%{name}.3.xz
%_mandir/man8/%{name}.8.xz

%files -n lib%{name}
%doc README.md LICENSE CHANGELOG
%_libdir/lib%{name}.so.2.0

%files -n %{name}-devel
%_includedir/%{name}_api.h
%_libdir/lib%{name}.so

%changelog
* Mon Nov 11 2019 Alexey Appolonov <alexey@altlinux.org> 2.0-alt2
- Build with glibc 2.30.

* Wed Aug 29 2018 Grigory Ustinov <grenka@altlinux.org> 2.0-alt1.1
- NMU: Rebuild with new openssl 1.1.0.

* Thu Nov 02 2017 Alexey Appolonov <alexey@altlinux.org> 2.0-alt1
- Initial ALT Linux release.
