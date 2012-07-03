%def_with _octave_arch
%define octave_pkg_version 1.0.8
%define octave_pkg_name econometrics
%define octave_descr_name Econometrics
Name: octave-%octave_pkg_name
Version: 1.0.8
Release: alt1
Summary: Econometrics.

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
Provides: octave(econometrics) = %version
# Depends: octave (>= 2.9.7), optim
Requires: octave >= 2.9.7 octave(optim)


%description
Octave-Forge - Extra packages for GNU Octave.
This package contains the %octave_descr_name GNU Octave extension.

Extension Description:
Econometrics functions including MLE and GMM based techniques.

%prep
%setup -n %octave_pkg_name-%version

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
* Mon Nov 28 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.8-alt1
- initial import by octave-package-builder

