# BEGIN SourceDeps(oneline):
BuildRequires: makeinfo
# END SourceDeps(oneline)
%define octpkg generate_html
Epoch: 1
Name: octave-%octpkg
Version: 0.3.3
Release: alt1
Summary: Generate HTML web page from help texts

Group: Sciences/Mathematics
License: GPLv3+
Url: http://octave.sourceforge.net/

Source0: https://downloads.sourceforge.net/project/octave/Octave%%20Forge%%20Packages/Individual%%20Package%%20Releases/%{octpkg}-%{version}.tar.gz

BuildRequires(pre): rpm-build-octave
BuildRequires: octave-devel
%if_with _octave_arch
BuildRequires: gcc-c++ gcc-g77 libfftw3-devel libhdf5-devel liblapack-devel libncurses-devel libreadline-devel
%else
BuildArch: noarch
%endif
Provides: octave(generate_html) = %version

# SystemRequirements: makeinfo [Debian] texinfo
BuildRequires: /usr/bin/makeinfo texinfo
# Depends: octave (>= 3.2.0)
Requires: octave >= 3.2.0


%description
This package provides functions for generating HTML pages that

%prep
%setup -q -n %{octpkg}-%{version}

%build
%octave_build

%install
%octave_install

%files
%doc DESCRIPTION COPYING NEWS
%_datadir/octave/packages/%octpkg-%version
%if_with _octave_arch
%_libdir/octave/packages/%octpkg-%version
%endif

%changelog
* Tue Nov 08 2022 Andrey Cherepanov <cas@altlinux.org> 1:0.3.3-alt1
- new version

* Tue Dec 01 2020 Igor Vlasenko <viy@altlinux.ru> 1:0.3.2-alt1
- regenerated from template by package builder

* Sat May 26 2018 Igor Vlasenko <viy@altlinux.ru> 1:0.3.1-alt1
- build for octave 4.4

* Wed Apr 13 2016 Igor Vlasenko <viy@altlinux.ru> 1:0.1.10-alt1
- regenerated from template by package builder

* Tue Jul 07 2015 Paul Wolneykien <manowar@altlinux.org> 1:0.1.5-alt3
- Rebuild with the next version of Octave: 4.0.0

* Tue Jan 14 2014 Paul Wolneykien <manowar@altlinux.ru> 1:0.1.5-alt2
- Rebuild with the next version of Octave: 3.8.0

* Tue Jan 08 2013 Paul Wolneykien <manowar@altlinux.ru> 1:0.1.5-alt1
- updated by octave-package-builder

* Fri Nov 18 2011 Igor Vlasenko <viy@altlinux.ru> 0.1.3-alt1
- initial import by octave-package-builder

