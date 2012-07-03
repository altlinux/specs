%define oldname octave-
%define octave_pkg_version 1.0.2
%define octave_pkg_name missing-functions
%define octave_descr_name missing-functions
Name: octave-missing-functions
Version: 1.0.2
Release: alt1
Summary: Missing Functions

Group: Sciences/Mathematics
License: GPL version 2 or later
URL: http://octave.sf.net

Source0: in/%octave_pkg_name-%version.tar.gz

BuildRequires: octave-devel
%if_with _octave_arch
BuildRequires: gcc-c++ libfftw3-devel libhdf5-devel liblapack-devel libncurses-devel libreadline-devel octave-devel
%else
BuildArch: noarch
%endif
Provides: octave(missing-functions) = %version
# Depends: octave (>= 3.0.0)
Requires: octave >= 3.0.0


%description
Octave-Forge - Extra packages for GNU Octave.
This package contains the %octave_descr_name GNU Octave extension.

Extension Description:
Find functions that are in Matlab but not in Octave.

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
* Mon Nov 28 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1
- initial import by octave-package-builder

