# BEGIN SourceDeps(oneline):
BuildRequires: makeinfo
# END SourceDeps(oneline)
%def_with _octave_arch
%define octave_pkg_version 0.5.0
%define octave_pkg_name doctest
%define octave_descr_name doctest
Name: octave-%octave_pkg_name
Version: 0.5.0
Release: alt1
Summary: Documentation tests

Group: Sciences/Mathematics
License: BSD-3-Clause
URL: https://github.com/catch22/octave-doctest

Source0: http://downloads.sourceforge.net/octave/%{octave_pkg_name}-%{octave_pkg_version}.tar.gz

BuildRequires: octave-devel
%if_with _octave_arch
BuildRequires: gcc-c++ gcc-g77 libfftw3-devel libhdf5-devel liblapack-devel libncurses-devel libreadline-devel
%else
BuildArch: noarch
%endif
Provides: octave(doctest) = %version
# Depends: octave (>= 4.0.0)
Requires: octave >= 4.0.0


%description
Octave-Forge - Extra packages for GNU Octave.
This package contains the %octave_descr_name GNU Octave extension.

Extension Description:
The Octave-Forge Doctest package finds specially-formatted

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
* Fri Dec 30 2016 Igor Vlasenko <viy@altlinux.ru> 0.5.0-alt1
- regenerated from template by package builder

* Tue Apr 12 2016 Igor Vlasenko <viy@altlinux.ru> 0.4.1-alt1
- initial import by package builder

