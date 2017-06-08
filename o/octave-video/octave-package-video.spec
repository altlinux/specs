# BEGIN SourceDeps(oneline):
BuildRequires: makeinfo
# END SourceDeps(oneline)
%def_with _octave_arch
%define octave_pkg_version 1.2.3
%define octave_pkg_name video
%define octave_descr_name video
Name: octave-%octave_pkg_name
Version: 1.2.3
Release: alt2.1
Summary: Video functions

Group: Sciences/Mathematics
License: FreeBSD
URL: http://octave.sf.net

Source0: https://downloads.sourceforge.net/project/octave/Octave%%20Forge%%20Packages/Individual%%20Package%%20Releases/%{octave_pkg_name}-%{octave_pkg_version}.tar.gz

BuildRequires: octave-devel
%if_with _octave_arch
BuildRequires: gcc-c++ gcc-g77 libfftw3-devel libhdf5-devel liblapack-devel libncurses-devel libreadline-devel
BuildRequires: libGL-devel libGLU-devel libGraphicsMagick-c++-devel libGraphicsMagick-devel fontconfig-devel libfreetype-devel libX11-devel libgl2ps-devel libcurl-devel libsuitesparse-devel libarpack-ng-devel libqrupdate-devel libpcre-devel
%else
BuildArch: noarch
%endif
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
%define build_flags CXXFLAGS=$CXXFLAGS
%build_flags octave -H --no-site-file --eval "pkg build -verbose -nodeps . %SOURCE0"

%install
mkdir -p %buildroot%_datadir/octave/packages
mkdir -p %buildroot%_libdir/octave/packages
octave -H --no-site-file --eval "pkg prefix %buildroot%_datadir/octave/packages %buildroot%_libdir/octave/packages; pkg install -verbose -local -nodeps %octave_pkg_name-%octave_pkg_version-$(octave -H --no-site-file --eval "printf([__octave_config_info__(\"canonical_host_type\"), \"-\",  __octave_config_info__(\"api_version\")])").tar.gz"

%files
%_datadir/octave/packages/%octave_pkg_name-%octave_pkg_version
%if_with _octave_arch
%_libdir/octave/packages/%octave_pkg_name-%octave_pkg_version
%endif

%changelog
* Thu Jun 08 2017 Igor Vlasenko <viy@altlinux.ru> 1.2.3-alt2.1
- rebuild with ffmpeg

* Thu May 18 2017 Paul Wolneykien <manowar@altlinux.org> 1.2.3-alt2
- regenerated from template by package builder

* Tue Sep 27 2016 Igor Vlasenko <viy@altlinux.ru> 1.2.3-alt1
- regenerated from template by package builder

* Wed Apr 13 2016 Igor Vlasenko <viy@altlinux.ru> 1.2.2-alt1
- initial import by package builder

