%define octave_pkg_name fuzzy-logic-toolkit
%define octave_descr_name fuzzy-logic-toolkit
Name: octave-%octave_pkg_name
Version: 0.3.0
Release: alt1
Summary: Octave Fuzzy Logic Toolkit

Group: Sciences/Mathematics
License: GPL version 2 or later
URL: http://octave.sf.net

Source0: %octave_pkg_name-%version.tar.gz

BuildRequires: octave-devel
%if_with _octave_arch
BuildRequires: gcc-c++ libfftw3-devel libhdf5-devel liblapack-devel libncurses-devel libreadline-devel octave-devel
%else
BuildArch: noarch
%endif
# Depends: octave (>= 3.2.4)
Requires: octave >= 3.2.4
Provides: octave(fuzzy-logic-toolkit) = 0.3.0


%description
Octave-Forge - Extra packages for GNU Octave.
This package contains the %octave_descr_name GNU Octave extension.

Extension Description:
A mostly MATLAB-compatible fuzzy logic toolkit for Octave.

%prep
%setup -n %octave_pkg_name

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
* Thu Nov 17 2011 Igor Vlasenko <viy@altlinux.ru> 0.3.0-alt1
- initial import by octave-package-builder

