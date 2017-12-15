Name: perl-Text-Markdown-Hoedown
Version: 1.02
Release: alt1.1

Summary: hoedown for Perl5
Group: Development/Perl
License: perl

Url: %CPAN Text-Markdown-Hoedown
Source: %name-%version.tar

BuildRequires: perl(parent.pm) perl(File/pushd.pm) perl-devel perl(CPAN/Meta.pm) perl(Module/Build.pm) perl(CPAN/Meta/Prereqs.pm)

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_autolib/Text/Markdown/Hoedown*
%perl_vendor_archlib/Text/Markdown/Hoedown*
%doc Changes LICENSE README.md

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.02-alt1.1
- rebuild with new perl 5.26.1

* Sun Oct 01 2017 Igor Vlasenko <viy@altlinux.ru> 1.02-alt1
- automated CPAN update

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1.1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1.1
- rebuild with new perl 5.20.1

* Thu Dec 12 2013 Vladimir Lettiev <crux@altlinux.ru> 1.01-alt1
- 1.01

* Wed Nov 06 2013 Vladimir Lettiev <crux@altlinux.ru> 0.07-alt1
- initial build for ALTLinux

