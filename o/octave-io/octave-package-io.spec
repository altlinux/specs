Serial: 1
# BEGIN SourceDeps(oneline):
BuildRequires: glibc-devel
# END SourceDeps(oneline)
%def_with _octave_arch
%define octave_pkg_version 2.0.2
%define octave_pkg_name io
%define octave_descr_name io
Name: octave-%octave_pkg_name
Version: 2.0.2
Release: alt1
Summary: Input/Output

Group: Sciences/Mathematics
License: GPLv3+, simplified BSD
URL: http://octave.sf.net

Source0: %octave_pkg_name-%version.tar.gz

BuildRequires: octave-devel
%if_with _octave_arch
BuildRequires: gcc-c++ gcc-g77 libfftw3-devel libhdf5-devel liblapack-devel libncurses-devel libreadline-devel octave-devel
%else
BuildArch: noarch
%endif
Provides: octave(io) = %version
# Depends: octave (>= 3.7.2)
Requires: octave >= 3.7.2


%description
Octave-Forge - Extra packages for GNU Octave.
This package contains the %octave_descr_name GNU Octave extension.

Extension Description:
Input/Output in external formats.

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
* Tue Jan 14 2014 Paul Wolneykien <manowar@altlinux.ru> 1:2.0.2-alt1
- updated by octave-package-builder

* Tue Jan 14 2014 Paul Wolneykien <manowar@altlinux.ru> 1:1.2.3-alt2
- Rebuild with the next version of Octave: 3.8.0

* Thu Oct 10 2013 Paul Wolneykien <manowar@altlinux.ru> 1:1.2.3-alt1
- updated by octave-package-builder

* Tue Jan 08 2013 Paul Wolneykien <manowar@altlinux.ru> 1:1.2.0-alt1
- updated by octave-package-builder

* Thu Nov 17 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.15-alt1
- initial import by octave-package-builder

