# BEGIN SourceDeps(oneline):
BuildRequires: makeinfo
# END SourceDeps(oneline)
%define octpkg ncarray
Name: octave-%octpkg
Version: 1.0.5
Release: alt1
Summary: ncarray

Group: Sciences/Mathematics
License: GPLv3+
URL: https://octave.sourceforge.io/ncarray/index.html

Source0: https://downloads.sourceforge.net/project/octave/Octave%%20Forge%%20Packages/Individual%%20Package%%20Releases/%{octpkg}-%{version}.tar.gz

BuildRequires(pre): rpm-build-octave
BuildRequires: octave-devel
%if_with _octave_arch
BuildRequires: gcc-c++ gcc-g77 libfftw3-devel libhdf5-devel liblapack-devel libncurses-devel libreadline-devel
%else
BuildArch: noarch
%endif
Provides: octave(ncarray) = %version
# Depends: octave (>= 3.4.0), netcdf (>= 1.0.2), statistics (>= 1.0.6)
Requires: octave >= 3.4.0 octave(netcdf) >= 1.0.2 octave(statistics) >= 1.0.6


%description
Access a single or a collection of NetCDF files as a multi-dimensional array

%prep
%setup -q -n %{octpkg}-%{version}

%build
%octave_build

%install
%octave_install

%files
%doc DESCRIPTION NEWS COPYING
%_datadir/octave/packages/%octpkg-%version
%if_with _octave_arch
%_libdir/octave/packages/%octpkg-%version
%endif

%changelog
* Tue Dec 26 2023 Igor Vlasenko <viy@altlinux.org> 1.0.5-alt1
- regenerated from template by package builder

* Tue Jul 07 2015 Paul Wolneykien <manowar@altlinux.org> 1.0.3-alt2
- Rebuild with the next version of Octave: 4.0.0

* Wed Jul 02 2014 Paul Wolneykien <manowar@altlinux.ru> 1.0.3-alt1
- updated by octave-package-builder

* Tue Jan 14 2014 Paul Wolneykien <manowar@altlinux.ru> 1.0.1-alt1
- updated by octave-package-builder

* Tue Jan 14 2014 Paul Wolneykien <manowar@altlinux.ru> 1.0.0-alt2
- Rebuild with the next version of Octave: 3.8.0

* Tue Jan 08 2013 Paul Wolneykien <manowar@altlinux.ru> 1.0.0-alt1
- updated by octave-package-builder

