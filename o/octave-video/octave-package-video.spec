%def_with _octave_arch
%define octave_pkg_version 1.2.3
%define octave_pkg_name video
%define octave_descr_name video
# BEGIN SourceDeps(oneline):
BuildRequires: makeinfo
# END SourceDeps(oneline)
%def_with _octave_arch
Name: octave-%octave_pkg_name
Version: 1.2.3
Release: alt1
Summary: Video functions

Group: Sciences/Mathematics
License: FreeBSD
URL: http://octave.sf.net

Source0: http://downloads.sourceforge.net/octave/%{octave_pkg_name}-%{octave_pkg_version}.tar.gz

BuildRequires: octave-devel
%if_with _octave_arch
BuildRequires: gcc-c++ gcc-g77 libfftw3-devel libhdf5-devel liblapack-devel libncurses-devel libreadline-devel
%else
BuildArch: noarch
%endif
Provides: octave(video) = %version

Provides: octave(video) = %version

# octave module BuildRequires: libavutil-dev libavformat-dev libswscale-dev libavcodec-dev from Debian Jessie
BuildRequires: libavutil-devel libavformat-devel libswscale-devel libavcodec-devel
# Depends: octave (>= 3.8.2)
Requires: octave >= 3.8.2


%description
Octave-Forge - Extra packages for GNU Octave.
This package contains the %octave_descr_name GNU Octave extension.

Extension Description:
A wrapper for ffmpeg's libavformat and libavcodec, implementing

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
* Tue Sep 27 2016 Igor Vlasenko <viy@altlinux.ru> 1.2.3-alt1
- regenerated from template by package builder

* Wed Apr 13 2016 Igor Vlasenko <viy@altlinux.ru> 1.2.2-alt1
- initial import by package builder

