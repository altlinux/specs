Serial: 1
%define octave_pkg_version 1.0.0
%define octave_pkg_name physicalconstants
%define octave_descr_name PhysicalConstants
Name: octave-%octave_pkg_name
Version: 1.0.0
Release: alt1
Summary: Physical Constants

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
Provides: octave(physicalconstants) = %version
# Depends: miscellaneous (>= 1.2.0)
Requires: octave(miscellaneous) >= 1.2.0


%description
Octave-Forge - Extra packages for GNU Octave.
This package contains the %octave_descr_name GNU Octave extension.

Extension Description:
Physical Constants from Atomic & Molecular Physics, taken from NIST

%prep
%setup -n physical-constants

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
* Tue Jan 08 2013 Paul Wolneykien <manowar@altlinux.ru> 1:1.0.0-alt1
- updated by octave-package-builder

* Mon Nov 28 2011 Igor Vlasenko <viy@altlinux.ru> 0.1.7-alt1
- initial import by octave-package-builder

