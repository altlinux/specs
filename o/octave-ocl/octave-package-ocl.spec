# BEGIN SourceDeps(oneline):
BuildRequires: makeinfo
# END SourceDeps(oneline)
%def_with _octave_arch
%define octpkg ocl
Name: octave-%octpkg
Version: 1.2.0
Release: alt1
Summary: OpenCL support for GNU Octave

Group: Sciences/Mathematics
License: GPLv3+
URL: http://octave.sf.net

Source0: https://downloads.sourceforge.net/project/octave/Octave%%20Forge%%20Packages/Individual%%20Package%%20Releases/%{octpkg}-%{version}.tar.gz

BuildRequires(pre): rpm-build-octave
BuildRequires: octave-devel
%if_with _octave_arch
BuildRequires: gcc-c++ gcc-g77 libfftw3-devel libhdf5-devel liblapack-devel libncurses-devel libreadline-devel
%else
BuildArch: noarch
%endif
Provides: octave(ocl) = %version
# Depends: octave (>= 4.2.0)
Requires: octave >= 4.2.0


%description
Package using OpenCL for parallelization,

%prep
%setup -n %octpkg-%version

%build
%octave_build

%install
%octave_install

%files
%doc DESCRIPTION COPYING NEWS doc
%_datadir/octave/packages/%octpkg-%version
%if_with _octave_arch
%_libdir/octave/packages/%octpkg-%version
%endif

%changelog
* Tue Nov 08 2022 Andrey Cherepanov <cas@altlinux.org> 1.2.0-alt1
- new version

* Tue Dec 01 2020 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt1
- initial import by package builder

