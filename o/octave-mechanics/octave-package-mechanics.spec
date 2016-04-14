# BEGIN SourceDeps(oneline):
BuildRequires: makeinfo
# END SourceDeps(oneline)
%def_with _octave_arch
%define octave_pkg_version 1.3.1
%define octave_pkg_name mechanics
%define octave_descr_name Mechanics
Serial: 1
Name: octave-%octave_pkg_name
Version: 1.3.1
Release: alt2
Summary: Classical Mechanics & Structural Analysis

Group: Sciences/Mathematics
License: GPLv3+
URL: http://octave.sf.net

Source0: http://downloads.sourceforge.net/octave/%{octave_pkg_name}-%{octave_pkg_version}.tar.gz

BuildRequires: octave-devel
%if_with _octave_arch
BuildRequires: gcc-c++ gcc-g77 libfftw3-devel libhdf5-devel liblapack-devel libncurses-devel libreadline-devel
%else
BuildArch: noarch
%endif
Provides: octave(mechanics) = %version
# Depends: octave (>= 3.4.0), linear-algebra (>= 2.0.0), general (>= 1.2.2), geometry (>= 1.2.1)
Requires: octave >= 3.4.0 octave(linear-algebra) >= 2.0.0 octave(general) >= 1.2.2 octave(geometry) >= 1.2.1


%description
Octave-Forge - Extra packages for GNU Octave.
This package contains the %octave_descr_name GNU Octave extension.

Extension Description:
Library with functions useful for numerical computation in classical mechanics and structural analysis.

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
* Thu Apr 14 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.3.1-alt2
- regenerated from template by package builder

* Wed Jan 15 2014 Cronport Service <cronport@altlinux.org> 1:1.3.1-alt1.M70T.1
- backport

* Tue Jan 08 2013 Paul Wolneykien <manowar@altlinux.ru> 1:1.3.1-alt1
- updated by octave-package-builder

* Thu Nov 17 2011 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1
- initial import by octave-package-builder

