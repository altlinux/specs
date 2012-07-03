%def_with _octave_arch
%define octave_pkg_name fl-core
%define octave_descr_name fl-core
Name: octave-%octave_pkg_name
Version: 1.0.0
Release: alt1
Summary: Fuzzy Logic Core for Octave

Group: Sciences/Mathematics
License: LGPL v3
Url: http://octave.sourceforge.net/

Source0: %octave_pkg_name-%version.tar.gz

BuildRequires: octave-devel
%if_with _octave_arch
BuildRequires: gcc-c++ libfftw3-devel libhdf5-devel liblapack-devel libncurses-devel libreadline-devel octave-devel
%else
BuildArch: noarch
%endif
# Depends: octave (>= 2.9.7)
Requires: octave >= 2.9.7
Provides: octave(fl-core) = 1.0.0


%description
Octave-Forge - Extra packages for GNU Octave.
This package contains the %octave_descr_name GNU Octave extension.

Extension Description:
The package contains code for basic functions in Fuzzy Logic for Octave.

%prep
%setup -n %octave_pkg_name

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
* Thu Nov 17 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1
- initial import by octave-package-builder

