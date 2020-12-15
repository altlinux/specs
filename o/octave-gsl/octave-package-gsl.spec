# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/octave makeinfo
# END SourceDeps(oneline)
%def_with _octave_arch
%define octpkg gsl
Name: octave-%octpkg
Version: 2.1.1
Release: alt3
Summary: GNU Scientific Library

Group: Sciences/Mathematics
License: GPL-2.0+
URL: http://octave.sf.net

Source0: https://downloads.sourceforge.net/project/octave/Octave%%20Forge%%20Packages/Individual%%20Package%%20Releases/%{octpkg}-%{version}.tar.gz

BuildRequires(pre): rpm-build-octave
BuildRequires: octave-devel
%if_with _octave_arch
BuildRequires: gcc-c++ gcc-g77 libfftw3-devel libhdf5-devel liblapack-devel libncurses-devel libreadline-devel
%else
BuildArch: noarch
%endif
Provides: octave(gsl) = %version

# octave module BuildRequires: gsl-devel
BuildRequires: libgsl-devel
# Depends: octave (>= 2.9.7)
Requires: octave >= 2.9.7

%description
Octave bindings to the GNU Scientific Library.  The GSL is a collection of
routines for numerical analysis.

%prep
%setup -q -n %{octpkg}-%{version}

%build
# Ignore warnings for configure check scripts
export CXXFLAGS="$CXXFLAGS -Wno-error=return-type"
%octave_build

%install
%octave_install

%files
%doc COPYING NEWS AUTHORS DESCRIPTION
%_datadir/octave/packages/%octpkg-%version
%if_with _octave_arch
%_libdir/octave/packages/%octpkg-%version
%endif

%changelog
* Tue Dec 15 2020 Andrey Cherepanov <cas@altlinux.org> 2.1.1-alt3
- build against octave 6

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 2.1.1-alt2
- rebuild with octave 5

* Tue Mar 12 2019 Igor Vlasenko <viy@altlinux.ru> 2.1.1-alt1
- regenerated from template by package builder

* Thu May 24 2018 Igor Vlasenko <viy@altlinux.ru> 2.1.0-alt1
- initial import by package builder

