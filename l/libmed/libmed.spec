Name:     libmed
Version:  3.3.1
Release:  alt1

Summary:  Library to store and exchange meshed data or computation result in MED format
License:  GPLv3 and LGPLv3
Group:    System/Libraries
Url:      https://www.salome-platform.org/downloads/current-version

Packager: Andrey Cherepanov <cas@altlinux.org>

Source:   med-%version.tar

BuildRequires: gcc-c++
BuildRequires: libhdf5-devel
BuildRequires: hdf5-8-tools
BuildRequires: gcc-fortran

%description
Library to store and exchange meshed data or computation result in MED format.

%package devel
Group: Development/C
Summary: Development files for libmed

%description devel
Development files for libmed.

%package tools
Group: Development/C
Summary: Utilities for work with MED format

%description tools
Utilities for work with MED format.

%prep
%setup -n med-%{version}_SRC

%build
%undefine _configure_gettext
%autoreconf
%configure --disable-static \
           --disable-python
%make_build

%install
%makeinstall_std
rm -f %buildroot%_libdir/*.la
rm -rf %buildroot%_datadir/doc/med

%check
%make_build check

%files
%doc AUTHORS README
%_libdir/*.so.*
%_libdir/libmed3.settings

%files devel
%_libdir/*.so
%_includedir/*

%files tools
%_bindir/*

%changelog
* Wed Apr 25 2018 Andrey Cherepanov <cas@altlinux.org> 3.3.1-alt1
- Initial build in Sisyphus.
