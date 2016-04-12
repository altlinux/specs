Serial: 1
%define octave_pkg_version 1.3.0
%define octave_pkg_name data-smoothing
%define octave_descr_name data-smoothing
Name: octave-%octave_pkg_name
Version: 1.3.0
Release: alt2
Summary: Data smoothing

Group: Sciences/Mathematics
License: GPL version 3 or later
URL: http://octave.sf.net

Source0: http://downloads.sourceforge.net/octave/%{octave_pkg_name}-%{octave_pkg_version}.tar.gz

BuildRequires: octave-devel
%if_with _octave_arch
BuildRequires: gcc-c++ gcc-g77 libfftw3-devel libhdf5-devel liblapack-devel libncurses-devel libreadline-devel octave-devel
%else
BuildArch: noarch
%endif
Provides: octave(data-smoothing) = %version
# Depends: octave (>= 3.6.0), optim (>= 1.0.3)
Requires: octave >= 3.6.0 octave(optim) >= 1.0.3


%description
Octave-Forge - Extra packages for GNU Octave.
This package contains the %octave_descr_name GNU Octave extension.

Extension Description:
Algorithms for smoothing noisy data

%prep
%setup -q -n %{octave_pkg_name}

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
* Tue Apr 12 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.3.0-alt2
- initial import by package builder

