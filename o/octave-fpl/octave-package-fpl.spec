%define octave_pkg_version 1.2.0
%define octave_pkg_name fpl
%define octave_descr_name fpl
Name: octave-%octave_pkg_name
Version: 1.2.0
Release: alt1
Summary: Fem PLotting

Group: Sciences/Mathematics
License: GNU/GPL
Url: http://octave.sourceforge.net/

Source0: %octave_pkg_name-%version.tar.gz

BuildRequires: octave-devel
%if_with _octave_arch
BuildRequires: gcc-c++ libfftw3-devel libhdf5-devel liblapack-devel libncurses-devel libreadline-devel octave-devel
%else
BuildArch: noarch
%endif

# SystemRequirements: dx ( >= 4.3.2), sed, bash
BuildRequires: opendx >= 4.3.2 sed bash
# Depends: octave ( >= 3.0.0 )
Requires: octave >= 3.0.0
Provides: octave(fpl) = 1.2.0


%description
Octave-Forge - Extra packages for GNU Octave.
This package contains the %octave_descr_name GNU Octave extension.

Extension Description:
Collection of routines to save data in different graphical formats.

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
* Fri Nov 18 2011 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1
- initial import by octave-package-builder

