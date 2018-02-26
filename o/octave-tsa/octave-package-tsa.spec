%define octave_pkg_version 4.1.1
%define octave_pkg_name tsa
%define octave_descr_name TSA
Name: octave-%octave_pkg_name
Version: 4.1.1
Release: alt1
Summary: The TSA-toolbox

Group: Sciences/Mathematics
License: GPL version 3 or later
URL: http://biosig-consulting.com/matlab/tsa

Source0: %octave_pkg_name-%version.tgz

BuildRequires: octave-devel
%if_with _octave_arch
BuildRequires: gcc-c++ libfftw3-devel libhdf5-devel liblapack-devel libncurses-devel libreadline-devel octave-devel
%else
BuildArch: noarch
%endif
# Depends: octave (> 2.9.0)
Requires: octave > 2.9.0
Provides: octave(tsa) = 4.1.1


%description
Octave-Forge - Extra packages for GNU Octave.
This package contains the %octave_descr_name GNU Octave extension.

Extension Description:
A toolbox for Time Series Analysis .

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
* Fri Nov 18 2011 Igor Vlasenko <viy@altlinux.ru> 4.1.1-alt1
- initial import by octave-package-builder

