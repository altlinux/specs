# BEGIN SourceDeps(oneline):
BuildRequires: pkgconfig(ginac)
# END SourceDeps(oneline)
%def_with _octave_arch
%define octave_pkg_version 1.1.0
%define octave_pkg_name symbolic
%define octave_descr_name Symbolic
Name: octave-%octave_pkg_name
Version: 1.1.0
Release: alt1
Summary: Symbolic Computations.

Group: Sciences/Mathematics
License: GPL version 2 or later
URL: http://octave.sf.net

Source0: %octave_pkg_name-%version.tar.gz

BuildRequires: octave-devel
%if_with _octave_arch
BuildRequires: gcc-c++ gcc-g77 libfftw3-devel libhdf5-devel liblapack-devel libncurses-devel libreadline-devel octave-devel
%else
BuildArch: noarch
%endif
Provides: octave(symbolic) = %version

# octave module BuildRequires: ginac-devel
BuildRequires: libginac-devel
# Depends: octave (>= 3.1.55)
Requires: octave >= 3.1.55


%description
Octave-Forge - Extra packages for GNU Octave.
This package contains the %octave_descr_name GNU Octave extension.

Extension Description:
Symbolic toolbox based on GiNaC and CLN.

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
* Thu Oct 10 2013 Paul Wolneykien <manowar@altlinux.ru> 1.1.0-alt1
- updated by octave-package-builder

