%define module_name Term-ProgressBar

Name: perl-%module_name
Version: 2.18
Release: alt1

Summary: Provides a progress meter on a standard terminal
Summary(ru_RU.UTF-8): Индикатор процесса в консоли.
Group: Development/Perl
URL: http://ftp.spbu.ru/CPAN/authors/id/F/FL/FLUFFY
License: GPL or Artistic
Source: http://www.cpan.org/authors/id/M/MA/MANWAR/Term-ProgressBar-%{version}.tar.gz
Buildarch: noarch
AutoReqProv: yes, perl
BuildRequires: perl-Class-MethodMaker perl-Module-Build perl-Term-ReadKey perl-devel perl(Test/Exception.pm) perl(Capture/Tiny.pm)
BuildRequires: perl-autodie

%description
Term::ProgressBar provides a simple progress bar on the terminal, to
let the user know that something is happening, roughly how much stuff
has been done, and maybe an estimate at how long remains.

%description -l ru_RU.UTF-8
Модуль Term::ProgressBar реализует простой индикатор процесса для 
консоли, который позволяет программе сообщать о том, что выполняется
работа, какая примерно часть сделана, и возможно оценку оставшегося времени.

%prep
%setup -q -n %module_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
#%doc README Changes
%perl_vendorlib/Term/ProgressBar.pm

%changelog
* Sun Dec 18 2016 Igor Vlasenko <viy@altlinux.ru> 2.18-alt1
- automated CPAN update

* Mon Jan 26 2015 Igor Vlasenko <viy@altlinux.ru> 2.17-alt1
- automated CPAN update

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 2.16-alt1
- automated CPAN update

* Mon Apr 14 2014 Igor Vlasenko <viy@altlinux.ru> 2.15-alt1
- automated CPAN update

* Wed Oct 09 2013 Igor Vlasenko <viy@altlinux.ru> 2.14-alt1
- automated CPAN update

* Thu Nov 25 2010 Igor Vlasenko <viy@altlinux.ru> 2.09-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Sat Mar 26 2005 Vyacheslav Dikonov <slava@altlinux.ru> 2.09-alt1
- ALTLinux build
