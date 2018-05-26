# BEGIN SourceDeps(oneline):
BuildRequires: makeinfo
# END SourceDeps(oneline)
%define octave_pkg_name secs3d
Name: octave-%octave_pkg_name
Version: 0.0.1
Release: alt4
Summary: SEmi Conductor Simulator in 3D

Group: Sciences/Mathematics
License: GPL version 2 or later
Url: http://octave.sourceforge.net/

Source0: https://downloads.sourceforge.net/project/octave/Octave%%20Forge%%20Packages/Individual%%20Package%%20Releases/%{octave_pkg_name}-%{version}.tar.gz

BuildRequires: octave-devel
%if_with _octave_arch
BuildRequires: gcc-c++ gcc-g77 libfftw3-devel libhdf5-devel liblapack-devel libncurses-devel libreadline-devel
%else
BuildArch: noarch
%endif
Provides: octave(secs3d) = %version
# Depends: octave (>= 3.2.4), bim, fpl
Requires: octave >= 3.2.4 octave(bim) octave(fpl)


%description
A Drift-Diffusion simulator for 3d semiconductor devices

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
%doc COPYING README DESCRIPTION
%_datadir/octave/packages/%octave_pkg_name-%version
%if_with _octave_arch
%_libdir/octave/packages/%octave_pkg_name-%version
%endif

%changelog
* Sat May 26 2018 Igor Vlasenko <viy@altlinux.ru> 0.0.1-alt4
- build for octave 4.4

* Tue Jul 07 2015 Paul Wolneykien <manowar@altlinux.org> 0.0.1-alt3
- Rebuild with the next version of Octave: 4.0.0

* Tue Jan 14 2014 Paul Wolneykien <manowar@altlinux.ru> 0.0.1-alt2
- Rebuild with the next version of Octave: 3.8.0

* Thu Nov 17 2011 Igor Vlasenko <viy@altlinux.ru> 0.0.1-alt1
- initial import by octave-package-builder

