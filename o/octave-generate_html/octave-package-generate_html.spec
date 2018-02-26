%define octave_pkg_version 0.1.3
%define octave_pkg_name generate_html
%define octave_descr_name generate_html
Name: octave-%octave_pkg_name
Version: 0.1.3
Release: alt1
Summary: Generate HTML web page from help texts

Group: Sciences/Mathematics
License: GPL version 3 or later
Url: http://octave.sourceforge.net/

Source0: %octave_pkg_name-%version.tar.gz

BuildRequires: octave-devel
%if_with _octave_arch
BuildRequires: gcc-c++ libfftw3-devel libhdf5-devel liblapack-devel libncurses-devel libreadline-devel octave-devel
%else
BuildArch: noarch
%endif

# SystemRequirements: makeinfo
BuildRequires: /usr/bin/makeinfo
# Depends: octave (>= 3.2.0)
Requires: octave >= 3.2.0
Provides: octave(generate_html) = 0.1.3


%description
Octave-Forge - Extra packages for GNU Octave.
This package contains the %octave_descr_name GNU Octave extension.

Extension Description:
This package provides functions for generating HTML pages that

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
* Fri Nov 18 2011 Igor Vlasenko <viy@altlinux.ru> 0.1.3-alt1
- initial import by octave-package-builder

