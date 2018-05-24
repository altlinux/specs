# BEGIN SourceDeps(oneline):
BuildRequires: libportaudio2-devel makeinfo
# END SourceDeps(oneline)
%def_with _octave_arch
%define octave_pkg_version 2.3.0
%define octave_pkg_name ltfat
%define octave_descr_name LTFAT
Name: octave-%octave_pkg_name
Version: 2.3.0
Release: alt1
Summary: The Large Time-Frequency Analysis Toolbox

Group: Sciences/Mathematics
License: GPLv3+
URL: http://ltfat.github.io/

Source0: https://downloads.sourceforge.net/project/octave/Octave%%20Forge%%20Packages/Individual%%20Package%%20Releases/%{octave_pkg_name}-%{octave_pkg_version}.tar.gz

BuildRequires: octave-devel
%if_with _octave_arch
BuildRequires: gcc-c++ gcc-g77 libfftw3-devel libhdf5-devel liblapack-devel libncurses-devel libreadline-devel
%else
BuildArch: noarch
%endif
Provides: octave(ltfat) = %version

# octave module BuildRequires: fftw3 [Debian] libfftw3-3, lapack [Debian] liblapack3,
BuildRequires: libfftw3-devel liblapack-devel
# Depends: octave (>= 3.8.0)
Requires: octave >= 3.8.0


%description
Octave-Forge - Extra packages for GNU Octave.
This package contains the %octave_descr_name GNU Octave extension.

Extension Description:
The Large Time/Frequency Analysis Toolbox (LTFAT) is a

%prep
%setup -q -n %{octave_pkg_name}

%build
octave -q -H --no-window-system --no-site-file --eval "pkg build -verbose -nodeps . %SOURCE0"

%install
mkdir -p %buildroot%_datadir/octave/packages
mkdir -p %buildroot%_libdir/octave/packages
%if_with _octave_arch
octave -H --no-window-system --no-site-file --eval "pkg prefix %buildroot%_datadir/octave/packages %buildroot%_libdir/octave/packages; pkg install -nodeps -verbose -local %octave_pkg_name-%octave_pkg_version-$(octave -H --no-window-system --no-site-file --eval "printf([__octave_config_info__(\"canonical_host_type\"), \"-\",  __octave_config_info__(\"api_version\")])").tar.gz"
%else
octave -q -H --no-window-system --no-site-file --eval "pkg prefix %buildroot%_datadir/octave/packages %buildroot%_libdir/octave/packages; pkg install -nodeps -verbose -local %octave_pkg_name-%octave_pkg_version-any-none.tar.gz"
%endif

%files
%_datadir/octave/packages/%octave_pkg_name-%octave_pkg_version
%if_with _octave_arch
%_libdir/octave/packages/%octave_pkg_name-%octave_pkg_version
%endif

%changelog
* Thu May 24 2018 Igor Vlasenko <viy@altlinux.ru> 2.3.0-alt1
- regenerated from template by package builder

* Tue May 22 2018 Igor Vlasenko <viy@altlinux.ru> 2.2.0-alt2
- rebuild with octave 4.4

* Thu May 18 2017 Paul Wolneykien <manowar@altlinux.org> 2.2.0-alt1
- regenerated from template by package builder

* Wed Apr 13 2016 Igor Vlasenko <viy@altlinux.ru> 2.1.2-alt1
- initial import by package builder

