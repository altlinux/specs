## SPEC file for Perl module Text::Aligner
## Used in SVK

Name: perl-Text-Aligner
Version: 0.07
Release: alt1

Summary: align output with given style
Summary(ru_RU.UTF-8): выравнивает вывод согласно заданному стилю

License: %perl_license
Group: Development/Perl

%define real_name Text-Aligner
URL: http://search.cpan.org/~anno/%real_name/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>
BuildArch: noarch

Source: %real_name-%version.tar

AutoReqProv: perl, yes
BuildRequires(pre): perl-devel rpm-build-licenses


# Automatically added by buildreq on Sun Nov 28 2010
BuildRequires: perl-Term-ANSIColor

%description
Perl module Text::Aligner is used to justify strings to various
alignment styles.

%description -l ru_RU.UTF-8
Модуль Perl Text::Aligner может быть использован для выравнивания
строк согласно различным стилям форматирования.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Text/Aligner*

%changelog
* Sun Nov 28 2010 Nikolay A. Fetisov <naf@altlinux.ru> 0.07-alt1
- New version

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Sun Apr 23 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.03-alt1
- Initial build for ALT Linux

* Tue May 24 2005 Nikolay A. Fetisov <naf@altlinux.ru> 0.03-alt0.1
- Build for new perl-5.8.7

* Sun Mar 06 2005 Nikolay A. Fetisov <naf@altlinux.ru> 0.03-alt0
- Initial build
