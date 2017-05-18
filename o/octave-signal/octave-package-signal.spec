# BEGIN SourceDeps(oneline):
BuildRequires: makeinfo
# END SourceDeps(oneline)
%def_with _octave_arch
%define octave_pkg_version 1.3.2
%define octave_pkg_name signal
%define octave_descr_name Signal
Epoch: 2
Name: octave-%octave_pkg_name
Version: 1.3.2
Release: alt2
Summary: Signal Processing.

Group: Sciences/Mathematics
License: GPLv3+, public domain
URL: http://octave.sf.net

Source0: https://downloads.sourceforge.net/project/octave/Octave%%20Forge%%20Packages/Individual%%20Package%%20Releases/%{octave_pkg_name}-%{octave_pkg_version}.tar.gz

BuildRequires: octave-devel
%if_with _octave_arch
BuildRequires: gcc-c++ gcc-g77 libfftw3-devel libhdf5-devel liblapack-devel libncurses-devel libreadline-devel
BuildRequires: libGL-devel libGLU-devel libGraphicsMagick-c++-devel libGraphicsMagick-devel fontconfig-devel libfreetype-devel libX11-devel libgl2ps-devel libcurl-devel libsuitesparse-devel libarpack-ng-devel libqrupdate-devel libpcre-devel
%else
BuildArch: noarch
%endif
Provides: octave(signal) = %version
# Depends: octave (>= 3.8.0), control (>= 2.4.5)
Requires: octave >= 3.8.0 octave(control) >= 2.4.5

%description
Octave-Forge - Extra packages for GNU Octave.
This package contains the %octave_descr_name GNU Octave extension.

Extension Description:
Signal processing tools, including filtering, windowing and display functions.

%prep
%setup -q -n %{octave_pkg_name}-%{octave_pkg_version}

%build
%define build_flags CXXFLAGS=$CXXFLAGS
%build_flags octave -H --no-site-file --eval "pkg build -verbose -nodeps . %SOURCE0"

%install
mkdir -p %buildroot%_datadir/octave/packages
mkdir -p %buildroot%_libdir/octave/packages
octave -H --no-site-file --eval "pkg prefix %buildroot%_datadir/octave/packages %buildroot%_libdir/octave/packages; pkg install -verbose -local -nodeps %octave_pkg_name-%octave_pkg_version-$(octave -H --no-site-file --eval "printf([__octave_config_info__(\"canonical_host_type\"), \"-\",  __octave_config_info__(\"api_version\")])").tar.gz"

%files
%_datadir/octave/packages/%octave_pkg_name-%octave_pkg_version
%if_with _octave_arch
%_libdir/octave/packages/%octave_pkg_name-%octave_pkg_version
%endif

%changelog
* Thu May 18 2017 Paul Wolneykien <manowar@altlinux.org> 2:1.3.2-alt2
- regenerated from template by package builder

* Thu Apr 14 2016 Igor Vlasenko <viy@altlinux.ru> 2:1.3.2-alt1
- regenerated from template by package builder

* Tue Jul 07 2015 Paul Wolneykien <manowar@altlinux.org> 2:1.3.0-alt2
- Rebuild with the next version of Octave: 4.0.0

* Thu Jun 18 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 2:1.3.0-alt1.1
- Rebuilt for gcc5 C++11 ABI.

* Wed Jul 02 2014 Paul Wolneykien <manowar@altlinux.ru> 2:1.3.0-alt1
- updated by octave-package-builder

* Tue Jan 14 2014 Paul Wolneykien <manowar@altlinux.ru> 2:1.2.2-alt2
- Rebuild with the next version of Octave: 3.8.0

* Thu Oct 10 2013 Paul Wolneykien <manowar@altlinux.ru> 2:1.2.2-alt1
- updated by octave-package-builder

* Tue Jan 08 2013 Paul Wolneykien <manowar@altlinux.ru> 2:1.2.0-alt1
- updated by octave-package-builder

* Thu Nov 17 2011 Igor Vlasenko <viy@altlinux.ru> 1:1.1.1-alt1
- initial import by octave-package-builder

