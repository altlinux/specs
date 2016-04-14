# BEGIN SourceDeps(oneline):
BuildRequires: makeinfo
# END SourceDeps(oneline)
%def_with _octave_arch
%define octave_pkg_version 1.2.1
%define octave_pkg_name miscellaneous
%define octave_descr_name Miscellaneous
Serial: 4
Name: octave-%octave_pkg_name
Version: 1.2.1
Release: alt1
Summary: Miscellaneous functions

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
Provides: octave(miscellaneous) = %version

# SystemRequirements: units
BuildRequires: units

# octave module BuildRequires: termcap-devel [Debian] libncurses5-dev
BuildRequires: libtinfo-devel libncurses-devel
# Depends: octave (>= 3.6.0), general (>= 1.3.1)
Requires: octave >= 3.6.0 octave(general) >= 1.3.1


%description
Octave-Forge - Extra packages for GNU Octave.
This package contains the %octave_descr_name GNU Octave extension.

Extension Description:
Miscellaneous tools that don't fit somewhere else.

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
* Thu Apr 14 2016 Igor Vlasenko <viy@altlinux.ru> 4:1.2.1-alt1
- regenerated from template by package builder

* Tue Jul 07 2015 Paul Wolneykien <manowar@altlinux.org> 4:1.2.0-alt5
- Rebuild with the next version of Octave: 4.0.0

* Thu Jun 18 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 4:1.2.0-alt4.1
- Rebuilt for gcc5 C++11 ABI.

* Tue Jan 14 2014 Paul Wolneykien <manowar@altlinux.ru> 4:1.2.0-alt4
- Rebuild with the next version of Octave: 3.8.0

* Wed Jan 09 2013 Paul Wolneykien <manowar@altlinux.ru> 4:1.2.0-alt3
- updated by octave-package-builder

* Wed Jan 09 2013 Paul Wolneykien <manowar@altlinux.ru> 3:1.2.0-alt2
- updated by octave-package-builder

* Tue Jan 08 2013 Paul Wolneykien <manowar@altlinux.ru> 2:1.2.0-alt1
- updated by octave-package-builder

* Thu Nov 17 2011 Igor Vlasenko <viy@altlinux.ru> 1:1.0.11-alt1
- initial import by octave-package-builder

