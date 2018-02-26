%def_with _octave_arch
%define octave_pkg_version 1.0.2
%define octave_pkg_name octproj
%define octave_descr_name OctPROJ
Name: octave-%octave_pkg_name
Version: 1.0.2
Release: alt1
Summary: GNU Octave bindings to PROJ.4

Group: Sciences/Mathematics
License: GPL version 3 or later (PROJ.4 is under MIT license)
URL: http://trac.osgeo.org/proj/

Source0: %octave_pkg_name-%version.tar.gz

BuildRequires: octave-devel
%if_with _octave_arch
BuildRequires: gcc-c++ libfftw3-devel libhdf5-devel liblapack-devel libncurses-devel libreadline-devel octave-devel
%else
BuildArch: noarch
%endif

# SystemRequirements: libproj-dev (>= 4.7.0) (Debian system)
BuildRequires: libproj-devel >= 4.7.0
# Depends: Octave (>= 2.9.7)
Requires: octave >= 2.9.7
Provides: octave(octproj) = 1.0.2


%description
Octave-Forge - Extra packages for GNU Octave.
This package contains the %octave_descr_name GNU Octave extension.

Extension Description:
This package allows to call functions of PROJ.4 library for

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
* Fri Nov 18 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1
- initial import by octave-package-builder

