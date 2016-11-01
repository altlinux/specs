# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/octave-config makeinfo texinfo
# END SourceDeps(oneline)
%def_with _octave_arch
%define octave_pkg_version 3.1.1
%define octave_pkg_name parallel
%define octave_descr_name parallel
Name: octave-%octave_pkg_name
Version: 3.1.1
Release: alt1
Summary: Parallel Computing.

Group: Sciences/Mathematics
License: GPLv3+
URL: http://octave.sf.net

Source0: http://downloads.sourceforge.net/octave/%{octave_pkg_name}-%{octave_pkg_version}.tar.gz

BuildRequires: octave-devel
%if_with _octave_arch
BuildRequires: gcc-c++ gcc-g77 libfftw3-devel libhdf5-devel liblapack-devel libncurses-devel libreadline-devel
%else
BuildArch: noarch
%endif
Provides: octave(parallel) = %version

# octave module BuildRequires: libgnutls..-dev
BuildRequires: libgnutls-devel
# Depends: octave (>= 3.8.0), struct (>= 1.0.12)
Requires: octave >= 3.8.0 octave(struct) >= 1.0.12


%description
Octave-Forge - Extra packages for GNU Octave.
This package contains the %octave_descr_name GNU Octave extension.

Extension Description:
Parallel execution package. See also package mpi, maintained

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
* Tue Nov 01 2016 Igor Vlasenko <viy@altlinux.ru> 3.1.1-alt1
- regenerated from template by package builder

* Tue Sep 27 2016 Igor Vlasenko <viy@altlinux.ru> 3.1.0-alt1
- regenerated from template by package builder

* Wed Apr 13 2016 Igor Vlasenko <viy@altlinux.ru> 3.0.4-alt1
- regenerated from template by package builder

* Tue Jul 07 2015 Paul Wolneykien <manowar@altlinux.org> 2.2.0-alt2
- Rebuild with the next version of Octave: 4.0.0

* Thu Jun 18 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.2.0-alt1.1
- Rebuilt for gcc5 C++11 ABI.

* Wed Jul 02 2014 Paul Wolneykien <manowar@altlinux.ru> 2.2.0-alt1
- updated by octave-package-builder

* Tue Jan 14 2014 Paul Wolneykien <manowar@altlinux.ru> 2.1.1-alt1
- updated by octave-package-builder

