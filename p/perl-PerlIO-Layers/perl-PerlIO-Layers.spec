Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-PerlIO-Layers
Version:        0.011
Release:        alt2_19
Summary:        Querying your file handle capabilities
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/PerlIO-Layers
Source0:        https://cpan.metacpan.org/authors/id/L/LE/LEONT/PerlIO-Layers-%{version}.tar.gz
BuildRequires:  perl-devel
BuildRequires:  perl-devel
BuildRequires:  rpm-build-perl
BuildRequires:  perl(ExtUtils/CBuilder.pm)
BuildRequires:  perl(Module/Build.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(warnings.pm)
# Run-time
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(Exporter.pm)
BuildRequires:  perl(List/Util.pm)
BuildRequires:  perl(PerlIO.pm)
BuildRequires:  perl(XSLoader.pm)
# Tests
BuildRequires:  perl(Data/Dumper.pm)
BuildRequires:  perl(File/Spec.pm)
BuildRequires:  perl(IO/Handle.pm)
BuildRequires:  perl(IPC/Open3.pm)
BuildRequires:  perl(Test/More.pm)


Source44: import.info

%description
Perl file handles are implemented as a stack of layers, with the bottom-most
usually doing the actual IO and the higher ones doing buffering,
encoding/decoding or transformations. PerlIO::Layers allows you to query the
file handle properties concerning these layers.

%prep
%setup -q -n PerlIO-Layers-%{version}

%build
perl Build.PL installdirs=vendor optimize="$RPM_OPT_FLAGS"
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
# %{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes LICENSE README
%{perl_vendor_archlib}/auto/*
%{perl_vendor_archlib}/PerlIO*

%changelog
* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 0.011-alt2_19
- update to new release by fcimport

* Thu Jan 24 2019 Igor Vlasenko <viy@altlinux.ru> 0.011-alt2_15
- rebuild with new perl 5.28.1

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.011-alt1_15
- update to new release by fcimport

* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 0.011-alt1_14
- update to new release by fcimport

* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.011-alt1_12.1
- rebuild with new perl 5.26.1

* Mon Oct 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.011-alt1_12
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.011-alt1_10
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.011-alt1_9
- update to new release by fcimport

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.011-alt1_8.1
- rebuild with new perl 5.24.1

* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.011-alt1_8
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.011-alt1_7
- update to new release by fcimport

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.011-alt1_6.1
- rebuild with new perl 5.22.0

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.011-alt1_6
- update to new release by fcimport

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.011-alt1_4.1
- rebuild with new perl 5.20.1

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.011-alt1_4
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.011-alt1_3
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.011-alt1_2
- update to new release by fcimport

* Wed Mar 19 2014 Igor Vlasenko <viy@altlinux.ru> 0.011-alt1_1
- update to new release by fcimport

* Mon Mar 10 2014 Igor Vlasenko <viy@altlinux.ru> 0.011-alt1
- automated CPAN update

* Wed Feb 19 2014 Igor Vlasenko <viy@altlinux.ru> 0.010-alt3_6
- moved to Sisyphus for Slic3r (by dd@ request)

* Thu Sep 05 2013 Cronbuild Service <cronbuild@altlinux.org> 0.010-alt2_6
- rebuild to get rid of unmets

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.010-alt1_6
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.010-alt1_5
- update to new release by fcimport

* Mon Mar 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.010-alt1_4
- update to new release by fcimport

* Thu Dec 13 2012 Igor Vlasenko <viy@altlinux.ru> 0.010-alt1_3
- initial release

