%define _unpackaged_files_terminate_build 1
%define dist String-Approx
Name: perl-%dist
Version: 3.28
Release: alt1.1

Summary: Perl extension for approximate matching (fuzzy matching)
License: Perl
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/J/JH/JHI/%{dist}-%{version}.tar.gz

# Automatically added by buildreq on Sat Oct 08 2011
BuildRequires: perl-devel

%description
String::Approx lets you match and substitute strings approximately.
With this you can emulate errors: typing errorrs, speling errors,
closely related vocabularies (colour color), genetic mutations
(GAG ACT), abbreviations (McScot, MacScot).
NOTE: String::Approx suits the task of string matching, not string
comparison, and it works for strings, not for text.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc ChangeLog PROBLEMS README README.apse Artistic COPYRIGHT COPYRIGHT.agrep LGPL
%perl_vendor_archlib/String/Approx.pm
%perl_vendor_autolib/String/Approx

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 3.28-alt1.1
- rebuild with new perl 5.26.1

* Tue May 09 2017 Igor Vlasenko <viy@altlinux.ru> 3.28-alt1
- automated CPAN update

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 3.27-alt1.1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 3.27-alt1.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 3.27-alt1.1
- rebuild with new perl 5.20.1

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 3.27-alt1
- 3.26 -> 3.27

* Sat Sep 01 2012 Vladimir Lettiev <crux@altlinux.ru> 3.26-alt2
- rebuilt for perl-5.16

* Sat Oct 08 2011 Alexey Tourbin <at@altlinux.ru> 3.26-alt1.2
- rebuilt for perl-5.14

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 3.26-alt1.1
- rebuilt with perl 5.12

* Mon May  4 2009 Sergey Kurakin <kurakin@altlinux.org> 3.26-alt1
- first build for AltLinux Sisyphus
