## SPEC file for Perl module XML::Tidy

Name: perl-XML-Tidy
Version: 1.12
Release: alt1

Summary: Perl module for tidy indenting of XML documents 
Summary(ru_RU.UTF-8): модуль Perl для выравнивания документов XML

License: %gpl3only
Group: Development/Perl

%define real_name XML-Tidy
%define real_version 1.12.B55J2qn
URL: http://search.cpan.org/dist/XML-Tidy/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>
BuildArch: noarch

Source: %real_name-%real_version.tar
Patch0: %real_name-1.12-alt-version_fix.patch

AutoReqProv: perl, yes
BuildRequires(pre): rpm-build-licenses

# Automatically added by buildreq on Tue Jun 21 2011
# optimized out: perl-Devel-Symdump perl-Encode perl-Math-BigInt perl-Math-BigInt-FastCalc perl-Memoize perl-Pod-Coverage perl-Pod-Escapes perl-Pod-Parser perl-Pod-Simple perl-XML-Parser perl-YAML-Tiny perl-devel perl-podlators
BuildRequires: perl-Math-BaseCnv perl-Module-Build perl-Test-Pod perl-Test-Pod-Coverage perl-XML-XPath

%description
Perl module XML::Tidy creates XML document objects  (with
inheritance from XML::XPath)  to tidy mixed-content  (ie.
non-data) text node indenting.  There are also some other
handy member  functions  to compress  &&  expand your XML
document object.

%description -l ru_RU.UTF-8
Модуль Perl XML:Tidy создаёт объекты в документах XML (с
помощью XML::XPath) с аккуратным выравниванием текстовых
тегов со смешанным содержанием  (т.е. тегов без данных).
Также он предоставляет несколько других полезных функций
для сжатия или развёртывания объектов в документах XML.


%prep
%setup -q -n %real_name-%real_version
%patch0

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README
%exclude /.perl.req
%_bindir/xmltidy
%perl_vendor_privlib/XML/Tidy*


%changelog
* Tue Jun 21 2011 Nikolay A. Fetisov <naf@altlinux.ru> 1.12-alt1
- New version

* Sun Nov 28 2010 Nikolay A. Fetisov <naf@altlinux.ru> 1.6-alt1
- New version

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.2.54-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Tue Aug 08 2006 Nikolay A. Fetisov <naf@altlinux.ru> 1.2.54-alt1
- Initial build for ALT Linux Sisyphus
