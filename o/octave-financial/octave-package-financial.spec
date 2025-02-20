%define octpkg financial
Epoch: 1
Name: octave-%octpkg
Version: 0.5.3
Release: alt2
Summary: Financial

Group: Sciences/Mathematics
License: GPLv3+
URL: http://octave.sf.net

Source0: https://downloads.sourceforge.net/project/octave/Octave%%20Forge%%20Packages/Individual%%20Package%%20Releases/%{octpkg}-%{version}.tar.gz
Patch0: octave-package-financial-octave-9.patch

BuildRequires(pre): rpm-build-octave
BuildRequires: octave-devel
BuildRequires: makeinfo
%if_with _octave_arch
BuildRequires: gcc-c++ gcc-g77 libfftw3-devel libhdf5-devel liblapack-devel libncurses-devel libreadline-devel
%else
BuildArch: noarch
%endif
Provides: octave(financial) = %version
# Depends: octave (>= 4.4.0), io (>= 2.4.11), statistics (>= 1.4.0)
Requires: octave >= 4.4.0 octave(io) >= 2.4.11 octave(statistics) >= 1.4.0


%description
Monte Carlo simulation, options pricing routines, financial

%prep
%setup -q -n %{octpkg}-%{version}
%patch0 -p1

%build
%octave_build

%install
%octave_install

%files
%doc COPYING DESCRIPTION NEWS
%_datadir/octave/packages/%octpkg-%version
%if_with _octave_arch
%_libdir/octave/packages/%octpkg-%version
%endif

%changelog
* Wed Feb 19 2025 Andrey Cherepanov <cas@altlinux.org> 1:0.5.3-alt2
- Rebuild with Octave 9.

* Tue Mar 12 2019 Igor Vlasenko <viy@altlinux.ru> 1:0.5.3-alt1
- regenerated from template by package builder

* Sat May 26 2018 Igor Vlasenko <viy@altlinux.ru> 1:0.5.1-alt1
- build for octave 4.4

* Wed Apr 13 2016 Igor Vlasenko <viy@altlinux.ru> 1:0.5.0-alt1
- regenerated from template by package builder

* Tue Jul 07 2015 Paul Wolneykien <manowar@altlinux.org> 1:0.4.0-alt3
- Rebuild with the next version of Octave: 4.0.0

* Tue Jan 14 2014 Paul Wolneykien <manowar@altlinux.ru> 1:0.4.0-alt2
- Rebuild with the next version of Octave: 3.8.0

* Tue Jan 08 2013 Paul Wolneykien <manowar@altlinux.ru> 1:0.4.0-alt1
- updated by octave-package-builder

* Mon Nov 28 2011 Igor Vlasenko <viy@altlinux.ru> 0.3.2-alt1
- initial import by octave-package-builder

