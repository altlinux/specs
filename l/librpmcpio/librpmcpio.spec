Name: librpmcpio
Version: 0.3
Release: alt1

Summary: Read cpio archive of .rpm packages
License: MIT
Group: System/Libraries

URL: https://github.com/svpv/rpmcpio
Source: %name-%version.tar

# Automatically added by buildreq on Sun Mar 04 2018
BuildRequires: librpm-devel

%package devel
Summary: Read cpio archive of .rpm packages
Group: System/Libraries
Requires: %name = %version-%release

%description
The rpmcpio library provides a simple API for reading the cpio archive
of .rpm packages.  Packaged files can be iterated and looked into.

%description devel
The rpmcpio library provides a simple API for reading the cpio archive
of .rpm packages.  Packaged files can be iterated and looked into.

%prep
%setup -q

%build
make

%install
mkdir -p %buildroot%_libdir
cp -av librpmcpio.so* %buildroot%_libdir
install -pD -m644 rpmcpio.h %buildroot%_includedir/rpmcpio.h

%files
%_libdir/librpmcpio.so.*

%files devel
%doc README.md example.c
%_includedir/rpmcpio.h
%_libdir/librpmcpio.so

%changelog
* Tue Mar 06 2018 Alexey Tourbin <at@altlinux.ru> 0.3-alt1
- fixed support for 2G+ payloads
- implemented verification of hardlink sets

* Sun Mar 04 2018 Alexey Tourbin <at@altlinux.ru> 0.2-alt1
- first beta release
- ported to the new rpm API
