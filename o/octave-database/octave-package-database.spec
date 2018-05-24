# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/octave-config libpq-devel makeinfo texinfo
# END SourceDeps(oneline)
%def_with _octave_arch
%define octave_pkg_version 2.4.3
%define octave_pkg_name database
%define octave_descr_name database
Name: octave-%octave_pkg_name
Version: 2.4.3
Release: alt1
Summary: Database.

Group: Sciences/Mathematics
License: GPLv3+
Url: http://octave.sourceforge.net/

Source0: https://downloads.sourceforge.net/project/octave/Octave%%20Forge%%20Packages/Individual%%20Package%%20Releases/%{octave_pkg_name}-%{octave_pkg_version}.tar.gz

BuildRequires: octave-devel
%if_with _octave_arch
BuildRequires: gcc-c++ gcc-g77 libfftw3-devel libhdf5-devel liblapack-devel libncurses-devel libreadline-devel
%else
BuildArch: noarch
%endif
Provides: octave(database) = %version

# octave module BuildRequires: Postgresql (>= 8.3)
BuildRequires: postgresql-devel >= 8.3
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
octave -q -H --no-window-system --no-site-file --eval "pkg build -verbose -nodeps . %SOURCE0"

%install
mkdir -p %buildroot%_datadir/octave/packages
mkdir -p %buildroot%_libdir/octave/packages
%if_with _octave_arch
octave -H --no-window-system --no-site-file --eval "pkg prefix %buildroot%_datadir/octave/packages %buildroot%_libdir/octave/packages; pkg install -nodeps -verbose -local %octave_pkg_name-%octave_pkg_version-$(octave -H --no-window-system --no-site-file --eval "printf([__octave_config_info__(\"canonical_host_type\"), \"-\",  __octave_config_info__(\"api_version\")])").tar.gz"
%else
octave -q -H --no-window-system --no-site-file --eval "pkg prefix %buildroot%_datadir/octave/packages %buildroot%_libdir/octave/packages; pkg install -nodeps -verbose -local %octave_pkg_name-%octave_pkg_version-any-none.tar.gz"
%endif

%files
%_datadir/octave/packages/%octave_pkg_name-%octave_pkg_version
%if_with _octave_arch
%_libdir/octave/packages/%octave_pkg_name-%octave_pkg_version
%endif

%changelog
* Thu May 24 2018 Igor Vlasenko <viy@altlinux.ru> 2.4.3-alt1
- initial import by package builder

