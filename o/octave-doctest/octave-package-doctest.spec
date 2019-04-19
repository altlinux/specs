# BEGIN SourceDeps(oneline):
BuildRequires: makeinfo
# END SourceDeps(oneline)
%define octpkg doctest
Name: octave-%octpkg
Version: 0.7.0
Release: alt1
Summary: Documentation tests

Group: Sciences/Mathematics
License: BSD-3-Clause
URL: https://octave.sourceforge.io/doctest

Source0: https://downloads.sourceforge.net/project/octave/Octave%%20Forge%%20Packages/Individual%%20Package%%20Releases/%{octpkg}-%{version}.tar.gz

BuildRequires(pre): rpm-build-octave
BuildRequires: octave-devel
%if_with _octave_arch
BuildRequires: gcc-c++ gcc-g77 libfftw3-devel libhdf5-devel liblapack-devel libncurses-devel libreadline-devel
%else
BuildArch: noarch
%endif
Provides: octave(doctest) = %version
# Depends: octave (>= 4.2.0)
Requires: octave >= 4.2.0


%description
Find and run example code within documentation.

%prep
%setup -q -n %{octpkg}-%{version}

%build
%octave_build

%install
%octave_install

%files
%doc README.md COPYING DESCRIPTION CONTRIBUTORS NEWS
%_datadir/octave/packages/%octpkg-%version
%if_with _octave_arch
%_libdir/octave/packages/%octpkg-%version
%endif

%changelog
* Fri Apr 19 2019 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt1
- regenerated from template by package builder

* Thu May 24 2018 Igor Vlasenko <viy@altlinux.ru> 0.6.1-alt1
- regenerated from template by package builder

* Tue May 22 2018 Igor Vlasenko <viy@altlinux.ru> 0.5.0-alt3
- rebuild with octave 4.4

* Thu May 18 2017 Paul Wolneykien <manowar@altlinux.org> 0.5.0-alt2
- regenerated from template by package builder

* Fri Dec 30 2016 Igor Vlasenko <viy@altlinux.ru> 0.5.0-alt1
- regenerated from template by package builder

* Tue Apr 12 2016 Igor Vlasenko <viy@altlinux.ru> 0.4.1-alt1
- initial import by package builder

