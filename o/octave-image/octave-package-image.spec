%def_with _octave_arch
%define octave_pkg_name image
%define octave_descr_name Image
Name: octave-%octave_pkg_name
Version: 1.0.15
Release: alt1
Summary: Image Processing

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
# Depends: octave (>= 3.2.0)
Requires: octave >= 3.2.0
Provides: octave(image) = 1.0.15


%description
Octave-Forge - Extra packages for GNU Octave.
This package contains the %octave_descr_name GNU Octave extension.

Extension Description:
The Octave-forge Image package provides functions for

%prep
%setup -n %octave_pkg_name-%version

%build
octave -q -H --no-site-file --eval "pkg build -nodeps . %SOURCE0"

%install
mkdir -p %buildroot%_datadir/octave/packages
mkdir -p %buildroot%_libdir/octave/packages
octave -q -H --no-site-file --eval "pkg prefix %buildroot%_datadir/octave/packages %buildroot%_libdir/octave/packages; pkg install -local -nodeps %octave_pkg_name-%version.tar.gz"

%files
%_datadir/octave/packages/%octave_pkg_name-%version
%if_with _octave_arch
%_libdir/octave/packages/%octave_pkg_name-%version
%endif

%changelog
* Thu Nov 17 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.15-alt1
- initial import by octave-package-builder

