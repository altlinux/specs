# BEGIN SourceDeps(oneline):
BuildRequires: makeinfo
# END SourceDeps(oneline)
%def_with _octave_arch
%define octave_pkg_name lssa
Name: octave-%octave_pkg_name
Version: 0.1.3
Release: alt1
Summary: Least squares spectral analysis

Group: Sciences/Mathematics
License: GPLv3+
URL: http://www.jstatsoft.org/v11/i02

Source0: https://downloads.sourceforge.net/project/octave/Octave%%20Forge%%20Packages/Individual%%20Package%%20Releases/%{octave_pkg_name}-%{version}.tar.gz

BuildRequires: octave-devel
%if_with _octave_arch
BuildRequires: gcc-c++ gcc-g77 libfftw3-devel libhdf5-devel liblapack-devel libncurses-devel libreadline-devel
%else
BuildArch: noarch
%endif
Provides: octave(lssa) = %version
# Depends: octave (>= 3.6.0)
Requires: octave >= 3.6.0


%description
A package implementing tools to compute spectral decompositions of

%prep
%setup -q -n %{octave_pkg_name}-%{version}

%build
octave -q -H --no-window-system --no-site-file --eval "pkg build -verbose -nodeps . %SOURCE0"

%install
mkdir -p %buildroot%_datadir/octave/packages
mkdir -p %buildroot%_libdir/octave/packages
%if_with _octave_arch
octave -H --no-window-system --no-site-file --eval "pkg prefix %buildroot%_datadir/octave/packages %buildroot%_libdir/octave/packages; pkg install -nodeps -verbose -local %octave_pkg_name-%version-$(octave -H --no-window-system --no-site-file --eval "printf([__octave_config_info__(\"canonical_host_type\"), \"-\",  __octave_config_info__(\"api_version\")])").tar.gz"
%else
octave -q -H --no-window-system --no-site-file --eval "pkg prefix %buildroot%_datadir/octave/packages %buildroot%_libdir/octave/packages; pkg install -nodeps -verbose -local %octave_pkg_name-%version-any-none.tar.gz"
%endif

%files
%doc DESCRIPTION NEWS COPYING
%_datadir/octave/packages/%octave_pkg_name-%version
%if_with _octave_arch
%_libdir/octave/packages/%octave_pkg_name-%version
%endif

%changelog
* Tue Mar 12 2019 Igor Vlasenko <viy@altlinux.ru> 0.1.3-alt1
- regenerated from template by package builder

* Tue Jul 07 2015 Paul Wolneykien <manowar@altlinux.org> 0.1.2-alt3
- Rebuild with the next version of Octave: 4.0.0

* Thu Jun 18 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.1.2-alt2.1
- Rebuilt for gcc5 C++11 ABI.

* Tue Jan 14 2014 Paul Wolneykien <manowar@altlinux.ru> 0.1.2-alt2
- Rebuild with the next version of Octave: 3.8.0

* Tue Jan 08 2013 Paul Wolneykien <manowar@altlinux.ru> 0.1.2-alt1
- updated by octave-package-builder

