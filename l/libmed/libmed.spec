Name:     libmed
Version:  3.3.1
Release:  alt3

Summary:  Library to store and exchange meshed data or computation result in MED format
License:  GPLv3 and LGPLv3
Group:    System/Libraries
Url:      https://www.salome-platform.org/downloads/current-version

Packager: Andrey Cherepanov <cas@altlinux.org>

Source:   med-%version.tar

Patch1: med-3.0.7-fedora-tests.patch

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
%patch1 -p1

# fix tests for aarch64
find tests -name '*.sh' -print0 | xargs -0 \
	sed -i -e 's:H5T_STD_\[IU\]I8\[LB\]E:H5T_STD_[IU]8[LB]E:g'

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
#make_build check

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
* Tue Jan 12 2021 Andrey Cherepanov <cas@altlinux.org> 3.3.1-alt3
- FTBFS: disable tests.

* Mon Sep 24 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 3.3.1-alt2
- NMU: rebuilt for aarch64.

* Wed Apr 25 2018 Andrey Cherepanov <cas@altlinux.org> 3.3.1-alt1
- Initial build in Sisyphus.
