%def_with _octave_arch
%define octave_pkg_version 1.3.7
%define octave_pkg_name nurbs
%define octave_descr_name Nurbs
Name: octave-%octave_pkg_name
Version: 1.3.7
Release: alt1
Summary: Nurbs.

Group: Sciences/Mathematics
License: GPLv3+
URL: http://octave.sf.net

Source0: %octave_pkg_name-%version.tar.gz

BuildRequires: octave-devel
%if_with _octave_arch
BuildRequires: gcc-c++ gcc-g77 libfftw3-devel libhdf5-devel liblapack-devel libncurses-devel libreadline-devel octave-devel
%else
BuildArch: noarch
%endif
Provides: octave(nurbs) = %version
# Depends: octave (>= 3.2)
Requires: octave >= 3.2


%description
Octave-Forge - Extra packages for GNU Octave.
This package contains the %octave_descr_name GNU Octave extension.

Extension Description:
Collection of routines for the creation, and manipulation of Non-Uniform Rational B-Splines (NURBS), based on the NURBS toolbox by Mark Spink.

%prep
%setup -c -n %name-%version

%build
tar czf ../%octave_pkg_name-%version.tar.gz *
rm -rf *
octave -q -H --no-site-file --eval "pkg build -nodeps . ../%octave_pkg_name-%version.tar.gz"

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
* Wed Jul 02 2014 Paul Wolneykien <manowar@altlinux.ru> 1.3.7-alt1
- updated by octave-package-builder

