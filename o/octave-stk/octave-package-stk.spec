# BEGIN SourceDeps(oneline):
BuildRequires: makeinfo
# END SourceDeps(oneline)
%def_with _octave_arch
%define octave_pkg_name stk
Name: octave-%octave_pkg_name
Version: 2.5.1
Release: alt1
Summary: STK: A Small Toolbox for Kriging

Group: Sciences/Mathematics
License: GPLv3+
URL: https://sourceforge.net/projects/kriging/

Source0: https://downloads.sourceforge.net/project/octave/Octave%%20Forge%%20Packages/Individual%%20Package%%20Releases/%{octave_pkg_name}-%{version}.tar.gz

BuildRequires: octave-devel
%if_with _octave_arch
BuildRequires: gcc-c++ gcc-g77 libfftw3-devel libhdf5-devel liblapack-devel libncurses-devel libreadline-devel
%else
BuildArch: noarch
%endif
Provides: octave(stk) = %version
# Depends: octave (>= 3.6.0)
Requires: octave >= 3.6.0


%description
The STK is a (not so) Small Toolbox for Kriging. Its primary

%prep
%setup -q -n %{octave_pkg_name}

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
%doc ChangeLog NEWS COPYING DESCRIPTION doc
%_datadir/octave/packages/%octave_pkg_name-%version
%if_with _octave_arch
%_libdir/octave/packages/%octave_pkg_name-%version
%endif

%changelog
* Tue Mar 12 2019 Igor Vlasenko <viy@altlinux.ru> 2.5.1-alt1
- regenerated from template by package builder

* Thu May 24 2018 Igor Vlasenko <viy@altlinux.ru> 2.5.0-alt1
- regenerated from template by package builder

* Tue May 22 2018 Igor Vlasenko <viy@altlinux.ru> 2.4.2-alt2
- rebuild with octave 4.4

* Thu May 18 2017 Paul Wolneykien <manowar@altlinux.org> 2.4.2-alt1
- regenerated from template by package builder

* Thu Apr 14 2016 Igor Vlasenko <viy@altlinux.ru> 2.3.4-alt1
- initial import by package builder

