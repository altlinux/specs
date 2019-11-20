Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
BuildRequires: gcc-c++
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-Boost-Geometry-Utils
Version:        0.15
Release:        alt2_24
Summary:        Boost::Geometry::Utils Perl module
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Boost-Geometry-Utils
Source0:        https://cpan.metacpan.org/authors/id/A/AA/AAR/Boost-Geometry-Utils-%{version}.tar.gz
# Fix for RT#96145
Patch0:         Boost-Geometry-Utils-0.15-multi_linestring2perl-only-extend-the-array-if-needed.patch
BuildRequires:  gcc-c++
BuildRequires:  perl-devel
BuildRequires:  rpm-build-perl
BuildRequires:  perl(Exporter.pm)
BuildRequires:  perl(ExtUtils/CBuilder.pm)
BuildRequires:  perl(ExtUtils/Typemaps/Default.pm)
BuildRequires:  perl(File/Temp.pm)
BuildRequires:  perl(Module/Build.pm)
BuildRequires:  perl(Module/Build/WithXSpp.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(XSLoader.pm)

 # Filters (not)shared c libs
Source44: import.info

%description
Boost::Geometry::Utils Perl module

%prep
%setup -q -n Boost-Geometry-Utils-%{version}
%patch0 -p1

%build
perl Build.PL installdirs=vendor optimize="$RPM_OPT_FLAGS"
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;

# %{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc CHANGES LICENSE README
%{perl_vendor_archlib}/auto/*
%{perl_vendor_archlib}/Boost*

%changelog
* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 0.15-alt2_24
- update to new release by fcimport

* Thu Jan 24 2019 Igor Vlasenko <viy@altlinux.ru> 0.15-alt2_20
- rebuild with new perl 5.28.1

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1_20
- update to new release by fcimport

* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1_19
- update to new release by fcimport

* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1_17.1
- rebuild with new perl 5.26.1

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1_17
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1_15
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1_13
- update to new release by fcimport

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1_12.1
- rebuild with new perl 5.24.1

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1_12
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1_11
- update to new release by fcimport

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1_10.1
- rebuild with new perl 5.22.0

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1_10
- update to new release by fcimport

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1_7.1
- rebuild with new perl 5.20.1

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1_7
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1_6
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1_4
- update to new release by fcimport

* Wed Feb 26 2014 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1_3
- moved to Sisyphus for Slic3r (by dd@ request)

