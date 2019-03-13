# BEGIN SourceDeps(oneline):
BuildRequires: libblas-devel makeinfo
# END SourceDeps(oneline)
BuildRequires: libgomp-devel
%def_with _octave_arch
%define octave_pkg_name nan
Name: octave-%octave_pkg_name
Version: 3.1.4
Release: alt1
Summary: The NaN-toolbox

Group: Sciences/Mathematics
License: GPLv3+
URL: http://pub.ist.ac.at/~schloegl/matlab/NaN

Source0: https://downloads.sourceforge.net/project/octave/Octave%%20Forge%%20Packages/Individual%%20Package%%20Releases/%{octave_pkg_name}-%{version}.tar.gz

BuildRequires: octave-devel
%if_with _octave_arch
BuildRequires: gcc-c++ gcc-g77 libfftw3-devel libhdf5-devel liblapack-devel libncurses-devel libreadline-devel
%else
BuildArch: noarch
%endif
Provides: octave(nan) = %version
# Depends: octave (> 3.2.0)
Requires: octave > 3.2.0


%description
A statistics and machine learning toolbox for data with and w/o missing values

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
%doc DESCRIPTION COPYING NEWS doc
%_datadir/octave/packages/%octave_pkg_name-%version
%if_with _octave_arch
%_libdir/octave/packages/%octave_pkg_name-%version
%endif

%changelog
* Wed Mar 13 2019 Igor Vlasenko <viy@altlinux.ru> 3.1.4-alt1
- regenerated from template by package builder

* Mon Mar 28 2016 Anton Midyukov <antohami@altlinux.org> 3.0.1-alt1
- new version
- added missing buildrequires

* Wed Jul 02 2014 Paul Wolneykien <manowar@altlinux.ru> 2.5.9-alt1
- updated by octave-package-builder

