%define module_name Net-SMTPS
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Authen/SASL.pm) perl(ExtUtils/MakeMaker.pm) perl(IO/Socket/SSL.pm) perl(Net/SMTP.pm) perl(base.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.09
Release: alt2
Summary: SSL/STARTTLS support for Net::SMTP
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/T/TO/TOMO/src/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
%summary

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/N*

%changelog
* Sat Jun 02 2018 Igor Vlasenko <viy@altlinux.ru> 0.09-alt2
- to Sisyphus as devscripts dep

* Sun Nov 05 2017 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1
- regenerated from template by package builder

* Sun Sep 24 2017 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- regenerated from template by package builder

* Mon May 01 2017 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- regenerated from template by package builder

* Sun Feb 26 2017 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- regenerated from template by package builder

* Mon Nov 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- regenerated from template by package builder

* Thu Sep 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- initial import by package builder

