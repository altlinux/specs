%define octave_pkg_name bim
%define octave_descr_name bim
Name: octave-%octave_pkg_name
Version: 1.0.2
Release: alt1
Summary: PDE Solver using a Finite Element/Finite Volume approach

Group: Sciences/Mathematics
License: GPL version 2 or later
Url: http://octave.sourceforge.net/

Source0: %octave_pkg_name-%version.tar.gz

BuildRequires: octave-devel
%if_with _octave_arch
BuildRequires: gcc-c++ libfftw3-devel libhdf5-devel liblapack-devel libncurses-devel libreadline-devel octave-devel
%else
BuildArch: noarch
%endif
# Depends: octave (>= 3.2.0), fpl, msh
Requires: octave >= 3.2.0 octave(fpl) octave(msh)
Provides: octave(bim) = 1.0.2


%description
Octave-Forge - Extra packages for GNU Octave.
This package contains the %octave_descr_name GNU Octave extension.

Extension Description:
Package for solving Diffusion Advection Reaction (DAR) Partial Differential Equations based on the Finite Volume Scharfetter-Gummel (FVSG) method a.k.a Box Integration Method (BIM)

%prep
%setup -n %octave_pkg_name-%version

%build
octave -q -H --no-site-file --eval "pkg build -nodeps . %SOURCE0"

%install
mkdir -p %buildroot%_datadir/octave/packages
mkdir -p %buildroot%_libdir/octave/packages
octave -q -H --no-site-file --eval "pkg prefix %buildroot%_datadir/octave/packages %buildroot%_libdir/octave/packages; pkg install -local -nodeps %octave_pkg_name-%version.tar.gz"

%files
%_datadir/octave/packages/%octave_pkg_name-%version
%if_with _octave_arch
%_libdir/octave/packages/%octave_pkg_name-%version
%endif

%changelog
* Thu Nov 17 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1
- initial import by octave-package-builder

