# BEGIN SourceDeps(oneline):
BuildRequires: makeinfo texinfo
# END SourceDeps(oneline)
%define octpkg queueing
Name: octave-%octpkg
Version: 1.2.8
Release: alt1
Summary: Octave package for Queueing Networks and Markov chains analysis

Group: Sciences/Mathematics
License: GPLv3+
URL: http://www.moreno.marzolla.name/software/queueing/

Source0: https://downloads.sourceforge.net/project/octave/Octave%%20Forge%%20Packages/Individual%%20Package%%20Releases/%{octpkg}-%{version}.tar.gz

BuildRequires(pre): rpm-build-octave
BuildRequires: octave-devel
%if_with _octave_arch
BuildRequires: gcc-c++ gcc-g77 libfftw3-devel libhdf5-devel liblapack-devel libncurses-devel libreadline-devel
%else
BuildArch: noarch
%endif
Provides: octave(queueing) = %version
# Depends: octave (>= 4.0.0)
Requires: octave >= 4.0.0


%description
The queueing package provides functions for queueing

%prep
%setup -q -n %{octpkg}

%build
%octave_build

%install
%octave_install

%files
%doc DESCRIPTION NEWS COPYING doc
%_datadir/octave/packages/%octpkg-%version
%if_with _octave_arch
%_libdir/octave/packages/%octpkg-%version
%endif

%changelog
* Wed Feb 19 2025 Andrey Cherepanov <cas@altlinux.org> 1.2.8-alt1
- new version

* Tue Dec 01 2020 Igor Vlasenko <viy@altlinux.ru> 1.2.7-alt1
- regenerated from template by package builder

* Tue Mar 12 2019 Igor Vlasenko <viy@altlinux.ru> 1.2.6-alt1
- regenerated from template by package builder

* Thu May 24 2018 Igor Vlasenko <viy@altlinux.ru> 1.2.5-alt1
- initial import by package builder

