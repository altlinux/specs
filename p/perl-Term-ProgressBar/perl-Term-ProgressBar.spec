%define module_name Term-ProgressBar

Name: perl-%module_name
Version: 2.09
Release: alt1.1

Summary: Provides a progress meter on a standard terminal
Summary(ru_RU.UTF-8): Индикатор процесса в консоли.
Group: Development/Perl
URL: http://ftp.spbu.ru/CPAN/authors/id/F/FL/FLUFFY
License: GPL or Artistic
Source: http://search.cpan.org/CPAN/authors/id/F/FL/FLUFFY/Term-ProgressBar-2.09.tar.gz
Buildarch: noarch
AutoReqProv: yes, perl
BuildRequires: perl-Class-MethodMaker perl-Module-Build perl-Term-ReadKey perl-devel
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
* Thu Nov 25 2010 Igor Vlasenko <viy@altlinux.ru> 2.09-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Sat Mar 26 2005 Vyacheslav Dikonov <slava@altlinux.ru> 2.09-alt1
- ALTLinux build
