%def_with _octave_arch
%define octave_pkg_name optim
%define octave_descr_name Optim
Name: octave-%octave_pkg_name
Version: 1.0.17
Release: alt1
Summary: Optimzation.

Group: Sciences/Mathematics
License: GPL version 2 or later and GFDL
URL: http://octave.sf.net

Source0: %octave_pkg_name-%version.tar.gz

BuildRequires: octave-devel
%if_with _octave_arch
BuildRequires: gcc-c++ libfftw3-devel libhdf5-devel liblapack-devel libncurses-devel libreadline-devel octave-devel
%else
BuildArch: noarch
%endif
# Depends: octave (>= 2.9.7), miscellaneous (>= 1.0.10), struct (>= 1.0.9)
Requires: octave >= 2.9.7 octave(miscellaneous) >= 1.0.10 octave(struct) >= 1.0.9
Provides: octave(optim) = 1.0.17


%description
Octave-Forge - Extra packages for GNU Octave.
This package contains the %octave_descr_name GNU Octave extension.

Extension Description:
Non-linear optimization toolkit.

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
* Thu Nov 17 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.17-alt1
- initial import by octave-package-builder

