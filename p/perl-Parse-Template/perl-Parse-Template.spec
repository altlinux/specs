# Spec file for Perl module ParseTemplate

Name: perl-Parse-Template
Version: 3.07
Release: alt1

Summary: processor for templates containing Perl expressions
Summary(ru_RU.UTF-8): обработчик шаблонов, содержащих выражения Perl

%define real_name ParseTemplate

License: %perl_license
Group: Development/Perl
URL: http://search.cpan.org/~pscust/ParseTemplate/

Packager: Nikolay Fetisov <naf@altlinux.ru>
BuildArch: noarch

Source: %real_name-%version.tar

AutoReqProv: perl, yes
BuildRequires(pre): perl-devel rpm-build-licenses

%description
Perl module Parse::Template evaluates Perl expressions placed 
within a text. This class can be used as a code generator, or
a generator of documents in  various document formats  (HTML,
XML, RTF, etc.).

%description -l ru_RU.UTF-8
Модуль Perl Parse::Template раскрывает размещённые в тексте 
выражения на Perl.  Этот класс  может быть  использован как 
генератор кода,  или  как генератор  документов в различных
форматах (HTML, XML, RTF, пр.)

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README
%doc examples/*
%perl_vendor_privlib/Parse/Template*

%changelog
* Mon Nov 29 2010 Nikolay A. Fetisov <naf@altlinux.ru> 3.07-alt1
- New version

* Sun Oct 10 2010 Nikolay A. Fetisov <naf@altlinux.ru> 3.05-alt1
- New version

* Wed Jun 28 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.37-alt1
- Initial build for ALT Linux

