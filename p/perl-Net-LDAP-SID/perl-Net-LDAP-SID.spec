# BEGIN SourceDeps(oneline):
BuildRequires: perl(ExtUtils/MakeMaker.pm) perl(Test/More.pm)
# END SourceDeps(oneline)
%define module_version 0.001
%define module_name Net-LDAP-SID
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.001
Release: alt2
Summary: Active Directory Security Identifier manipulation
Group: Development/Perl
License: perl
URL: https://github.com/karpet/net-ldap-sid

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/K/KA/KARMAN/%{module_name}-%{module_version}.tar.gz
BuildArch: noarch

%description
my $sid = Net::LDAP::SID->new( $binary );
 # or
 my $sid = Net::LDAP::SID->new( $string );

 print $sid->as_string;
 print $sid->as_binary;
%prep
%setup -q -n %{module_name}-%{module_version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/N*

%changelog
* Thu Sep 28 2017 Igor Vlasenko <viy@altlinux.ru> 0.001-alt2
- to Sisyphus

* Sun Jul 03 2016 Igor Vlasenko <viy@altlinux.ru> 0.001-alt1
- initial import by package builder

