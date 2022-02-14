Name: libspnav
Version: 0.3
Release: alt1
Summary: Open source alternative to 3DConnextion drivers

License: BSD
Group: System/Libraries
URL: http://spacenav.sourceforge.net/
Vcs: https://github.com/FreeSpacenav/libspnav
Source: %name-%version.tar

BuildRequires:  libX11-devel

%description
The spacenav project provides a free, compatible alternative to the
proprietary 3Dconnexion device driver and SDK, for their 3D input
devices (called "space navigator", "space pilot", "space traveller",
etc).

This package provides the library needed for applications to connect to
the user land daemon.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
Development files for %name.

%prep
%setup -q
#patch0 -p1

%build
# Set libdir properly
sed -i "s/libdir=lib/libdir=%_lib/g" configure
%configure 
sed -i "s/CFLAGS =/CFLAGS +=/g" Makefile
%make_build

%install
%makeinstall_std

# Remove static library
rm -f %buildroot%_libdir/%name.a

%files
%doc README.md
%_libdir/*.so.0*

%files devel
%doc examples
%_libdir/*.so
%_includedir/*.h

%changelog
* Mon Feb 14 2022 Andrey Cherepanov <cas@altlinux.org> 0.3-alt1
- New version.
- Build from upstream git tag.

* Wed Jul 13 2016 Andrey Cherepanov <cas@altlinux.org> 0.2.3-alt1
- Initial buuld in Sisyphus (based on spec from Fedora)

