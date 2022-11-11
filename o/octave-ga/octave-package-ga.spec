# BEGIN SourceDeps(oneline):
BuildRequires: makeinfo
# END SourceDeps(oneline)
%define octpkg ga
Epoch: 1
Name: octave-%octpkg
Version: 0.10.3
Release: alt1
Summary: Genetic Algorithm

Group: Sciences/Mathematics
License: GPL version 3 or later
URL: http://octave.sf.net

Source0: https://downloads.sourceforge.net/project/octave/Octave%%20Forge%%20Packages/Individual%%20Package%%20Releases/%{octpkg}-%{version}.tar.gz

BuildRequires(pre): rpm-build-octave
BuildRequires: octave-devel
%if_with _octave_arch
BuildRequires: gcc-c++ gcc-g77 libfftw3-devel libhdf5-devel liblapack-devel libncurses-devel libreadline-devel
%else
BuildArch: noarch
%endif
Provides: octave(ga) = %version
# Depends: octave (>= 3.4.0)
Requires: octave >= 3.4.0


%description
Genetic optimization code

%prep
%setup -q -n %{octpkg}-%{version}

%build
%octave_build

%install
%octave_install

%files
%doc DESCRIPTION COPYING NEWS doc
%_datadir/octave/packages/%octpkg-%version
%if_with _octave_arch
%_libdir/octave/packages/%octpkg-%version
%endif

%changelog
* Fri Apr 08 2022 Andrey Cherepanov <cas@altlinux.org> 1:0.10.3-alt1
- new version

* Wed Dec 01 2021 Igor Vlasenko <viy@altlinux.org> 1:0.10.2-alt1
- regenerated from template by package builder

* Thu Jun 13 2019 Igor Vlasenko <viy@altlinux.ru> 1:0.10.1-alt1
- regenerated from template by package builder

* Sat May 26 2018 Igor Vlasenko <viy@altlinux.ru> 1:0.10.0-alt4
- build for octave 4.4

* Tue Jul 07 2015 Paul Wolneykien <manowar@altlinux.org> 1:0.10.0-alt3
- Rebuild with the next version of Octave: 4.0.0

* Tue Jan 14 2014 Paul Wolneykien <manowar@altlinux.ru> 1:0.10.0-alt2
- Rebuild with the next version of Octave: 3.8.0

* Tue Jan 08 2013 Paul Wolneykien <manowar@altlinux.ru> 1:0.10.0-alt1
- updated by octave-package-builder

* Thu Nov 17 2011 Igor Vlasenko <viy@altlinux.ru> 0.9.8-alt1
- initial import by octave-package-builder

