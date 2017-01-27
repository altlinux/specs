%def_with _octave_arch
%define octave_pkg_version 1.2.1
%define octave_pkg_name zeromq
%define octave_descr_name zeromq
# BEGIN SourceDeps(oneline):
BuildRequires: makeinfo
# END SourceDeps(oneline)
%def_with _octave_arch
Name: octave-%octave_pkg_name
Version: 1.2.1
Release: alt1.1
Summary: ZeroMQ Toolbox

Group: Sciences/Mathematics
License: GPLv3+
URL: http://octave.sourceforge.net

Source0: http://downloads.sourceforge.net/octave/%{octave_pkg_name}-%{octave_pkg_version}.tar.gz

BuildRequires: octave-devel
%if_with _octave_arch
BuildRequires: gcc-c++ gcc-g77 libfftw3-devel libhdf5-devel liblapack-devel libncurses-devel libreadline-devel
%else
BuildArch: noarch
%endif
Provides: octave(zeromq) = %version

Provides: octave(zeromq) = %version

# SystemRequirements: zmq
BuildRequires: libzeromq-devel
# Depends: octave (>= 4.0.0)
Requires: octave >= 4.0.0


%description
Octave-Forge - Extra packages for GNU Octave.
This package contains the %octave_descr_name GNU Octave extension.

Extension Description:
ZeroMQ bindings for GNU Octave

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
* Fri Jan 27 2017 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1.1
- rebuild

* Tue Sep 27 2016 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1
- regenerated from template by package builder

* Wed Apr 13 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1
- initial import by package builder

