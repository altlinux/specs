# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/mkoctfile /usr/bin/octave
# END SourceDeps(oneline)
%def_with _octave_arch
%define octave_pkg_version 0.8.4
%define octave_pkg_name odepkg
%define octave_descr_name OdePkg
Name: octave-%octave_pkg_name
Version: 0.8.4
Release: alt2.1
Summary: OdePkg

Group: Sciences/Mathematics
License: GPLv2+
URL: http://octave.sf.net

Source0: %octave_pkg_name-%version.tar.gz

BuildRequires: octave-devel
%if_with _octave_arch
BuildRequires: gcc-c++ gcc-g77 libfftw3-devel libhdf5-devel liblapack-devel libncurses-devel libreadline-devel octave-devel
%else
BuildArch: noarch
%endif
Provides: octave(odepkg) = %version
# Depends: octave (>= 3.2.0)
Requires: octave >= 3.2.0


%description
Octave-Forge - Extra packages for GNU Octave.
This package contains the %octave_descr_name GNU Octave extension.

Extension Description:
A package for solving ordinary differential equations and more.

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
* Tue Jul 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.4-alt2.1
- Rebuilt with updated openblas

* Tue Jan 14 2014 Paul Wolneykien <manowar@altlinux.ru> 0.8.4-alt2
- Rebuild with the next version of Octave: 3.8.0

* Thu Oct 10 2013 Paul Wolneykien <manowar@altlinux.ru> 0.8.4-alt1
- updated by octave-package-builder

* Tue Jan 08 2013 Paul Wolneykien <manowar@altlinux.ru> 0.8.2-alt1
- updated by octave-package-builder

