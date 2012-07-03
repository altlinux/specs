%define octave_pkg_version 0.3.2
%define octave_pkg_name financial
%define octave_descr_name financial
Name: octave-%octave_pkg_name
Version: 0.3.2
Release: alt1
Summary: Financial

Group: Sciences/Mathematics
License: GPL version 3 and GPL version 2 or later
URL: http://octave.sf.net

Source0: %octave_pkg_name-%version.tar.gz

BuildRequires: octave-devel
%if_with _octave_arch
BuildRequires: gcc-c++ libfftw3-devel libhdf5-devel liblapack-devel libncurses-devel libreadline-devel octave-devel
%else
BuildArch: noarch
%endif
Provides: octave(financial) = %version
# Depends: octave (>= 3.0.0), time (>= 1.0.5), miscellaneous (>= 1.0.6)
Requires: octave >= 3.0.0 octave(time) >= 1.0.5 octave(miscellaneous) >= 1.0.6


%description
Octave-Forge - Extra packages for GNU Octave.
This package contains the %octave_descr_name GNU Octave extension.

Extension Description:
Financial manipulation and plotting functions

%prep
%setup -n %octave_pkg_name-%version

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
* Mon Nov 28 2011 Igor Vlasenko <viy@altlinux.ru> 0.3.2-alt1
- initial import by octave-package-builder

