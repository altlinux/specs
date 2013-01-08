# BEGIN SourceDeps(oneline):
BuildRequires: gcc-fortran
# END SourceDeps(oneline)
%def_with _octave_arch
%define octave_pkg_version 0.3.3
%define octave_pkg_name optiminterp
%define octave_descr_name optiminterp
Name: octave-%octave_pkg_name
Version: 0.3.3
Release: alt1
Summary: optiminterp

Group: Sciences/Mathematics
License: GPL version 2 or later
URL: http://octave.sf.net

Source0: %octave_pkg_name-%version.tar.gz

BuildRequires: octave-devel
%if_with _octave_arch
BuildRequires: gcc-c++ gcc-g77 libfftw3-devel libhdf5-devel liblapack-devel libncurses-devel libreadline-devel octave-devel
%else
BuildArch: noarch
%endif
Provides: octave(optiminterp) = %version
# Depends: octave (>= 2.9.9)
Requires: octave >= 2.9.9


%description
Octave-Forge - Extra packages for GNU Octave.
This package contains the %octave_descr_name GNU Octave extension.

Extension Description:
An optimal interpolation toolbox for octave. This package provides functions to perform a n-dimensional optimal interpolations of arbitrarily distributed data points.

%prep
%setup -n %octave_pkg_name

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
* Tue Jan 08 2013 Paul Wolneykien <manowar@altlinux.ru> 0.3.3-alt1
- updated by octave-package-builder

