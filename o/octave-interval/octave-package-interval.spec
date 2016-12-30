# BEGIN SourceDeps(oneline):
BuildRequires: makeinfo texinfo
# END SourceDeps(oneline)
%def_with _octave_arch
%define octave_pkg_version 2.0.0
%define octave_pkg_name interval
%define octave_descr_name interval
Name: octave-%octave_pkg_name
Version: 2.0.0
Release: alt1
Summary: Real-valued interval arithmetic

Group: Sciences/Mathematics
License: GPL-3.0+
Url: http://octave.sourceforge.net/

Source0: http://downloads.sourceforge.net/octave/%{octave_pkg_name}-%{octave_pkg_version}.tar.gz

BuildRequires: octave-devel
%if_with _octave_arch
BuildRequires: gcc-c++ gcc-g77 libfftw3-devel libhdf5-devel liblapack-devel libncurses-devel libreadline-devel
%else
BuildArch: noarch
%endif
Provides: octave(interval) = %version

# SystemRequirements: mpfr (>= 3.1.0) [Debian] libmpfr4 (>= 3.1.0)
BuildRequires: libmpfr-devel >= 3.1.0 libmpfr4 >= 3.1.0

# octave module BuildRequires: mpfr (>= 3.1.0) [Debian] libmpfr-dev (>= 3.1.0)
BuildRequires: libmpfr-devel >= 3.1.0 libmpfr-devel >= 3.1.0
# Depends: octave (>= 3.8.0)
Requires: octave >= 3.8.0


%description
Octave-Forge - Extra packages for GNU Octave.
This package contains the %octave_descr_name GNU Octave extension.

Extension Description:
The interval package for real-valued interval arithmetic allows

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
* Fri Dec 30 2016 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt1
- regenerated from template by package builder

* Tue Sep 27 2016 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1
- regenerated from template by package builder

* Wed Apr 13 2016 Igor Vlasenko <viy@altlinux.ru> 1.4.1-alt1
- initial import by package builder

