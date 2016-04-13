# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/octave /usr/bin/octave-config makeinfo
# END SourceDeps(oneline)
%def_with _octave_arch
%define octave_pkg_version 1.1.10
%define octave_pkg_name octcdf
%define octave_descr_name octcdf
Name: octave-%octave_pkg_name
Version: 1.1.10
Release: alt1
Summary: octcdf

Group: Sciences/Mathematics
License: GPLv2+
URL: http://octave.sf.net

Source0: http://downloads.sourceforge.net/octave/%{octave_pkg_name}-%{octave_pkg_version}.tar.gz

BuildRequires: octave-devel
%if_with _octave_arch
BuildRequires: gcc-c++ gcc-g77 libfftw3-devel libhdf5-devel liblapack-devel libncurses-devel libreadline-devel
%else
BuildArch: noarch
%endif
Provides: octave(octcdf) = %version

# octave module BuildRequires: netcdf-devel
BuildRequires: libnetcdf-devel
# Depends: octave (>= 3.4.0)
Requires: octave >= 3.4.0


%description
Octave-Forge - Extra packages for GNU Octave.
This package contains the %octave_descr_name GNU Octave extension.

Extension Description:
A NetCDF interface for octave. This interface is obsolete. Please use the netcdf package instead (possibly in combination with ncarray).

%prep
%setup -q -n %{octave_pkg_name}

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
* Wed Apr 13 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.10-alt1
- initial import by package builder

