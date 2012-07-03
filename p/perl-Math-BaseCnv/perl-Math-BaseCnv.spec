## SPEC file for Perl module Math-BaseCnv

Name: perl-Math-BaseCnv
Version: 1.8
Release: alt1

Summary: Perl module with functions to convert between number bases
Summary(ru_RU.UTF-8): модуль Perl с функциями для преобразования систем счисления

License: %gpl3only
Group: Development/Perl

%define real_name Math-BaseCnv
%define real_version 1.8.B59BrZX
URL: http://search.cpan.org/dist/Math-BaseCnv/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>
BuildArch: noarch

Source: %real_name-%real_version.tar
Patch0: %real_name-1.8-alt-version_fix.patch

AutoReqProv: perl, yes
BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Sun Nov 28 2010
BuildRequires: perl-Math-BigInt-FastCalc perl-Memoize perl-Module-Build perl-Test-Pod perl-Test-Pod-Coverage

%description
Perl module Math::BaseCnv provides a few simple functions
for converting between arbitrary number bases.

%description -l ru_RU.UTF-8
Модуль Perl Math::BaseCnv содержит несколько простых
функций для преобразования представления чисел между
произвольными системами счисления.

%prep
%setup -q -n %real_name-%real_version
%patch0

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README CHANGES
%doc bin ex
%perl_vendor_privlib/Math/BaseCnv*
%exclude %_bindir/cnv

%changelog
* Tue Jun 21 2011 Nikolay A. Fetisov <naf@altlinux.ru> 1.8-alt1
- New version 1.8

* Sun Nov 28 2010 Nikolay A. Fetisov <naf@altlinux.ru> 1.6-alt1
- New version 1.6

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.4.75-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Fri Aug 10 2007 Nikolay A. Fetisov <naf@altlinux.ru> 1.4.75-alt1
- New version 1.4.75
  * added Test::Pod(::Coverage) tests && PREREQ entries
  * added b85 for IPv6, gen'd META.yml (w/ newline before EOF), up'd minor ver
  * added b64sort() && put pod at bottom

* Tue Aug 08 2006 Nikolay A. Fetisov <naf@altlinux.ru> 1.2.59-alt1
- Initial build for ALT Linux Sisyphus
