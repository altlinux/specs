# BEGIN SourceDeps(oneline):
BuildRequires: gcc-fortran makeinfo
# END SourceDeps(oneline)
%def_with _octave_arch
%define octave_pkg_version 0.2.3
%define octave_pkg_name tisean
%define octave_descr_name TISEAN
Name: octave-%octave_pkg_name
Version: 0.2.3
Release: alt1
Summary: Nonlinear Time Series Analysis.

Group: Sciences/Mathematics
License: GPLv3+
URL: https://bitbucket.org/josiah425/tisean

Source0: http://downloads.sourceforge.net/octave/%{octave_pkg_name}-%{octave_pkg_version}.tar.gz

BuildRequires: octave-devel
%if_with _octave_arch
BuildRequires: gcc-c++ gcc-g77 libfftw3-devel libhdf5-devel liblapack-devel libncurses-devel libreadline-devel
%else
BuildArch: noarch
%endif
Provides: octave(tisean) = %version
# Depends: octave (>= 4.0.0), signal (>= 1.3.0)
Requires: octave >= 4.0.0 octave(signal) >= 1.3.0


%description
Octave-Forge - Extra packages for GNU Octave.
This package contains the %octave_descr_name GNU Octave extension.

Extension Description:
Port of TISEAN 3.0.1

%prep
%setup -q -n %{octave_pkg_name}-%{octave_pkg_version}

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
* Wed Apr 13 2016 Igor Vlasenko <viy@altlinux.ru> 0.2.3-alt1
- initial import by package builder

