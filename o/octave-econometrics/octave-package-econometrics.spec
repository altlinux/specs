# BEGIN SourceDeps(oneline):
BuildRequires: makeinfo
# END SourceDeps(oneline)
%def_with _octave_arch
%define octave_pkg_version 1.1.1
%define octave_pkg_name econometrics
%define octave_descr_name Econometrics
Name: octave-%octave_pkg_name
Version: 1.1.1
Release: alt3
Summary: Econometrics.

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
Provides: octave(econometrics) = %version
# Depends: octave (>= 2.9.7), optim
Requires: octave >= 2.9.7 octave(optim)


%description
Octave-Forge - Extra packages for GNU Octave.
This package contains the %octave_descr_name GNU Octave extension.

Extension Description:
Econometrics functions including MLE and GMM based techniques.

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
* Thu Apr 14 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt3
- regenerated from template by package builder

* Wed Jan 15 2014 Cronport Service <cronport@altlinux.org> 1.1.1-alt1.M70T.1
- backport

* Wed Oct 16 2013 Cronport Service <cronport@altlinux.org> 1.1.1-alt0.M70T.1
- backport

* Mon Nov 28 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.8-alt1
- initial import by octave-package-builder

