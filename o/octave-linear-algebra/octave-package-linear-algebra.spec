Serial: 1
%def_with _octave_arch
%define octave_pkg_version 2.2.0
%define octave_pkg_name linear-algebra
%define octave_descr_name Linear-algebra
Name: octave-%octave_pkg_name
Version: 2.2.0
Release: alt1
Summary: Linear algebra.

Group: Sciences/Mathematics
License: GPLv3+, LGPLv3+, FreeBSD
URL: http://octave.sf.net

Source0: %octave_pkg_name-%version.tar.gz

BuildRequires: octave-devel
%if_with _octave_arch
BuildRequires: gcc-c++ gcc-g77 libfftw3-devel libhdf5-devel liblapack-devel libncurses-devel libreadline-devel octave-devel
%else
BuildArch: noarch
%endif
Provides: octave(linear-algebra) = %version
# Depends: octave (>= 3.2.3), general (>= 1.3.0)
Requires: octave >= 3.2.3 octave(general) >= 1.3.0


%description
Octave-Forge - Extra packages for GNU Octave.
This package contains the %octave_descr_name GNU Octave extension.

Extension Description:
Additional linear algebra code, including general SVD and matrix functions.

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
* Tue Jan 08 2013 Paul Wolneykien <manowar@altlinux.ru> 1:2.2.0-alt1
- updated by octave-package-builder

* Thu Nov 17 2011 Igor Vlasenko <viy@altlinux.ru> 2.1.0-alt1
- initial import by octave-package-builder

