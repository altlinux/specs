Name: routino
Version: 3.4.1
Release: alt1
Summary: Router for OpenStreetMap Data
License: AGPL-3.0
Group: Sciences/Geosciences
Url: http://routino.org/
Source0: %name-%version.tar

Patch0: routino-3.3.2-fedora-alt-fix-configuration.patch

# Automatically added by buildreq on Sun Apr 12 2020
# optimized out: glibc-kernheaders-generic glibc-kernheaders-x86 perl python2-base sh4
BuildRequires: bzlib-devel liblzma-devel zlib-devel

%description
Routino is an application for finding a route between two points using
the dataset of topographical information collected by OpenStreetMap.

%package data
Summary: Data files for routino and libroutino.
Group: Sciences/Geosciences
BuildArch: noarch

%description data
This package contains the architecture-independent data files used by routino
and libroutino.

%package doc
Summary: Documentation files for routino and libroutino.
Group: Documentation
BuildArch: noarch

%description doc
This package contains the architecture-independent documentation files for
routino and libroutino.

%package -n libroutino0
Summary: Routing library for OpenStreetMap Data
Group: System/Libraries
Requires: %name-data = %EVR

%description -n libroutino0
The Routino library is a library for finding a route between two points using
the dataset of topographical information collected by OpenStreetMap.

%package -n libroutino-slim0
Summary: Routing library for OpenStreetMap Data
Group: System/Libraries
Requires: %name-data = %EVR

%description -n libroutino-slim0
The Routino library is a library for finding a route between two points using
the dataset of topographical information collected by OpenStreetMap.

%package -n libroutino-devel
Summary: Development files for %{name}-libs
Group: Development/C
Requires: libroutino0 = %EVR
Requires: libroutino-slim0 = %EVR

%description -n libroutino-devel
This package contains the files required to compile applications that use
libroutino or libroutino-slim.


%define docdir %_defaultdocdir/%name-%version

%prep
%setup
%patch -p1

%build
export CFLAGS="%optflags" LDFLAGS="%optflags"
%make_build libdir=%_libdir docdir=%docdir

%install
%makeinstall_std libdir=%_libdir docdir=%docdir

%define _unpackaged_files_terminate_build 1

%check
make test

%files
%_bindir/*

%files data
%_datadir/%name/

%files doc
%docdir

%files -n libroutino0
%_libdir/libroutino.so.*

%files -n libroutino-slim0
%_libdir/libroutino-slim.so.*

%files -n libroutino-devel
%_includedir/%name.h
%_libdir/lib%{name}*.so

%changelog
* Sun Aug 20 2023 Gleb F-Malinovskiy <glebfm@altlinux.org> 3.4.1-alt1
- Updated to 3.4.1.

* Sat Mar 27 2021 Gleb F-Malinovskiy <glebfm@altlinux.org> 3.3.3-alt1
- Updated to 3.3.3.

* Sun Apr 12 2020 Gleb F-Malinovskiy <glebfm@altlinux.org> 3.3.2-alt1
- Updated to 3.3.2.

* Sat Nov 19 2011 Egor Glukhov <kaman@altlinux.org> 2.1.2-alt1
- New version

* Tue Nov 23 2010 Egor Glukhov <kaman@altlinux.org> 1.5.1-alt1
- Initial build for Sisyphus
