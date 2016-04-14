# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/octave makeinfo
# END SourceDeps(oneline)
%def_with _octave_arch
%define octave_pkg_version 2.2.2
%define octave_pkg_name linear-algebra
%define octave_descr_name Linear-algebra
Serial: 1
Name: octave-%octave_pkg_name
Version: 2.2.2
Release: alt1
Summary: Linear algebra.

Group: Sciences/Mathematics
License: GPLv3+, LGPLv3+, FreeBSD
URL: http://octave.sf.net

Source0: http://downloads.sourceforge.net/octave/%{octave_pkg_name}-%{octave_pkg_version}.tar.gz

BuildRequires: octave-devel
%if_with _octave_arch
BuildRequires: gcc-c++ gcc-g77 libfftw3-devel libhdf5-devel liblapack-devel libncurses-devel libreadline-devel
%else
BuildArch: noarch
%endif
Provides: octave(linear-algebra) = %version
# Depends: octave (>= 4.0.0)
Requires: octave >= 4.0.0


%description
Octave-Forge - Extra packages for GNU Octave.
This package contains the %octave_descr_name GNU Octave extension.

Extension Description:
Additional linear algebra code, including general SVD and matrix functions.

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
* Thu Apr 14 2016 Igor Vlasenko <viy@altlinux.ru> 1:2.2.2-alt1
- regenerated from template by package builder

* Wed Jan 15 2014 Cronport Service <cronport@altlinux.org> 1:2.2.0-alt1.M70T.1
- backport

* Tue Jan 08 2013 Paul Wolneykien <manowar@altlinux.ru> 1:2.2.0-alt1
- updated by octave-package-builder

* Thu Nov 17 2011 Igor Vlasenko <viy@altlinux.ru> 2.1.0-alt1
- initial import by octave-package-builder

