## SPEC file for Perl module BFD
## Used in SVK

%define version    0.31
%define release    alt1

Name: perl-BFD
Version: %version
Release: alt1.1

Summary: dump of data structures for debugging purposes
Summary(ru_RU.UTF-8): выводит структуры данных для отладочных целей

License: GPL or Artistic
Group: Development/Perl

%define real_name BFD
URL: http://search.cpan.org/~rbs/%real_name/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>
BuildArch: noarch

Source: http://search.cpan.org/CPAN/authors/id/R/RB/RBS/%real_name-%version.tar.gz

AutoReqProv: perl, yes
BuildPreReq: perl-devel


%description
Perl module  BFD allows for impromptu dumping of output to
STDERR. Useful when you want to take a peek at a nest Perl 
data structure  by emitting  (relatively) nicely formatted 
output.

%description -l ru_RU.UTF-8
Модуль Perl  BFD осуществляет импровизированный вывод данных
из структур  Perl в STDERR.  Может быть полезен для быстрого
просмотра вложенных  структур Perl'а, так как (сравнительно) 
красиво форматирует выводимые данные.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc CHANGES README
%perl_vendor_privlib/BFD*

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.31-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Sun Apr 23 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.31-alt1
- Initial build for ALT Linux

* Tue May 24 2005 Nikolay A. Fetisov <naf@altlinux.ru> 0.31-alt0.1
- Build for new perl-5.8.7

* Sun Mar 06 2005 Nikolay A. Fetisov <naf@altlinux.ru> 0.31-alt0
- Initial build
