# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/python makeinfo
# END SourceDeps(oneline)
%define octave_pkg_version 2.3.0
%define octave_pkg_name symbolic
%define octave_descr_name symbolic
Name: octave-%octave_pkg_name
Version: 2.3.0
Release: alt1
Summary: Octave Symbolic Package using SymPy

Group: Sciences/Mathematics
License: GPL-3.0+
URL: http://github.com/cbm755/octsympy

Source0: http://downloads.sourceforge.net/octave/%{octave_pkg_name}-%{octave_pkg_version}.tar.gz

BuildRequires: octave-devel
%if_with _octave_arch
BuildRequires: gcc-c++ gcc-g77 libfftw3-devel libhdf5-devel liblapack-devel libncurses-devel libreadline-devel
%else
BuildArch: noarch
%endif
Provides: octave(symbolic) = %version

# SystemRequirements: python, sympy (>= 0.7.5)
BuildRequires: python sympy >= 0.7.5

# octave module BuildRequires: python, sympy (>= 0.7.5)
BuildRequires: python sympy >= 0.7.5
# Depends: octave (>= 3.8)
Requires: octave >= 3.8


%description
Octave-Forge - Extra packages for GNU Octave.
This package contains the %octave_descr_name GNU Octave extension.

Extension Description:
The Octave-Forge Symbolic package adds symbolic calculation

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
* Wed Apr 13 2016 Igor Vlasenko <viy@altlinux.ru> 2.3.0-alt1
- initial import by package builder

