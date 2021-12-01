# BEGIN SourceDeps(oneline):
BuildRequires: libgomp-devel makeinfo
# END SourceDeps(oneline)
%def_with _octave_arch
%define octpkg nurbs
Name: octave-%octpkg
Version: 1.4.3
Release: alt1
Summary: Nurbs.

Group: Sciences/Mathematics
License: GPLv3+
URL: http://octave.sf.net

Source0: https://downloads.sourceforge.net/project/octave/Octave%%20Forge%%20Packages/Individual%%20Package%%20Releases/%{octpkg}-%{version}.tar.gz

BuildRequires(pre): rpm-build-octave
BuildRequires: octave-devel
%if_with _octave_arch
BuildRequires: gcc-c++ gcc-g77 libfftw3-devel libhdf5-devel liblapack-devel libncurses-devel libreadline-devel
%else
BuildArch: noarch
%endif
Provides: octave(nurbs) = %version
# Depends: octave (>= 5.1)
Requires: octave >= 5.1


%description
Collection of routines for the creation, and manipulation of Non-Uniform Rational B-Splines (NURBS), based on the NURBS toolbox by Mark Spink.

%prep
%setup -q -n %{octpkg}-%{version}

%build
%octave_build

%install
%octave_install

%files
%doc DESCRIPTION COPYING NEWS
%_datadir/octave/packages/%octpkg-%version
%if_with _octave_arch
%_libdir/octave/packages/%octpkg-%version
%endif

%changelog
* Wed Dec 01 2021 Igor Vlasenko <viy@altlinux.org> 1.4.3-alt1
- regenerated from template by package builder

* Tue Dec 15 2020 Andrey Cherepanov <cas@altlinux.org> 1.3.13-alt4
- rebuild against octave 6

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 1.3.13-alt3
- rebuild with octave 5

* Tue May 22 2018 Igor Vlasenko <viy@altlinux.ru> 1.3.13-alt2
- rebuild with octave 4.4

* Thu May 18 2017 Paul Wolneykien <manowar@altlinux.org> 1.3.13-alt1
- regenerated from template by package builder

* Thu Apr 14 2016 Igor Vlasenko <viy@altlinux.ru> 1.3.10-alt1
- initial import by package builder

