# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Math/Complex.pm) perl(Module/Signature.pm) perl(Scalar/Util.pm) perl(Socket.pm) perl(overload.pm) perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define upstream_name    Math-Matrix
%define upstream_version 0.91

%{?perl_default_filter}

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    alt1_1

Summary:    Matrix data type (transpose, multiply etc)
License:    GPL or Artistic
Group:      Development/Perl
Source0:    https://cpan.metacpan.org/modules/by-module/Math/%{upstream_name}-%{upstream_version}.tar.gz
Url:        https://metacpan.org/release/%{upstream_name}

BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildRequires: perl(Test/More.pm)
BuildRequires: perl-devel
BuildArch:  noarch
Source44: import.info

%description
The following methods are available: concat, transpose, etc.

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
%doc Changes META.json META.yml  README SIGNATURE
%perl_vendor_privlib/*

%changelog
* Tue Sep 08 2020 Igor Vlasenko <viy@altlinux.ru> 0.91-alt1_1
- update by mgaimport

* Tue Sep 01 2020 Igor Vlasenko <viy@altlinux.ru> 0.91-alt1
- automated CPAN update

* Wed Jul 27 2016 Igor Vlasenko <viy@altlinux.ru> 0.8-alt1_5
- update by mgaimport

* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 0.8-alt1_4
- update by mgaimport

* Thu Oct 16 2014 Igor Vlasenko <viy@altlinux.ru> 0.8-alt1_3
- update by mgaimport

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.8-alt1_2
- update by mgaimport

* Thu Feb 20 2014 Igor Vlasenko <viy@altlinux.ru> 0.8-alt1_1
- moved to Sisyphus

* Tue Oct 29 2013 Igor Vlasenko <viy@altlinux.ru> 0.5-alt1_4
- mga update

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.5-alt1_3
- mgaimport update

* Thu Jul 25 2013 Igor Vlasenko <viy@altlinux.ru> 0.5-alt1_2
- converted for ALT Linux by srpmconvert tools

