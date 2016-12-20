Name: perl-Server-Starter
Version: 0.33
Release: alt1

Summary: Server::Starter - a superdaemon for hot-deploying server programs
License: Perl
Group: Development/Perl

Url: %CPAN Server-Starter
# Cloned from git://github.com/kazuho/p5-Server-Starter.git
Source: %name-%version.tar

BuildArch: noarch
BuildRequires: perl-Test-TCP perl-Proc-Wait3 perl-Scope-Guard perl-List-MoreUtils perl-Module-Install perl(Test/Requires.pm)

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%_bindir/start_server
%_man1dir/start_server*
%perl_vendor_privlib/Server/Starter*
%doc Changes README*

%changelog
* Tue Dec 20 2016 Igor Vlasenko <viy@altlinux.ru> 0.33-alt1
- automated CPAN update

* Fri Oct 16 2015 Igor Vlasenko <viy@altlinux.ru> 0.32-alt1
- automated CPAN update

* Sat Jan 03 2015 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1
- automated CPAN update

* Fri Jul 25 2014 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1
- automated CPAN update

* Sun Jun 29 2014 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1
- automated CPAN update

* Mon Oct 01 2012 Vladimir Lettiev <crux@altlinux.ru> 0.12-alt1
- 0.11 -> 0.12

* Sat Jul 30 2011 Vladimir Lettiev <crux@altlinux.ru> 0.11-alt1
- initial build
