%define module_name Unicode-UTF8simple

Name: perl-%module_name
Version: 1.06
Release: alt1.1

Summary: Conversions to/from UTF8 from/to charactersets
Summary(ru_RU.UTF-8): Обеспечивает преобразование текста из/в UTF-8 в/из различных кодировок
Group: Development/Perl
URL: http://search.cpan.org/~gus/Unicode-UTF8simple-1.06/
License: GPL or Artistic
Source: http://search.cpan.org/CPAN/authors/id/G/GU/GUS/Unicode-UTF8simple-1.06.tar.gz

Buildarch: noarch
AutoReqProv: yes, perl
BuildRequires: perl-Class-MethodMaker perl-Module-Build perl-Term-ReadKey perl-devel

%description
This utf-8 converter is written in plain perl and works with hopefully
any perl 5 version. It was mainly written because more recent modules
such as Encode do not work under older Perl 5.0 installations.

%description -l ru_RU.UTF-8
Данный перекодировщик utf-8 написан на чистом perl и должен работать с
любой версией среды perl 5. Этот модуль был написан потому, что более новые
модули, например Encode не работают в старом Perl 5.0.

%prep
%setup -q -n %module_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README gb2312.txt
%perl_vendorlib/Unicode/UTF8simple.pm

%changelog
* Mon Nov 29 2010 Igor Vlasenko <viy@altlinux.ru> 1.06-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Tue Jan 17 2006 Vyacheslav Dikonov <slava@altlinux.ru> 1.06-alt1
- ALTLinux build
