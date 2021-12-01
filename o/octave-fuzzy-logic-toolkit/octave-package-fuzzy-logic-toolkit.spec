# BEGIN SourceDeps(oneline):
BuildRequires: makeinfo
# END SourceDeps(oneline)
%define octpkg fuzzy-logic-toolkit
Epoch: 1
Name: octave-%octpkg
Version: 0.4.6
Release: alt1
Summary: Octave Fuzzy Logic Toolkit

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
Provides: octave(fuzzy-logic-toolkit) = %version
# Depends: octave (>= 3.2.4)
Requires: octave >= 3.2.4


%description
A mostly MATLAB-compatible fuzzy logic toolkit for Octave.

%prep
%setup -q -n %{octpkg}

%build
%octave_build

%install
%octave_install

%files
%doc DESCRIPTION ChangeLog COPYING NEWS
%_datadir/octave/packages/%octpkg-%version
%if_with _octave_arch
%_libdir/octave/packages/%octpkg-%version
%endif

%changelog
* Wed Dec 01 2021 Igor Vlasenko <viy@altlinux.org> 1:0.4.6-alt1
- regenerated from template by package builder

* Thu Apr 14 2016 Igor Vlasenko <viy@altlinux.ru> 1:0.4.5-alt1
- regenerated from template by package builder

* Tue Jul 07 2015 Paul Wolneykien <manowar@altlinux.org> 1:0.4.4-alt2
- Rebuild with the next version of Octave: 4.0.0

* Wed Jul 02 2014 Paul Wolneykien <manowar@altlinux.ru> 1:0.4.4-alt1
- updated by octave-package-builder

* Tue Jan 14 2014 Paul Wolneykien <manowar@altlinux.ru> 1:0.4.2-alt2
- Rebuild with the next version of Octave: 3.8.0

* Tue Jan 08 2013 Paul Wolneykien <manowar@altlinux.ru> 1:0.4.2-alt1
- updated by octave-package-builder

* Thu Nov 17 2011 Igor Vlasenko <viy@altlinux.ru> 0.3.0-alt1
- initial import by octave-package-builder

