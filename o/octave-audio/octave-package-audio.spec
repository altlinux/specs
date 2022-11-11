# BEGIN SourceDeps(oneline):
BuildRequires: makeinfo texinfo
# END SourceDeps(oneline)
%def_with _octave_arch
%define octpkg audio
Name: octave-%octpkg
Version: 2.0.4
Release: alt1
Summary: Audio Toolbox

Group: Sciences/Mathematics
License: GPLv3+
URL: http://octave.sourceforge.net

Source0: https://downloads.sourceforge.net/project/octave/Octave%%20Forge%%20Packages/Individual%%20Package%%20Releases/%{octpkg}-%{version}.tar.gz

BuildRequires(pre): rpm-build-octave
BuildRequires: octave-devel
%if_with _octave_arch
BuildRequires: gcc-c++ gcc-g77 libfftw3-devel libhdf5-devel liblapack-devel libncurses-devel libreadline-devel
%else
BuildArch: noarch
%endif
Provides: octave(audio) = %version

# SystemRequirements: rtmidi
BuildRequires: librtmidi-devel
# Depends: octave (>= 4.0.0)
Requires: octave >= 4.0.0


%description
Audio and MIDI Toolbox for GNU Octave

%prep
%setup -q -n %{octpkg}-%{version}

%build
%octave_build

%install
%octave_install

%files
%doc DESCRIPTION README.md NEWS COPYING doc
%_datadir/octave/packages/%octpkg-%version
%if_with _octave_arch
%_libdir/octave/packages/%octpkg-%version
%endif

%changelog
* Fri Apr 08 2022 Andrey Cherepanov <cas@altlinux.org> 2.0.4-alt1
- new version

* Wed Dec 01 2021 Igor Vlasenko <viy@altlinux.org> 2.0.3-alt1
- regenerated from template by package builder

* Tue Dec 01 2020 Igor Vlasenko <viy@altlinux.ru> 2.0.2-alt1
- regenerated from template by package builder

* Tue Jul 07 2015 Paul Wolneykien <manowar@altlinux.org> 1.1.4-alt3
- Rebuild with the next version of Octave: 4.0.0

* Thu Jun 18 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.1.4-alt2.1
- Rebuilt for gcc5 C++11 ABI.

* Tue Jan 14 2014 Paul Wolneykien <manowar@altlinux.ru> 1.1.4-alt2
- Rebuild with the next version of Octave: 3.8.0

* Fri Nov 18 2011 Igor Vlasenko <viy@altlinux.ru> 1.1.4-alt1
- initial import by octave-package-builder

