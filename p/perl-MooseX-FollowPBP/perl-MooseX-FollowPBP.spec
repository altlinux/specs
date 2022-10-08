# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define upstream_name    MooseX-FollowPBP
%define upstream_version 0.05

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    alt3_11

Summary:    Names accessors in the I<Perl Best Practices> style
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        https://metacpan.org/release/%{upstream_name}
Source0:    https://cpan.metacpan.org/modules/by-module/MooseX/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildRequires: perl(Moose.pm)
BuildRequires: perl(Test/More.pm)
BuildArch:  noarch
Source44: import.info

%description
This module does not provide any methods. Simply loading it changes the
default naming policy for the loading class so that accessors are separated
into get and set methods. The get methods are prefixed with "get_" as the
accessor, while set methods are prefixed with "set_". This is the naming
style recommended by Damian Conway in _Perl Best Practices_.

If you define an attribute with a leading underscore, then both the get and
set method will also have an underscore prefix.

If you explicitly set a "reader" or "writer" name when creating an
attribute, then that attribute's naming scheme is left unchanged.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%makeinstall_std

%files
%doc Changes INSTALL LICENSE META.json META.yml README SIGNATURE
%perl_vendor_privlib/*

%changelog
* Sat Oct 08 2022 Igor Vlasenko <viy@altlinux.org> 0.05-alt3_11
- to Sisyphus as perl-Geo-Gpx dep

* Sun Apr 10 2022 Cronbuild Service <cronbuild@altlinux.org> 0.05-alt2_11
- update by mgaimport

* Sat Feb 15 2020 Igor Vlasenko <viy@altlinux.ru> 0.05-alt2_10
- update by mgaimport

* Thu Oct 04 2018 Igor Vlasenko <viy@altlinux.ru> 0.05-alt2_9
- update by mgaimport

* Wed Jul 27 2016 Igor Vlasenko <viy@altlinux.ru> 0.05-alt2_8
- update by mgaimport

* Sun Feb 21 2016 Igor Vlasenko <viy@altlinux.ru> 0.05-alt2_7
- update by mgaimport

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.05-alt2_6
- update by mgaimport

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.05-alt2_4
- update by mgaimport

* Tue Sep 02 2014 Cronbuild Service <cronbuild@altlinux.org> 0.05-alt2_3
- rebuild to get rid of unmets

* Tue Oct 29 2013 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1_3
- mga update

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1_2
- mgaimport update

* Thu Jul 25 2013 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1_1
- converted for ALT Linux by srpmconvert tools

