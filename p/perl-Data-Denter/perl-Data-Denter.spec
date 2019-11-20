Group: Development/Perl
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-Data-Denter
Version:        0.15
Release:        alt2_29
License:        GPL+ or Artistic
Summary:        An alternative to Data::Dumper and Storable
Source:         https://cpan.metacpan.org/authors/id/I/IN/INGY/Data-Denter-%{version}.tar.gz
Url:            https://metacpan.org/release/Data-Denter
BuildArch:      noarch
# Build
BuildRequires:  perl-devel
BuildRequires:  rpm-build-perl
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
# Runtime
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(Exporter.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(vars.pm)
# Tests only
BuildRequires:  perl(Data/Dumper.pm)
BuildRequires:  perl(diagnostics.pm)
BuildRequires:  perl(Test.pm)
Source44: import.info

%description
The main problem with Data::Dumper (one of my all-time favorite modules)
is that you have to use 'eval()' to deserialize the data you've dumped.
This is great if you can trust the data you're evaling, but horrible if
you can't. A good alternative is Storable.pm. It can safely thaw your
frozen data.  But if you want to read/edit the frozen data, you're out of
luck, because Storable uses a binary format. Even Data::Dumper's output
can be a little cumbersome for larger data objects. Enter Data::Denter.

Data::Denter is yet another Perl data serializer/deserializer. It formats
nested data structures in an indented fashion. It is optimized for human
readability/editability, safe deserialization, and (eventually) speed.


%prep
%setup -q -n Data-Denter-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
%make_build

%install
make pure_install DESTDIR=%{buildroot}
# %{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendor_privlib}/*

%changelog
* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 0.15-alt2_29
- update to new release by fcimport

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.15-alt2_25
- update to new release by fcimport

* Mon Oct 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.15-alt2_23
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.15-alt2_22
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.15-alt2_21
- update to new release by fcimport

* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.15-alt2_20
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.15-alt2_19
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.15-alt2_17
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.15-alt2_15
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.15-alt2_14
- update to new release by fcimport

* Tue Oct 01 2013 Igor Vlasenko <viy@altlinux.ru> 0.15-alt2_13
- Sisyphus build

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1_13
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1_12
- update to new release by fcimport

* Wed Feb 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1_11
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1_10
- update to new release by fcimport

* Wed May 23 2012 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1_8
- fc import

