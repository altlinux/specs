Serial: 1
%define octave_pkg_version 0.9.1
%define octave_pkg_name dataframe
%define octave_descr_name dataframe
Name: octave-%octave_pkg_name
Version: 0.9.1
Release: alt1
Summary: Data Frame

Group: Sciences/Mathematics
License: GPL version 3 or later
URL: http://octave.sf.net

Source0: %octave_pkg_name-%version.tar.gz

BuildRequires: octave-devel
%if_with _octave_arch
BuildRequires: gcc-c++ gcc-g77 libfftw3-devel libhdf5-devel liblapack-devel libncurses-devel libreadline-devel octave-devel
%else
BuildArch: noarch
%endif
Provides: octave(dataframe) = %version
# Depends: octave (>= 3.2.0)
Requires: octave >= 3.2.0


%description
Octave-Forge - Extra packages for GNU Octave.
This package contains the %octave_descr_name GNU Octave extension.

Extension Description:
Data manipulation toolbox similar to R data.frame

%prep
%setup -n %octave_pkg_name

%build
octave -q -H --no-site-file --eval "pkg build -nodeps . %SOURCE0"

%install
mkdir -p %buildroot%_datadir/octave/packages
mkdir -p %buildroot%_libdir/octave/packages
octave -q -H --no-site-file --eval "pkg prefix %buildroot%_datadir/octave/packages %buildroot%_libdir/octave/packages; pkg install -local -nodeps %octave_pkg_name-%octave_pkg_version.tar.gz"

%files
%_datadir/octave/packages/%octave_pkg_name-%octave_pkg_version
%if_with _octave_arch
%_libdir/octave/packages/%octave_pkg_name-%octave_pkg_version
%endif

%changelog
* Tue Jan 08 2013 Paul Wolneykien <manowar@altlinux.ru> 1:0.9.1-alt1
- updated by octave-package-builder

* Tue Nov 29 2011 Igor Vlasenko <viy@altlinux.ru> 0.8.2-alt1
- updated by octave-package-builder

* Fri Nov 18 2011 Igor Vlasenko <viy@altlinux.ru> 0.8-alt1
- initial import by octave-package-builder

