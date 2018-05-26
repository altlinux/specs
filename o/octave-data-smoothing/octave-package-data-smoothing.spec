# BEGIN SourceDeps(oneline):
BuildRequires: makeinfo
# END SourceDeps(oneline)
%define octave_pkg_name data-smoothing
Epoch: 1
Name: octave-%octave_pkg_name
Version: 1.3.0
Release: alt3
Summary: Data smoothing

Group: Sciences/Mathematics
License: GPL version 3 or later
URL: http://octave.sf.net

Source0: https://downloads.sourceforge.net/project/octave/Octave%%20Forge%%20Packages/Individual%%20Package%%20Releases/%{octave_pkg_name}-%{version}.tar.gz

BuildRequires: octave-devel
%if_with _octave_arch
BuildRequires: gcc-c++ gcc-g77 libfftw3-devel libhdf5-devel liblapack-devel libncurses-devel libreadline-devel
%else
BuildArch: noarch
%endif
Provides: octave(data-smoothing) = %version
# Depends: octave (>= 3.6.0), optim (>= 1.0.3)
Requires: octave >= 3.6.0 octave(optim) >= 1.0.3


%description
Algorithms for smoothing noisy data

%prep
%setup -q -n %{octave_pkg_name}

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
%doc COPYING DESCRIPTION NEWS
%_datadir/octave/packages/%octave_pkg_name-%version
%if_with _octave_arch
%_libdir/octave/packages/%octave_pkg_name-%version
%endif

%changelog
* Sat May 26 2018 Igor Vlasenko <viy@altlinux.ru> 1:1.3.0-alt3
- build for octave 4.4

* Tue Apr 12 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.3.0-alt2
- initial import by package builder

