# BEGIN SourceDeps(oneline):
BuildRequires: makeinfo
# END SourceDeps(oneline)
%define octpkg matgeom
Name: octave-%octpkg
Version: 1.2.3
Release: alt1
Summary: Computational Geometry

Group: Sciences/Mathematics
License: FreeBSD
URL: https://github.com/mattools/matGeom

Source0: https://downloads.sourceforge.net/project/octave/Octave%%20Forge%%20Packages/Individual%%20Package%%20Releases/%{octpkg}-%{version}.tar.gz

BuildRequires(pre): rpm-build-octave
BuildRequires: octave-devel
%if_with _octave_arch
BuildRequires: gcc-c++ gcc-g77 libfftw3-devel libhdf5-devel liblapack-devel libncurses-devel libreadline-devel
%else
BuildArch: noarch
%endif
Provides: octave(matgeom) = %version
# Depends: octave (>= 4.2.0)
Requires: octave >= 4.2.0


%description
Geometry toolbox for 2D/3D geometric computing

%prep
%setup -q -n %{octpkg}-%{version}

%build
%octave_build

%install
%octave_install

%files
%doc DESCRIPTION NEWS COPYING
%_datadir/octave/packages/%octpkg-%version
%if_with _octave_arch
%_libdir/octave/packages/%octpkg-%version
%endif

%changelog
* Wed Dec 01 2021 Igor Vlasenko <viy@altlinux.org> 1.2.3-alt1
- regenerated from template by package builder

* Tue Dec 01 2020 Igor Vlasenko <viy@altlinux.ru> 1.2.2-alt1
- initial import by package builder

