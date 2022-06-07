Name:     libxc
Version:  5.2.3
Release:  alt1

Summary:  Library of exchange-correlation functionals for density-functional theory
License:  MPL-2.0
Group:    Sciences/Chemistry
URL:      https://www.tddft.org/programs/libxc/
VCS:      https://gitlab.com/libxc/libxc

Packager: Andrey Cherepanov <cas@altlinux.org>

Source:   %name-%version.tar

BuildRequires: gcc-fortran

%description
Libxc is a library of exchange-correlation functionals for density-functional
theory. The aim is to provide a portable, well tested and reliable set of
exchange and correlation functionals that can be used by a variety of programs.

%package devel
Summary: Development files for %name
Group: Development/C

%description devel
%{summary}.

%prep
%setup

%build
%autoreconf
%configure \
    --enable-shared \
    --disable-static
%make_build

%install
%makeinstall_std

%files
%doc README.md AUTHORS
%_bindir/xc-info
%_bindir/xc-threshold
%_libdir/*.so.*

%files devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*.pc

%changelog
* Mon Jun 06 2022 Andrey Cherepanov <cas@altlinux.org> 5.2.3-alt1
- Initial build for Sisyphus.
