# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/octave-config /usr/bin/pg_config libpq-devel makeinfo texinfo
# END SourceDeps(oneline)
%def_with _octave_arch
%define octave_pkg_version 2.4.1
%define octave_pkg_name database
%define octave_descr_name database
Name: octave-%octave_pkg_name
Version: 2.4.1
Release: alt1
Summary: Database.

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
Provides: octave(database) = %version
# Depends: octave (>= 3.6.2), struct (>= 1.0.12)
Requires: octave >= 3.6.2 octave(struct) >= 1.0.12


%description
Octave-Forge - Extra packages for GNU Octave.
This package contains the %octave_descr_name GNU Octave extension.

Extension Description:
Interface to SQL databases, currently only postgresql using libpq.

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
* Fri Apr 15 2016 Igor Vlasenko <viy@altlinux.ru> 2.4.1-alt1
- initial import by package builder

