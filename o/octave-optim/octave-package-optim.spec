Serial: 1
%def_with _octave_arch
%define octave_pkg_version 1.3.0
%define octave_pkg_name optim
%define octave_descr_name Optim
Name: octave-%octave_pkg_name
Version: 1.3.0
Release: alt1
Summary: Optimization.

Group: Sciences/Mathematics
License: GFDL, GPLv3+, modified BSD, public domain
URL: http://octave.sf.net

Source0: %octave_pkg_name-%version.tar.gz

BuildRequires: octave-devel
%if_with _octave_arch
BuildRequires: gcc-c++ gcc-g77 libfftw3-devel libhdf5-devel liblapack-devel libncurses-devel libreadline-devel octave-devel
%else
BuildArch: noarch
%endif
Provides: octave(optim) = %version
# Depends: octave (>= 3.4.0), miscellaneous (>= 1.0.10), struct (>= 1.0.10), parallel (>= 2.0.5)
Requires: octave >= 3.4.0 octave(miscellaneous) >= 1.0.10 octave(struct) >= 1.0.10 octave(parallel) >= 2.0.5


%description
Octave-Forge - Extra packages for GNU Octave.
This package contains the %octave_descr_name GNU Octave extension.

Extension Description:
Non-linear optimization toolkit.

%prep
%setup -T -c %name-%version

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
* Tue Jan 14 2014 Paul Wolneykien <manowar@altlinux.ru> 1:1.3.0-alt1
- updated by octave-package-builder

* Tue Jan 14 2014 Paul Wolneykien <manowar@altlinux.ru> 1:1.2.2-alt2
- Rebuild with the next version of Octave: 3.8.0

* Tue Jan 08 2013 Paul Wolneykien <manowar@altlinux.ru> 1:1.2.2-alt1
- updated by octave-package-builder

* Thu Nov 17 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.17-alt1
- initial import by octave-package-builder

