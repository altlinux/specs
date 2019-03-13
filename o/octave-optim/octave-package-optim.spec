# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/octave-config makeinfo texinfo
# END SourceDeps(oneline)
%def_with _octave_arch
%define octave_pkg_name optim
Epoch: 1
Name: octave-%octave_pkg_name
Version: 1.5.3
Release: alt1
Summary: Optimization.

Group: Sciences/Mathematics
License: GPLv3+, modified BSD, public domain
Url: http://octave.sourceforge.net/

Source0: https://downloads.sourceforge.net/project/octave/Octave%%20Forge%%20Packages/Individual%%20Package%%20Releases/%{octave_pkg_name}-%{version}.tar.gz

BuildRequires: octave-devel
%if_with _octave_arch
BuildRequires: gcc-c++ gcc-g77 libfftw3-devel libhdf5-devel liblapack-devel libncurses-devel libreadline-devel
%else
BuildArch: noarch
%endif
Provides: octave(optim) = %version
# Depends: octave (>= 3.6.0), struct (>= 1.0.12), statistics (>= 1.4.0)
Requires: octave >= 3.6.0 octave(struct) >= 1.0.12 octave(statistics) >= 1.4.0


%description
Non-linear optimization toolkit.

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
* Tue Mar 12 2019 Igor Vlasenko <viy@altlinux.ru> 1:1.5.3-alt1
- regenerated from template by package builder

* Tue Feb 12 2019 Andrey Bychkov <mrdrew@altlinux.org> 1:1.5.2-alt4
- no return statement in the non-void function fixed (according g++8)

* Tue May 22 2018 Igor Vlasenko <viy@altlinux.ru> 1:1.5.2-alt3
- rebuild with octave 4.4

* Thu May 18 2017 Paul Wolneykien <manowar@altlinux.org> 1:1.5.2-alt2
- regenerated from template by package builder

* Tue Nov 01 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.5.2-alt1
- regenerated from template by package builder

* Tue Sep 27 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.5.1-alt1
- regenerated from template by package builder

* Wed Apr 13 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.5.0-alt1
- initial import by package builder

