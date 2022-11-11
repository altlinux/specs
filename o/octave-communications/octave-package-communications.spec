# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/octave makeinfo texinfo
# END SourceDeps(oneline)
%def_with _octave_arch
%define octpkg communications
Epoch: 1
Name: octave-%octpkg
Version: 1.2.4
Release: alt1
Summary: Communications

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
Provides: octave(communications) = %version
# Depends: octave (>= 4.4), signal (>= 1.1.3)
Requires: octave >= 4.4 octave(signal) >= 1.1.3


%description
Digital Communications, Error Correcting Codes (Channel Code), Source Code functions, Modulation and Galois Fields

%prep
%setup -q -n %{octpkg}-%{version}

%build
%octave_build

%install
%octave_install

%files
%doc COPYING DESCRIPTION NEWS doc
%_datadir/octave/packages/%octpkg-%version
%if_with _octave_arch
%_libdir/octave/packages/%octpkg-%version
%endif

%changelog
* Fri Apr 08 2022 Andrey Cherepanov <cas@altlinux.org> 1:1.2.4-alt1
- new version

* Wed Dec 01 2021 Igor Vlasenko <viy@altlinux.org> 1:1.2.3-alt1
- regenerated from template by package builder

* Tue Dec 01 2020 Igor Vlasenko <viy@altlinux.ru> 1:1.2.2-alt1
- regenerated from template by package builder

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

