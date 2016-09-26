# BEGIN SourceDeps(oneline):
BuildRequires: makeinfo
# END SourceDeps(oneline)
%def_with _octave_arch
%define octave_pkg_version 0.2.2
%define octave_pkg_name image-acquisition
%define octave_descr_name image-acquisition
Name: octave-%octave_pkg_name
Version: 0.2.2
Release: alt1
Summary: Image Acquisition

Group: Sciences/Mathematics
License: GPLv3+
Url: http://octave.sourceforge.net/

Source0: http://downloads.sourceforge.net/octave/%{octave_pkg_name}-%{octave_pkg_version}.tar.gz

BuildRequires: octave-devel
%if_with _octave_arch
BuildRequires: gcc-c++ gcc-g77 libfftw3-devel libhdf5-devel liblapack-devel libncurses-devel libreadline-devel
%else
BuildArch: noarch
%endif
Provides: octave(image-acquisition) = %version

# octave module BuildRequires: libv4l-dev (>= 0.8.8), libfltk1.1-dev (>= 1.1.0)
BuildRequires: libv4l-devel >= 0.8.8 libfltk-devel >= 1.1.0
# Depends: octave (>= 3.8.0)
Requires: octave >= 3.8.0


%description
Octave-Forge - Extra packages for GNU Octave.
This package contains the %octave_descr_name GNU Octave extension.

Extension Description:
The Octave-forge Image Aquisition package provides functions

%prep
%setup -q -n %{octave_pkg_name}-%{octave_pkg_version}

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
* Tue Sep 27 2016 Igor Vlasenko <viy@altlinux.ru> 0.2.2-alt1
- initial import by package builder

