%define _unpackaged_files_terminate_build 1
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define	major 0
%define libname	libgarmin%major
%define develname libgarmin-devel

%define svn_ver svn320

Name: libgarmin
Version: 0.1.0
Release: alt3
Summary: Libgarmin is an open source (GPLv2) for Garmin image format maps.
License: GPLv2+
Group: Sciences/Geosciences
Url: http://libgarmin.sourceforge.net
Source: %name-%svn_ver.tar
Patch0:	libgarmin-shared.diff
Patch1:	libgarmin-0.1-automake-1.12.diff

# Automatically added by buildreq on Mon Dec 15 2008
BuildRequires: libGConf-devel rpm-build-java rpm-macros-fillup subversion

%description
Garmin is a leader in the gps navigation, so learn from
the best. Open source community is moving towards.
www.openstreetmap.org data. Understanding Garmin's format
will allow creation of Garmin compatible maps from OSM data
and creation/design of a new map format for OSM data.

%package utils
Summary: Various utlilities to manipulate Garmin image files
Group: File tools
Requires: %libname = %EVR
Conflicts: libgarmin < 0.1.0-alt3

%description utils
Libgarmin is a library used to parse IMG files from Garmin GPS devices.

This package contains various utlilities to manipulate Garmin image files.

%package -n %libname
Summary: C library to parse and use Garmin image files
Group: System/Libraries

%description -n	%libname
Libgarmin is a library used to parse IMG files from Garmin GPS devices.

This package contains the shared %{name} library.

%package -n %develname
Summary: Libraries and headers needed for developing with SynCE
Group: Development/C
Requires: %libname = %EVR
Conflicts: libgarmin < 0.1.0-alt3

%description -n %develname
Libraries and headers needed for developing with SynCE

%prep
%setup -q -n %name
%patch0 -p1
%patch1 -p1

%build
mkdir -p m4
autoreconf -fi
%configure \
    --disable-static

svn upgrade > /dev/null 2>&1 || :
%make

%install
%makeinstall

rm -rf %buildroot%_datadir/%name/doc

%files utils
%_bindir/gar*
%dir %_datadir/%name
%_datadir/%name/garmintypes.txt

%files -n %libname
%doc COPYING README TODO
%_libdir/*.so.%{major}
%_libdir/*.so.%{major}.*

%if_enabled static
%files devel-static
%_libdir/*.a
%endif

%files -n %develname
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*

%changelog
* Sun Dec 05 2021 Igor Vlasenko <viy@altlinux.org> 0.1.0-alt3
- fixed build
- shared libs policy

* Mon Mar 11 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.1.0-alt2.2
- Removed redundant BR: rpm-macros-xmms (fixes FTBFS).

* Thu Nov 28 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt2.1
- Fixed build

* Tue Apr 02 2013 Andrey Cherepanov <cas@altlinux.org> 0.1.0-alt2
- Fix build with new Subversion

* Mon Dec 15 2008 Grigory Milev <week@altlinux.ru> 0.1.0-alt1
- Initital build for ALT Linux
