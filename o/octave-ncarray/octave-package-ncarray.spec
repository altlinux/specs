%define octave_pkg_version 1.0.0
%define octave_pkg_name ncarray
%define octave_descr_name ncArray
Name: octave-%octave_pkg_name
Version: 1.0.0
Release: alt1
Summary: ncArray

Group: Sciences/Mathematics
License: GPLv2+
URL: http://octave.sf.net

Source0: %octave_pkg_name-%version.tar.gz

BuildRequires: octave-devel
%if_with _octave_arch
BuildRequires: gcc-c++ gcc-g77 libfftw3-devel libhdf5-devel liblapack-devel libncurses-devel libreadline-devel octave-devel
%else
BuildArch: noarch
%endif
Provides: octave(ncarray) = %version
# Depends: octave (>= 3.4.0), octcdf (>= 1.1.5)
Requires: octave >= 3.4.0 octave(octcdf) >= 1.1.5


%description
Octave-Forge - Extra packages for GNU Octave.
This package contains the %octave_descr_name GNU Octave extension.

Extension Description:
Access a single or a collection of NetCDF files as a multi-dimensional array

%prep
%setup -n ncArray

%build
octave -q -H --no-site-file --eval "pkg build -nodeps . %SOURCE0"

%install
mkdir -p %buildroot%_datadir/octave/packages
mkdir -p %buildroot%_libdir/octave/packages
octave -q -H --no-site-file --eval "pkg prefix %buildroot%_datadir/octave/packages %buildroot%_libdir/octave/packages; pkg install -local -nodeps %octave_pkg_name-%octave_pkg_version.tar.gz"

%files
%_datadir/octave/packages/%octave_pkg_name-%octave_pkg_version
%if_with _octave_arch
%_libdir/octave/packages/%octave_pkg_name-%octave_pkg_version
%endif

%changelog
* Tue Jan 08 2013 Paul Wolneykien <manowar@altlinux.ru> 1.0.0-alt1
- updated by octave-package-builder

