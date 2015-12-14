Name: unibilium
Version: 1.2.0
Release: alt1

Summary: Unibilium is a very basic terminfo library
License: GPLv3
Group: System/Legacy libraries

Url: https://github.com/mauke/unibilium/
Source: %name-%version.tar
Patch0: libdir.patch
Packager:Konstantin Artyushkin <akv@altlinux.org>

#PreReq:
#Requires:
#Provides:
#Conflicts:

#BuildPreReq:
BuildRequires:perl-podlators
#BuildArch:

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
%patch 

%build
#%%configure
%make_build PREFIX=/usr 

%install
%makeinstall_std PREFIX=/usr 
#%%makeinstall 

%files
%doc  README LICENSE Changes
%_libdir/libunibilium.so.0
%_libdir/libunibilium.so.0.3.0
%_man3dir/unibi*

%files devel
%_includedir/unibilium.h
%_libdir/libunibilium.so
%_pkgconfigdir/unibilium.pc

%files devel-static
%_libdir/libunibilium.a

%changelog

* Mon Dec 14 2015 Konstantin Artyushkin <akv@altlinux.org> 1.2.0-alt1
- initial build for ALT Linux Sisyphus

