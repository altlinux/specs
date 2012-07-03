%define dist String-Approx
Name: perl-%dist
Version: 3.26
Release: alt1.2

Summary: Perl extension for approximate matching (fuzzy matching)
License: Perl
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

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
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc BUGS ChangeLog PROBLEMS README README.apse
%perl_vendor_archlib/String
%perl_vendor_autolib/String

%changelog
* Sat Oct 08 2011 Alexey Tourbin <at@altlinux.ru> 3.26-alt1.2
- rebuilt for perl-5.14

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 3.26-alt1.1
- rebuilt with perl 5.12

* Mon May  4 2009 Sergey Kurakin <kurakin@altlinux.org> 3.26-alt1
- first build for AltLinux Sisyphus
