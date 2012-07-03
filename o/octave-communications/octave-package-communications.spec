%def_with _octave_arch
%define octave_pkg_version 1.1.0
%define octave_pkg_name communications
%define octave_descr_name Communications
Name: octave-%octave_pkg_name
Version: 1.1.0
Release: alt1
Summary: Communications.

Group: Sciences/Mathematics
License: GPL version 2 or later
URL: http://octave.sf.net

Source0: %octave_pkg_name-%version.tar.gz

BuildRequires: octave-devel
%if_with _octave_arch
BuildRequires: gcc-c++ libfftw3-devel libhdf5-devel liblapack-devel libncurses-devel libreadline-devel octave-devel
%else
BuildArch: noarch
%endif
# Depends: octave (>= 3.4), signal (>= 1.0.0), image
Requires: octave >= 3.4 octave(signal) >= 1.0.0 octave(image)
Provides: octave(communications) = 1.1.0


%description
Octave-Forge - Extra packages for GNU Octave.
This package contains the %octave_descr_name GNU Octave extension.

Extension Description:
Digital Communications, Error Correcting Codes (Channel Code), Source Code functions, Modulation and Galois Fields

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
* Fri Nov 18 2011 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1
- initial import by octave-package-builder

