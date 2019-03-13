# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/octave-config makeinfo
# END SourceDeps(oneline)
%def_with _octave_arch
%define octave_pkg_name io
Epoch: 1
Name: octave-%octave_pkg_name
Version: 2.4.12
Release: alt1
Summary: Input/Output

Group: Sciences/Mathematics
License: GPLv3+, simplified BSD
URL: http://octave.sf.net

Source0: https://downloads.sourceforge.net/project/octave/Octave%%20Forge%%20Packages/Individual%%20Package%%20Releases/%{octave_pkg_name}-%{version}.tar.gz

BuildRequires: octave-devel
%if_with _octave_arch
BuildRequires: gcc-c++ gcc-g77 libfftw3-devel libhdf5-devel liblapack-devel libncurses-devel libreadline-devel
%else
BuildArch: noarch
%endif
Provides: octave(io) = %version
# Depends: octave (>= 3.8.0)
Requires: octave >= 3.8.0


%description
Input/Output in external formats.

%prep
%setup -q -n %{octave_pkg_name}-%{version}

%build
octave -q -H --no-window-system --no-site-file --eval "pkg build -verbose -nodeps . %SOURCE0"

%install
mkdir -p %buildroot%_datadir/octave/packages
mkdir -p %buildroot%_libdir/octave/packages
%if_with _octave_arch
octave -H --no-window-system --no-site-file --eval "pkg prefix %buildroot%_datadir/octave/packages %buildroot%_libdir/octave/packages; pkg install -nodeps -verbose -local %octave_pkg_name-%version-$(octave -H --no-window-system --no-site-file --eval "printf([__octave_config_info__(\"canonical_host_type\"), \"-\",  __octave_config_info__(\"api_version\")])").tar.gz"
%else
octave -q -H --no-window-system --no-site-file --eval "pkg prefix %buildroot%_datadir/octave/packages %buildroot%_libdir/octave/packages; pkg install -nodeps -verbose -local %octave_pkg_name-%version-any-none.tar.gz"
%endif

%files
%doc DESCRIPTION COPYING NEWS doc
%_datadir/octave/packages/%octave_pkg_name-%version
%if_with _octave_arch
%_libdir/octave/packages/%octave_pkg_name-%version
%endif

%changelog
* Tue Mar 12 2019 Igor Vlasenko <viy@altlinux.ru> 1:2.4.12-alt1
- regenerated from template by package builder

* Mon May 21 2018 Andrey Cherepanov <cas@altlinux.org> 1:2.4.11-alt1
- New version.

* Thu May 18 2017 Paul Wolneykien <manowar@altlinux.org> 1:2.4.7-alt1
- regenerated from template by package builder

* Fri Dec 30 2016 Igor Vlasenko <viy@altlinux.ru> 1:2.4.5-alt1
- regenerated from template by package builder

* Tue Sep 27 2016 Igor Vlasenko <viy@altlinux.ru> 1:2.4.3-alt1
- regenerated from template by package builder

* Wed Apr 13 2016 Igor Vlasenko <viy@altlinux.ru> 1:2.4.1-alt1
- regenerated from template by package builder

* Tue Jul 07 2015 Paul Wolneykien <manowar@altlinux.org> 1:2.2.2-alt2
- Rebuild with the next version of Octave: 4.0.0

* Thu Jun 18 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 1:2.2.2-alt1.1
- Rebuilt for gcc5 C++11 ABI.

* Wed Jul 02 2014 Paul Wolneykien <manowar@altlinux.ru> 1:2.2.2-alt1
- updated by octave-package-builder

* Tue Jan 14 2014 Paul Wolneykien <manowar@altlinux.ru> 1:2.0.2-alt1
- updated by octave-package-builder

* Tue Jan 14 2014 Paul Wolneykien <manowar@altlinux.ru> 1:1.2.3-alt2
- Rebuild with the next version of Octave: 3.8.0

* Thu Oct 10 2013 Paul Wolneykien <manowar@altlinux.ru> 1:1.2.3-alt1
- updated by octave-package-builder

* Tue Jan 08 2013 Paul Wolneykien <manowar@altlinux.ru> 1:1.2.0-alt1
- updated by octave-package-builder

* Thu Nov 17 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.15-alt1
- initial import by octave-package-builder

