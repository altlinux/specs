# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/octave makeinfo perl(FileHandle.pm) perl(IPC/Open3.pm) perl(Text/Wrap.pm) texinfo
# END SourceDeps(oneline)
%def_with _octave_arch
%define octave_pkg_version 1.2.1
%define octave_pkg_name communications
%define octave_descr_name Communications
Serial: 1
Name: octave-%octave_pkg_name
Version: 1.2.1
Release: alt1
Summary: Communications

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
Provides: octave(communications) = %version
# Depends: octave (>= 3.4), signal (>= 1.1.3)
Requires: octave >= 3.4 octave(signal) >= 1.1.3


%description
Octave-Forge - Extra packages for GNU Octave.
This package contains the %octave_descr_name GNU Octave extension.

Extension Description:
Digital Communications, Error Correcting Codes (Channel Code), Source Code functions, Modulation and Galois Fields

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
* Thu Apr 14 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.2.1-alt1
- regenerated from template by package builder

* Wed Jan 15 2014 Cronport Service <cronport@altlinux.org> 1:1.2.0-alt0.M70T.1
- backport

* Wed Oct 16 2013 Cronport Service <cronport@altlinux.org> 1:1.1.1-alt1.M70T.1
- backport

* Tue Jan 08 2013 Paul Wolneykien <manowar@altlinux.ru> 1:1.1.1-alt1
- updated by octave-package-builder

* Fri Nov 18 2011 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1
- initial import by octave-package-builder

