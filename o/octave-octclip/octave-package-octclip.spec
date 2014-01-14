%def_with _octave_arch
%define octave_pkg_version 1.0.3
%define octave_pkg_name octclip
%define octave_descr_name OctCLIP
Name: octave-%octave_pkg_name
Version: 1.0.3
Release: alt2
Summary: GNU Octave clipping polygons tool

Group: Sciences/Mathematics
License: GPLv3+, modified BSD
URL: http://davis.wpi.edu/~matt/courses/clipping/

Source0: %octave_pkg_name-%version.tar.gz

BuildRequires: octave-devel
%if_with _octave_arch
BuildRequires: gcc-c++ gcc-g77 libfftw3-devel libhdf5-devel liblapack-devel libncurses-devel libreadline-devel octave-devel
%else
BuildArch: noarch
%endif
Provides: octave(octclip) = %version
# Depends: Octave (>= 2.9.7)
Requires: octave >= 2.9.7


%description
Octave-Forge - Extra packages for GNU Octave.
This package contains the %octave_descr_name GNU Octave extension.

Extension Description:
This package allows to do boolean operations with polygons using

%prep
%setup -T -c %name-%version

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
* Tue Jan 14 2014 Paul Wolneykien <manowar@altlinux.ru> 1.0.3-alt2
- Rebuild with the next version of Octave: 3.8.0

* Thu Oct 10 2013 Paul Wolneykien <manowar@altlinux.ru> 1.0.3-alt1
- updated by octave-package-builder

* Fri Nov 18 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1
- initial import by octave-package-builder

